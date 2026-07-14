// Convention checks for the JSON:API endpoint families (credit-risk, sanctions,
// interest rates / spreads). Guards against regressions of the accuracy issues
// fixed under PRD-59: every operation must document the standard error responses,
// and any paginated endpoint must bound page[limit] with maximum + default.
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const PATHS_DIR = process.env.PATHS_DIR || 'paths';
const FAMILY = /^(credit-risk_|sanctions_|rates_|spreads_).*\.yaml$/;
const REQUIRED_RESPONSES = ['401', '403', '404', '422', '429'];

function pageLimitBlock(text) {
  const start = text.indexOf('- name: page[limit]');
  if (start === -1) {
    return null;
  }

  const rest = text.slice(start);
  const end = rest.search(/\n {4}- name: |\n {4}responses:/);

  return end === -1 ? rest : rest.slice(0, end);
}

function checkFile(text) {
  const problems = [];

  for (const code of REQUIRED_RESPONSES) {
    if (!text.includes(`'${code}':`)) {
      problems.push(`missing '${code}' response`);
    }
  }

  const block = pageLimitBlock(text);
  if (block !== null) {
    if (!/\n\s+maximum:/.test(block)) {
      problems.push('page[limit] without "maximum"');
    }
    if (!/\n\s+default:/.test(block)) {
      problems.push('page[limit] without "default"');
    }
  }

  return problems;
}

const files = readdirSync(PATHS_DIR).filter((f) => FAMILY.test(f)).sort();

if (files.length === 0) {
  console.error(`check-conventions: no path files matched in "${PATHS_DIR}"`);
  process.exit(1);
}

const violations = [];
for (const file of files) {
  for (const problem of checkFile(readFileSync(join(PATHS_DIR, file), 'utf8'))) {
    violations.push(`${file}: ${problem}`);
  }
}

if (violations.length > 0) {
  console.error(`check-conventions: ${violations.length} violation(s):`);
  for (const v of violations) {
    console.error(`  x ${v}`);
  }
  process.exit(1);
}

console.log(`check-conventions: OK - ${files.length} endpoint file(s) pass conventions.`);

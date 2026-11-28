#!/usr/bin/env bash
set -euo pipefail

if [[ $# != 1 ]]; then
  echo "Usage: bash verify.sh /path/to/formal-conjectures" >&2
  exit 2
fi
source_dir="$(cd "$(dirname "$0")" && pwd)"
checkout="$(cd "$1" && pwd)"
pin=9097e2f90e66d2f6244209cb1c07f7120d17ec53
if [[ "$(git -C "$checkout" rev-parse HEAD)" != "$pin" ]]; then
  echo "Expected formal-conjectures at $pin" >&2
  exit 1
fi
work="$(mktemp -d)"
trap 'rm -rf -- "$work"' EXIT
mkdir "$work/OMAStatements"
module=OMAStatements/S_oeis_a345680
statement_revision=e793ecba1edeb34ade053096959185eb3fae1809
curl -fsSL "https://raw.githubusercontent.com/rpabani/open-math-agents/$statement_revision/statements/oeis-a345680.lean" -o "$work/$module.lean"

cp "$source_dir/Proof.lean" "$work/Audit.lean"
cat >> "$work/Audit.lean" <<'LEAN'

example : type_of% @OMA.S_oeis_a345680.main := OMA.solution

/-- info: 'OMA.solution' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms OMA.solution
LEAN
cd "$checkout"
lake env bash -eu -c '
  export LEAN_PATH="$1:$LEAN_PATH"
  lean --root="$1" -o "$1/$2.olean" "$1/$2.lean"
  lean --root="$1" "$1/Audit.lean"
' _ "$work" "$module"
echo "Verified OMA.solution against the pinned statement and its three reported axioms."

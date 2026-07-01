#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VIEWER_DIR="$ROOT_DIR/.edtrace-viewer"
PORT="${PORT:-5173}"

if ! command -v git >/dev/null 2>&1; then
  echo "git is required to clone the edtrace viewer." >&2
  exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is required to run the edtrace viewer frontend." >&2
  exit 1
fi

if [ ! -d "$VIEWER_DIR/.git" ]; then
  git clone --depth 1 https://github.com/percyliang/edtrace "$VIEWER_DIR"
fi

npm --prefix="$VIEWER_DIR/frontend" install

rm -f "$VIEWER_DIR/frontend/var"
ln -s "$ROOT_DIR/var" "$VIEWER_DIR/frontend/var"

cat <<EOF

Edtrace viewer starting on:
  http://127.0.0.1:$PORT/?trace=var/traces/edtrace_lectures.lecture_01.json

Other traces:
  var/traces/edtrace_lectures.lecture_02.json
  ...
  var/traces/edtrace_lectures.lecture_16.json

EOF

npm --prefix="$VIEWER_DIR/frontend" run dev -- --host 127.0.0.1 --port "$PORT"

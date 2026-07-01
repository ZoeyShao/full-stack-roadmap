#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PUBLISH_DIR="${PUBLISH_DIR:-$ROOT_DIR/published-site}"

"$ROOT_DIR/build-edtrace-frontend.sh"

rm -rf "$PUBLISH_DIR"
mkdir -p "$PUBLISH_DIR"

cp "$ROOT_DIR/index.html" "$PUBLISH_DIR/index.html"
cp -R "$ROOT_DIR/lectures" "$PUBLISH_DIR/lectures"
cp -R "$ROOT_DIR/lessons" "$PUBLISH_DIR/lessons"
cp -R "$ROOT_DIR/reference" "$PUBLISH_DIR/reference"
cp -R "$ROOT_DIR/trace" "$PUBLISH_DIR/trace"

touch "$PUBLISH_DIR/.nojekyll"

cat <<EOF

Built GitHub Pages site:
  $PUBLISH_DIR

Publish this directory as your GitHub Pages site.

Expected URLs after publishing from a project repo:
  https://<owner>.github.io/<repo>/
  https://<owner>.github.io/<repo>/trace/?trace=var/traces/edtrace_lectures.lecture_01.json

Local preview:
  python3 -m http.server 8000 -b 127.0.0.1 -d "$PUBLISH_DIR"
  http://127.0.0.1:8000/

EOF

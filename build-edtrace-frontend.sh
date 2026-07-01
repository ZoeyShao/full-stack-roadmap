#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VIEWER_DIR="$ROOT_DIR/.edtrace-viewer"
PUBLISH_DIR="${PUBLISH_DIR:-$ROOT_DIR/trace}"
EDTRACE_BASE_DIR="${EDTRACE_BASE_DIR:-/full-stack-roadmap/trace/}"

if ! command -v git >/dev/null 2>&1; then
  echo "git is required to clone the edtrace viewer." >&2
  exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is required to build the edtrace viewer frontend." >&2
  exit 1
fi

if [ ! -d "$VIEWER_DIR/.git" ]; then
  git clone --depth 1 https://github.com/percyliang/edtrace "$VIEWER_DIR"
fi

npm --prefix="$VIEWER_DIR/frontend" install

mkdir -p "$ROOT_DIR/images" "$VIEWER_DIR/frontend/public"
rm -f "$VIEWER_DIR/frontend/public/var" "$VIEWER_DIR/frontend/public/images"
ln -s "$ROOT_DIR/var" "$VIEWER_DIR/frontend/public/var"
ln -s "$ROOT_DIR/images" "$VIEWER_DIR/frontend/public/images"

rm -rf "$PUBLISH_DIR"
mkdir -p "$PUBLISH_DIR"

VITE_EDTRACE_BASE_DIR="$EDTRACE_BASE_DIR" \
VITE_EDTRACE_DIST_DIR="$PUBLISH_DIR" \
  npm --prefix="$VIEWER_DIR/frontend" run build

# The upstream template uses an absolute /vite.svg favicon path, which is noisy
# on GitHub Pages project sites. The favicon is not needed for the courseware.
sed -i.bak '/rel="icon".*vite\.svg/d' "$PUBLISH_DIR/index.html"
rm -f "$PUBLISH_DIR/index.html.bak"

cat <<EOF

Built edtrace frontend:
  $PUBLISH_DIR

Base path:
  $EDTRACE_BASE_DIR

Open after publishing:
  trace/?trace=var/traces/edtrace_lectures.lecture_01.json

Local preview:
  python3 -m http.server 8000 -b 127.0.0.1 -d "$ROOT_DIR/.."
  http://127.0.0.1:8000/full-stack-roadmap/trace/?trace=var/traces/edtrace_lectures.lecture_01.json

EOF

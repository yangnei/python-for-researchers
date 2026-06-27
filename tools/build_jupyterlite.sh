#!/usr/bin/env bash
# Build the in-browser JupyterLite app into docs/jupyter, with the per-session
# notebooks (docs/notebooks/*.ipynb) preloaded as content. Pyodide itself loads
# from a CDN at runtime, so the committed output is ~70 MB, not hundreds.
#
# One-time tooling setup (kept out of the PDF .venv to avoid dependency clashes):
#   python3 -m venv .venv-jlite
#   .venv-jlite/bin/pip install jupyterlite-core jupyterlite-pyodide-kernel jupyter-server
#
# Always regenerate the notebooks first:
#   python3 tools/build_notebooks.py
#   bash tools/build_jupyterlite.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
JLITE="$ROOT/.venv-jlite/bin/jupyter"

rm -rf "$ROOT/docs/jupyter" "$ROOT/build/jlite"
mkdir -p "$ROOT/build/jlite"
cd "$ROOT/build/jlite"
"$JLITE" lite build \
  --contents "$ROOT/docs/notebooks" \
  --output-dir "$ROOT/docs/jupyter"
echo "Built docs/jupyter ($(du -sh "$ROOT/docs/jupyter" | cut -f1))"

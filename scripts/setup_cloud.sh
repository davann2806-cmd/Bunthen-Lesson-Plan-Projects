#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FONTS_SRC="$REPO_ROOT/fonts"

echo "==> Installing bundled Khmer & Math fonts from $FONTS_SRC"
mkdir -p "$HOME/.local/share/fonts/ngs" "$HOME/.fonts/ngs"
cp -f "$FONTS_SRC"/* "$HOME/.local/share/fonts/ngs/"
cp -f "$FONTS_SRC"/* "$HOME/.fonts/ngs/"

if command -v fc-cache >/dev/null 2>&1; then
  fc-cache -f "$HOME/.local/share/fonts" "$HOME/.fonts" || fc-cache -fv
fi

echo "==> Checking XeLaTeX & PyMuPDF"
xelatex --version | head -n 2
python3 -c "import fitz; print('PyMuPDF OK:', fitz.__doc__.splitlines()[0])"
echo "==> Cloud LaTeX environment ready."

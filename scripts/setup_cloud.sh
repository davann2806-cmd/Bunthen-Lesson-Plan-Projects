#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FONTS_SRC="$REPO_ROOT/fonts"

run_root() {
  if [ "$(id -u)" -eq 0 ]; then
    "$@"
  elif command -v sudo >/dev/null 2>&1; then
    sudo "$@"
  else
    echo "ERROR: root or sudo is required to install packages: $*" >&2
    return 1
  fi
}

echo "==> [Bunthen Lesson Plan Projects] Checking TeX Live (XeLaTeX) & PyMuPDF"
if ! command -v xelatex >/dev/null 2>&1; then
  echo "==> Installing XeLaTeX & TeX Live packages..."
  run_root apt-get update
  run_root env DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    texlive-xetex \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-pictures \
    texlive-science \
    texlive-fonts-recommended \
    fontconfig \
    lmodern \
    python3-pip
else
  echo "==> xelatex already installed."
fi

if ! python3 -c "import fitz" >/dev/null 2>&1; then
  echo "==> Installing PyMuPDF (fitz)..."
  python3 -m pip install --break-system-packages pymupdf || python3 -m pip install pymupdf
else
  echo "==> PyMuPDF already installed."
fi

echo "==> Installing bundled Khmer & Math fonts from $FONTS_SRC"
mkdir -p "$HOME/.local/share/fonts/bunthen" "$HOME/.fonts/bunthen"
cp -f "$FONTS_SRC"/* "$HOME/.local/share/fonts/bunthen/"
cp -f "$FONTS_SRC"/* "$HOME/.fonts/bunthen/"

if command -v fc-cache >/dev/null 2>&1; then
  fc-cache -f "$HOME/.local/share/fonts" "$HOME/.fonts" || fc-cache -fv
fi

echo "==> Verification:"
xelatex --version | head -n 2
python3 -c "import fitz; print('PyMuPDF OK:', fitz.__doc__.splitlines()[0])"
echo "==> Bunthen Lesson Plan Projects Cloud XeLaTeX environment ready."

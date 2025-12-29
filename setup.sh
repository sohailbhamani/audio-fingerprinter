#!/bin/bash

# Setup script for audio-fingerprinter

echo "Setting up audio-fingerprinter..."

# Check for fpcalc
if ! command -v fpcalc &> /dev/null; then
    echo "⚠️  fpcalc (chromaprint) not found!"
    echo "Please install it:"
    echo "  sudo apt-get install libchromaprint-tools"
    echo "  # or download from https://acoustid.org/chromaprint"
else
    echo "✅ fpcalc found: $(which fpcalc)"
fi

# Create venv if not exists
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "✅ Virtual environment created at .venv"
fi

# Install
source .venv/bin/activate
pip install -e .
echo "✅ Installed audio-fingerprinter in editable mode"

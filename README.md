# Audio Fingerprinter

[![CI](https://github.com/sohailbhamani/audio-fingerprinter/actions/workflows/ci.yml/badge.svg)](https://github.com/sohailbhamani/audio-fingerprinter/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

A GPL-licensed CLI tool for generating AcoustID audio fingerprints using Chromaprint.

## Features

- **AcoustID Fingerprinting**: Generate unique audio fingerprints compatible with the AcoustID database
- **Duration Extraction**: Returns audio duration alongside fingerprint
- **JSON Output**: Clean JSON output for easy integration

## Prerequisites

This tool requires the `fpcalc` binary from Chromaprint:

```bash
# Ubuntu/Debian
sudo apt-get install libchromaprint-tools

# macOS
brew install chromaprint
```

## Installation

```bash
# Clone the repository
git clone https://github.com/sohailbhamani/audio-fingerprinter.git
cd audio-fingerprinter

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in development mode
pip install -e ".[dev]"
```

## Usage

```bash
# Generate fingerprint for an audio file
audio-fingerprinter fingerprint path/to/song.mp3
```

### Output

```json
{
  "fingerprint": "AQADtNQyRZGkJEqS5EhyBMmR...",
  "duration": 245.32
}
```

## Development

```bash
# Run tests
pytest

# Run linter
ruff check .

# Run type checker
mypy src/
```

## Dependencies

- [pyacoustid](https://github.com/beetbox/pyacoustid) - Python bindings for Chromaprint
- [Chromaprint](https://acoustid.org/chromaprint) - Audio fingerprinting library (fpcalc binary)
- [Click](https://click.palletsprojects.com/) - CLI framework

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

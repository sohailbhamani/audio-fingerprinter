# audio-fingerprinter

Audio fingerprinting CLI for deduplication and AcoustID/MusicBrainz lookup. Wraps [Chromaprint](https://acoustid.org/chromaprint).

## Features

- **Audio Fingerprinting** — Generate unique fingerprints
- **Duplicate Detection** — Find duplicate tracks
- **AcoustID Lookup** — Identify unknown tracks
- **MusicBrainz Integration** — Fetch metadata

## Installation

```bash
pip install audio-fingerprinter
```

## Usage

```bash
# Generate fingerprint
audio-fingerprinter fingerprint track.mp3

# Find duplicates in a directory
audio-fingerprinter dedupe ./music/

# Lookup track on AcoustID
audio-fingerprinter lookup track.mp3
```

## Requirements

- Python 3.9+
- Chromaprint

## License

MIT — See [LICENSE](LICENSE)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

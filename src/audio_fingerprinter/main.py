import json
import logging
import sys
from pathlib import Path

import acoustid
import click

# Configure logging to stderr
logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="%(message)s")
logger = logging.getLogger("audio-fingerprinter")


@click.group()
def cli():
    """Audio Fingerprinter CLI using Chromaprint."""
    pass


@cli.command()
@click.argument("audio_path", type=click.Path(exists=True, path_type=Path))
def fingerprint(audio_path: Path):
    """Generate AcoustID fingerprint for audio file."""
    try:
        # returns (duration, fingerprint)
        # force_fpcalc=True to ensure we use valid external tool or fail
        duration, fp = acoustid.fingerprint_file(str(audio_path), force_fpcalc=False)

        result = {
            "fingerprint": fp.decode("utf-8") if isinstance(fp, bytes) else fp,
            "duration": float(duration),
        }
        click.echo(json.dumps(result))

    except acoustid.FpcalcNotFoundError:
        logger.error("fpcalc not found! Please install chromaprint/fpcalc.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Fingerprinting failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    cli()

import subprocess
import json
import pytest
import sys
import os
import tempfile
import numpy as np
import soundfile as sf
import shutil

SAMPLE_RATE = 44100


def generate_tone(freq, duration, amp=0.5):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    return amp * np.sin(2 * np.pi * freq * t)


@pytest.fixture
def test_audio_file():
    """Create a temporary sine wave audio file."""
    # 440 Hz sine wave for 5 seconds
    audio = generate_tone(440, 5.0)

    fd, path = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    sf.write(path, audio, SAMPLE_RATE)

    yield path

    if os.path.exists(path):
        os.remove(path)


def run_fingerprinter(file_path):
    cmd = [
        sys.executable,
        "-m",
        "audio_fingerprinter.main",
        "fingerprint",
        str(file_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result


def test_fingerprint_success(test_audio_file):
    """Verify fingerprint generation works with fpcalc."""
    if not shutil.which("fpcalc"):
        pytest.fail("fpcalc not found, cannot test fingerprinting")

    result = run_fingerprinter(test_audio_file)
    assert result.returncode == 0

    data = json.loads(result.stdout)
    assert "fingerprint" in data
    assert "duration" in data
    assert isinstance(data["fingerprint"], str)
    assert len(data["fingerprint"]) > 10
    assert abs(data["duration"] - 5.0) < 0.2

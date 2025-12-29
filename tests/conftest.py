"""Shared test fixtures for audio-fingerprinter tests."""

import os
import tempfile

import numpy as np
import pytest
import soundfile as sf

SAMPLE_RATE = 44100


def generate_tone(freq, duration, amp=0.5):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    return amp * np.sin(2 * np.pi * freq * t)


@pytest.fixture
def test_audio_file():
    """Create a temporary sine wave audio file (5.0 seconds)."""
    audio = generate_tone(440, 5.0)

    fd, path = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    sf.write(path, audio, SAMPLE_RATE)

    yield path

    if os.path.exists(path):
        os.remove(path)


@pytest.fixture
def silence_file():
    """Create a temporary silent audio file."""
    audio = np.zeros(int(SAMPLE_RATE * 5.0))

    fd, path = tempfile.mkstemp(suffix="_silence.wav")
    os.close(fd)
    sf.write(path, audio, SAMPLE_RATE)

    yield path

    if os.path.exists(path):
        os.remove(path)

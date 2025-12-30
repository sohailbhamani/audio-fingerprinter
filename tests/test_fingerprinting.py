"""Fingerprinting tests."""

import json
import shutil
import subprocess
import sys

import pytest


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


class TestFingerprintGeneration:
    """Test acoustic fingerprint generation."""

    def test_fingerprint_valid_audio(self, test_audio_file):
        """Verify fingerprinting works for valid audio."""
        if not shutil.which("fpcalc"):
            pytest.skip("fpcalc not installed")

        result = run_fingerprinter(test_audio_file)
        assert result.returncode == 0

        data = json.loads(result.stdout)
        assert "fingerprint" in data
        assert isinstance(data["fingerprint"], str)
        assert len(data["fingerprint"]) > 10
        assert abs(data["duration"] - 5.0) < 0.2

    def test_fingerprint_consistency(self, test_audio_file):
        """Verify same audio produces same fingerprint."""
        if not shutil.which("fpcalc"):
            pytest.skip("fpcalc not installed")

        res1 = run_fingerprinter(test_audio_file)
        res2 = run_fingerprinter(test_audio_file)

        fp1 = json.loads(res1.stdout)["fingerprint"]
        fp2 = json.loads(res2.stdout)["fingerprint"]

        assert fp1 == fp2

    def test_fingerprint_silence(self, silence_file):
        """Verify silence handling (Chromaprint might fail or return empty)."""
        if not shutil.which("fpcalc"):
            pytest.skip("fpcalc not installed")

        result = run_fingerprinter(silence_file)

        # fpcalc typically returns a fingerprint even for silence, or very short
        if result.returncode == 0:
            data = json.loads(result.stdout)
            assert "fingerprint" in data


class TestErrorHandling:
    """Test error handling."""

    def test_missing_file(self):
        result = run_fingerprinter("/nonexistent.wav")
        assert result.returncode != 0

    def test_invalid_file_format(self):
        """Test with a text file renamed to .wav."""
        import os
        import tempfile

        fd, path = tempfile.mkstemp(suffix=".wav")
        os.write(fd, b"This is not audio data")
        os.close(fd)

        try:
            result = run_fingerprinter(path)
            assert result.returncode != 0
        finally:
            if os.path.exists(path):
                os.remove(path)

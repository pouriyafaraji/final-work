"""Create the directory layout for the Persian Emotional TTS project."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DIRECTORIES = (
    "data/raw",
    "data/processed",
    "models/acoustic",
    "models/emotion_extractor",
    "models/vocoder",
    "configs",
)


def main() -> None:
    """Create all project directories, including missing parent directories."""
    for relative_path in DIRECTORIES:
        directory = PROJECT_ROOT / relative_path
        directory.mkdir(parents=True, exist_ok=True)

        # Keep the directory layout visible in Git without tracking future data.
        (directory / ".gitkeep").touch(exist_ok=True)
        print(f"Ready: {relative_path}/")


if __name__ == "__main__":
    main()

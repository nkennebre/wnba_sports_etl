from pathlib import Path

# Base project directory (auto-detected from current file location)
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
ICON_DIR = BASE_DIR / "icons"

# Default plot styling
DEFAULT_LOGO_ZOOM = 0.15
DEFAULT_WATERMARK_POSITION = "bottom-right"

# Watermark settings
USE_WATERMARK_IMAGE = False

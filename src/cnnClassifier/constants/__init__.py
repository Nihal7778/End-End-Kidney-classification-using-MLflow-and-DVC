from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

from pathlib import Path

CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"

print(f"Config path: {CONFIG_FILE_PATH}")
print(f"Config exists: {CONFIG_FILE_PATH.exists()}")
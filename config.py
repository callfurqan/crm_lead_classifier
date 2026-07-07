from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# -----------------------------
# Paths
# -----------------------------

ROOT_DIR = Path(__file__).parent

INPUT_DIR = ROOT_DIR / "input"

OUTPUT_DIR = ROOT_DIR / "output"

LOG_DIR = OUTPUT_DIR / "logs"

EMAIL_OUTPUT = OUTPUT_DIR / "emails"

SMS_OUTPUT = OUTPUT_DIR / "sms"

CALL_OUTPUT = OUTPUT_DIR / "calls"

COMBINED_OUTPUT = OUTPUT_DIR / "combined"

# -----------------------------
# LLM
# -----------------------------

USE_LLM = os.getenv("USE_LLM", "False").lower() == "true"

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "")

LLM_MODEL = os.getenv("LLM_MODEL", "")

LLM_API_KEY = os.getenv("LLM_API_KEY", "")

# -----------------------------
# Classification
# -----------------------------

CONFIDENCE_THRESHOLD = 90

MERGE_DUPLICATES = True

EXPORT_COMBINED = True

LOG_LEVEL = "INFO"
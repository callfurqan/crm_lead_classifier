import json
from pathlib import Path


class JsonLoader:

    @staticmethod
    def load(file_path: Path):

        with open(file_path, "r", encoding="utf-8") as f:

            return json.load(f)
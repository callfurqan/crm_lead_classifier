from src.core.loader import JsonLoader
from src.core.detector import DatasetDetector
from src.core.logger import get_logger

from src.processors import PROCESSOR_REGISTRY

from config import INPUT_DIR


logger = get_logger(__name__)


class Pipeline:

    def run(self):

        json_files = list(INPUT_DIR.glob("*.json"))

        if not json_files:
            logger.warning("No JSON files found.")
            return

        total_leads = 0

        for file in json_files:

            logger.info(f"Loading {file.name}")

            data = JsonLoader.load(file)

            dataset = DatasetDetector.detect(data)

            logger.info(f"Detected: {dataset.value}")

            processor_cls = PROCESSOR_REGISTRY.get(dataset)

            if processor_cls is None:
                logger.warning(f"No processor registered for {dataset}")
                continue

            processor = processor_cls()

            leads = processor.process(data)

            total_leads += len(leads)

            logger.info(f"Parsed {len(leads)} leads")

        logger.info(f"Total Parsed Leads : {total_leads}")
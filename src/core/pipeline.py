from src.core.loader import JsonLoader
from src.core.detector import DatasetDetector
from src.core.logger import get_logger

from src.processors import PROCESSOR_REGISTRY
from src.classifiers import ClassifierFactory
from src.exporters import ExcelExporter

from config import INPUT_DIR


logger = get_logger(__name__)


class Pipeline:

    def run(self):

        json_files = list(INPUT_DIR.glob("*.json"))

        if not json_files:
            logger.warning("No JSON files found.")
            return

        total_leads = 0
        all_leads = []

        classifier = ClassifierFactory.create()

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

            # Processor now returns ProcessorResult
            result = processor.process(data)

            for lead in result.leads:
                classifier.classify(lead)

            total_leads += len(result.leads)
            all_leads.extend(result.leads)

            logger.info(
                f"Parsed {result.stats.parsed} leads "
                f"(Skipped={result.stats.skipped}, "
                f"Errors={result.stats.errors})"
            )

            if result.leads:
                sample = result.leads[0]

                logger.info(
                    f"Sample Lead -> "
                    f"Name={sample.name}, "
                    f"Phone={sample.phone}, "
                    f"Interactions={len(sample.interactions)}, "
                    f"Status={sample.classification.status.value}"
                )

        logger.info(f"Total Parsed Leads : {total_leads}")

        if all_leads:
            exporter = ExcelExporter()
            written = exporter.export(all_leads)

            for path in written:
                logger.info(f"Exported {path.name}")

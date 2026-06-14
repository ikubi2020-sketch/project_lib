import logging

logging.basicConfig(
    level="INFO",
    format="%(asctime)s | %(level)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log", encoding="utf-8")
    ]
)

logger = logging.getLogger(__name__)
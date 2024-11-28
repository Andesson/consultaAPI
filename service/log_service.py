import logging
from logging.handlers import TimedRotatingFileHandler
import os

def setup_logging():
    # Cria diretório para logs, se não existir
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Log diário
    daily_log_file = os.path.join(log_directory, "daily_log.log")
    daily_handler = TimedRotatingFileHandler(
        daily_log_file, when="midnight", interval=1, backupCount=30
    )
    daily_handler.setLevel(logging.INFO)
    daily_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    monthly_log_file = os.path.join(log_directory, "monthly_log.log")
    monthly_handler = TimedRotatingFileHandler(
        monthly_log_file, when="midnight", interval=30, backupCount=12
    )
    monthly_handler.setLevel(logging.INFO)
    monthly_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(daily_handler)
    logger.addHandler(monthly_handler)

    return logger
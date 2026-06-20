import pymysql
import logging
from helpers.set_logger import LoggerFactory
from helpers.config import settings

logger = LoggerFactory.get_logger(
    name="database_connection",
    log_file=settings.Log_file_signup,
    level=logging.INFO
)


def get_db_connection():
    try:
        connection = pymysql.connect(
            host= settings.Endpoint,
            user=settings.user,
            password=settings.password,
            database=settings.database,
            port=settings.port
        )

        logger.info("The connection is being made in the database")
        return connection

    except Exception as e:
        logger.info(f"Database connection is failed {e}")
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from core.config import settings
from core.logger_utils import get_logger

logger = get_logger(__file__)

class MongoDatabaseConnector:
    """Singleton class to connect to MongoDB database."""

    _instance = None
    client: MongoClient | None = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            try:
                cls._instance.client = MongoClient(settings.MONGO_DATABASE_HOST)
                logger.info(
                    f"Connection to database with uri: {settings.MONGO_DATABASE_HOST} successful"
                )
            except ConnectionFailure:
                logger.error("Couldn't connect to the database.")
                raise
        return cls._instance

    def get_database(self):
        assert self.client, "Database connection not initialized"
        return self.client[settings.MONGO_DATABASE_NAME]

    def close(self):
        if self.client:
            self.client.close()
            logger.info("Connection to database has been closed.")
            # To allow re-initialization after closing, which is good for tests
            MongoDatabaseConnector._instance = None
            MongoDatabaseConnector.client = None


connection = MongoDatabaseConnector()
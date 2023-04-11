import os

# Get the absolute path of the directory containing this file
TEST_DB = "test.db"
basedir = os.path.abspath(os.path.dirname(__file__))


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, TEST_DB)
    LOG_FILE_NAME = "log-test.txt"

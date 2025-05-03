import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "db")
SECRETS_FILE = os.path.join(BASE_DIR, "database", "generated_secrets.json")
NUM_SQLI_TASKS = 6
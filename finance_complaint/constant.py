from dataclasses import dataclass
from datetime import datetime
import os
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

@dataclass # declare a class without init 
class EnvironmentVariable:
    mongo_db_url = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariable()
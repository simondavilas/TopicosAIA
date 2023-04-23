import os

# DATASET PATH
DATASET_PATH = os.getenv("DATASET_PATH", "../fs/")
# USER DB
USER_DB = os.getenv("USER_DB", "root")
# PASS DB
PASS_DB = os.getenv("PASS_DB", "Deyka2023")
# IP SERVER DB
IP_SERVER = os.getenv("IP_SERVER", "localhost:3306")
# NAME DB
NAME_DB = os.getenv("NAME_DB", "mlops-inference")

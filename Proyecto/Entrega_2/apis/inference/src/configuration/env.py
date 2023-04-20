import os

# MODEL PATH
MODEL_PATH = os.getenv("MODEL_PATH", "/opt/topicsIA/model/")
# DATASET PATH
DATASET_PATH = os.getenv("DATASET_PATH", "/opt/topicsIA/dataset/")
# USER DB
USER_DB = os.getenv("USER_DB", "root")
# PASS DB
PASS_DB = os.getenv("PASS_DB", "topicosIA")
# IP SERVER DB
IP_SERVER = os.getenv("IP_SERVER", "10.43.102.112")
# NAME DB
NAME_DB = os.getenv("NAME_DB", "inference")

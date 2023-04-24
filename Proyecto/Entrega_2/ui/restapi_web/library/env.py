import os


# URL PROCESS DATA
URL_PROCESS_DATA = os.getenv("URL_PROCESS_DATA", "http://localhost:82/ui/procesar-info")

# URL PROCESS DATA
URL_TRAIN = os.getenv("URL_TRAIN", "http://localhost:82/ui/entrenar_modelo")

# URL PROCESS DATA
URL_SAVE_DATA = os.getenv("URL_SAVE_DATA", "http://localhost:82/ui/save_data")

# URL PROCESS DATA
URL_PREDICT_MODEL = os.getenv("URL_PREDICT_MODEL", "http://localhost:82/ui/predict_model")
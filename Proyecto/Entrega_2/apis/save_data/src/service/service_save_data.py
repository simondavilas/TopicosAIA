import uvicorn
from fastapi import FastAPI

import core.save_data_core as sd

app = FastAPI()


@app.get("/save_data")
async def save_data():
    sd.save("feature")
    return {"code": "ok", "description": "Se agrego exitosamente archivos al conjunto de datos"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
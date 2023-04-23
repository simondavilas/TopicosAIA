import uvicorn
from fastapi import FastAPI, HTTPException

import core.process_data as process

app = FastAPI()


@app.get('/procesar-info')
def process_info(data):
    if data == 'cover_type':
        process.process_info('cover_type')
    else:
        raise HTTPException(status_code=500, detail="Conjunto de datos desconocido: " + data)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
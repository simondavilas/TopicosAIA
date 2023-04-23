import uvicorn

import core.train_model as train
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get('/entrenar_modelo')
def train_model(model):
    if model == 'cover_type':
        cover_type_metrics = train.train_model('cover_type')
        return cover_type_metrics
    else:
        raise HTTPException(status_code=500, detail="modelo desconocido: " + model)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
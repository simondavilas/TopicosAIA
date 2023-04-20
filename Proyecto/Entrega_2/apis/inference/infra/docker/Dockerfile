FROM python:3.9
RUN mkdir -p /opt/topicsIA
RUN mkdir -p /opt/topicsIA/dataset
RUN mkdir -p /opt/topicsIA/model
WORKDIR /opt/topicsIA
COPY inference/src/  ./
ADD inference/infra/docker/requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
ENTRYPOINT ["uvicorn", "service.service_inference:app", "--host", "0.0.0.0", "--port", "8080"]


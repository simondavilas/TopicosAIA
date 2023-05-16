FROM python:3.7
RUN apt update && apt install -y python3-venv gcc
RUN apt-get install -y python3-dev build-essential

ENV VENV=/.venv/mlops-puj
RUN python3 -m venv ${VENV}
RUN mkdir -p $VENV/src
ENV PATH=$VENV/bin:$PATH
RUN pip install -U pip
RUN pip install psycopg2 mlflow awscli boto3


# Expose the port that the MLFlow tracking server runs on
EXPOSE 5000
# Default database credentials
ENV DB_USERNAME=topicosIA
ENV DB_PASSWORD=topicosIA
ENV DB_URL=metadata-db-mlfow-svc:5432
ENV DB_NAME=metadata-mlfow
ENV ARTIFACT_STORE=s3://mlflows3/artifacts

ENTRYPOINT mlflow server --default-artifact-root $ARTIFACT_STORE \
        --backend-store-uri postgresql://$DB_USERNAME:$DB_PASSWORD@$DB_URL/$DB_NAME --host 0.0.0.0 --serve-artifacts
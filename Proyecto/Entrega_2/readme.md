# Proyecto 2
Proyecto con arquitectura de microservicios e infraestructura basada en kubernetes para implementar flujo de validación, procesamiento, entrenamiento e inferencia
con machine learning y mlops

Clona el proyecto

```
https://github.com/simondavilas/TopicosAIA.git
```

## Construir Imagenes Docker

construir las imagenes de docker para las apis y la ui

```
cd Proyecto/Entrega_2
```
after, execute.

```
cd apis

docker image build -t mlops/project2-process-data:1.0.0 -f process_data/infra/docker/Dockerfile .

docker image build -t mlops/project2-train-model:1.0.0 -f train_model/infra/docker/Dockerfile .

docker image build -t mlops/project2-inference:1.0.0 -f inference/infra/docker/Dockerfile .

docker image build -t mlops/project2-save-data:1.0.0 -f save_data/infra/docker/Dockerfile .


```

```
cd ../ui/restapi_web

docker image build -t mlops/project2-ui:1.0.0  .

```

## Ejecutar/Crear Recursos K8s

```
cd ../../
kubectl apply -f k8s

```

En la carpeta apis ejecutar los comandos:

docker image build -t mlops/project2-process-data:1.0.0 -f process_data/infra/docker/Dockerfile .

docker image build -t mlops/project2-train-model:1.0.0 -f train_model/infra/docker/Dockerfile .

docker image build -t mlops/project2-inference:1.0.0 -f inference/infra/docker/Dockerfile .

docker image build -t mlops/project2-save-data:1.0.0 -f save_data/infra/docker/Dockerfile .


En la carpeta Entrega_2

kubectl apply -f k8s


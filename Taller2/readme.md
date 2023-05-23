docker build -t grupo3_t2 .
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
sudo docker run -it --name grupo3_t2 -e TZ=America/Bogota --rm -p 8889:8889  -v $PWD:/work grupo3_t2
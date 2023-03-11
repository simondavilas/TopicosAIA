    docker build -t grupo3_e1 .
    docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
    sudo docker run -it --name grupo3_e1 -e TZ=America/Bogota --rm -p 8888:8888  -v $PWD:/work grupo3_e1
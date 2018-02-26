docker-compose up -d
docker build -t project1_send ./send
docker run --net="project1_myNetwork" -i project1_send

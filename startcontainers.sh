# just the first time
# docker build -t scrapper-image:latest .
# docker run --name scrapperapp -v$PWD/app:/app -p 5000:5000 scrapper-image:latest

docker-compose up -d
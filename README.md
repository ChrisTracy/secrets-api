docker pull christracy/secrets-api

docker run --name secrets-api -d -e LIMIT=520 -e Default_nbytes=50 -p 8181:5050 christracy/secrets-api

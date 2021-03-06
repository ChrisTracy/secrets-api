# set base image (host OS)
FROM python:3.8-slim

# expose port defined in flask app
EXPOSE 5050

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /app

# command to run on container start
CMD [ "python", "./SAPI-Server.py" ]
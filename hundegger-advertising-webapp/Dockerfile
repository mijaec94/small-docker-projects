# Inspired by https://docker-curriculum.com/

# use python as base-image
FROM python:3.6

# create folder and cd to it
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# copy everything else
COPY . /usr/src/app

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]





# Use the Python3.7.2 image
# FROM python:3.7.2-stretch
# pull official base image
FROM python:3.8.1-slim-buster

# Set the working directory to /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install uWSGI
RUN pip install -r requirements.txt

CMD ["uwsgi" , "app.ini"]
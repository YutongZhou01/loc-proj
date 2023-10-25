# Use the official Python image as the base image for the backend
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /backend
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install required system packages and dependencies
RUN apt-get update && \
    apt-get install -y 
RUN apt-get install poppler-utils -y
# Copy the requirements.txt file and install Python dependencies
COPY backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

# Copy the rest of the backend code
COPY backend/ .

CMD [ "python3", "-m" , "flask", "run"]

# Use the official Node.js image as the base image
FROM node:20.5.1

# Set the working directory inside the container for frontend
WORKDIR /frontend

# Copy the frontend source code and install Node.js dependencies
COPY frontend/package.json frontend/package-lock.json ./

RUN npm i --silent

EXPOSE 80

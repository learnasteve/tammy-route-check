FROM python:3.9-slim

WORKDIR /app

# Install any needed packages specified in requirements.txt
#RUN apt-get update && apt-get install -y libpq-dev  # Add this line to install postgres dev files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Make port 7860 available to the world outside this container
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

COPY . /app

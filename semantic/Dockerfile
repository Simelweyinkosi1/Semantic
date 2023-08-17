# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script to the container
COPY semantic.py /app/

# Install spaCy and download the 'en_core_web_md' model
RUN pip install spacy && \
    python -m spacy download en_core_web_md

# Run the Python script when the container starts
CMD ["python", "semantic.py"]

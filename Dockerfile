# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit runs on
EXPOSE 8501

# Define environment variable
#ENV LC_ALL=C.UTF-8
#ENV LANG=C.UTF-8

# Run streamlit when the container launches
CMD ["streamlit", "run", "app3.py"]

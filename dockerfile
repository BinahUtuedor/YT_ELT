# Define build arguments
ARG AIRFLOW_VERSION=2.9.2
ARG PYTHON_VERSION=3.10

# Use the arguments in the FROM line
FROM apache/airflow:${AIRFLOW_VERSION}-python${PYTHON_VERSION}

# Set Airflow home directory
ENV AIRFLOW_HOME=/opt/airflow

# Copy requirements.txt into the container
COPY requirements.txt /

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
# Base Jupyter PySpark image
FROM jupyter/pyspark-notebook:latest

USER root

# Install system deps needed for psycopg2
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Python packages you'll likely need
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Try to download Postgres JDBC (optional fallback - still mount ./libs for reliability)
ARG POSTGRES_JDBC_VERSION=42.6.0
ENV SPARK_HOME=/usr/local/spark
RUN wget -q https://jdbc.postgresql.org/download/postgresql-${POSTGRES_JDBC_VERSION}.jar -P ${SPARK_HOME}/jars/ || true

# Ensure correct ownership
RUN chown -R jovyan:users /home/jovyan /usr/local/spark/jars

USER jovyan

EXPOSE 8888 4040
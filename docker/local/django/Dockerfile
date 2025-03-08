# Use an official Python image.
FROM python:3.12.5

# Set environment variables
ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles

# Set the working directory to /app
WORKDIR $APP_HOME

# Metadata for image
LABEL maintainer="Sunil Kumar"
LABEL description="Development image for Realty Hub Project"

# Prevents Python from writing .pyc files to disk.
ENV PYTHONDONTWRITEBYTECODE 1

# Ensures that Python output is logged straight to the terminal (e.g., for Docker logs)
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update \
&& apt-get install -y build-essential \
&& apt-get install -y libpq-dev \
&& apt-get install -y gettext \
&& apt-get install -y netcat-openbsd gcc postgresql \
&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT ["/entrypoint"]
# syntax=docker/dockerfile:1

FROM python:3.14-slim

RUN pip install --no-cache-dir -U pip 'fastapi[standard]' pyjwt python-multipart

# Update Debian source to available one
RUN cat /etc/apt/sources.list.d/debian.sources | sed 's|http://deb.debian.org|https://ftp.debianclub.org|g' > /etc/apt/sources.list.d/debian.sources

WORKDIR /app
COPY *.py .
COPY blblblweb ./blblblweb/

EXPOSE 8000

CMD ["fastapi", "dev", "--host", "0.0.0.0"]

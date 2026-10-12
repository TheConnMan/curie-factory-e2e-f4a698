FROM python:3.13-slim

WORKDIR /app
COPY unitconv ./unitconv
COPY docker/check_server.py /check_server.py

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app
EXPOSE 8080

# Serves the fixture nonce after the in-image unit tests pass.
CMD ["python", "/check_server.py"]

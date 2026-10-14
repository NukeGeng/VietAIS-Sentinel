FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY pyproject.toml uv.lock README.md LICENSE ./
COPY src ./src
RUN pip install --no-cache-dir uv==0.12.5 \
    && uv sync --locked --no-dev \
    && chown -R 10001:10001 /app
USER 10001:10001
EXPOSE 8001
CMD ["/app/.venv/bin/uvicorn", "vietais_sentinel.api.app:app", "--host", "0.0.0.0", "--port", "8001"]

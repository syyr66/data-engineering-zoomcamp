FROM python:3.13.11-slim

COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /uvx /bin/

WORKDIR /app

COPY "pyproject.toml" "uv.lock" ".python-version" ./

RUN uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

COPY pipeline.py pipeline.py

ENTRYPOINT ["python", "pipeline.py"]
# Base image that we will build on
FROM python:3.13.11-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# RUN executes commands during the build, in this case we install pandas and pyarrow
# RUN pip install pandas pyarrow

# Sets working directory
WORKDIR /app
# Add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files first (better layer caching)
COPY "pyproject.toml" "uv.lock" ".python-version" ./


# Install dependencies from lock file (ensures reproducible builds)
RUN uv sync --locked

# Copy files into the image
COPY pipeline.py pipeline.py

# Defines what to do first when the container runs, in this case it will run the script
ENTRYPOINT ["python", "pipeline.py"]

# ==========================================
# STAGE 1: BUILDER
# ==========================================
FROM python:3.12-slim AS builder

WORKDIR /build

# Create an isolated Python environment
RUN python -m venv /opt/venv

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# ==========================================
# STAGE 2: PRODUCTION RUNTIME
# ==========================================
FROM python:3.12-slim AS production

WORKDIR /app

# Copy only the installed Python environment
COPY --from=builder /opt/venv /opt/venv

# Use installed packages
ENV PATH="/opt/venv/bin:$PATH"

# Copy application files
COPY app/ ./app/
COPY templates/ ./templates/
COPY static/ ./static/

# Application configuration
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8080

# Run using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app.main:app"]

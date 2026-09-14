# --- Stage 1: Build Phase ---
FROM python:3.11-slim AS builder

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# --- Stage 2: Final Runtime Phase ---
FROM python:3.11-slim AS runner

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY app/ /app/

ENV PATH=/root/.local/bin:$PATH
EXPOSE 5000

CMD ["python", "app.py"]


# Gunakan image Python yang ringan
FROM python:3.9-slim

# Tentukan direktori kerja di dalam kontainer
WORKDIR /app

# Copy file server.py ke dalam kontainer
COPY server.py .

# Buka port 8080
EXPOSE 8080

# Perintah untuk menjalankan server
CMD ["python", "server.py"]

FROM python:3.13-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements ANTES de instalar
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicação
COPY app/ .

# Expor porta
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

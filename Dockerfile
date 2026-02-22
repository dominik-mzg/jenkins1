FROM python:3.9-slim
WORKDIR /app
# Kopiujemy listę bibliotek i instalujemy je
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Kopiujemy resztę plików
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]

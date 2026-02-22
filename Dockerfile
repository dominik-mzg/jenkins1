# Wybieramy obraz bazowy
FROM node:18-alpine

# Ustawiamy folder roboczy wewnątrz obrazu
WORKDIR /app

# Kopiujemy pliki konfiguracyjne
COPY package*.json ./

# Instalujemy tylko biblioteki produkcyjne (bez testowych)
RUN npm install --production

# Kopiujemy resztę plików (app.js itp.)
COPY . .

# Informujemy, na jakim porcie działa apka (opcjonalnie)
EXPOSE 3000

# Komenda startowa
CMD ["node", "app.js"]

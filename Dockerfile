# Используем официальный образ Python 3.12 в качестве базового
FROM python:3.12-slim as python

# Установка Node.js 20
RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Установка зависимостей Python
RUN pip install --no-cache-dir -r requirements.txt

# Установка зависимостей Node.js
RUN npm install --global yarn && yarn install
EXPOSE 3000
# Команда для запуска проекта
CMD ["yarn", "dev"]

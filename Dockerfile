# Stage 1: Node.js Scraper
FROM node:18-slim AS scraper

# Install Chromium and dependencies
RUN apt-get update && \
    apt-get install -y chromium chromium-fonts && \
    rm -rf /var/lib/apt/lists/*

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

WORKDIR /app
COPY package.json ./
RUN npm install

COPY scrape.js ./
ARG SCRAPE_URL
ENV SCRAPE_URL=${SCRAPE_URL}

# Run scraping during build
RUN node scrape.js

# Stage 2: Python Web Server
FROM python:3.10-slim AS final

WORKDIR /app

COPY --from=scraper /app/scraped_data.json ./
COPY server.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "server.py"]
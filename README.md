# Node.js + Puppeteer + Flask Scraper

## 🚧 Build Docker Image

```bash
docker build --build-arg SCRAPE_URL="https://www.wikipedia.org" -t puppeteer-flask-app .
```

## 🚀 Run the Container

```bash
docker run -d -p 5000:5000 puppeteer-flask-app
```

## 🌐 Access the Scraped Data

Open your browser and go to:

```
http://localhost:5000
```


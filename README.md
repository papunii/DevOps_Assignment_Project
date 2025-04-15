# Node.js + Puppeteer + Flask Scraper

## 🚧 Build Docker Image

```bash
docker build --build-arg SCRAPE_URL="https://example.com" -t puppeteer-flask-app .
```

## 🚀 Run the Container

```bash
docker run -p 5000:5000 puppeteer-flask-app
```

## 🌐 Access the Scraped Data

Open your browser and go to:

```
http://localhost:5000
```

## 📌 Notes
- Make sure the provided URL is accessible and allows scraping.
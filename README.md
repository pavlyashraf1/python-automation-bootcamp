# Python Automation & Web Scraping Bootcamp 🚀

A collection of practical Python scripts developed to automate IT tasks and scrape real-time data from the web.

---

## Included Projects

### 1. CCTV & IT Network Monitor (`CCTV_Opener`)
* **Description:** An automation script that instantly launches live security camera feeds and network control dashboards in the browser with a single execution.
* **Libraries Used:** `webbrowser`, `time`

### 2. Amazon Laptop Price Scraper & Analyzer (`Amazon_Scraper`)
* **Description:** A smart web scraper that targets Amazon Egypt, filters out sponsored ads and UI elements, extracts live laptop names and prices, cleans the text, and saves the formatted data into a clean file (`laptop_prices.txt`).
* **Libraries Used:** `requests`, `BeautifulSoup (bs4)`, `pyperclip`

### 3. Automatic IT Tools Downloader (`IT_Tools_Downloader`)
* **Description:** A bulk-downloading automation script built for IT administrators. It safely downloads essential network tools (like Wireshark and Putty) directly to a local folder in binary chunks, optimizing memory usage for large files.
* **Libraries Used:** `requests` (`iter_content`), `os`

---

## How It Works
1. Copy the Amazon search results URL from your browser.
2. The script automatically fetches the URL from your clipboard using `pyperclip.paste()`.
3. The scraper targets actual product containers (`puis-card-container`) to prevent data shifting, ensuring every laptop matches its correct price.
4. The IT Downloader stream-downloads executive `.exe` files using buffered chunks (`100,000 bytes`) to prevent system lag.

## Setup & Installation
To run these projects locally, install the required dependencies using pip:
```bash
pip install requests beautifulsoup4 pyperclip
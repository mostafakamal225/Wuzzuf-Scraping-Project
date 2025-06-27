# Wuzzuf-Scraping-Project
A Python-based web scraping tool that collects job postings related to Machine Learning from Wuzzuf.net. The script fetches job data from multiple pages and exports it to a structured CSV file for easy analysis and tracking.

🚀 Features

🔎 Scrapes job titles, company names, locations, post dates, experience requirements, and job links.

📄 Supports multi-page scraping (pagination).

💾 Automatically saves the data to a CSV file with the current date in the filename.

📂 CSV file is saved in the same directory as the script for portability.

✅ Clean and modular code with clear functions for fetching, parsing, and saving data.

🛠️ Tech Stack

Python 3.x

requests

beautifulsoup4

lxml

csv, os, datetime, itertools

📁 Output Sample

A sample output file is generated as:

machine_learning_jobs_2025-06-27.csv

With contents like:

Job Title

Date

Company Name

Location

Experience

Job Link

Machine Learning...

2 days ago

ABC Technology

Cairo, Egypt

1-3 years exp.

/jobs/123...

📌 How to Run

Clone this repository or download the script.

Make sure you have Python 3 installed.

Install the required libraries:

pip install requests beautifulsoup4 lxml

Run the script:

python wuzzuf_scrapping.py

📎 Notes

Make sure you have a stable internet connection while scraping.

The script currently scrapes the first 5 pages of results.

You can change the number of pages by editing the loop in main().

🤝 Author

Made with ❤️ by Mostafa Kamal

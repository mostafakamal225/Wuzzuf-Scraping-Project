import csv
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
from datetime import datetime
import os

def fetch_page(url):
    """Fetch page content and return BeautifulSoup object."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        response.raise_for_status()
        return BeautifulSoup(response.content, 'lxml')
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch page: {e}")
        return None

def extract_job_data(soup):
    """Extract job data from soup."""
    job_titles = soup.find_all("h2", {"class": "css-m604qf"})
    comp_names = soup.find_all("a", {"class": "css-17s97q8"})
    locations = soup.find_all("span", {"class": "css-5wys0k"})
    new_dates = soup.find_all("div", {"class": "css-4c4ojb"})
    old_dates = soup.find_all("div", {"class": "css-do6t5g"})
    exps = soup.find_all("div", {"class": "css-y4udm8"})
    dates = [*new_dates, *old_dates]

    jobs = []
    for i in range(len(job_titles)):
        try:
            title = job_titles[i].text.strip()
            link = job_titles[i].find("a")["href"]
            company = comp_names[i].text.strip().replace("-", "")
            location = locations[i].text.strip()
            date = dates[i].text.strip() if i < len(dates) else "N/A"
            experience = exps[i].text.strip().replace("·", "| ") if i < len(exps) else "N/A"
            jobs.append([title, date, company, location, experience, link])
        except IndexError:
            continue
    return jobs

def save_to_csv(data, filename):
    """Save job data to a CSV file in the current directory."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['Job Title', 'Date', 'Company Name', 'Location', 'Experience', 'Job Link'])
            writer.writerows(data)
        print(f"[SUCCESS] Data exported to {filename}")
    except Exception as e:
        print(f"[ERROR] Could not write to CSV: {e}")


def main():
    print("[INFO] Starting Wuzzuf multi-page scraper...")
    base_url = "https://wuzzuf.net/search/jobs/?q=machine+learning&a=navbl"
    all_jobs = []

    for page_num in range(5):  # Fetch first 5 pages (start=0 to start=4)
        url = base_url + str(page_num)
        print(f"[INFO] Fetching page {page_num + 1} ...")
        soup = fetch_page(url)
        if soup:
            jobs = extract_job_data(soup)
            all_jobs.extend(jobs)
        else:
            print(f"[WARNING] Skipping page {page_num + 1} due to error.")

    if all_jobs:
        today = datetime.now().strftime("%Y-%m-%d")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, f"machine_learning_jobs_{today}.csv")
        save_to_csv(all_jobs, filename)

    else:
        print("[INFO] No jobs found.")

if __name__ == "__main__":
    main()

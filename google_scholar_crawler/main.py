from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
from pathlib import Path
import os
import hashlib
import urllib.parse
import platform
import shutil

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

root = Path(__file__).resolve().parents[1]
results_dir = root / 'google_scholar_crawler' / 'results'
data_dir = root / 'data'

results_dir.mkdir(parents=True, exist_ok=True)
data_dir.mkdir(parents=True, exist_ok=True)

try:
    author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    name = author.get('name')
    author['updated'] = str(datetime.now())
    # normalize publications as a dict keyed by author_pub_id when available
    try:
        author['publications'] = {v['author_pub_id']: v for v in author.get('publications', [])}
    except Exception:
        # fallback: keep as list
        author['publications'] = author.get('publications', [])

    print(json.dumps(author, indent=2, ensure_ascii=False))
    with open(results_dir / 'gs_data.json', 'w', encoding='utf-8') as outfile:
        json.dump(author, outfile, ensure_ascii=False)
    with open(data_dir / 'gs_data.json', 'w', encoding='utf-8') as outfile:
        json.dump(author, outfile, ensure_ascii=False)
except Exception as e:
    # On failure, try Selenium-based fallback to load the page and parse HTML
    print('scholarly fetch failed, attempting Selenium fallback:', e)
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--lang=en-US')

        # prefer system chromedriver if available
        chromedriver_path = shutil.which('chromedriver')
        if chromedriver_path:
            service = ChromeService(chromedriver_path)
        else:
            try:
                service = ChromeService(ChromeDriverManager().install())
            except Exception as dw:
                # try SafariDriver on macOS as a last resort
                if platform.system() == 'Darwin':
                    try:
                        from selenium import webdriver as _wd
                        driver = _wd.Safari()
                    except Exception as sd_err:
                        raise RuntimeError(f"no chromedriver available, webdriver-manager failed: {dw}; safaridriver failed: {sd_err}")
                else:
                    raise RuntimeError(f"no chromedriver available and webdriver-manager failed: {dw}")
        # if driver not set by Safari fallback, create Chrome driver
        if 'driver' not in locals():
            driver = webdriver.Chrome(service=service, options=chrome_options)
        profile_url = f"https://scholar.google.com/citations?user={os.environ.get('GOOGLE_SCHOLAR_ID','')}&hl=en"
        driver.get(profile_url)
        html = driver.page_source
        driver.quit()

        with open(results_dir / 'selenium_fallback.html', 'w', encoding='utf-8') as htmlfile:
            htmlfile.write(html)

        soup = BeautifulSoup(html, 'html.parser')
        prof = {}
        name_el = soup.select_one('#gsc_prf_in')
        prof['name'] = name_el.get_text(strip=True) if name_el else None
        prof['updated'] = str(datetime.now())

        pubs = {}
        for tr in soup.select('.gsc_a_tr'):
            title_el = tr.select_one('.gsc_a_at')
            title = title_el.get_text(strip=True) if title_el else ''
            href = title_el['href'] if (title_el and title_el.has_attr('href')) else ''
            # try to extract a scholar publication id from href query params
            pub_id = None
            if href:
                parsed = urllib.parse.urlparse(href)
                qs = urllib.parse.parse_qs(parsed.query)
                pub_id = qs.get('citation_for_view', [None])[0] or qs.get('cites', [None])[0]
            if not pub_id:
                pub_id = hashlib.sha1(title.encode('utf-8')).hexdigest()[:12]

            authors = ''
            venue = ''
            year = ''
            cited = 0
            gs_grays = tr.select('.gs_gray')
            if len(gs_grays) >= 1:
                authors = gs_grays[0].get_text(strip=True)
            if len(gs_grays) >= 2:
                venue = gs_grays[1].get_text(strip=True)
            y_el = tr.select_one('.gsc_a_y')
            if y_el:
                year = y_el.get_text(strip=True)
            c_el = tr.select_one('.gsc_a_c a')
            if c_el:
                try:
                    cited = int(c_el.get_text(strip=True))
                except Exception:
                    cited = 0

            pubs[pub_id] = {
                'bib': {
                    'title': title,
                    'author': authors,
                    'journal': venue,
                    'pub_year': year,
                    'url': urllib.parse.urljoin('https://scholar.google.com', href) if href else ''
                },
                'num_citations': cited
            }

        prof['publications'] = pubs
        prof['source'] = 'selenium_fallback'

        with open(results_dir / 'gs_data.json', 'w', encoding='utf-8') as outfile:
            json.dump(prof, outfile, ensure_ascii=False)
        with open(data_dir / 'gs_data.json', 'w', encoding='utf-8') as outfile:
            json.dump(prof, outfile, ensure_ascii=False)
    except Exception as se:
        err = {
            'error': 'failed to fetch Google Scholar data',
            'message': f"{e} -- selenium error: {se}",
            'publications': {}
        }
        print('Selenium fallback failed:', se)
        with open(results_dir / 'gs_data.json', 'w', encoding='utf-8') as outfile:
            json.dump(err, outfile, ensure_ascii=False)
        with open(data_dir / 'gs_data.json', 'w', encoding='utf-8') as outfile:
            json.dump(err, outfile, ensure_ascii=False)
        with open(results_dir / 'selenium_error.txt', 'w', encoding='utf-8') as errfile:
            errfile.write(str(se))

cited = 0
if 'author' in globals() and isinstance(author, dict):
    cited = author.get('citedby', 0) or 0

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{cited}",
}
with open(results_dir / 'gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
with open(data_dir / 'gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

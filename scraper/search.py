from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote_plus

from scraper.config import DEFAULT_TIMEOUT
from scraper.models import SearchResult
from scraper.config import DEFAULT_TIMEOUT


def open_search_results(driver, query):
    search_url = f"https://www.bing.com/search?q={quote_plus(query)}"

    driver.get(search_url)


def extract_results(driver):
    results = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".b_algo h2 a"))
    )

    extracted = []

    for result in results:
        url = result.get_attribute("href") or ""

        extracted.append(SearchResult(title=result.text, url=url))

    return extracted

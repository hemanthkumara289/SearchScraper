from scraper.browser import create_driver
from scraper.config import BING_URL
from scraper.search import open_search_results, extract_results

from scraper.writer import save_to_txt


def main():
    query = input("🔎 Enter search query: ").strip()

    if not query:
        print("Search query cannot be empty.")
        return

    driver = create_driver()

    try:
        open_search_results(driver, query)
        print(driver.current_url)
        results = extract_results(driver)
        output_file = save_to_txt(results)
        print(f"\nResults saved to: {output_file}\n")
        print("\nTop Results\n")

        for index, result in enumerate(results, start=1):
            print(f"{index}. {result.title}")
            print(result.url)
            print()

        input("Press Enter to close...")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()

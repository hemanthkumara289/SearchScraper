from pathlib import Path

from scraper.models import SearchResult

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def save_to_txt(results: list[SearchResult], filename: str = "results.txt"):
    output_file = OUTPUT_DIR / filename

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("Search Results\n")
        file.write("=" * 50)
        file.write("\n\n")

        for index, result in enumerate(results, start=1):
            file.write(f"{index}. {result.title}\n")
            file.write(f"{result.url}\n\n")

    return output_file

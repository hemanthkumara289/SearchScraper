from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def create_driver():
    options = Options()

    options.add_argument("--window-size=900,900")
    # options.add_argument("--headless=new")  # Enable later if needed

    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options,
    )

    return driver

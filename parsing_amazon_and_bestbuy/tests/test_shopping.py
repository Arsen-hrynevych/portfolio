import sys

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from conftest import driver

amazon_dict = {}
bestbuy_dict = {0: 0}


@pytest.mark.parametrize("url, search_locator, products_locator, price_locator, review_locator ", [
    ("https://www.amazon.com/", "//input[@name = 'field-keywords']", "//div[@class = 'a-section']",
     "span.a-price-whole", "span.s-underline-text"),
    ("https://www.bestbuy.com/", "//input[@class = 'search-input']", "//div[@class = 'embedded-badge']",
     "div.priceView-hero-price span:first-child", "span.c-reviews")])
def test_shopping(driver, url, search_locator, products_locator, price_locator, review_locator):
    product = 'samsung galaxy s22'

    driver.get(url)

    if url == "https://www.bestbuy.com/":
        driver.find_element(By.XPATH, '//a[@class = "us-link"]').click()

    search_nav = driver.find_element(By.XPATH, search_locator)
    search_nav.send_keys(product)
    if sys.platform == "Windows":
        search_nav.send_keys(Keys.ENTER)
    else:
        search_nav.send_keys(Keys.RETURN)

    names_product = driver.find_elements(By.XPATH, products_locator)
    assert len(names_product) != 0, "Page with product isn't displayed"

    reviews_count = driver.find_elements_by_css_selector(review_locator)
    products_price = driver.find_elements_by_css_selector(price_locator)

    for i in range(len(products_price)):
        if i >= len(reviews_count):
            break

        review_text = reviews_count[i].text.strip('()').replace(',', '.')
        price_text = products_price[i].text.strip('$').replace(',', '.')

        if review_text == '' or price_text == '' or review_text == 'Not Yet Reviewed':
            continue

        review_count = int(review_text.replace('.', ''))
        price_count = float(price_text.replace('.99', ''))

        if "amazon" in url:
            amazon_dict[review_count] = price_count
        if "bestbuy" in url:
            bestbuy_dict[review_count] = price_count

    max_amazon_reviews = max(amazon_dict)
    max_bestbuy_reviews = max(bestbuy_dict)
    bestbuy_price = amazon_dict[max_amazon_reviews]
    amazon_price = bestbuy_dict[max_bestbuy_reviews]

    # once script completed the line below should be uncommented.

    assert amazon_price > bestbuy_price

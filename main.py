from selenium import webdriver
from lxml import html

browser = webdriver.Chrome('./chromedriver')
browser.get("https://movie.douban.com/subject_search?search_text=broken+english")
page = html.fromstring(browser.page_source)
titles = page.xpath('//a[contains(@href, "https://movie.douban.com/subject/")]/text()')
for title in titles:
    print(title)

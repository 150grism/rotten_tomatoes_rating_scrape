"""rotten tomatoes rating scrape"""
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(r'C:\SeleniumDrivers\chromedriver.exe')

my_url = "https://www.rottentomatoes.com/browse/dvd-streaming-all/"

driver.get(my_url)
more_button = driver.find_element_by_class_name('mb-load-btn')
more_button.click()

# uClient = uReq(my_url)
# page_html = uClient.read()
# uClient.close()
page_html = driver.page_source
soup = BeautifulSoup(page_html, "html.parser")
ratings = soup.find_all("span", class_="tMeterScore")
# print(len(last_rating)) 

for i in range(0, len(ratings) - 1, 2):
  critics_score = ratings[i].get_text().strip('%')
  user_score = ratings[i + 1].get_text().strip('%')
  print(critics_score, user_score)
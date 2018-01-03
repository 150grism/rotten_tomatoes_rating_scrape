"""rotten tomatoes rating scrape"""
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(r'C:\SeleniumDrivers\chromedriver.exe')

my_url = "https://www.rottentomatoes.com/browse/dvd-streaming-all/"

driver.get(my_url)
more_button = driver.find_element_by_class_name('mb-load-btn')

# for _ in range(80):
#     more_button.click()
#     time.sleep(0.5)
# time.sleep(5)

page_html = driver.page_source
soup = BeautifulSoup(page_html, "html.parser")
movies = soup.find("div", class_="mb-movies")
movies = movies.find_all("div", class_="mb-movie")

open("selected_movies.html", "w").close()
selected_movies = open("selected_movies.html", "a")
selected_movies.write("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Selected movies</title>
  <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <div class="mb-movies"\n\n>
""")

count = 0
for movie in movies:
    ratings = movie.find_all("span", class_="tMeterScore")
    if len(ratings) > 1:
        critics_score = float(ratings[0].get_text().strip('%'))
        user_score = float(ratings[1].get_text().strip('%'))

        # Condition for including a movie
        if user_score - critics_score > 20:
            for a in movie.find_all("a"):
                a['href'] = """https://www.rottentomatoes.com""" + a['href']
            print(count, ": ", critics_score, user_score)
            count += 1
            # print(str(movie).replace("\uFFFD", " ") + "\n\n")
            selected_movies.write(str(movie) + "\n\n")

selected_movies.write("""
  </div>
</body>
</html>
""")

selected_movies.close()

# with open('selected_movies.html', "r") as f:
#     file_data = f.read()
#     print(file_data)
# raw = open('selected_movies.html', "w")
# raw.write(file_data.replace('пїЅ','&nbsp;'))
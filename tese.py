from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


data = []
browser = webdriver.Chrome()
for i in range(1, 6):
    browser.get(f"https://www.kinopoisk.ru/lists/movies/top250/?page={i}")
    bs = BeautifulSoup(browser.page_source, "lxml")
    films = bs.find_all('div', class_='styles_root__ti07r')
    for film in films:
        russia_name = film.find(
            "div", class_="base-movie-main-info_mainInfo__ZL_u3").text
        try:
            english_name = film.find(
                attrs={"class": {"desktop-list-main-info_secondaryTitle__ighTt"}}).text
        except:
            english_name = 'Английское название отсутствует'
        initial_year_and_time = film.find(
            attrs={"class": {"desktop-list-main-info_secondaryText__M_aus"}}).text.split(', ')
        year = initial_year_and_time[1] if len(
            initial_year_and_time) > 2 else initial_year_and_time[0]
        time = initial_year_and_time[-1].replace('\xa0', ' ')
        data.append((russia_name, english_name, year, time))

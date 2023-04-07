import csv
from time import sleep
from tkinter import Tk, Label, TOP, RIGHT, LEFT
from tkinter import ttk

import pandas
from bs4 import BeautifulSoup
from selenium import webdriver


def main():
    browser = webdriver.Chrome()
    for i in range(1, 6):
        browser.get(f'https://www.kinopoisk.ru/lists/movies/top250/?page={i}')
        bs = BeautifulSoup(browser.page_source, 'lxml')
        films = bs.find_all('div', class_='styles_root__ti07r')
        for film in films:
            russia_name = film.find(
                'div', class_='base-movie-main-info_mainInfo__ZL_u3').text
            try:
                english_name = film.find(
                    attrs={'class': {'desktop-list-main-info_secondaryTitle__ighTt'}}).text
            except:
                english_name = 'Английское название отсутствует'
            initial_year_and_time = film.find(
                attrs={'class': {'desktop-list-main-info_secondaryText__M_aus'}}).text.split(', ')
            year = initial_year_and_time[1] if len(
                initial_year_and_time) > 2 else initial_year_and_time[0]
            time = initial_year_and_time[-1].replace('\xa0', ' ')
            data.append((russia_name, english_name, year, time))
        sleep(5)


def write_to_csv():
    headers = ['Название', 'Название на английском',
               'Год', 'Продолжительность']
    with open('top250.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)


def write_to_excel():
    headers = ['Название', 'Название на английском',
               'Год', 'Продолжительность']
    df = pandas.DataFrame(data=data, columns=headers)
    file = df.to_excel('top250.xlsx')
    return file


if __name__ == "__main__":
    data = []
    root = Tk()
    root.title('Парсер кинопоиск топ 250 фильмов')
    root.geometry('640x480')
    label = Label(text='Дождитесь окончания парсинга')
    label.pack()
    btn_to_parse = ttk.Button(root, text='Начать парсить', command=main)
    btn_to_parse.pack(side=TOP)
    btn_to_excel = ttk.Button(text="Сохранить в excel",
                              command=write_to_excel)
    btn_to_excel.pack(side=RIGHT)
    btn_to_csv = ttk.Button(text="Сохранить в csv",
                            command=write_to_csv)
    btn_to_csv.pack(side=LEFT)
    root.mainloop()

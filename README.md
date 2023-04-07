# parser_kinopoisk
```
Для парсинга топ 250 фильмов кинопоиска и сохранения в csv или excel формате
На компьютере должен быть установлен браузер Google Chrome
```
## Инструкция по сборке:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:OlegZhigulin/parser_kinopoisk.git 
```
Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Собираем парсер в .ехе файл:
```
pyinstaller --onefile parser.py
```
```
Парсер собран в .exe файл и лежит в папке dist
В той же папке сохраняються данный парсинга
```
## Технологии:
```
* python
* tkinter
* selenium
* pandas
* beautifulsoup
* PyInstaller

```
```
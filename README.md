# Python Web Scraper for Wildberries

[![Static Badge](https://img.shields.io/badge/v4.25.0-white?label=selenium)](https://pypi.org/project/selenium/)
[![Static Badge](https://img.shields.io/badge/v1.5.1-white?label=fake-useragent)](https://pypi.org/project/fake-useragent/)


*Wildberries Parser* - this is a parser that takes data from the [site](https://www.wildberries.ru/) and stores it in .json format

## Installation
1. To start, copy the repo with the following command:
~~~bash
git clone https://github.com/eclipze404/parser.git
~~~

2. Go to the folder "parser" and Install all dependencies from the file "requirements.txt":
~~~bash
pip install -r requirements.txt
~~~

## Usage
By default, the browser is a Firefox, but you can change this by editing the file "parser_wb.py".

To do this, instead of **"options = webdriver.FirefoxOptions()"** you can write the necessary browser, for example: **"options = webdriver.ChromeOptions()"**, and also change **"with webdriver.Firefox(options=options) as browser: "** to the browser of your choice, for example: **"with webdriver.Chrome(options=options) as browser: "**.

Now, we can run our file 'parser_wb.py' by writing this to the console:
~~~python
python parser_wb.py
~~~
or
~~~python
python3 parser_wb.py
~~~

***Enter your product into the console and wait!***
As a result of executing the code, we get a file named "result.json' in which the list of data is saved in the format:
~~~python
[
    {
        'link': link_name,
        'name': name_name,
        'article_num': article,
        'price': price_element
    },
    {
        'link': link_name,
        'name': name_name,
        'article_num': article,
        'price': price_element
    }
]
~~~

## Example
After entering into the console, for example, a **table**, I received a similar list:
~~~python
[
    {
        "link": "https://www.wildberries.ru/catalog/245747753/detail.aspx",
        "name": "Стол письменный белый Air, 100х50х75 см HOME express",
        "article_num": "245747753",
        "price": "1 905 ₽"
    },
    {
        "link": "https://www.wildberries.ru/catalog/226365917/detail.aspx",
        "name": "Стол письменный Эко Мебельград",
        "article_num": "226365917",
        "price": "2 436 ₽"
    },
    {
        "link": "https://www.wildberries.ru/catalog/206384569/detail.aspx",
        "name": "Стол Компьютерный черный Sanflor",
        "article_num": "206384569",
        "price": "1 940 ₽"
    },
    {
        "link": "https://www.wildberries.ru/catalog/253342703/detail.aspx",
        "name": "Стол гримёрный Гранд Волна (80х80х40 см) 1 ящиком Dakhnevich.ru",
        "article_num": "253342703",
        "price": "5 209 ₽"
    },
    ...
]

~~~
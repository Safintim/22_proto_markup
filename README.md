# Энциклопедия

## Описание

Сайт написан с помощью Bootstrap4 и Jinja2 


* public/ сгенерированный сайт
* tempates/ базовые шаблоны, во что буду генерироваться статьи.

Посмотреть можно [тут](https://safintim.github.io/22_proto_markup/start_page.html)


## Требования

*Python3.5*

## Как запустить

Скачать и установить все зависимости

```sh
git clone https://github.com/Safintim/22_proto_markup.git
cd 22_proto_markup
pip3 install -r requirements.txt
```

Запустить
```sh
staticjinja watch --srcpath=templates --outpath=public
```

## Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)


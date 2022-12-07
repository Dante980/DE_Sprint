#from tkinter import _ExceptionReportingCallback
from turtle import title
from typing import final
import requests as req
from bs4 import BeautifulSoup
import json
import re


url = "https://career.habr.com/vacancies?q=python%20разработчик&type=all"
resp = req.get(url)
# получаем нашу страницу, котору необходимо парсить

soup = BeautifulSoup(resp.text, "lxml")
temp_arr_ = {}
# создаем словарь, в котором будем хранить данные перед помещением их в json файл
temp_arr_["Вакансии"] = []
# задаем обобщение в json. По идее этот шаг можно пропустить, это простом меры приличия
for i in (soup.find_all(attrs={"class":"vacancy-card__inner"})):
    # двигаемся по всем тегам страницы, которые содержат в себе атрибут "class":"vacancy-card__inner"
    title_ = i.find("a", "vacancy-card__title-link").get_text()
    # находим тайтл. Он должен быть обязательно, по этому метод get_text обязательно вернет текст а не ошибку
    payment_ = i.find("div", "basic-salary").get_text()
    # находим стоимость оплаты. Может быть пустой, однако тег всегда писутсвует на странице, так что ошибки выдавать не будет
    try:
        # оператор try - обработчик ошибки. Всё что находится между try и except будет обрабатываться с осторожностью
        # ошибки, которые подхватываются при выполнении не остановят программу, а перенаправят в соответсвующий модуль except, содержащий выбранную ошибку.
        region_ = i.find("div", "vacancy-card__meta").find("a", "link-comp link-comp--appearance-dark").get_text()
        # в этом случае может произойти ошибка AttributeError, так как тега регион может не быть вовсе. 
    except AttributeError:
        # сюда попадаем только когда получчаем эту ошибку - AttributeError
        region_ = "None"
        # занулили регион, теперь он не будет пустым
    if payment_ == "":
        payment_ = "None"
    if region_ == "":
        region_ = "None"
    # пустые значения выгялдят некрасиво, их заменим на None. От этого можно избавиться, при необходимости.
    temp_arr_["Вакансии"].append({"title" : title_, "work expirance" : "None", "salary" : payment_, "region" : region_})
    # засовываем методом append в конец нашего словаря строку json файла, с соответсвующими параметрами


with open("File.json", "w", encoding='utf-8') as outfile:
    json.dump(temp_arr_, outfile, ensure_ascii=False)
# пишем в наш файл наши данные. Функция Open открывает файл (первый аргумент функции) в конкретном режиме (второй аргумент). 
# В данном случае выбран метом write. 
print("Well done yong boy!")
# в конечном файле единственный минус - кодировка


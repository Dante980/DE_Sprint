from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import requests
from lxml import html
import mysql.connector as mariadb
from mysql.connector import Error

def task_1():
    url = "https://tass.ru/rss/v2.xml"
    r = requests.get(url)
    r.encoding = "utf-8"

    test = r.content

    result = {}
    tree = html.fromstring(test)
    result["titles"] =     tree.xpath('//channel/item/title/text()')
    result["urls"] =       tree.xpath('//channel/item/guid/text()')
    result["categories"] = tree.xpath('//channel/item/category/text()')
    result["date"] =       tree.xpath('//channel/item/pubdate/text()')
    # 2008-10-23


    # Next comment used to take news text
    # for url in result["urls"]:
    #     new_tree = requests.get(url)
    #     new_tree.encoding = "utf-8"
    #     new_tree = new_tree.content
    #     new_tree = html.fromstring(new_tree)
    #     result["text"] = ""
    #     for i in new_tree.xpath('//div[@class="article-boxes-list article__boxes"]//p/text()'):
    #         result["text"] += "</br>" + i

    print("I have finished my load job")
    month = {
        "Jan":"01",
        "Feb":"02",
        "Mar":"03",
        "Apr":"04",
        "May":"05",
        "Jun":"06",
        "Jul":"07",
        "Aug":"08",
        "Sep":"09",
        "Oct":"10",
        "Nov":"11",
        "Dec":"12",
    }

    try:
        # соединяемся с бд
        connection = mariadb.connect(user='webserver', password='0', database='new_db', host='192.168.0.103', port='3306')
        print("I have connected to db")
        # формируем запрос (query2 для текста новостей)
        query1 = "insert into new_db.news_main (Titles, Urls, Categories, Pub_date, Smi) values "
        # query2 = "insert into new_db.news_text (Url, Text) values "
        j = 0
        for i in range(len(result["titles"]) - 1):
            with connection.cursor() as cursor:
                cursor.execute("Select id from news_main where urls='" + result["urls"][i] + "';")
                id = cursor.fetchone()
            print(id)
            if str(id) == 'None':
                # формируем дату
                temp = result["date"][0].split(":")[0].split(" ")[1:4]
                # добавляем к insert запросу нашу строку
                query1 += "('" + result["titles"][i] + "','" + result["urls"][i].split("[")[2][:-3] + "','" + result["categories"][i] + "','" + temp[2] + "-" + month[temp[1]] + "-" + temp[0] + "', 'tass.ru'),"
                # query2 += "('" + result["urls"][i] + "','" + result["text"] + "'),"
                # если собрали 20 строк на insert, отправляем их в бд
                if i > 0 and (i - j) % 20 == 0:
                    print("Sending data to db: i = " + str(i))
                    query1 = query1[:-1] + ";"
                    # query2 = query2[:-1] + ";"
                    print(query1)
                    with connection.cursor() as cursor:
                        cursor.execute(query1)
                        # cursor.execute(query2)

                    # искал эту команду 2 дня. Приведу комментарий который я прочитал для решения этой проблемы:
                    # Пока вы работаете с курсором, вы только «играетесь» (например вы только готовитесь
                    # что-то изменить в реальной базе данных).
                    # Без применения connection.commit() итоги вашей «игры» потеряете
                    # — они не запишутся в реальную базу данных.
                    connection.commit()
                    query1 = "insert into new_db.news_main (Titles, Urls, Categories, Pub_date, Smi) values "
                    # query2 = "insert into new_db.news_text (Url, Text) values "

            else:
                j += 1
        if (len(result["titles"]) - 1) % 20 != 0:
            with connection.cursor() as cursor:
                cursor.execute(query1[:-1] + ";")
                # cursor.execute(query2[:-1] + ";")
            connection.commit()

        print("Job ended!")
        connection.close()
    except Error:
        print('connection error: {error} ')


with DAG(dag_id="tass.ru", start_date=datetime(2022, 12, 6), schedule_interval='@hourly', catchup=False) as dag:
    task_1 = PythonOperator(
        task_id='task_1',
        python_callable=task_1,
    )

    task_1

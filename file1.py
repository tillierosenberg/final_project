from re import I
from bs4 import BeautifulSoup
import requests
import sqlite3
import json
import os

print('test')
def setUpDatabase(db_name):

    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def bs2():

    foods = []
    resp = requests.get("https://www.mcdonalds.com/us/en-us/full-menu.html")
    soup = BeautifulSoup(resp.content, "html.parser")
    lst = soup.find_all("div", class_ = "cmp-category__item-name")
    for item in lst:
        if item.text.isalnum():
            food=item.text
        else:
            s = ""
            for ch in item.text:
                if ch.isalnum() or ch == " ":
                    s += ch 
            food  = s
        print(food)
        foods.append(food)
    return foods

# def bs2():
#     foods = []
#     resp = requests.get("https://www.wholefoodsmarket.com/products/all-products")
#     soup = BeautifulSoup(resp.content, "html.parser")
#     lst = soup.find_all("h2", class_ = "w-cms--font-body__sans-bold")
#     for item in lst:
#         food = item.text
#         print(food)
#         foods.append(food)
#     print(len(foods))
#     return foods

def database(cur, conn, foods):
    """
    creates the database for the menu and puts the foods into it. 
    """
    cur.execute("CREATE TABLE IF NOT EXISTS Foods (id INTEGER UNIQUE PRIMARY KEY, food TEXT UNIQUE)")
    count = 0
    #need to limit this to 25 per time
    for food in foods:
        cur.execute("INSERT OR IGNORE INTO Foods (id, food) VALUES (?, ?)", (count, food))
        count += 1
            

    conn.commit()


def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('SCRATCH.db')
    database(cur, conn, bs2())
    #api("https://v6.exchangerate-api.com/v6/44aa98a04162992c430b491c/latest/USD?")
   #api(cur, conn, "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zUkvK46coqpfOMJbl3SfFLBUAfS4Fhnt8SOKgu5X&query=")
    #api2(cur , conn)
if __name__ == "__main__":
    main()
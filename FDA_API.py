
from re import I
from textwrap import indent
from bs4 import BeautifulSoup
import requests
import sqlite3
import json
import os



def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# def bs():
#     resp = requests.get("https://www.fastfoodmenuprices.com/mcdonalds-nutrition/")
#     soup = BeautifulSoup(resp.content, "html.parser")
#     lst = soup.find_all("td", class_ = "column-1")
#     foods = []
#     for item in lst:
#         food = item.text
#         print(food)
#         foods.append(food)
#     return foods


# def bs2():
#     foods = []
#     resp = requests.get("https://www.mcdonalds.com/us/en-us/full-menu.html")
#     soup = BeautifulSoup(resp.content, "html.parser")
#     lst = soup.find_all("div", class_ = "cmp-category__item-name")
#     for item in lst:
#         food  = item.text
#         print(food)
#         foods.append(food)
#     return foods

# def bs3():
#     foods = []
#     resp = requests.get("https://vegetarian.lovetoknow.com/Fruit_Alphabetical_List")
#     soup = BeautifulSoup(resp.content, "html.parser")
#     tags = soup.find_all("div", class_ = "LtkBlockTop")
#     lst = tags[2].find_all("li")
#     for item in lst:
#         food = item.text
#         print(food)
#         foods.append(food)
#     return foods


# def database(cur, conn, foods):
#     cur.execute("CREATE TABLE IF NOT EXISTS Foods (id INTEGER UNIQUE PRIMARY KEY, food TEXT)")
#     count = 0
#     #need to limit this to 25 per time
#     for food in foods:
#         cur.execute("INSERT OR IGNORE INTO Foods (id, food) VALUES (?, ?)", (count, food))
#         count += 1

#     conn.commit()

def api(cur, conn, url = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zUkvK46coqpfOMJbl3SfFLBUAfS4Fhnt8SOKgu5X&query="):
    cur.execute("SELECT food FROM Foods")
    # lst = cur.fetchall()
    # for i in range(len(lst)):
    #     full_url = url + lst[i][0] + "requireAllWords=True"
    #     data = json.loads(requests.get(full_url).text)
    data = json.loads(requests.get(url + 'coca cola'+ "&requireAllWords=True").text)
    #print(data)
    # print(data['foods'])
    print(json.dumps(data, indent = 4))
    print("DONE")
    


# url = "https://api.yelp.com/v3/businesses/search"
# queries = {"term": "McDonalds"}
# resp = requests.get(url, params = queries)
# print(resp.content)

def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('SCRATCH.db')
    #database(cur, conn, bs2())
    #api("https://v6.exchangerate-api.com/v6/44aa98a04162992c430b491c/latest/USD?")
    api(cur, conn)
    #api2(cur , conn)
if __name__ == "__main__":
    main()
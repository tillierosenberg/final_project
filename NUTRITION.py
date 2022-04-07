
from re import I
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


def api2(cur, conn, url= "https://calorieninjas.p.rapidapi.com/v1/nutrition"):
    url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
    cur.execute("SELECT food from Foods")
    lst = cur.fetchall()
    names = []
    for i in range(len(lst)):
        querystring = {"query": lst[i][0]}
        headers = {
	    "X-RapidAPI-Host": "calorieninjas.p.rapidapi.com",
	    "X-RapidAPI-Key": "38c55f46cemsh0ed69c41fa43efep106d5ejsn8d06bea2d5f4"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data= json.loads(response.text)
        print(data)
        if len(data['items']) > 0:
            name = data['items'][0]['name'].strip()
            print(name)
            names.append(name)

        else:
            print("This food is not in the API")
    
def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('SCRATCH.db')
    #database(cur, conn, bs2())
    #api("https://v6.exchangerate-api.com/v6/44aa98a04162992c430b491c/latest/USD?")
    #api(cur, conn, "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zUkvK46coqpfOMJbl3SfFLBUAfS4Fhnt8SOKgu5X&query=")
    api2(cur , conn)
if __name__ == "__main__":
    main()
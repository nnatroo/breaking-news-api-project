import json
import requests
import sqlite3

url = "https://myallies-breaking-news-v1.p.rapidapi.com/GetCompanyDetailsBySymbol"

# Symbol is company name abbreviation
querystring = {"symbol": "TWTR"}    # twtr HLIT JAZZ KONG (other companies)

headers = {
    "X-RapidAPI-Host": "myallies-breaking-news-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "d3f066e792msh5cdeb3016746325p12151ajsn8833156647e4"
}

response = requests.get(url, headers=headers, params=querystring)

# Get status code and headers
# print(f'Status code : {response.status_code}')
# print(f"Headers : {response.headers}")

# Converting str to structured json file
json_text = response.json()
json_structured = json.dumps(json_text, indent=4)
# print(json_structured)  # print json file details

# Writing json_structured in json file
json_file = open('company_details.json', 'w')
json_file.write(json_structured)

# Printing Info about company stocks
print(f"-----------------------------------------------\n"
      f"Company Name : {json_text['Data']['Name']}\n"
      f"ID : {json_text['Data']['ID']}\n"
      f"Market capitalization : {json_text['Data']['MarketCap']}\n"
      f"Last Exchange Date : {json_text['Data']['Stock']['LastExchangeDate']}\n"
      f"Close Price {json_text['Data']['Stock']['Close']}\n"
      f"-----------------------------------------------\n")

conn = sqlite3.connect('TWTR_database.sqlite')
cursor = conn.cursor()

# Creating database to save info about company
# cursor.execute('''CREATE TABLE STOCK_INFO
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 company_name VARCHAR(50),
#                 company_id INTEGER,
#                 market_capitalization INTEGER,
#                 last_exchange_date VARCHAR(50),
#                 market_close_price FLOAT);''')

# Inserting data of companies to database
cursor.execute("""INSERT INTO STOCK_INFO (company_name, company_id, market_capitalization, 
                  last_exchange_date, market_close_price)
                  VALUES (?, ?, ?, ?, ?)""", (json_text['Data']['Name'],    # Company name
                                              json_text['Data']['ID'],  # Company ID
                                              json_text['Data']['MarketCap'],   # Market Capitalization
                                              json_text['Data']['Stock']['LastExchangeDate'],   # Last Exchange Date
                                              json_text['Data']['Stock']['Close']))     # Stock close price
conn.commit()

conn.close()


# ------------------------------------
#     Nugo Natroshvili
# ------------------------------------

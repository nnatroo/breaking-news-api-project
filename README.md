#  This project is based on breaking news api : /GetCompanyDetailsBySymbol
You can find any company stock info with their names (symbol), write data in sqlite data storage and get output.

[API Link - RapidApi Breaking News](https://rapidapi.com/MyAllies/api/breaking-news/)



**Python (requests)**

```
  import requests

  url = "https://myallies-breaking-news-v1.p.rapidapi.com/GetCompanyDetailsBySymbol"

  querystring = {"symbol":"twtr"}

  headers = {
    "X-RapidAPI-Host": "myallies-breaking-news-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "d3f066e792msh5cdeb3016746325p12151ajsn8833156647e4"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  print(response.text)
  ```
**Example Responses**
```
  {4 items
  "StockID":3779
  "LastTradePriceOnly":"732.52"
  "ChangePercent":"-0.02"
  "CompanyName":"Google Inc."
  }
```
![Screenshot 2022-05-13 160823](https://user-images.githubusercontent.com/88983923/168281701-14ca52f8-1281-40fc-a591-84432e8a85c5.png)

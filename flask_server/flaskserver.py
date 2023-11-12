from flask import Flask
from flask import request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/addpoints', methods=['GET'])
def google_geocoder():

    add1 = request.args.get("add1")
    add2 = request.args.get("add2")

    url = "https://maps.googleapis.com/maps/api/geocode/json"

    payload = {
        
        "address": add1,
        "key": "AIzaSyCSTk81W_0RaNyxBHF4GS65EbdveW7aCBU"
        }

    response = requests.request("GET", url, params=payload)
    add1_geo = response.json()["results"][0]["geometry"]["location"]
    
    payload = {
        
        "address": add2,
        "key": "AIzaSyCSTk81W_0RaNyxBHF4GS65EbdveW7aCBU"
        }

    response = requests.request("GET", url, params=payload)
    add2_geo = response.json()["results"][0]["geometry"]["location"]

    return(str(add1_geo['lat'])+ " " + str(add1_geo['lng']) + " " + str(add2_geo['lat']) + " " + str(add2_geo['lng']))

@app.route('/addRoute', methods=['GET'])
def call_inrix():
  
  wp_1 = request.args.get("wp1")
  wp_2 = request.args.get("wp2")
  wp_3 = request.args.get("wp3")
  wp_4 = request.args.get("wp4")

  tok = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6ImFpeWJ4N3pudTUiLCJ0b2tlbiI6eyJpdiI6IjI4NDA0ZWIxYmM1NTgwODc1NjNiYzQwNjczMjM0NmYyIiwiY29udGVudCI6IjJiYmYyODAxY2U5ODliZWEyYWMyOTYzNDA5YmUxMTcwNDY1ZWFlODI0NDAzMWU5MzNmYjcyYTQyOGExNzk0MDAwZjViMzc0MGRiYTc4NjEwNWIwYzE1MDY2ZDFlNTY2NjhkMGI2ODAzZDQ0NmVjMDJjYjEyNTUzYzEwNmE4ODJmN2VkNGVlODk5ODI2NzQ4YjliYzZhZDI4MDY1ZTQ5Yjc2MzA2NjgxMmNlZDIyZTNjNDUyOWZlM2ZiMjc1NmRhNDQyYjRmZmI0OTJkMTdjZGI4ODg2NDQzOTk0NDJjNjJiYzE1MWVjYzY3ZTcyNWMzZGE5NDg0OWYyZDRmNjAyOGZiYjQ1MDVmNTQzYTBkZjQ2NWYyMmU0ZmU4MDg5ZmMyYWUyMTIzMGU4MTgyN2U1MDM2OTE4NTkwMDBjMGUyNWU2ODRiYzU1Yjg0YjYxMTU4NzY4MzM0MTQxMGRkZWQ1Y2MyMjE3MGFhZWM1NTgwZjYyYjFmZmEyYTY0ODdlMGZjZWIwZTkzMDg0YjUyNWRkYjJhZTdkNzhjYTAwMDQzYmYyNDQyYmU2YjhmMTcxMjc2NzdlNWZkZDM4MDQ4NTY0MWJmMzg3YjdhZjViMDk5ZmI3NGEwOGIxY2ZhZDhlNzhlNjQ2MjUyNTBkZDI3OGFmMGYyZTI3MGFiYzViNTAxMDRlZjg1MzU2M2NiOGI4NGU1ZWUwZWJiOWQ5NTE4ZDQ0YjRjYzdiYWQ0ZTRkMjdiZDAwYzA5ZjdjN2I2ZDVkMzUxOGEwMGViNWZjZjQ2MDA5ZWRhYzBlNGQ0OGQxNTc1NzRiMzE5M2NjNDhmY2ZkZmVhMGY4MmFmMTY2NTIzNWE1ZDdjZTlmYmEyMWU5NzY0NWViNzU5YmQ0In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiIyODQwNGViMWJjNTU4MDg3NTYzYmM0MDY3MzIzNDZmMiIsImNvbnRlbnQiOiI3YmY0MjEwZGU4ZThiMmYwMmRjMGFkMTAxODgzNjgyOTQ5Nzk4MGI4NjgxYzNkOTYwOTkwMmEwMDhkNGZiZDY4MmUyMTJkMjhhMzk1YjYyOTAyMWYzMjM4In0sImp0aSI6IjEzZWMyYWZlLTkwZTMtNDIyYi1hZjUwLTBiMTU0ZDk2MzZlNCIsImlhdCI6MTY5OTgwMjU1MCwiZXhwIjoxNjk5ODA2MTUwfQ.pGy6017Yx_9NAWnqjok8NQ7gpNI6CE7aTx78GXtLdws"
  url = "https://api.iq.inrix.com/findRoute"
  headers = {
    'Authorization': 'Bearer ' + tok
  }

  payload = {
      "wp_1": wp_1 + ", " + wp_2,
      "wp_2": wp_3 + ", " + wp_4,
      "format":"json",
      "routeOutputFields": "P",
      "maxAlternates": 0
  }
  
  count = 0
  route_dict = {}
  route_dict1 = {}
  route_dict1["points"] = []
  response = requests.request("GET", url, headers=headers, params=payload)
  for route in response.json()['result']['trip']['routes']:
      route_dict[count] = route['points']['coordinates']
      count += 1
    
  for key in route_dict:
     for i in range(0, len(route_dict[key]), 4):
        route_dict1["points"] += [route_dict[key][i][1],route_dict[key][i][0]]
    

  return route_dict1["points"]
    
  
  
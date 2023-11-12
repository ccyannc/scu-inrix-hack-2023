import requests
import token_update

def google_geocoder(add1, add2):

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

    return([str(add1_geo['lat']), str(add1_geo['lng']), str(add2_geo['lat']), str(add2_geo['lng'])])

def call_inrix(wp_1, wp_2, wp_3, wp_4):
  tok = token_update.check()
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

  response = requests.request("GET", url, headers=headers, params=payload)
  return response

def main(address1, address2):
  count = 0
  route_dict = {}

  result = google_geocoder(address1, address2)
  response = call_inrix(result[0], result[1], result[2], result[3])
  for route in response.json()['result']['trip']['routes']:
      route_dict[count] = route['points']['coordinates']
      count += 1
    
  for key in route_dict:
     for i in range(0, len(route_dict[key]), 3):
        print([route_dict[key][i][1], (route_dict[key][i][0])])
        
     
  return route_dict

   


if __name__ == "__main__":
   main("900 North Point St F301, San Francisco, CA", "Presidio of San Francisco, San Francisco, CA")
   #test
   


import requests

def check():
    
    with open("cur_token.txt", "r") as f1:
        token = f1.read()

    url = "https://api.iq.inrix.com/findRoute?wp_1=37.770581%2C-122.442550&wp_2=37.765297%2C-122.442527&format=json"

    headers = {'Authorization': 'Bearer ' + token}
    response = requests.request("GET", url, headers=headers)

    if "errors" in response.json():
        print("token expired, renewed")
        token = write_token()
    else:
        print("token ok")
    
    return token


def write_token():
    appId = "aiybx7znu5"
    hashToken = "YWl5Yng3em51NXxBVEViTDhBV05FN3JtWHh3Yjh0Uk85WWdxMDhjWkRuRjJCYVJUbnBs"

    url = "https://api.iq.inrix.com/auth/v1/appToken"

    payload = {"appId": appId, "hashToken": hashToken}

    response = requests.request("GET", url, params=payload)

    with open("cur_token.txt", "w") as f1:
        f1.write(response.json()["result"]["token"])
        return response.json()["result"]["token"]


if __name__ == "__main__":
    check()



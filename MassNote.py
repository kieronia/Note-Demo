import requests,json,time
token = input(" > Token?\n > ")
message = input(" > Note message?\n > ")
headers = {'Authorization': token}
resp = requests.get("https://discord.com/api/v8/users/@me/relationships",headers=headers)
data = json.loads(resp.text)
deleted = int(0)

for i in range(len(data)):
    print(f" + https://discordapp.com/api/v8/users/@me/notes/{data[i]['id']}")
    abc = requests.put(f"https://discordapp.com/api/v8/users/@me/notes/{data[i]['id']}", json={'note': message}, headers=headers)
    print(abc.text)
    time.sleep(1)
input(" > Done!\n > ")

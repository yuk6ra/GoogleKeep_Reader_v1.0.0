import gkeepapi

# Gmailアカウントでログイン、xxxとyyyはご自分ので書き換え

with open("Secret.txt", "r", encoding="utf-8") as Secret:
    reader = Secret.read().split()
    userID = reader[0]
    Password = reader[1]

keep = gkeepapi.Keep()

s = keep.login(userID, Password)

gnotes = keep.find(query='memo')

for x in gnotes:
    print(x.text + "/" + str(x.timestamps.created))
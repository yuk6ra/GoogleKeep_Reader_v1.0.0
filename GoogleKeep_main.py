import gkeepapi

# find Google Account ID and Password
with open("Secret.txt", "r", encoding="utf-8") as Secret:
    reader = Secret.read().split()
    account_id = reader[0]
    password = reader[1]

keep = gkeepapi.Keep()

# pass login
keep.login(account_id, password)

# find the keyword of query="Test"
g_memo = keep.find(query='Test')

# indicate the found memos
for x in g_memo:
    print(x.text + "/" + str(x.timestamps.created))

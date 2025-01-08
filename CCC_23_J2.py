dic = {}
dic["Poblano"] = 1500
dic["Mirasol"] = 6000
dic["Serrano"] = 15500
dic["Cayenne"] = 40000
dic["Thai"] = 75000
dic["Habanero"] = 125000
ans = 0
total = int(input())
for i in range(total):
    name = input()
    ans += dic[name]
print(name)
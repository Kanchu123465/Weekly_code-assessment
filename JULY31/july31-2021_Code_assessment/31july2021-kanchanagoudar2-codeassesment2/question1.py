import json
import requests
try:
    information=requests.get("https://jsonplaceholder.typicode.com/todos")
    allinfo=data.json()
    resultlist=[]
    result_list2=[i for i in allinfo if i["completed"]==True]
    resultlist.append(result_list2)
    print(resultlist)

except:
    print("check with link")

else:
    print("we got all info")

finally:
    print("task completed ")
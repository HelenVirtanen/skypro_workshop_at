import requests


def get_tasks_test():
    response = requests.get("https://todo-app-sky.herokuapp.com/")
    assert response.status_code == 200
    assert type(response.json()) is list













#def get_tasks_test():
#    response = requests.get("https://todo-app-sky.herokuapp.com/")
#
#    count = len(response.json())
#    print(count)
#    body = {"title":"+1 задача","completed":False}
#    new_task = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
#    
#    response_2 = requests.get("https://todo-app-sky.herokuapp.com/")
# 
#    assert len(response_2.json()) == count + 1
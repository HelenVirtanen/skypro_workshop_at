import requests


#def get_tasks_test():
#    response = requests.get("https://todo-app-sky.herokuapp.com/")
#    assert response.status_code == 200
#    assert type(response.json()) is list

def get_list_tasks_test():
    
    body = {"title":"Сходить на воркшоп","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    len_response_body = len(response.json())

    response = requests.get("https://todo-app-sky.herokuapp.com/")

    assert response.status_code == 200
    assert type(response.json()) is list
    assert len_response_body == 10
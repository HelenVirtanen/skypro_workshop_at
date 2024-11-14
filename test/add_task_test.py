import requests


def add_task_test():
    body = {"title":"Сходить на воркшоп","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response.json()
    assert response.status_code == 200
    assert response['completed'] == None

def test_add_2():
    body = {"title":"Сходить на воркшоп","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body['completed'] == None

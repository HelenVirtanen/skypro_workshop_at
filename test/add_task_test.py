import requests


def test_add():
    body = {"title":"Сделать кофе","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body['completed'] == False

def test_add_2():
    body = {"title":"Сделать кофе","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 400
    assert response_body['completed'] == False

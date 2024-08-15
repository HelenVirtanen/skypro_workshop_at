import requests


def test_add():
    body = {"title":"новая задача","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body['completed'] == None


"прошу дать отпуск"

def test_add_with_title():
    body = {"title":"test_title"}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body['completed'] == None
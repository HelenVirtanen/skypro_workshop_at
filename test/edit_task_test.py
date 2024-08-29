import requests


def test_edit():
    body = {"title":"Посмотреть фильм","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    
    body = {"title":"Пойти в парк"}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200
    
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200

    assert response.json()['title']=="generated-1"


def test_edit_completed():
    body = {"title":"На море всем!"}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    
    body = {"completed":True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200
    
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200
    assert response.json()['completed']==True

    assert response.json()['title']=="Пойти в парк"


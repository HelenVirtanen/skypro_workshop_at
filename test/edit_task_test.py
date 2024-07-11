import requests


def test_edit():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    
    body = {"title":"generated-1"}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200
    
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200
    assert response.json()['title'] == "generated-1"





#def test_edit_title():
#    body = {"title":"first task","completed":False}
#    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
#    id = response.json()["id"]
#    
#    body = {"title":"first task edited"}
#    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
#    assert response.status_code == 200
#    
#    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
#    assert response.status_code == 200
#    assert response.json()['title'] == "first task edited"
#
#def test_edit_completed():
#    body = {"title":"second task","completed":False}
#    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
#    id = response.json()["id"]
#    
#    body = {"completed":True}
#    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
#    assert response.status_code == 200
#    
#    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
#    assert response.status_code == 200
#    assert response.json()['completed'] == True
#
#def test_edit_both():
#    body = {"title":"third task","completed":False}
#    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
#    id = response.json()["id"]
#    
#    body = {"title":"third task edited", "completed":True}
#    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
#    assert response.status_code == 200
#    
#    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
#    assert response.status_code == 200
#    assert response.json()['completed'] == True
#    assert response.json()['title'] == "third task edited"
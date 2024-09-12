import requests


def test_delete():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    
    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    
    
    assert response.status_code == 200








#def test_get_deleted_task():
#    body = {"title":"to delete","completed":False}
#    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
#    id = response.json()["id"]
#    
#    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
#    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
#
#    assert response.status_code == 200

#def test_get_deleted_unknown_task():
#    body = {"title":"удалить","completed":False}
#    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
#    response = requests.delete(f'https://todo-app-sky.herokuapp.com/100000')
#
#    assert response.status_code == 200
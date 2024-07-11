import requests


def test_add():
    body = {"title":"новая задача","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body['completed'] == None










#def test_add_task_only_title():
#    body = {"title":"only title"}
#    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
#    response_body = response.json()
#    
#    assert response.status_code == 200
#    assert response_body['title'] == 'only title'
#
#def test_add_task_without_title():
#    body = {"title":""}
#    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
#    response_body = response.json()
#    
#    assert response.status_code == 200
#    assert response_body['title'] == ""
#
#def test_add_task_completed():
#    body = {"completed":True}
#    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
#    response_body = response.json()
#    
#    assert response.status_code == 404
#    assert response_body['completed'] == True
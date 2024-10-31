import requests

def test_add_task():
    body = {"title":"Shopping","completed":True}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body['completed'] == None
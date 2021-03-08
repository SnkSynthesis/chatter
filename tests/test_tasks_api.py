
task = {
    "name": "Test Task", 
    "desc": "Make sure tests work",
    "completed": False
}

completed_task = {
    "name": "Test Task", 
    "desc": "Make sure tests work",
    "completed": True
}

def test_create(client):
    response = client.post("/tasks/", json=task)
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    assert data["name"] == task["name"]
    assert data["desc"] == task["desc"]
    assert data["completed"] == task["completed"]


def test_read(client):
    response = client.get("/tasks/1/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert {"id": 1, **task} == data

    response = client.get("/tasks/")
    assert response.status_code == 200, response.text
    assert data in response.json()

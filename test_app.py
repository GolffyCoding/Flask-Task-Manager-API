import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_empty_tasks_list(client):
    rv = client.get('/tasks')
    assert rv.status_code == 200
    assert json.loads(rv.data)['tasks'] == []

def test_create_task(client):
    task_data = {
        'title': 'Test Task',
        'description': 'Test Description'
    }
    rv = client.post('/tasks', 
                     data=json.dumps(task_data),
                     content_type='application/json')
    assert rv.status_code == 201
    response_data = json.loads(rv.data)
    assert response_data['task']['title'] == 'Test Task'
    assert response_data['task']['description'] == 'Test Description'
    assert response_data['task']['done'] == False
    assert 'id' in response_data['task']

def test_get_task(client):
    task_data = {'title': 'Test Task'}
    client.post('/tasks',
                data=json.dumps(task_data),
                content_type='application/json')
    
    rv = client.get('/tasks/1')
    assert rv.status_code == 200
    response_data = json.loads(rv.data)
    assert response_data['task']['title'] == 'Test Task'

def test_update_task(client):
    task_data = {'title': 'Test Task'}
    client.post('/tasks',
                data=json.dumps(task_data),
                content_type='application/json')
    
    update_data = {
        'title': 'Updated Task',
        'done': True
    }
    rv = client.put('/tasks/1',
                    data=json.dumps(update_data),
                    content_type='application/json')
    assert rv.status_code == 200
    response_data = json.loads(rv.data)
    assert response_data['task']['title'] == 'Updated Task'
    assert response_data['task']['done'] == True

def test_delete_task(client):
    task_data = {'title': 'Test Task'}
    client.post('/tasks',
                data=json.dumps(task_data),
                content_type='application/json')
    
    rv = client.delete('/tasks/1')
    assert rv.status_code == 200
    assert json.loads(rv.data)['result'] == True
    
    rv = client.get('/tasks/1')
    assert rv.status_code == 404

def test_create_task_without_title(client):
    task_data = {'description': 'Test Description'}
    rv = client.post('/tasks',
                     data=json.dumps(task_data),
                     content_type='application/json')
    assert rv.status_code == 400
    assert 'error' in json.loads(rv.data)

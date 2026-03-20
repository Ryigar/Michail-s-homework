import requests

base_url = "https://ru.yougile.com/api-v2"
api_key = ""     # Подставить значение из формы сдачи домашнего задания
not_exist_id = 123456789


# Создание нового проекта

def test_create_positive():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    project_body = {
        "title": "Hometask1",
        "users": {
            "028fe740-0cfa-4b60-9083-0db74c33f001": "admin"
        }
    }
    resp = requests.post(
        f"{base_url}/projects", json=project_body, headers=headers)
    assert resp.status_code == 201
    project_id = resp.json()["id"]
    assert project_id is not None

    requests.put(
        f"{base_url}/projects/{project_id}",
        json={"deleted": True}, headers=headers)


def test_create_negative():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    project = {
        "title": "",
        "users": {
            "028fe740-0cfa-4b60-9083-0db74c33f001": "admin"
        }
    }
    resp = requests.post(f"{base_url}/projects", json=project, headers=headers)
    assert resp.status_code == 400
    assert resp.json()["message"][0] == "title should not be empty"


# Изменение проекта


def test_update_positive():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    project_body = {
        "title": "Hometask1",
        "users": {
            "028fe740-0cfa-4b60-9083-0db74c33f001": "admin"
        }
    }
    resp = requests.post(
        f"{base_url}/projects", json=project_body, headers=headers)
    assert resp.status_code == 201
    project_id = resp.json()["id"]

    update_project = {
        "title": "Lesson08"
    }
    resp_put = requests.put(
        f"{base_url}/projects/{project_id}",
        json=update_project, headers=headers)
    assert resp_put.status_code == 200
    resp_get = requests.get(
        f"{base_url}/projects/{project_id}", headers=headers)
    assert resp_get.status_code == 200
    assert resp_get.json()["title"] == "Lesson08"

    requests.put(
        f"{base_url}/projects/{project_id}",
        json={"deleted": True}, headers=headers)


def test_update_negative():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    project = {
        "title": "Python",
        "users": {
            "028fe740-0cfa-4b60-9083-0db74c33f001": "admin"
        }
    }
    resp = requests.put(
        f"{base_url}/projects/{not_exist_id}", json=project, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["message"] == "Проект не найден"


# Получение по ID

def test_get_id_positive():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    project_body = {
        "title": "Hometask",
        "users": {
            "028fe740-0cfa-4b60-9083-0db74c33f001": "admin"
        }
    }
    resp = requests.post(
        f"{base_url}/projects", json=project_body, headers=headers)
    assert resp.status_code == 201
    project_id = resp.json()["id"]

    resp_get = requests.get(
        f"{base_url}/projects/{project_id}", headers=headers)
    assert resp_get.status_code == 200
    assert resp_get.json()["title"] == "Hometask"
    assert resp_get.json()["id"] == project_id

    requests.put(
        f"{base_url}/projects/{project_id}",
        json={"deleted": True}, headers=headers)


def test_get_id_negative():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    resp_get = requests.get(
        f"{base_url}/projects/{not_exist_id}", headers=headers)
    assert resp_get.status_code == 404
    assert resp_get.json()["message"] == "Проект не найден"

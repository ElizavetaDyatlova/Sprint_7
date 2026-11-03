import pytest
from helpers import generate_random_string
from api_client import create_courier, login_courier, delete_courier

@pytest.fixture
def courier():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()
    payload = {"login": login, "password": password, "firstName": first_name}
    
    create_courier(payload)
    
    yield login, password
    
    response_login = login_courier({"login": login, "password": password})
    if response_login.status_code == 200:
        courier_id = response_login.json().get("id")
        delete_courier(courier_id)
import pytest
from helpers import register_new_courier_and_return_login_password, get_courier_id, delete_courier


@pytest.fixture
def courier():
    courier_data = register_new_courier_and_return_login_password()
    
    if not courier_data:
        pytest.fail("Не удалось создать курьера для теста")

    yield courier_data

    login = courier_data[0]
    password = courier_data[1]
    
    courier_id = get_courier_id(login, password)
    if courier_id:
        delete_courier(courier_id)
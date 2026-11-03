import allure
import requests
from urls import Urls

@allure.step("Создать курьера")
def create_courier(payload):
    return requests.post(Urls.CREATE_COURIER, data=payload)

@allure.step("Логин курьера")
def login_courier(payload):
    return requests.post(Urls.LOGIN_COURIER, data=payload)

@allure.step("Удалить курьера по ID: {courier_id}")
def delete_courier(courier_id):
    return requests.delete(f"{Urls.CREATE_COURIER}/{courier_id}")

@allure.step("Создать заказ")
def create_order(payload):
    return requests.post(Urls.CREATE_ORDER, json=payload)

@allure.step("Получить список заказов")
def get_orders():
    return requests.get(Urls.GET_ORDERS_LIST)
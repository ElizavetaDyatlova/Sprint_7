import allure
from api_client import get_orders

@allure.feature("Список заказов")
class TestGetOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_list_success(self):
        response = get_orders()
        
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        assert "orders" in response.json(), "В ответе отсутствует ключ 'orders'"
        assert isinstance(response.json()["orders"], list), "Поле 'orders' не является списком"
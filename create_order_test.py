# Радик Рухуллаев, Меркурий 10 — Дипломный проект. Инженер по тестированию плюс.
# Тестируем API Яндекс Самокат

import sender_stand_request


# Создание заказа. Выводит его номер. Запрос к API
def create_new_order():
    response = sender_stand_request.post_new_order()
    assert response.status_code == 201
    return response.json()["track"]


# Тест на создание и получение заказа в БД. Запрос к БД
def test_create_and_get_new_order():
    track = create_new_order()
    response = sender_stand_request.get_order_info(str(track))
    assert response.status_code == 200

# Алексей Косцов, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import create_order

order = create_order.order_num

def positive_assert ():
    order_response = create_order.order_search(order)
    assert order_response.status_code == 200


def test_status_code():
    positive_assert()
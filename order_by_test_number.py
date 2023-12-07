import create_order
import data


order = create_order.order_num

def positive_assert (order):
    order_response = create_order.order_search(order)
    assert order_response.status_code == 200


def test_order_code():
    positive_assert(order)
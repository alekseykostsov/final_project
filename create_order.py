import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.new_order,
                         json=body)

response = post_new_order(data.body);
order_num = response.json()["track"]
# print(response)
# print(order_num)

def order_search (num):
    return requests.get(configuration.URL_SERVICE + configuration.number_order + str(num))

# order = order_search(order_num)
# print(order.status_code)



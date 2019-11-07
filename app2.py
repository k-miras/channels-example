#!/usr/bin/env python
# from asgiref.sync import async_to_sync
# from channels_rabbitmq.core import RabbitmqChannelLayer
from celery import Celery
app = Celery('tasks', broker='pyamqp://guest:guest@rabbitmq//', backend='rpc://')


@app.task(name="get_initial_configs")
def get_initial_configs(param):
    return param
# async def start():
#     layer2 = RabbitmqChannelLayer(
#         host="amqp://guest:guest@rabbitmq",
#         local_capacity=1000000000,
#         remote_capacity=10000000000,
#         prefetch_count=10000,
#         expiry=6000000,
#         local_expiry=None,
#         group_expiry=8640000000,
#         ssl_context=None,
#         groups_exchange="second")
#     channel2 = await layer2.new_channel()
#     await layer2.group_add("test-group", channel2)
#     while True:
#         message = await layer2.receive(channel2)
#         print(message)
#     exit(0)

# if __name__ == "__main__":
    # async_to_sync(start)()

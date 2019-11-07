#!/usr/bin/env python
import asyncio
import aioamqp
from celery import Celery



async def callback(channel, body, envelope, properties):
    print(" [x] Received %r" % body)


async def receive():
    transport, protocol = await aioamqp.from_url("amqp://guest:guest@rabbitmq")
    channel = await protocol.channel()
    await channel.queue_declare(queue_name='hello')
    await channel.basic_consume(callback, queue_name='hello')


def on_configs(result):
    print("called")
    print(result)
    print("starting main loop: "+result)
    event_loop = asyncio.new_event_loop()
    event_loop.run_until_complete(receive())
    print("started")
    event_loop.run_forever()

if __name__ == "__main__":
    app = Celery('tasks',
        broker='pyamqp://guest:guest@rabbitmq//',
        backend='rpc://')
    print("calling")
    result = app.send_task("get_initial_configs", args=["test,bitches"]).then(on_configs).get()

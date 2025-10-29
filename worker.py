import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from workflows.agent import AgentWorkflow
from activities import openai_responses, get_weather_alerts, random_stuff, get_location
from temporalio.contrib.pydantic import pydantic_data_converter

from concurrent.futures import ThreadPoolExecutor


async def main():
    client = await Client.connect(
        "localhost:7233",
        data_converter=pydantic_data_converter,
    )

    worker = Worker(
        client,
        task_queue="chaotic-agent-python-task-queue",
        workflows=[
            AgentWorkflow,
        ],
        activities=[
            openai_responses.create,
            get_weather_alerts.get_weather_alerts,
            random_stuff.get_random_number,
            get_location.get_location_info,
            get_location.get_ip,
        ],
        activity_executor=ThreadPoolExecutor(max_workers=10),
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())

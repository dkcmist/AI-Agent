from dotenv import load_dotenv
_ = load_dotenv()

import json
from agent import pretty_print_messages, Agent, Swarm


def get_weather(location, time="now"):
    return json.dumps({"location": location, "temperature": "65", "time": time})


def send_email(recipient, subject, body):
    return f"Sent! email to {recipient} with the subject: {subject} and body: {body}"


weather_agent = Agent(
    name="Weather Agent",
    instructions="You are a helpful agent for giving information on weather.",
    functions=[get_weather, send_email],
)

client = Swarm()
print("Starting Single Agent - Weather Agent")
print('Ask me how is the weather today in Brussels?')

messages = []
agent = weather_agent

while True:
    user_input = input("\033[90mUser\033[0m: ")
    messages.append({"role": "user", "content": user_input})

    response = client.run(agent=agent, messages=messages)
    pretty_print_messages(response.messages)

    messages.extend(response.messages)
    agent = response.agent
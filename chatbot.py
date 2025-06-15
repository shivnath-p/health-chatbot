import json

def load_health_data():
    with open('data/health_data.json', 'r') as file:
        return json.load(file)

def get_response(user_input, health_data):
    user_input = user_input.lower()
    for topic in health_data:
        if any(keyword in user_input for keyword in health_data[topic]['keywords']):
            return health_data[topic]['response']
    return "I'm not sure. Please consult a doctor for accurate information."

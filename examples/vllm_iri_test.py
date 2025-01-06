import requests
import json
import dotenv
import os
dotenv.load_dotenv()

url = str(os.getenv("VLLM_ENDPOINT"))
api_key = str(os.getenv("VLLM_API_KEY"))
model = str(os.getenv("VLLM_MODEL"))

def send_chat_request():
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "  # Add your bearer token here if required
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "testing, testing, who are you?"}
        ],
        "max_tokens": 100
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        print(json.dumps(result, indent=2))
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    send_chat_request()

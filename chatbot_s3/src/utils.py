#This Python code snippet demonstrates how to interact with an API endpoint to generate text using a model named "llama". Here’s an explanation of each part:

import json #This module is used to convert Python objects to JSON strings and vice versa, allowing data to be transmitted to the API in the correct format.
import requests #A library for making HTTP requests (e.g., GET, POST). Here, it's used to send a POST request to the API.


#A function that sends a request to the Llama API to generate text
def call_llama(model, prompt, stream=False):
    url = 'http://localhost:11434/api/generate'
    data = {
        'model': model,  #model: Specifies the version or type of the Llama model to use (e.g., "llama3.2")
        'prompt':prompt,  #prompt: The input text for which the model should generate a response
        'stream': stream  #stream: A boolean indicating whether the response should be streamed in chunks (default is False)
    }
    
    #json.dumps(data): Converts the data dictionary to a JSON-formatted string, which is required for the API request.
    json_data = json.dumps(data)
    #url: The API endpoint for text generation. It's pointing to a local server running on port 8501.
    #requests.post: Sends a POST request to the API with the JSON data and headers.
    #headers: Specifies that the content being sent is in JSON format
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'}, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        return f'Error: {response.status_code}'
    
#Ensures that the code inside this block runs only when the script is executed directly (not when imported as a module)
if __name__ == '__main__':
    model = 'llama3.2'
    #prompt: Takes user input as the question or command for the model.
    prompt = input('please enter your question: ')
    #Extracts and prints the generated response from the API.
    response = call_llama(model, prompt)
    if "response" in response:
        print(response["response"])
    else:
        print(f"error: {response["error"]}")
        if "details" in response:
            print(f"details : {response["details"]}")


    
import json

def loadResponses(filePath):
    """Load chatbot responses from a JSON file."""
    try:
        with open(filePath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading responses: {e}")
        return []

def chatbotResponse(userInput, responses):
    """Return a predefined response based on user input."""
    responseDict = {entry["input"]: entry["response"] for entry in responses}
    return responseDict.get(userInput.lower(), "I'm sorry, I don't understand.")

if __name__ == "__main__":
    responses = loadResponses("chats.json")
    if responses:
        while True:
            userInput = input("You: ")
            if userInput.lower() == "bye":
                print("Bot: Goodbye! Have a great day!")
                break
            print(f"Bot: {chatbotResponse(userInput, responses)}")

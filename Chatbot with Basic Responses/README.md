![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)

![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# Chatbot with Basic Responses

## 🛠️ Description

This is a simple chatbot that provides predefined responses based on user input. It reads possible inputs and corresponding responses from a JSON file, and can handle basic conversational interactions. If the user input doesn't match any predefined options, the chatbot will respond with a default message.

## ⚙️ Languages or Frameworks Used
- Python
- JSON

## 🌟 How to Run

1. Clone or download the repository.
2. Create a JSON file named `chats.json` containing predefined inputs and responses.
3. Open the file `chatbot.py` in your Python IDE or text editor.
4. Run the script.
5. Start chatting with the bot. To exit, type "bye".

### Example `chats.json` format:

```json
[
    {"input": "hello", "response": "Hello! How can I assist you today?"},
    {"input": "how are you?", "response": "I'm just a program, so I don't have feelings, but thanks for asking!"}
]
```

### Example Usage:

- **You:** hello
- **Bot:** Hello! How can I assist you today?
- **You:** bye
- **Bot:** Goodbye! Have a great day!

## 🤖 Author
[AtharvaPawar456](https://github.com/AtharvaPawar456)
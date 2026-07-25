# Gemini ChatBot (PySide6)

A desktop AI chatbot built with **Python**, **PySide6**, and the **Google Gemini API**. This project provides a clean graphical interface that allows users to chat with Google's Gemini models directly from a desktop application.

> **Status:** 🚧 Work in Progress

## Features

* Modern desktop GUI built with PySide6
* Integration with the Google Gemini API
* Send prompts and receive AI-generated responses
* Read-only chat response area
* Simple and easy-to-use interface
* Designed to be expanded with additional AI features

## Technologies Used

* Python 3
* PySide6
* Google GenAI SDK
* Qt Widgets

## Project Structure

```
Gemini-ChatBot/
│
├── main.py              # Main application
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Gemini-ChatBot.git
cd Gemini-ChatBot
```

### 2. Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate it

```bash
.venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

or

```bash
pip install PySide6 google-genai
```

## API Key Setup

Create an environment variable named:

```
GEMINI_API_KEY
```

Assign it your Google Gemini API key.

On Windows (Command Prompt):

```cmd
set GEMINI_API_KEY=your_api_key_here
```

On PowerShell:

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

## Running the Project

```bash
python main.py
```

## Current Features

* Send prompts to Gemini
* Display AI responses inside the application
* Desktop interface using Qt Widgets

## Planned Improvements

* Conversation history
* Streaming AI responses
* Dark and light themes
* Markdown rendering
* Chat bubbles
* Save conversations
* Load previous chats
* Multiple Gemini model selection
* Keyboard shortcut (Enter to send)
* Better error handling
* Typing indicator
* Settings page

## Screenshots

*Screenshots will be added as the project develops.*

## Learning Goals

This project was created to improve my understanding of:

* Python application development
* Desktop GUI programming with PySide6
* Working with APIs
* Event-driven programming
* Building AI-powered desktop applications
* Software project structure

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Author

**Omar Global**

Computer Science (Robotics Computing) Student

Learning AI, Python, Desktop Development, and Robotics while building real-world projects.

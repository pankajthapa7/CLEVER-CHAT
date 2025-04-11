
# Clever Chat App

A clever chat application leveraging AI to provide intelligent responses using Python, Flask, and ChatterBot.

## Requirements

- Python 3.x
- Flask
- Flask-SocketIO
- ChatterBot & ChatterBot-Corpus
- spaCy

## Setup

1. **Clone the repository** and navigate into the directory:
    ```bash
    git clone https://github.com/your-username/clever-chat.git
    cd clever-chat
    ```

2. **Create a virtual environment** and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Train the chatbot:**
    ```bash
    python train.py
    ```

5. **Run the application:**
    ```bash
    python app.py
    ```

6. **Access the chat app:** Open your browser and go to `http://localhost:5000`

## Features

- Real-time chat with AI-powered responses
- Easy to expand with more complex conversational data



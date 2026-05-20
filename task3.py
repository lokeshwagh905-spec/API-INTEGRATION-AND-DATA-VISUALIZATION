# AI Chatbot using NLP (NLTK)
# CODTECH Internship Task

import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Chat patterns and responses
pairs = [

    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],

    [
        r"what is your name ?",
        ["I am an AI Chatbot created using Python and NLTK."]
    ],

    [
        r"how are you ?",
        ["I am doing great. Thank you for asking!"]
    ],

    [
        r"what can you do ?",
        ["I can answer simple questions and chat with users."]
    ],

    [
        r"who created you ?",
        ["I was created for the CODTECH internship project."]
    ],

    [
        r"(.*) your favorite language ?",
        ["My favorite language is Python."]
    ],

    [
        r"what is python ?",
        ["Python is a popular programming language used for AI, web development, and more."]
    ],

    [
        r"what is ai ?",
        ["AI stands for Artificial Intelligence."]
    ],

    [
        r"bye|exit|quit",
        ["Goodbye!", "See you later!", "Chat ended."]
    ],

    [
        r"(.*)",
        ["Sorry, I don't understand that question."]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chatbot
print("=" * 50)
print("      AI CHATBOT WITH NLP")
print("      Type 'bye' to exit")
print("=" * 50)

chatbot.converse()
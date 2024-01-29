# Importing the necessary libraries
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot. You can call me Chatbot."]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry"]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ]
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)
print("Please input your questions!")
# Start the conversation
chatbot.converse()
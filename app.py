from flask import Flask, request, jsonify
from chatterbot import   ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import wikipedia

app = Flask(__name__)

# Create a new chat bot
chatbot = ChatBot('Melinda')

# Create a new trainer for the chat bot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chat bot on the English corpus
trainer.train('chatterbot.corpus.english')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    
    # Check if the user's name is "Bhupinder"
    if request.form.get('user_name', '').lower() == 'bhupinder':
        # Customize behavior for Bhupinder (more loving responses)
        response = "Hey Bhupinder, you're my favorite person! 💖 Let's spread love and happiness together!"
    else:
        # Get a response from the chat bot
        response = chatbot.get_response(user_input).text
    
    # Check if the user input is a question
    if user_input.endswith('?'):
        try:
            # Try to find an answer on Wikipedia
            wikipedia.set_lang('en')  # Set language to English
            wiki_summary = wikipedia.summary(user_input)
            response += f"\n\nHere's what I found on Wikipedia:\n{wiki_summary}"
        except wikipedia.exceptions.DisambiguationError as e:
            # If there are multiple results, choose the first one
            wiki_summary = wikipedia.summary(e.options[0])
            response += f"\n\nHere's what I found on Wikipedia:\n{wiki_summary}"
        except wikipedia.exceptions.PageError:
            response += "\n\nI'm sorry, I couldn't find any information on that topic."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

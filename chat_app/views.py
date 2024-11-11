from django.shortcuts import render,redirect
import google.generativeai as genai
from django.contrib.sessions.models import Session




def chatbot_page(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    if request.method == 'GET':
        # Clear chat history if it exists in the session
        if 'chat' in request.session:
            del request.session['chat']
        # Define an empty chat list
        chat = []
    elif request.method == 'POST':
        user_message = request.POST.get('user_message')
        bot_response = interact_with_chatbot(user_message)
        
        # Initialize chat history if it doesn't exist in the session
        chat = request.session.get('chat', [])
        
        # Append user message and bot response to chat history
        chat.append({"sender": "user", "text": user_message})
        chat.append({"sender": "bot", "text": bot_response})

        # Save updated chat history to session
        request.session['chat'] = chat

    return render(request, 'chat_bot.html', {'chat': chat})

def interact_with_chatbot(user_message):
    genai.configure(api_key="AIzaSyBdB6Hs6yC9UHy7nKs4OC3m-ztKdmdFmAQ")

    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    convo.send_message(user_message)

    # Retrieve response from the chat
    response = convo.last.text
    return response
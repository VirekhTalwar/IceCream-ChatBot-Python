from flask import Flask, render_template, request, jsonify

import openai

openai.api_key = "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"



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    chat_messages = [{'role': 'system', 'content': 'You provide customer service for an softy ice cream store located in bld no 5a,Kamat gardens,Mapusa,Goa,India.2 flavours of softy chocolate and vanilla are currently available, we also have pista and strawberry  depending on day of your visit.The store is owned by ajit hosmani.Contact Detail is 7387307948. Both softys are priced a 20 rupees each.you can also get a mixture of both that is priced at 30,store opens at 9am and closes at 10pm every day of the week'}, {'role': 'user', 'content': input}]
    return get_openai_response(chat_messages)

def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
    )

    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    app.run()

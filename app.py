from flask import Flask, render_template, request

app = Flask(__name__)

# Store previous messages in a list
user_messages = []
api_messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ITPApp', methods=['GET', 'POST'])
def login():
    global user_messages
    global api_messages

    if request.method == 'POST':
        user_input = request.form.get('userInput')

        # Check if user input is not None before calling lower()
        if user_input is not None:
            # Store user input in messages list
            user_messages.append(user_input)

            # Simulate API response
            if user_input.lower() == 'hello':
                api_response = 'Hello from the API!'
            else:
                api_response = 'API response for: ' + user_input

            # Store API response in messages list
            api_messages.append(api_response)

            return render_template('ITPApp.html', user_input=user_input, user_messages=user_messages, api_messages=api_messages)

    return render_template('ITPApp.html', user_messages=user_messages, api_messages=api_messages)

if __name__ == '__main__':
    app.run(debug=True)

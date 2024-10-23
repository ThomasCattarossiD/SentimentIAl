from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    output = ""
    if request.method == 'POST':
        # Get the input from the text box
        user_input = request.form['user_input']
        output = f"You entered: {user_input}"  # Process input as needed

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)

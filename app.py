from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load a model for detecting offensive, racist, or hateful content
toxicity_model = pipeline('text-classification', model="cardiffnlp/twitter-roberta-base-offensive")

@app.route('/', methods=['GET', 'POST'])
def home():
    output = ""
    if request.method == 'POST':
        # Get the input from the text box
        user_input = request.form['user_input']

        # Run the text through the toxicity model to detect offensive or harmful content
        result = toxicity_model(user_input)[0]
        label = result['label']
        score = result['score']

        # Provide output based on the label (e.g., OFFENSIVE or NON-OFFENSIVE)
        if label == 'offensive' and score > 0.5:  # Adjust threshold as needed
            output = "The message is likely to contain harmful or offensive content."
        else:
            output = "The message does not seem to break TOS regarding racism or hate speech."

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)

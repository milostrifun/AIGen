from flask import Flask, request, jsonify, render_template
from chatbot_logic import financial_chatbot

app = Flask(__name__)

@app.route('/')
def index():
    # Render the form where queries can be entered
    return render_template('query.html')

@app.route('/financial_chatbot', methods=['GET'])
def financial_chatbot_route():
    company = request.args.get('company')
    year = request.args.get('year')
    query = request.args.get('query')

    # Validate that all parameters are present
    if not company or not year or not query:
        return render_template('response.html', response="Missing required parameters."), 400

    # Call the financial chatbot function from the chatbot_logic module
    response = financial_chatbot(company, year, query)
    return render_template('response.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from utils import calculate_monthly_payment, calculate_total_cost

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page with input fields and result display area
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve input values from the request
    loan_amount = float(request.form['loan_amount'])
    duration_years = int(request.form['duration'])
    annual_interest_rate = float(request.form['interest_rate'])

    # Calculate monthly payment and total cost using utility functions
    monthly_payment = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
    total_cost = calculate_total_cost(monthly_payment, duration_years)

    # Return the results in JSON format to be displayed on the page
    return jsonify({
        'monthly_payment': monthly_payment,
        'total_cost': total_cost
    })

if __name__ == '__main__':
    app.run(debug=True)
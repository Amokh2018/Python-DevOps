from flask import Flask, render_template, request, jsonify
from utils import calculate_monthly_payment, calculate_total_cost, calculate_remaining_balance

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    loan_amount = float(request.form['loan_amount'])
    duration_years = int(request.form['duration'])
    annual_interest_rate = float(request.form['interest_rate'])

    monthly_payment = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
    total_cost = calculate_total_cost(monthly_payment, duration_years)
    remaining_balances = calculate_remaining_balance(loan_amount, duration_years, annual_interest_rate)

    return jsonify({
        'monthly_payment': monthly_payment,
        'total_cost': total_cost,
        'remaining_balances': remaining_balances
    })

if __name__ == '__main__':
    app.run(debug=True)
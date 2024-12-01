def calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    total_payments = duration_years * 12
    
    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
    else:
        monthly_payment = loan_amount / total_payments

    return round(monthly_payment, 2)

def calculate_total_cost(monthly_payment, duration_years):
    """
    Calculate the total cost of the loan over its entire duration.

    Parameters:
    - monthly_payment (float): The monthly payment amount.
    - duration_years (int): The duration of the loan in years.

    Returns:
    - float: The total cost of the loan.
    """
    total_payments = duration_years * 12
    total_cost = monthly_payment * total_payments
    return round(total_cost, 2)

def calculate_remaining_balance(loan_amount, duration_years, annual_interest_rate):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    total_payments = duration_years * 12
    monthly_payment = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)

    balances = []
    remaining_balance = loan_amount

    for month in range(1, total_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        balances.append(round(remaining_balance, 2))

    return balances
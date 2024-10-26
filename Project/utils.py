def calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate):
    """
    Calculate the monthly loan payment with compounded annual interest.

    Parameters:
    - loan_amount (float): The total amount of the loan.
    - duration_years (int): The duration of the loan in years.
    - annual_interest_rate (float): The annual interest rate as a percentage (e.g., 5.5 for 5.5%).

    Returns:
    - float: The monthly payment amount.
    """
    # Convert annual interest rate to a monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    # Total number of monthly payments
    total_payments = duration_years * 12
    
    # Calculate monthly payment using the amortizing loan formula with compounded interest
    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
    else:
        # If the interest rate is 0, simply divide the loan by the number of payments
        monthly_payment = loan_amount / total_payments

    return round(monthly_payment, 2)

def calculate_total_cost(monthly_payment, duration_years):
    """
    Calculate the total cost of the loan.

    Parameters:
    - monthly_payment (float): The monthly payment amount.
    - duration_years (int): The duration of the loan in years.

    Returns:
    - float: The total cost of the loan.
    """
    total_payments = duration_years * 12
    total_cost = monthly_payment * total_payments
    return round(total_cost, 2)
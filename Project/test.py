import unittest
from utils import calculate_monthly_payment, calculate_total_cost, calculate_remaining_balance

class TestLoanCalculatorUtils(unittest.TestCase):
    def test_calculate_monthly_payment_with_interest(self):
        # Test case with a non-zero cumulative interest rate
        loan_amount = 10000  # $10,000 loan amount
        duration_years = 5   # 5 years duration
        annual_interest_rate = 5  # 5% annual interest rate

        # Expected monthly payment calculated using the updated formula
        expected_payment = 188.71  # Approximate value for the test case

        result = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
        self.assertAlmostEqual(result, expected_payment, places=2)

    def test_calculate_monthly_payment_no_interest(self):
        # Test case with a zero interest rate
        loan_amount = 10000  # $10,000 loan amount
        duration_years = 5   # 5 years duration
        annual_interest_rate = 0  # 0% interest rate

        # Expected monthly payment when interest is zero
        expected_payment = 166.67  # Expected value for a 0% interest loan

        result = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
        self.assertAlmostEqual(result, expected_payment, places=2)

    def test_calculate_total_cost(self):
        # Test total cost calculation with a given monthly payment and duration
        monthly_payment = 188.71  # Monthly payment based on 5% interest rate
        duration_years = 5  # Loan duration in years

        # Expected total cost of the loan over 5 years
        expected_total_cost = 11322.6  # Approximate value for the total cost

        result = calculate_total_cost(monthly_payment, duration_years)
        self.assertAlmostEqual(result, expected_total_cost, places=2)

    def test_calculate_remaining_balance(self):
        # Test remaining balance calculation
        loan_amount = 10000  # $10,000 loan amount
        duration_years = 5   # 5 years duration
        annual_interest_rate = 5  # 5% annual interest rate

        # Calculate expected remaining balance length (should be duration_years * 12)
        expected_payments = duration_years * 12
        remaining_balances = calculate_remaining_balance(loan_amount, duration_years, annual_interest_rate)

        # Ensure the number of calculated balances matches the expected number of payments
        self.assertEqual(len(remaining_balances), expected_payments)

        # Check that the final balance is close to zero, indicating the loan is fully repaid
        self.assertAlmostEqual(remaining_balances[-1], 0, places=2)

if __name__ == '__main__':
    unittest.main()
import unittest
from utils import calculate_monthly_payment, calculate_total_cost, calculate_remaining_balance

class TestLoanCalculatorUtils(unittest.TestCase):
    def test_calculate_monthly_payment_with_interest(self):
        # Test case with non-zero interest rate
        loan_amount = 10000
        duration_years = 5
        annual_interest_rate = 5
        expected_payment = 188.71
        result = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
        self.assertAlmostEqual(result, expected_payment, places=2)

    def test_calculate_monthly_payment_no_interest(self):
        # Test case with zero interest rate
        loan_amount = 10000
        duration_years = 5
        annual_interest_rate = 0
        expected_payment = 166.67
        result = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
        self.assertAlmostEqual(result, expected_payment, places=2)

    def test_calculate_total_cost(self):
        # Test total cost calculation
        monthly_payment = 188.71  # Monthly payment based on 5% interest rate
        duration_years = 5  # Loan duration in years
        expected_total_cost = 11322.6
        result = calculate_total_cost(monthly_payment, duration_years)
        self.assertAlmostEqual(result, expected_total_cost, places=2)

    def test_calculate_remaining_balance(self):
        # Test remaining balance calculation
        loan_amount = 10000
        duration_years = 5
        annual_interest_rate = 5

        # Calculate remaining balances
        balances = calculate_remaining_balance(loan_amount, duration_years, annual_interest_rate)

        # Test that the correct number of balances is returned (initial balance + monthly balances)
        self.assertEqual(len(balances), duration_years * 12 + 1)  # Include the initial balance

        # Test that the first balance matches the initial loan amount
        self.assertAlmostEqual(balances[0], loan_amount, places=2)

        # Test that the last balance is effectively zero within tolerance
        self.assertLessEqual(abs(balances[-1]), 0.5)  # Allow up to $0.50 rounding error
if __name__ == '__main__':
    unittest.main()
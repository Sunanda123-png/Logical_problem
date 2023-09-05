"""Generate a loan amortization schedule for a $200,000 mortgage with an annual interest rate of 4.5% and a loan duration
of 30 years.
Question: What is the monthly payment, interest, principal, and remaining balance for each month of the mortgage?
M = (P * r * (1 + r)^n) / ((1 + r)^n - 1)
"""


class LoanAmortization:
    def __init__(self, amount, rate, years):
        self.amount = amount
        self.rate = rate
        self.time = years

    def calculate_amortization_schedule(self):
        monthly_rate = self.rate / 12 / 100
        months = 12 * self.time
        monthly_payment = (self.amount * monthly_rate * (1 + monthly_rate) ** months) / (
                (1 + monthly_rate) ** (months - 1))

        remaining_balance = self.amount
        ammortization_schedule = []

        for month in range(1, months + 1):
            interest_payment = remaining_balance * monthly_rate
            principle_payment = monthly_payment - interest_payment
            remaining_balance = remaining_balance - principle_payment
            # total_amount_paid = total_amount_paid + monthly_payment

            ammortization_schedule.append({
                'month': month,
                'monthly_payment': monthly_payment,
                'interest_payment': interest_payment,
                'principle_payment': principle_payment,
                'remaining_balance': remaining_balance
            })

        return ammortization_schedule


loan = LoanAmortization(200000, 4.5, 30)
repayment_details = loan.calculate_amortization_schedule()
print(f'Amortization details:- {repayment_details}')

"""Generate a loan amortization schedule for a $10,000 personal loan with an annual interest rate of 8% and a loan 
duration of 5 years.
Question: What is the monthly payment, interest, principal, and remaining balance for each month of the personal loan?
"""
amortization = LoanAmortization(10000, 8, 5)
repayment = amortization.calculate_amortization_schedule()
print(f'Amortization details:- {repayment}')


def print_amortization_schedule(schedule):
    print(f"{'Month':<10}{'Payment':<18}{'Interest':<18}{'Principal':<18}{'Balance':<18}")
    print("=" * 80)
    for entry in schedule:
        month, monthly_payment, interest_payment, principal_payment, remaining_balance = entry
        print(f"{month:<10}${monthly_payment:.2f}${interest_payment:.2f}${principal_payment:.2f}${remaining_balance:.2f}")





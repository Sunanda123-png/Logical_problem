"""
Problem: Loan Interest Calculation with Variable Rates
Write a Python function that calculates the total interest charged on a loan with variable interest rates over a given
 time period.
The function should take the following inputs:
Loan amount (A)
List of interest rates (R) corresponding to different time periods List of time durations (T) for each interest rate
"""


def calculate_total_interest(A, R, T):
    total_interest = 0
    for rate, duration in zip(R, T):
        interest = A * rate * duration
        total_interest += interest
    return total_interest


loan_amount = 1000
interest_rates = [0.02, 0.03, 0.05, 0.07]
time_periods = [2, 3, 5, 10]

total_interest_charged = calculate_total_interest(loan_amount, interest_rates, time_periods)
print(f"Total interest charged: ${total_interest_charged:.2f}")

"""Use Case: Calculate compound interest for a loan with monthly compounding.
Question: What is the final amount of a $10,000 loan with an annual interest rate of 5% compounded monthly after 3 years?
"""


def calculate_compound_interest(A, R, T, n):
    compound_interest = A * (1 + R / 100 / n) ** (n * T)
    return compound_interest


amount = 10000
rate = 5
time = 3
n = 12
final_amount = calculate_compound_interest(amount, rate, time, n)
print(f'final amount of the loan :- ${final_amount: .2f}')

"""
Use Case: Calculate compound interest for an investment with quarterly compounding.
Question: How much will a $5,000 investment grow to after 7 years with an annual interest rate of 8% compounded quarterly?
"""


def calculate_compound_interest_investment(A, R, T, n):
    compound_interest = A * (1 + R / n) ** (n * T)
    return compound_interest


amount = 5000
rate = 0.08
time = 7
n = 4
final_amount = calculate_compound_interest_investment(amount, rate, time, n)
print(f'final amount of the investment :- ${final_amount:.2f}')

"""
Use Case: Calculate compound interest for a savings account with daily compounding.
Question: If I deposit $1,000 in a savings account with an annual interest rate of 4.5% compounded daily,
how much will I have after 2 years?
"""


def calculate_compound_interest_saving_account(A, R, T, n):
    compound_interest = A * (1 + R / n) ** (n * T)
    return compound_interest


amount = 1000
rate = 0.045
time = 2
n = 365
final_amount = calculate_compound_interest_saving_account(amount, rate, time, n)
print(f'final amount of the savings :- ${final_amount:.2f}')







class Compounding:
    """
    Calculate compound interest for a mortgage with semi-annual compounding.
    Question: What is the total amount owed on a $200,000 mortgage with an annual interest rate of 3.8% compounded
    semi annually after 25 years?
    :return: total amount which is principle amount and total interest

    Use Case: Calculate compound interest for an investment with annual compounding.
    Question: If I invest $50,000 in a fixed deposit with an annual interest rate of 6.5% compounded annually,
    what will be the maturity value after 10 years?
    """
    def __init__(self, principle_amount, interest_rate, time_period, frequency_compounding):
        self.amount = principle_amount
        self.rate = interest_rate
        self.time = time_period
        self.frequency = frequency_compounding

    def compounding_for_mortgage(self):
        total_interest = self.amount*(1+self.rate/self.frequency)**(self.frequency*self.time)
        total_amount = self.amount + total_interest
        return total_amount


compounding = Compounding(200000, 0.038, 25, 2)
amount_owed = compounding.compounding_for_mortgage()
print(f'Total amount with adding mortgage owed on a $200000 is ${amount_owed:.2f}')

fixed_deposite = Compounding(50000, 0.065, 10, 1)
maturity = fixed_deposite.compounding_for_mortgage()
print(f'Maturity value after 10 years:- ${maturity:.2f}')
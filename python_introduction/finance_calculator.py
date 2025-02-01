monthly_income = int(input("Enter your monthly income: \n"))
monthly _expenses= int(input("Enter your monthly expenses: \n"))
savings = (monthly_income - monthly_expenses)

projected_savings = (savings * 12 + (savings * 12 * 0.05))

print (f" your monthly savings are: {savings}.\n \nProjected savings after one year, with interest is {projected_savings}" )

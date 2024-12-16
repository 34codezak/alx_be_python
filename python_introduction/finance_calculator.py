monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly  expenses:"))

#Calculate monthly savings and projected annual savings
monthly_savings = monthly_income - monthly_expenses
projectedSavings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#output the user's momnthly savings and projected annual savings
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projectedSavings}")
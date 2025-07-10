import locale

locale.setlocale(locale.LC_ALL, '')

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
projected_1year_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# sets locale to users' default settings
formated_savings = locale.currency(monthly_savings, grouping=True, symbol=True)
formated_yearly_savings = locale.currency(
    projected_1year_savings, grouping=True, symbol=True)

print("Your monthly savings are ", formated_savings)
print("Projected savings after one year, with interest is: ",
      formated_yearly_savings)

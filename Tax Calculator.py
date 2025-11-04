def tax_calculator(income):
    if income < 0:
        print("Input a valid income.")
        return None
    elif income <= 2000:
        tax = 0 
    elif income <= 4000:
        tax = 0.15
    elif income <= 7000:
        tax = 0.2
    elif income <= 10000:
        tax = 0.25
    elif income <= 14000:
        tax = 0.3
    else:
        tax = 0.35
    return tax

income = float(input("How much do you make monthly? "))

tax = tax_calculator(income)

if tax is not None:
    total_tax = income * tax
    net_income = income - total_tax

    total_tax = round(total_tax, 2)
    net_income = round(net_income, 2)

    print(f"Income: {income} ETB")
    print(f"Tax Rate: {tax * 100}%")
    print(f"Tax Owed: {total_tax} ETB")
    print(f"Net Income: {net_income} ETB")

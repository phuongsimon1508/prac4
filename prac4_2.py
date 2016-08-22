def main():
    incomes = []
    months = int(input("How many months? "))

    for monthCounter in range(1, months + 1):
        income = float(input("Enter income for month {} ".format(months)))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for monthCounter in range(1, months + 1):
        income = incomes[monthCounter - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(monthCounter, income, total))


main()

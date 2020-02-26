revenue = 100
costs = 50
#revenue = int(input('Enter your revenue: '))
#costs = int(input('Enter your costs: '))

profit = revenue - costs
if profit < 0:
    print(f'You have losses! Your loss is: {-profit}')
elif profit > 0:
    print(f'You have profit! Your profit is: {profit}')
    print(f'The profitability of sale is: {profit/revenue}')
    employees_number = 2
    #employees_number = int(input('Enter number of employees: '))
    print(f'The profit per employee is (for {employees_number} employees): {profit/employees_number}')
else:
    print('You are breaking even!')

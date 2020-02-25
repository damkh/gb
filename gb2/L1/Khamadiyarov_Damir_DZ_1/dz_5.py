#revenue = int(input('Enter your revenue: '))
#costs = int(input('Enter your costs: '))
revenue = 100
costs = 50
profit = revenue - costs
if profit < 0:
    print(f'You have losses! Your loss is: {-profit}')
elif profit > 0:
    print(f'You have profit! Your profit is: {profit}')
    print(f'The profitability of sale is: {profit/revenue}')
    #employees_number = int(input('Enter number of employees: '))
    employees_number = 2
    print(f'The profit per employee is: {profit/employees_number}')
else:
    print('You are breaking even!')

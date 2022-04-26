applePrice = .50
userName = input("What is your name? ")

message = ' hello {}, apples cost ${:,.2f} each, how many would you like to buy?'.format(userName, applePrice)

quantity = int(input(message))

print('Thank you {} for your purchase of {:,} apples at a cost of ${:,.2f} each '.format(userName, quantity, applePrice))

prompt = input("Please enter a description for the product ")

quantity = int(input('How many would you like? '))

price = float(input('please enter price of item '))

discount = 1

if price >= 39.99: 
   priceAfterDiscount = price*.75
elif price >= 19.99:
    priceAfterDiscount = price* .85

salesTax = 0.065

discountedAmount = price-priceAfterDiscount

priceAfterTax = salesTax*priceAfterDiscount

taxAmount = float(priceAfterDiscount*quantity+priceAfterTax)



print('{:,} {} at a cost of ${:,.2f} each '.format(quantity, prompt, priceAfterDiscount))

print(f"Sales tax: {(priceAfterTax):,.2f}")

print(f"Total amount due: {(taxAmount):,.2f}")

print(f"You saved: {((price-priceAfterDiscount)*quantity):,.2f} today.")
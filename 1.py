# tax = input("Enter tax: ")
# subtotal = input("Enter subtotal: ")
# item1 = input("Enter cost of item 1: ")
# item2 = input("Enter cost of item 2: ")
# tip = input("Enter total tip paid: ")

# tax = float(tax)
# subtotal = float(subtotal)
# item1 = float(item1)
# item2 = float(item2)
# tip = float(tip)


tax 		= 2.39
subtotal 	= 29.85
item1 		= 11.95
item2 		= 3.95
tip 		= 3.50

# Returns the tax percent in decimal form
def calcTaxPct(tax, subtotal):
	taxPct = tax / subtotal
	return taxPct

taxPct = calcTaxPct(tax, subtotal)

items = []
items.append(item1)
items.append(item2)
sumItems = sum(items)
sumItemsTax = sumItems * taxPct + sumItems
itemsTaxTip = sumItemsTax + (tip / 2)
itemsTaxTip = round(itemsTaxTip, 2)

tipPct = (tip / subtotal) * 100
tipPct = round(tipPct, 2)

print("Grand Total: $" + str(itemsTaxTip))
print("You tipped: " + str(tipPct) + "%")

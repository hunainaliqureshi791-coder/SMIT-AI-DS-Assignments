# Name: Your Name
# Roll No: SMIT-AI-DS-XXXXX
# Course: AI & Data Science
# Assignment: 01

items = []
prices = []

while True:
    item = input("Enter item name (or 'done'): ")
    if item.lower() == "done":
        break

    price = float(input("Enter price:"))
    items.append(item)
    prices.append(price)

total = sum(prices)

discount = 0
if total > 100:
    discount = total * 0.10
elif total > 50:
    discount = total * 0.05

final_amount = total - discount

print("\n----- Receipt -----")
for i in range(len(items)):
    print(items[i], "-", prices[i])

print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
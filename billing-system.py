units = int(input("Enter units consumed: "))
bill = 0

if units <= 100:
    bill = units * 5

elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 8)

else:
    bill = (100 * 5) + (200 * 8) + ((units - 300) * 12)

print(f"Total Electricity Bill: ${bill}")
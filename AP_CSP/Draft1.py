def afford(income):
    global twenty_eight
    month = int(income)/12
    twenty_eight = round(((month * 0.28) * 100))/100


def price(m, down, intr, year):
    rate = int(intr)/1200
    for x in year:
        n = x * 12
        p = m * (1 + rate)
        p = (m * (((1+rate)**n)-1)/(rate * (1+rate)**n)) + int(down)
        prices_of_house.append(p)

def rounded(house):
    for i in range(len(house)): 
        house[i] = round(house[i]*100)/100

income = input("Enter yearly gross income: ")
interest = input("Enter currently interest rate: ")
downPayment = input("Amount going towards down payment: ")
years = [15, 20, 25, 30]
prices_of_house = []
twenty_eight = 0

afford(income)
price(twenty_eight, downPayment, interest, years)
rounded(prices_of_house)

print("")
print("Income: " + income)
print("Down Payment: " + downPayment)
print("Interest Rate: " + interest + "%")
print("Houses that you can afford: ")
for e, c in enumerate(years):
    print("Years: " + str(c))
    print("Price: " + str(prices_of_house[e]))
    print("")

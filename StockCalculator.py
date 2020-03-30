import requests
from bs4 import BeautifulSoup

#check if stock symbol entered exists and has valid data
def isValid(code):
    try:
        URL = 'https://finance.yahoo.com/quote/' + code.strip() + '/'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
        if(price == ""):
            print("Error: Stock data not found, please try again")
            return False
        return price
    except:
        print("Error: Invalid stock symbol entered, please try again")
        return False

#returns the price of a stock
def getPrice():

    code = input("Enter stock symbol: ")
    price = isValid(code)
    if not price:               #if stock symbol entered does not contain valid data, return
        return

    floatPrice = float(price)
    print("Price for " + code + " is: $" + format(floatPrice, '.2f'))

    return floatPrice

#calculates the gain or loss of a stock investment
def gainOrLoss(stockPrice):

    try:
        shares = float(input("\nEnter the number of shares you have bought for this stock: "))

        if(shares <= 0):
            print("Error: Number of shares entered is invalid")
            return

        totalInvested = float(input("Enter the total amount you have invested for this stock: "))

        currentInvestmentValue = float(shares * stockPrice)  # current value of investment
        difference = currentInvestmentValue - totalInvested  # dollar amount of gain or loss of investment
        percentDifference = ((currentInvestmentValue - totalInvested) / totalInvested) * 100  # percent gain or loss

        print("Current Value of Investment: $" + format(currentInvestmentValue, '.2f'))
        print("Total Invested: $" + format(totalInvested, '.2f'))
        print("Percent Change: " + format(percentDifference, '.2f') + "%")
        print("Gain/Loss: $" + format(difference, '.2f'))

    except:
        print("Error: Invalid data was entered, please try again")

#calls a method depending on the user's selection from the menu
def selection(option):
    if option == 1:
        return getPrice()
    elif option == 2:
        result = getPrice()
        if result:          #if stock symbol entered is valid, continue with gain/loss calculation
            return gainOrLoss(result)
    elif option == 3:
        return False
    else:
        print("Error: Invaild selection, please try again")


while(True):
    print("\nMenu:")
    print("1) Get price of a stock")
    print("2) Get gain/loss of investment")
    print("3) Exit program")

    try:
        c = int(input("\nEnter a number to make a selection: "))
        if selection(c) is False:
            break
    except:
        print("Error: Invalid selection, please try again")


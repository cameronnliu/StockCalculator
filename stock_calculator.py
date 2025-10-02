# Idea: Prompt the user for information about their stock 
# 
# First: Prompt the user for their starting money (initial investment)

import os; import requests 

# Getting API Key
api = os.getenv("vantage_api")


# Error checking for API Key 
if api is None: 
    raise ValueError("API Key is not set. Go into .zshrc and set the API key.")

def get_function_data(function, ticker):
    url = 'https://www.alphavantage.co/query?function=FUNCTION_NAME&keywords=EXAMPLE&apikey=DEMO'
    url = url.replace("DEMO", api)
    url = url.replace("function=FUNCTION_NAME", str(function))
    r = requests.get(url)
    data = r.json()
    return data



# def calculate_max_shares(info: dict, shares_amt: int):
#     balance = info["balance"]

#     balance / shares_amt: 


# def name_to_ticker(name):



# Need to redo this 
def ticker_search_stock(input, info):
    # Input = Y means that they know what they want to invest in.
    if input == "y":
        symbol = input("What stock would you like to invest in?\n")
        get_function_data("function=" + symbol.upper())
    else:
        print("For help, here is the list of the Top 100 Stocks and their prices.\n")
        print("--STOCKLIST--")
        value = input("Would you like to invest in a company, or search the general list? Enter '1' to invest, and '2' for general list.\n")
        if value.lower() == 1:
            ticker = input("What stock would you like to invest in?\n")
            type = input("Would you like to purchase whole shares, or dollar amounts? Type '1' for whole shares and '2' for dollar amounts.\n")
            if type == 1:
                shares_amt = input("How many shares would you like to purchase?\n")

        if value.lower() == 2:
            print("general list")



# Here is the basic prompt management. 
def prompt_no_recursions():
    info = {
        "status": True,
        "balance": None,
        "symbol": None, 
        "category": None
    }

    while info["status"]: 
        if info["balance"] == None:
            # Step 1, asking for balance
            info["balance"] = float(input("Hello! This is a stock-calculator simulator.\nTo start, please list me the intial investment that you will start with, in USD.\n\n"))

        elif info["status"] == None:
            # Step 2, asking/finding Ticker Symbol
            info["status"] = input(f"\nYour starting balance is ${info["balance"]}!\nDo you know what stock would you like to invest in?\n\n")
            if info["status"][0].lower() == "y":
                ticker_search_stock(False)
            else:
                # then call ticker_search
                ticker_search_stock(True)

        elif info["category"] == None:
            # Step 3, asking for the type of investing
            info["category"] = input(f"\nWhat types of example investing are you interested in? Some of the types are:\n  -Stocks\n  -Options\n  -Bonds\n\n")
            function = None
            if info["category"].lower() == "stocks":
                # Which Stock would you like to invest in?
                function = "function=SYMBOL_SEARCH"
                break
            elif info["category"].lower() == "options":
                # Which Options would you like to invest in? 
                function = "function=REALTIME_OPTIONS"
                break
            else: 
                # Which Bonds would you like to invest in?
                break  
        else:
            info["balance"] = False



 # status = input("Would you like to see the different markets?\n")
        # if status[0].lower() == "y":
        #     print("--MARKETS--")
        # else:
        #     status = input("Would you like to search for companies?\n")




def main(): 
    prompt_no_recursions()
main()



# Recursive prompt. Will switch to this, as this is better I believe. 

# def prompt(status, symbol, balance): 
#     if balance == None:
#         balance = float(input("Hello! This is a stock-calculator simulator.\nTo start, please list me the intial investment that you will start with, in USD.\n\n"))
#         prompt(False, None, balance)
#     elif symbol == None:
#         symbol = input(f"\nYour starting balance is ${balance}!\nWhat stock would you like to invest in?\n\n")
#         prompt(False, symbol, balance)
#     else: 
#         prompt(False, symbol, balance)

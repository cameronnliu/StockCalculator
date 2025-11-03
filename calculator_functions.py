# File used to calculate functions for basic stock number calculations 


def calculate_max_shares(balance, share_price, share_count, ticker): 
    # balance: user's balance 
    # amt: how much money the person wants to put into the stock 
    # share_count: amount of shares the person wants to buy 
    # ticker: the ticker symbol, just used for outputs

    total_price = share_count * share_price

    if total_price > balance: 
        print(f"Insufficient funds of {total_price - balance}! Try again, and purchase a lower amount of shares!\n")
        calculate_max_shares(balance, share_price, share_count, ticker)
    else:
        print(f"You are purchasing ${share_price} of {ticker}, equal to {share_count} shares. You have ${balance - share_count} remaining.\n\n")
    
    return share_count, balance

def calculate_dollar_amt(balance, share_price, amt_to_invest, ticker): 
    # balance: user's balance 
    # amt: how much money the person wants to put into the stock 
    # share_count: amount of shares the person wants to buy 
    # ticker: the ticker symbol, just used for outputs

    if amt_to_invest > balance: 
        print(f"Insufficient funds of {amt_to_invest - balance}! Try again, and purchase a lower amount of shares!\n")
        calculate_dollar_amt(balance, amt_to_invest, ticker)
    else:
        share_count = amt_to_invest / share_price
        print(f"You are purchasing ${amt_to_invest} of {ticker}, which is {share_count} shares of {ticker}. You have ${balance - amt_to_invest} remaining.\n\n")
    
    return share_count, balance
        
    
# def main(): 
#     calculate_max_shares(1000, 11, 10, "A")
# main()
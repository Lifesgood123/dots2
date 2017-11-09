from sys import argv

com = float(0.06)
sale = float(input("Sale amount> "))
cost = float(input("cost amount> "))

def get_margin(cost, sale):
    margin = 1-(cost/sale)
    return margin

def get_commision(cost, sale, com):
    commision = sale*com
    print(get_margin(cost, sale))
    return commision 

print(get_commision(cost, sale, com))

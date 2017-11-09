# $0-13350 10%
# 13351 - 50800 15%
# 50801 - 131200 25%
# 131201 - 212500 28%
# 212501 - 416700 33%
# 416701 - 444550 35%
# 444551+         39.6%
bracketrate1 = .15
bracketrate2 = .25
bracketrate3 = .28
bracketrate4 = .33
bracketrate5 = .35
bracketrate6 = .396
bracket1use = 13350*bracketrate1
bracket2use = 50800*bracketrate2
bracket3use = 131200*bracketrate3
bracket4use = 212500*bracketrate4
bracket5use = 416700*bracketrate5
bracket6use = 444551
bracket1 = 
bracket2 = 
bracket3 = 
bracket4 = 
bracket5 = 
bracket6 = 

income = 10000 

if income > 444550:
    taxble = income - bracket6
    total = (taxble*bracketrate6) + bracket1 + bracket2 + bracket3 + bracket4 + bracket5
    print("%d" % total)
elif income >



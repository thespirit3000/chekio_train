#!/usr/local/bin/checkio --domain=py run best-stock

# You are given the current stock prices. You have to find out which stocks cost more.
# 
# Input:The dictionary where the market identifier code is a key and the value is a stock price.
# 
# Output:A string and the market identifier code.
# 
# Preconditions:All the prices are unique.
# 
# 
# END_DESC

#


#

#

#
#



def best_stock(data):
    max = 0
    ind = ''
    for x in data:
        if data.get(x) > max:
            max = data.get(x)
            ind = x
    

    # your code here
    return ind


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
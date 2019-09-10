#!/usr/local/bin/checkio --domain=py run house-password

# 
# END_DESC

def checkio(data):
    a=0
    b=0
    c=0
    if len(data) > 9:
        list=[]
        for i in range(0,len(data)):
            list.append(data[i])
        print(list)
        for el in list:
            if el.isdigit(): a= 1+a
            if el.islower(): b= 1+b
            if el.isupper(): c= 1+c
        if a>0 and b>0 and c>0: return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
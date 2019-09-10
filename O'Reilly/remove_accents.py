#!/usr/local/bin/checkio --domain=py run remove-accents

# Assuming you are developing a user based system like facebook, you will want to provide the functionality to search for other members regardless of the presence of accents in a username. Without using 3rd party collation library, you will need to remove the accents from username before comparison.
# 
# é - letter with accent; e - letter without accent; ̀ and ́ - stand alone accents;
# 
# Input:A phrase as a string (unicode)
# 
# Output:An accent free Unicode string.
# 
# How it is used:It might be a part username verification process or system that propose username based on first and last name of user
# 
# Precondition:0≤|input|≤40
# 
# 
# END_DESC

def checkio(in_string):
    "remove accents"
    
    return in_string

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
#!/usr/local/bin/checkio --domain=py run bird-language

# Stephan has a friend who happens to be a little mechbird.    Recently, he was
# trying to teach it how to speak basic language.    Today the bird spoke its
# first word: "hieeelalaooo".    This sounds a lot like "hello", but with too
# many vowels.    Stephan asked Nikola for help and he helped to examine how th
# e bird changes words.    With the information they discovered, we should help
# them to make a translation module.
#
# The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ⇒ la
# or le);- after each vowel letter the bird appends two of the same letter (a ⇒
# aaa);Vowels letters == "aeiouy".
# You are given an ornithological phrase as several words which are separated b
# y white-spaces    (each pair of words by one whitespace).    The bird does no
# t know how to punctuate its phrases and only speaks words as letters.    All
# w
# ords are given in lowercase.    You should translate this phrase from the bir
# d
# language to something more understandable.
#
# Input:A bird phrase as a string.
#
# Output:The translation as a string.
#
# Precondition:re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
# A phrase always has the translation.
#
#
# END_DESC

VOWELS = "aeiouy"
punctuation = " ,./?!"


def translate(phrase):
    s = ''
    i = 0
    lenght = len(phrase)
    while i < lenght:
        s += phrase[i]
        if phrase[i] in punctuation:
            i += 1
        elif phrase[i] in VOWELS:
            i += 3
        else:
            i += 2
    return s


if __name__ == '__main__':
    print("Example:")
    print(translate("hoooowe yyyooouuu duoooiiine"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

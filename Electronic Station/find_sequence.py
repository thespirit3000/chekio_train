#!/usr/local/bin/checkio --domain=py run find-sequence

# “There’s nothing here...” sighed Nikola.
# 
# “You’re kidding right? All treasure is buried treasure! It wouldn’t be treasure otherwise!” SaidSofia. “Here, take these.” She produced three shovels from a backpack that seemed to appear out of thin air.
# 
# “Where did you get-”
# 
# “Don’t ask questions. Just dig!” She hopped on the shovel and began digging furiously.
# 
# CLUNK
# 
# “Hey we hit something.” Stephen exclaimed in surprise.
# 
# “It’s the treasure!” Sofia was jumping up and down in excitement.
# 
# The trio dug around the treasure chest and pulled it out of the hole and wiped the dirt off. Sofia tried grabbing        the lid but it was locked. Nikola studied the locking mechanism.
# 
# “I’ve seen this type of lock before. It’s pretty simple. We just need to check whether there is a sequence of 4        or more matching numbers and output a bool.”
# 
# “Easy enough. Let’s open this sucker up!” Sofia was shaking in excitement.
# 
# You are given a matrix of NxN (4≤N≤10).    You should check if there is a sequence of 4 or more matching digits.    The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
# 
# Input:A matrix as a list of lists with integers.
# 
# Output:Whether or not a sequence exists as a boolean.
# 
# Precondition:
# 0 ≤ len(matrix) ≤ 10
# all(all(0 < x < 10 for x in row) for row in matrix)
# 
# 
# END_DESC

def checkio(matrix):
    #replace this for solution
    return True or False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
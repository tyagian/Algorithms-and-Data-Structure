"""
Note: Binary search expect sorted list
Eg-1 Locate card position
url: https://jovian.ai/aakashns/python-binary-search
Add possible edge cases:
The number query occurs somewhere in the middle of the list cards.
query is the first element in cards.
query is the last element in cards.
The list cards contains just one element, which is query.
The list cards does not contain number query.
The list cards is empty.
The list cards contains repeating numbers.
The number query occurs at more than one position in cards.
(can you think of any more variations?)
"""
def locate_card(cards, query):
    low, high = 0, len(cards) - 1
    mid = (low+high) // 2
    mid_number = cards[mid]
    while low <= high:
        if mid_number == query:
            return mid
        elif mid_number < query:
           low = mid + 1
        elif mid_number > query:
            high = mid - 1
    return -1
"""
def output(cards, query):
    output = locate_card(cards, query)
    return output
"""
"""
test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}

locate_card(**test['input']) == test['output']
"""
cards = [1,4,6,7,11,17,19]
query = 7
l = locate_card(cards, query)
print (l)
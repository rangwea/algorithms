# coding=utf-8


def insertsort(items):
    '''
        Just like sorting a hand of poke

        Args
            items:original list
    '''

    for i in range(2, len(items)):
        key = items[i]
        j = i - 1
        while j > 0 and items[j] > key:
            items[j + 1] = items[j]
            j = j - 1
        items[j + 1] = key


items = [1, 4, 3, 5, 5, 10, 6, 7]
insertsort(items)
print(items)
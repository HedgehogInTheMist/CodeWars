'''
Create a method partition that accepts a list and a method/block.
It should return two arrays: the first, with all the elements for which the given block returned true,
and the second for the remaining elements.
The equivalent in Python would be:
animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
partition(animals, lambda x: len(x) == 3)
    # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
'''
def partition(arr: list, classifier_method):
    classifier_boolean_list = list(map(classifier_method, arr))
    result = [arr[element] for element in range(len(classifier_boolean_list)) if
              classifier_boolean_list[element] == True]

    return result, [element for element in arr if element not in result]
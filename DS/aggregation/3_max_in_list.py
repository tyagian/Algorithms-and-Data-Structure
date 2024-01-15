#4. Find Maximum in List of Lists:
#Question: Given a list of lists, find the maximum element across all sublists.

def max_in_list_of_lists(lists):
    flat_list = [num for sublist in lists for num in sublist]
    return max(flat_list)
def dup_array(self, input_array):
    new_list = []
    a = input_array
    for i in range(1,(len(input_array)-1)):
        if a[i] in input_array:
            new_list = new_list.append(a[i])
    return new_list



input_array = dup_array([3,4,4,5,6,2,3,5])
print input_array
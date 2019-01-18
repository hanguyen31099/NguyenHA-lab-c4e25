def get_even_list(list_number):
    new_list=[]
    for j in list_number:
        if j%2==0:
            new_list.append(j)
    return new_list
even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

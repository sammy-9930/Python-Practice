def min_index_sum(arr1, arr2):
    index_1 = 5
    index_2 = 5
    for i in range(len(arr1)):
        indx = arr2.index(arr1[i])

        if i + indx < index_1 + index_2:
            index_1 = i 
            index_2 = indx

    print(arr1[index_1], index_1+index_2)


fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
fav2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']
min_index_sum(fav1, fav2)

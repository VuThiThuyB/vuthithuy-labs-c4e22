def get_even_list(list):
    new_list = []
    for i in range(len(list)):
        if list[i]%2 == 0:
            new_list.append(list[i])
    print(new_list)

list = [1,4,5,-1,10]
get_even_list(list)
def get_even_list(l):
    new_l = []
    for num in l:
        if num %2 == 0:
            new_l.append(num)
    return new_l
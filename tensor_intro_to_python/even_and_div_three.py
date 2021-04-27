def even_and_div_three(first, second):
    i = first
    while i <= second:
        if i % 2 == 0 and i % 3 == 0:
            print(i)
            i += 1
        else:
            i += 1
    return 'Finish!'

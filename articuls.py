def all_subsets_list(original_set_as_lst):
    all_subsets = [[]]
    for x in original_set_as_lst:
        all_subsets.extend([subset + [x] for subset in all_subsets])
    return all_subsets

def articuls(articul_str):
    dot_divided_only_articul_lst = list(articul_str.replace(' ', '.'))
    divider_indexes = []

    for i, x in enumerate(dot_divided_only_articul_lst):
        if x == '.':
            divider_indexes.append(i)

    all_divider_indexes_combinations = all_subsets_list(divider_indexes)

    for indexses_combination in all_divider_indexes_combinations:
        articul = dot_divided_only_articul_lst[:]
        for index in indexses_combination:
            articul[index] = ' '

        print ''.join(articul)


if __name__ == '__main__':
    
    articuls('1.2')
    print
    articuls('1.2.3')
    print
    articuls('1.2.3.4')
    print
    articuls('1.2 3 4.5')


# -*- coding: utf-8 -*-

"""
Future: (important) Adding cool visual end, with turing machine and tape. (urgent) self.instructions extracted from tape

Author: Vishal Paudel (2003)
Motivation: The Emperor's New Mind, Roger Penrose (Chapter 2: Algorithms and Turing Machines)
Scope: The current one only runs UN*2

Last Edit: February 17, 2021 (Probably giving astrological data makes more sense, that is, if worlds change)

Note: My usual defensive programming, I have to have more knowledge than a first sem, to comment on the implementation
"""


from Miscellaneous import print_custom


def bubble_sort(*, source, bool_mute: bool = False) -> list:
    """
    This function is the normal replication of bubble sort algorithm. <wiki_link>.
    (list, bool=False) -> list

    :param source: The list that you want to sort
    :param bool_mute: Pass True if you don't want to see print statements
    :return: temp_lst_main: A deep copy of your list only sorted ascending order
    """
    iter(source)  # To check if the 'source' can be iterated over, i.e. get_item is defined for 'source'

    print_custom(source, bool_mute)

    source = list(source)
    int_outer_index = 0

    int_swap_count = 0
    int_head_shift = 0

    while int_outer_index < (len(source)):

        inner_index = 0
        while inner_index < (len(source) - int_outer_index - 1):

            if source[inner_index] > source[inner_index + 1]:
                """
                New swapper found!
                """

                source[inner_index], source[inner_index + 1] = source[inner_index + 1], source[inner_index]

                print_custom('|\nSwap Happened\n|\n' + str(source), bool_mute)
                int_swap_count += 1

            inner_index += 1

            print_custom('|\nHead shifted\n|\n' + str(source), bool_mute)
            int_head_shift += 1

        if int_swap_count == 0:
            print_custom('|\nThe List was already Sorted !\n', bool_mute)
            break

        int_outer_index += 1

    print_custom('\n' + str(int_swap_count) + ' time swaps', bool_mute)
    print_custom(f'Total number of constant time operations: {int_swap_count + int_head_shift} ⪅ O(n^2)', bool_mute)

    return source


if __name__ == "__main__":

    my_lst = [5, 6, 4, 66, 3]

    print(bubble_sort(source=my_lst, bool_mute=False))

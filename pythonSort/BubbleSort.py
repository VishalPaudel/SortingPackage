# -*- coding: utf-8 -*-

"""
Future: (important) Adding cool visual end, with turing machine and tape. (urgent) self.instructions extracted from tape

Author: Vishal Paudel (2003)
Motivation: The Emperor's New Mind, Roger Penrose (Chapter 2: Algorithms and Turing Machines)
Scope: The current one only runs UN*2

Last Edit: February 17, 2021 (Probably giving astrological data makes more sense, that is, if worlds change)

Note: My usual defensive programming, I have to have more knowledge than a first sem, to comment on the implementation
"""


def bubble_sort(lst_main: list, bool_mute: bool = False) -> list:
    """
    This function is the normal replication of bubble sort algorithm. <wiki_link>.
    (list, bool=False) -> list

    :param lst_main: The list that you want to sort
    :param bool_mute: Pass True if you don't want to see print statements
    :return: temp_lst_main: A deep copy of your list only sorted ascending order
    """
    print(lst_main)

    lst_main = list(lst_main)
    int_outer_index = 0

    int_swap_count = 0
    int_head_shift = 0

    while int_outer_index < (len(lst_main)):

        inner_index = 0
        while inner_index < (len(lst_main) - int_outer_index - 1):

            if lst_main[inner_index] > lst_main[inner_index + 1]:
                """
                New swapper found!
                """

                lst_main[inner_index], lst_main[inner_index + 1] = lst_main[inner_index + 1], lst_main[inner_index]

                if not bool_mute:
                    print('|\nSwap Happened\n|', lst_main, sep='\n')
                    int_swap_count += 1

            inner_index += 1

            if not bool_mute:
                print('|\nHead shifted\n|', lst_main, sep='\n')
                int_head_shift += 1

        if int_swap_count == 0:
            if not bool_mute:
                print('|\nThe List was already Sorted !\n')
            break

        int_outer_index += 1

    if not bool_mute:
        print('\n' + str(int_swap_count), 'time swaps')
        print(f'The total number of constant time operations: {int_swap_count + int_head_shift} ⪅ O(n^2)')

    return lst_main


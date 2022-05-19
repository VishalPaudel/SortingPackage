
# -*- coding: utf-8 -*-
# !/usr/bin/env python


"""
Future: (important) Adding cool visual end, with turing machine and tape. (urgent) self.instructions extracted from tape

Author: Vishal Paudel (2003)
Motivation: The Emperor's New Mind, Roger Penrose (Chapter 2: Algorithms and Turing Machines)
Scope: The current one only runs UN*2

Last Edit: February 17, 2021 (Probably giving astrological data makes more sense, that is, if worlds change)

Note: My usual defensive programming, I have to have more knowledge than a first sem, to comment on the implementation
"""


from Miscellaneous import print_custom


def selection_sort(*, source, bool_mute: bool = False) -> list | tuple:
    """
    This is the replication of Selection Sort O( n^2 ) <wiki link>.
    (iterable, bool=False) -> list

    :param source: The list that you want to sort
    :param bool_mute: Pass True if you don't want to see print statements
    :return: temp_lst_main: A deep copy of your list only sorted ascending order
    """

    iter(source)

    if len(source) <= 1:
        print_custom("Already Sorted!", bool_mute)
        return source

    def minimum_element(sliced_source):

        if len(sliced_source) == 0:

            print_custom("The size of the List is Zero!", bool_mute)
            return None

        index = 0
        lowest_element_index = 0
        min_element = sliced_source[0]

        while index < len(sliced_source):

            if sliced_source[index] < min_element:

                min_element = sliced_source[index]
                lowest_element_index = index

            index += 1

        return min_element, lowest_element_index

    def remove_element(sliced_source, element):

        element_index = 0

        while element_index != len(sliced_source):

            if sliced_source[element_index] == element:
                print_custom(f"Deleting {element}", bool_mute)

    lst = [-10, -2, 4, 5, -9, -9.5, 2]

    print_custom(minimum_element(lst))

    prefix = []
    suffix = source

    while len(prefix) < len(source):

        min_val, index = minimum_element(suffix)

        prefix.append(min_val)
        print(suffix)
        suffix = suffix[0:index] + suffix[index + 1:]

    return prefix


if __name__ == "__main__":

    lst = [5, 4, 1, 2, 3]

    print(selection_sort(source=lst, bool_mute=False))

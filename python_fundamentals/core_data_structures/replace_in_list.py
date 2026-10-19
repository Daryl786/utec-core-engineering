#!/usr/bin/env python3


def replace_in_list(my_list, idx, element):
    """Reemplaza el elemento en idx; devuelve la lista."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

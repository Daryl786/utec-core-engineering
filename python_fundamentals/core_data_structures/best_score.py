#!/usr/bin/env python3


def best_score(a_dictionary):
    """Devuelve la clave con el valor mas grande, o None."""
    if not a_dictionary:
        return None
    best_key = None
    best_value = None
    for key in a_dictionary:
        if best_value is None or a_dictionary[key] > best_value:
            best_key = key
            best_value = a_dictionary[key]
    return best_key

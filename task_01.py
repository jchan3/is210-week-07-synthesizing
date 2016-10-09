#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_01."""


def get_matches(players):
    """A function that creates a list of unique matchups from a list of
        player names.

    Args:
        players(list): A list of player names.

    Returns:
        list: A list of unique matchups stored as tuples.

    Examples:

        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

    """
    match_list = []
    for index, item in enumerate(players):
        for index2, item2 in enumerate(players):
            if index < index2:
                new_match = (item, item2)
                match_list.append(new_match)

    return match_list

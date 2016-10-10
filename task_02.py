#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_02."""


import getpass
import authentication


def login(username, maxattempts=3):
    """A function that prompts for and authenticates the password of a username.

    Args:
        username(str): A string representing the username of the user attempting
        to log in.
        maxattempts(int, optional): An integer represents the maximum number of
        prompted attempts before the functiion returns False. Defaults: Three

    Returns:
        boolean: A value of True or False if authentication succeeds.

    Examples:

        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False

    """
    been_authenticated = False
    attempts = 0
    question = 'Please enter your password: '
    errormsg = 'Incorrect username or password. You have {} attempts left.'

    while attempts < maxattempts:
        myval = getpass.getpass(question)

        if authentication.authenticate(username, myval):
            been_authenticated = True
            break
        else:
            attempts += 1
            print errormsg.format(maxattempts - attempts)

    return been_authenticated

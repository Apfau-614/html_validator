#!/bin/python3
import re


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    >>> validate_html('<a href="https://example.com">link</a>')
    True
    '''

    try:
        tags = _extract_tags(html)
    except ValueError:
        return False

    stack = []

    for tag in tags:
        if not tag.startswith('</'):
            name = tag[1:-1].split()[0]
            stack.append(name)
        else
            if len(stack) == 0:
                return False
            name = tag[2:-1].split()[0]
            if stack[-1] == name:
                stack.pop()
            else:
                return False

    return len(stack) == 0




    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the stack.py file.
    # The main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags.


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    i = 0
    n = len(html)

    while i < n:
        if html[i] == '<':
            close_idx = html.find('>', i + 1)
            if close_idx == -1:
                raise ValueError('found < without matching >')
            inner = html[i + 1:close_idx]
            if '<' in inner:
                raise ValueError('found < without matching >')
            tags.append(html[i:close_idx + 1])
            i = close_idx + 1
        else:
            i += 1

    return tags

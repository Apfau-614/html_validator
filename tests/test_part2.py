'''
Test cases for HTML tags that also contain attributes within the tags.
'''

import HTML_Validator


def test__extract_tags_1():
    assert HTML_Validator._extract_tags('this is a <strong test>') == ['<strong>']

def test__extract_tags_2():
    assert HTML_Validator._extract_tags('this is a <a href="https://izbicki.me">link</a>') == ['<a>','</a>']

def test__extract_tags_3():
    assert HTML_Validator._extract_tags('this is a <a href="https://izbicki.me">') == ['<a>']

def test__extract_tags_4():
    assert HTML_Validator._extract_tags('this is a <a href="https://izbicki.me">link and a <span class=bold id=test></span></a>') == ['<a>','<span>','</span>','</a>']


def test_validate_html_1():
    assert not HTML_Validator.validate_html('this is a <strong test>')

def test_validate_html_2():
    assert HTML_Validator.validate_html('this is a <strong test> bold me </strong>')

def test_validate_html_3():
    assert HTML_Validator.validate_html('this is a <a href="https://izbicki.me">link</a>')

def test_validate_html_4():
    assert not HTML_Validator.validate_html('this is a <a href="https://izbicki.me">')

def test_validate_html_5():
    assert HTML_Validator.validate_html('this is a <a href="https://izbicki.me">link and a <span class=bold id=test></span></a>')

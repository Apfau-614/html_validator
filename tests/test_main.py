import HTML_Validator
import pytest


def test__extract_tags_1():
    assert HTML_Validator._extract_tags('') == []

def test__extract_tags_2():
    assert HTML_Validator._extract_tags('python in fun') == []

def test__extract_tags_3():
    assert HTML_Validator._extract_tags('<strong></strong>') == ['<strong>','</strong>']

def test__extract_tags_4():
    assert HTML_Validator._extract_tags('python in <strong>fun</strong>') == ['<strong>','</strong>']

def test__extract_tags_5():
    assert HTML_Validator._extract_tags('<a><b><c></a></b><f>') == ['<a>','<b>','<c>','</a>','</b>','<f>']

def test__extract_tags_6():
    with pytest.raises(ValueError, match='found < without matching >'):
        HTML_Validator._extract_tags('<')

def test__extract_tags_7():
    with pytest.raises(ValueError, match='found < without matching >'):
        HTML_Validator._extract_tags('this is a <strong test')

def test__extract_tags_8():
    with pytest.raises(ValueError, match='found < without matching >'):
        HTML_Validator._extract_tags('this is a <strong< test')

def test__extract_tags_9():
    n = 10000
    open_tags = [ '<' + str(i) + '>' for i in range(n) ]
    close_tags = [ '</' + str(i) + '>' for i in range(n) ]
    tags = open_tags + close_tags
    assert HTML_Validator._extract_tags(' '.join(tags)) == tags


def test_validate_html_1():
    assert HTML_Validator.validate_html('')

def test_validate_html_2():
    assert HTML_Validator.validate_html('<a></a>')

def test_validate_html_3():
    assert not HTML_Validator.validate_html('<a>')

def test_validate_html_4():
    assert not HTML_Validator.validate_html('</a>')

def test_validate_html_5():
    assert HTML_Validator.validate_html('<strong></strong><b></b>')

def test_validate_html_6():
    assert HTML_Validator.validate_html('<strong><b></b></strong>')

def test_validate_html_6():
    assert HTML_Validator.validate_html('<strong><strong></strong></strong>')

def test_validate_html_7():
    assert not HTML_Validator.validate_html('<strong><b></strong></b>')

def test_validate_html_8():
    assert HTML_Validator.validate_html('this is a test <em>hello!</em>')

def test_validate_html_9():
    assert HTML_Validator.validate_html('''
    <html>
    <head>
    <title>This is an awesome webpage!</title>
    </head>
    <body>
    <p>Programming is the <strong>best</strong>!</p>
    </body>
    </html>
    ''')

def test_validate_html_10():
    assert not HTML_Validator.validate_html('''
    <html>
    <head>
    <title>This is an awesome webpage!</title>
    </head>
    <body>
    <p>Programming is the <strong>best</strong>!
    </body>
    </html>
    ''')

def test_validate_html_11():
    assert not HTML_Validator.validate_html('<')

def test_validate_html_12():
    assert not HTML_Validator.validate_html('this is a <strong test')

def test_validate_html_13():
    assert not HTML_Validator.validate_html('this is a <strong< test')

def test_validate_html_14():
    n = 10000
    open_tags = [ '<' + str(i) + '>' for i in range(n) ]
    close_tags = [ '</' + str(i) + '>' for i in range(n) ]
    close_tags.reverse()
    tags = open_tags + close_tags
    assert HTML_Validator.validate_html(' '.join(tags))
    assert not HTML_Validator.validate_html(' '.join(open_tags))
    assert not HTML_Validator.validate_html(' '.join(close_tags))
    assert not HTML_Validator.validate_html(' '.join(tags[0:-1]))

def test_validate_html_15():
    n = 10000
    tags = [ '<' + str(i) + '></' + str(i) + '>' for i in range(n) ]
    assert HTML_Validator.validate_html(' '.join(tags))

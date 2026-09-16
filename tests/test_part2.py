'''
Test cases for HTML tags that also contain attributes within the tags.
'''

import HTML_Validator


# HINT:
# All the test cases in this file or for the validate_html function.
# But the easiest way to get them to pass is to modify the extract_tags function.


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

def test_validate_html_7():
    # </div> missing
    assert not HTML_Validator.validate_html('''
    <html lang=en>
    <body id=main>
    <div class=container>
    <p style="color: red">Visit <a href="https://izbicki.me">my site</a>!</p>
    </body>
    </html>
    ''')

def test_validate_html_8():
    # <em> and <strong> closed out of order
    assert not HTML_Validator.validate_html('''
    <body class=dark>
    <p id=p1>Programming is the <strong class=big><em>best</strong></em>!</p>
    </body>
    ''')

def test_validate_html_10():
    # nested lists, all matched, same tag names repeated
    assert HTML_Validator.validate_html('''
    <ul class=outer>
      <li id=a>one<ul class=inner><li id=a1>one.one</li></ul></li>
      <li id=b>two</li>
    </ul>
    ''')

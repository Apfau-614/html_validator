'''
Test cases for HTML tags that also contain attributes within the tags.

NOTE:
It is customary to write test cases in a sequence of "simplest to most complicated",
which allows us to develop our code starting with the simplest features first.
The HTML in this file is more complicated than the HTML in part1,
and that's why it is in its own separate file labeled part2.

HINT:
All the test cases in this file or for the validate_html function.
But the easiest way to get them to pass is to modify the extract_tags function.
My solution didn't have to modify validate_html at all.
I strongly encourage you to add some doctests to the _extract_tags function
that are related to attributes and get those doctests to pass.
If you created good doctests, then the more complicated "integration tests"
in this file will pass "automatically".
Working on simpler doctests for _extract_tags will be much easier
than working on the more complicated tests in this file.
'''

import HTML_Validator


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

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

def test_validate_html_6():
    # deep nesting, every tag carries attributes
    n = 10000
    opens  = ['<t%d class="c%d" id=i%d>' % (i, i, i) for i in range(n)]
    closes = ['</t%d>' % i for i in reversed(range(n))]
    assert HTML_Validator.validate_html('text '.join(opens + closes))
    assert not HTML_Validator.validate_html('text '.join(opens))
    assert not HTML_Validator.validate_html('text '.join(opens + closes[:-1]))

def test_validate_html_7():
    # flat sequence of sibling tags with attributes containing angle-free noise
    n = 10000
    doc = ''.join('<p style="a:%d" data-x=\'y z\'>para %d</p>\n' % (i, i) for i in range(n))
    assert HTML_Validator.validate_html('<body id=main>' + doc + '</body>')
    assert not HTML_Validator.validate_html('<body id=main>' + doc)

def test_validate_html_8():
    # mismatched-order interleaving deep in an otherwise valid large document
    n = 5000
    prefix = ''.join('<d%d k=v>' % i for i in range(n))
    suffix = ''.join('</d%d>' % i for i in reversed(range(n)))
    assert not HTML_Validator.validate_html(prefix + '<a href="x"><b id=y></a></b>' + suffix)
    assert HTML_Validator.validate_html(prefix + '<a href="x"><b id=y></b></a>' + suffix)

def test_validate_html_9():
    # attribute values that are near-misses for tag syntax (slashes, equals, spaces)
    n = 2000
    doc = ''.join(
        '<a href="https://izbicki.me/path/%d?q=1&r=2" target=_blank>link %d</a>' % (i, i)
        for i in range(n))
    assert HTML_Validator.validate_html('<html lang=en><body>' + doc + '</body></html>')
    assert not HTML_Validator.validate_html('<html lang=en><body>' + doc + '</html></body>')

def test_validate_html_10():
    # same tag name repeated/self-nested with differing attributes
    n = 10000
    doc = '<div class=x>' * n + 'content' + '</div>' * n
    assert HTML_Validator.validate_html(doc)
    assert not HTML_Validator.validate_html(doc + '</div>')

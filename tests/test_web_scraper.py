from web_scraper import __version__
from web_scraper.web_scraper import *


def test_version():
    assert __version__ == '0.1.0'


def test_citation_count():
    url = 'https://en.m.wikipedia.org/wiki/History_of_Mexico'
    expected = '5 citations needed'
    actual = get_citations_needed_count(url)
    assert actual == expected


def test_citation_report():
    url = 'https://en.m.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_report(url)[1]
    expected ='h'

    assert actual == expected

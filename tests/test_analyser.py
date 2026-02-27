import pytest

from excuse.analyser import analyze


def test_analyze_length():
    result = analyze("I was late because of traffic")
    assert result["length"] == len("I was late because of traffic")


def test_analyze_keyword():
    result = analyze("Please excuse me")
    assert result["has_please"] is True

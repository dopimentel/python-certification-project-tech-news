import pytest
from unittest.mock import MagicMock
from tech_news.analyzer.reading_plan import ReadingPlanService


@pytest.fixture
def mock_find_news_valid_values():
    mock = MagicMock()
    yield mock


@pytest.fixture
def mock_find_news_invalid_values():
    mock = MagicMock()
    yield mock


@pytest.fixture
def mock_find_news_negative_value():
    mock = MagicMock()
    yield mock


def test_reading_plan_group_news(mock_find_news_valid_values, mock_find_news_invalid_values, mock_find_news_negative_value):
    test_reading_plan_group_news_valid_values(mock_find_news_valid_values)
    test_reading_plan_group_news_invalid_values(mock_find_news_invalid_values)
    test_reading_plan_group_news_negative_value(mock_find_news_negative_value)


def test_reading_plan_group_news_valid_values(mock_find_news_valid_values):
    mock_find_news_valid_values.return_value = [
        {"title": "Title 1", "reading_time": 5},
        {"title": "Title 2", "reading_time": 10},
        {"title": "Title 3", "reading_time": 15},
    ]
    result = ReadingPlanService.group_news_for_available_time(10)
    assert result == {
        "readable": [
            {"unfilled_time": 5, "chosen_news": [("Title 1", 5)]},
            {"unfilled_time": 0, "chosen_news": [("Title 2", 10)]},
        ],
        "unreadable": [("Title 3", 15)],
    }
    mock_find_news_valid_values.assert_called_once()


def test_reading_plan_group_news_invalid_values(mock_find_news_invalid_values):
    invalid_values = [-5, 0]
    for value in invalid_values:
        with pytest.raises(ValueError):
            ReadingPlanService.group_news_for_available_time(value)
    mock_find_news_invalid_values.assert_not_called()


def test_reading_plan_group_news_negative_value(mock_find_news_negative_value):
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-5)
    mock_find_news_negative_value.assert_not_called()

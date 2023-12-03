import unittest
from unittest.mock import patch

from src.views import get_currencies, get_stocks


class GetStocksTestCase(unittest.TestCase):
    @patch("src.views.requests.get")
    def test_get_stocks_success(self, mock_requests_get):
        mock_response = {"Global Quote": {"01. symbol": "AAPL", "05. price": "350.12"}}
        mock_requests_get.return_value.json.return_value = mock_response
        stocks = get_stocks(["AAPL"])

        self.assertEqual(stocks, [{"stock": "AAPL", "price": "350.12"}])

    @patch("src.views.requests.get")
    def test_get_stocks_exception(self, mock_requests_get):
        mock_requests_get.side_effect = Exception("API Error")

        stocks = get_stocks(["AAPL"])

        self.assertEqual(stocks, ([], []))

    @patch("requests.get")
    def test_get_currencies_success(self, mock_get):
        mock_data = {
            "Realtime Currency Exchange Rate": {
                "1. From_Currency Code": "USD",
                "5. Exchange Rate": "75.50",
            }
        }
        mock_get.return_value.json.return_value = mock_data

        result = get_currencies(["USD"])

        expected_result = [{"currency": "USD", "rate": "75.50"}]
        self.assertEqual(result, expected_result)

    @patch("requests.get")
    def test_get_currencies_error(self, mock_get):
        mock_get.return_value.json.side_effect = Exception("API error")

        result = get_currencies(["USD"])

        expected_result = ([], [])
        self.assertEqual(result, expected_result)

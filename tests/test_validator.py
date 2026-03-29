import pytest
from unittest.mocked import patch, MagicMock
from validator import statusvalidator, portvalidator

def test_statusvalidator_success():
    # We "mock" requests.get so it doesn't actually hit the internet
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        result = statusvalidator("google.com")
        assert result is True

def test_statusvalidator_failure():
    with patch('requests.get') as mock_get:
        # Simulate a timeout or connection error
        mock_get.side_effect = Exception("Connection Error")
        result = statusvalidator("dummy.com")
        assert isinstance(result, Exception)

def test_portvalidator_open():
    with patch('socket.socket') as mock_socket:
        # connect_ex returns 0 if the port is open
        mock_socket.return_value.__enter__.return_value.connect_ex.return_value = 0
        result = portvalidator("google.com", 80)
        assert result is True

def test_portvalidator_closed():
    with patch('socket.socket') as mock_socket:
        # Any non-zero return means the port is closed
        mock_socket.return_value.__enter__.return_value.connect_ex.return_value = 111
        result = portvalidator("google.com", 9999)
        assert result is False
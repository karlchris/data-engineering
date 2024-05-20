import io
import my_module
import pytest

def test_count_lines_in_file(mocker):
    mock_file_manager = mocker.MagicMock()
    mock_file = mocker.MagicMock(spec=io.IOBase)
    mock_file_manager.return_value.__enter__.return_value = mock_file

    mocker.patch('my_module.FileManager', mock_file_manager)

    # Set up the mock file to return 5 lines
    mock_file.readlines.return_value = ['line\n'] * 5

    assert my_module.count_lines_in_file('filename.txt') == 5

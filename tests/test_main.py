import sys
from unittest.mock import patch

from main import parse_args


def test_parse_args():
    sys.argv = ['main.py', 'file1.log', 'file2.log', '--report', 'output.log']
    args = parse_args()
    assert args.files == ['file1.log', 'file2.log']
    assert args.report == 'output.log'


@patch('main.LogProcessor.extract_logs')
def test_main_with_no_data(mock_extract, capsys):
    mock_extract.return_value = None
    sys.argv = ['main.py', 'dummy.log', '--report']

    from main import main
    main()

    captured = capsys.readouterr()
    assert "No valid log data" in captured.out


@patch('main.LogProcessor.is_valid_filename')
def test_main_invalid_report_filename(mock_valid, capsys):
    mock_valid.return_value = False
    sys.argv = ['main.py', 'dummy.log', '--report', 'invalid/report.log']

    from main import main
    main()

    captured = capsys.readouterr()
    assert "Error: Invalid report filename" in captured.out
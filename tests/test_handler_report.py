from handler_report import HandlerReport


def test_generate():
    handler = HandlerReport()
    data = [('INFO', '/path'), ('WARNING', '/path'), ('INFO', '/another')]
    result = handler.generate(data)
    assert result == {
        '/path': {'INFO': 1, 'WARNING': 1},
        '/another': {'INFO': 1}
    }

def test_display(capsys):
    handler = HandlerReport()
    data = {'/path': {'INFO': 2}, '/another': {'WARNING': 1}}
    handler.display(data)
    captured = capsys.readouterr()
    assert "HANDLER" in captured.out
    assert "INFO" in captured.out
    assert "TOTAL" in captured.out


def test_save(tmp_path):
    handler = HandlerReport()
    data = {'/path': {'INFO': 2}}
    test_file = tmp_path / "test_report.log"

    handler.save(data, str(test_file))

    content = test_file.read_text()
    assert "HANDLER" in content
    assert "INFO" in content
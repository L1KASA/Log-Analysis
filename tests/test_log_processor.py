from log_processor import LogProcessor


def test_is_valid_filename_valid():
    assert LogProcessor.is_valid_filename("valid_file.log") == True

def test_is_valid_filename_invalid():
    invalid_names = ["file/name.log", "file\\name.log", "file:name.log", "file???"]
    for name in invalid_names:
        assert LogProcessor.is_valid_filename(name) == False

def test_extract_logs_with_valid_file(tmp_path):
    test_file = tmp_path / "test.log"
    content = """
    2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]
    2025-03-28 12:21:51,000 INFO django.request: GET /admin/dashboard/ 200 OK [192.168.1.68]
    2025-03-28 12:40:47,000 CRITICAL django.core.management: DatabaseError: Deadlock detected
    2025-03-28 12:25:45,000 DEBUG django.db.backends: (0.41) SELECT * FROM 'products' WHERE id = 4;
    2025-03-28 12:03:09,000 DEBUG django.db.backends: (0.19) SELECT * FROM 'users' WHERE id = 32;
"""
    test_file.write_text(content)
    result = LogProcessor.extract_logs(str(test_file))
    assert result == [('INFO', '/api/v1/reviews/'), ('INFO', '/admin/dashboard/')]

def test_extract_logs_with_invalid_file():
    result = LogProcessor.extract_logs("invalid_file.log")
    assert result is None
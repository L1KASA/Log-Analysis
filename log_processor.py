from typing import Optional, List, Tuple
import re


class LogProcessor:
    @staticmethod
    def is_valid_filename(filename) -> bool:
        return not any(x in filename for x in '/\\:*?"<>|')

    @staticmethod
    def extract_logs(filename: str) -> Optional[List[Tuple[str, str]]]:
        try:
            with open(filename, 'r') as f:
                pattern = r"(\w+)\s+django\.request.*?((?:\/\w+)+\/)"
                matches = []
                for line in f:
                    match = re.search(pattern, line)
                    if match:
                        matches.append((match.group(1), match.group(2)))
                return matches if matches else None
        except Exception as e:
            print(f'Error reading {filename}: {e}')
            return None

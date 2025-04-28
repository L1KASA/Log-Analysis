import sys
from typing import List, Tuple, Dict
from report import Report


class HandlerReport(Report):
    def __init__(self):
        self.levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    def generate(self, data: List[Tuple[str, str]]) -> Dict[str, Dict[str, int]]:
        result = {}
        for level, path in data:
            if path not in result:
                result[path] = {}
            result[path][level] = result[path].get(level, 0) + 1
        return result

    def _prepare_report(self, data: Dict[str, Dict[str, int]]):
        sorted_handlers = sorted(data.keys())
        handler_width = max(len(handler) for handler in sorted_handlers) + 2
        level_width = max(len(level) for level in self.levels) + 2

        header = f"{'HANDLER':<{handler_width}}"
        for level in self.levels:
            header += f"{level:<{level_width}}"
        separator = "-" * len(header)

        grand_total = 0
        total_counts = {level: 0 for level in self.levels}
        rows = []

        for handler in sorted_handlers:
            counts = data[handler]
            row_total = 0
            row = f"{handler:<{handler_width}}"

            for level in self.levels:
                count = counts.get(level, 0)
                row += f"{count:<{level_width}}"
                row_total += count
                total_counts[level] += count

            grand_total += row_total
            rows.append(row)

        footer = f"{'TOTAL':<{handler_width}}"
        for level in self.levels:
            footer += f"{total_counts[level]:<{level_width}}"

        return header, separator, rows, footer, grand_total

    def display(self, data: Dict[str, Dict[str, int]]) -> None:
        header, separator, rows, footer, grand_total = self._prepare_report(data)

        print(header)
        print(separator)
        print('\n'.join(rows))
        print(separator)
        print(footer)
        print("\nTotal requests:", grand_total)

    def save(self, data: Dict[str, Dict[str, int]], output_filename: str) -> None:
        if not output_filename:
            return

        try:
            header, separator, rows, footer, grand_total = self._prepare_report(data)

            with open(output_filename, 'w') as f:
                f.write(header + '\n')
                f.write(separator + '\n')
                f.write('\n'.join(rows) + '\n')
                f.write(separator + '\n')
                f.write(footer + '\n')
                f.write(f"\nTotal requests: {grand_total}\n")

            print(f"Report saved to: {output_filename}")
        except Exception as e:
            print(f"Save error: {str(e)}", file=sys.stderr)

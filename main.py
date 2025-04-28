import argparse
import multiprocessing
from typing import Tuple, List, Optional

from handler_report import HandlerReport
from log_processor import LogProcessor


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Analyze Django request logs.',
        usage='%(prog)s [files ...]] --report [output file]',
        epilog="Examples:\n"
               "python main.py logs/app1.log logs/app2.log --report \n"
               "python main.py logs/app1.log logs/app2.log --report handler.log",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'files',
        nargs='+',
        help='Log files to process (optional)'
    )
    parser.add_argument(
        '--report',
        metavar='OUTPUT_FILE',
        nargs='?',
        const='handlers.log',
        help='Output file for the report (default: handlers.log)'
    )

    return parser.parse_args()


def process_file(filename: str) -> Optional[List[Tuple[str, str]]]:
    return LogProcessor.extract_logs(filename)


def main():
    args = parse_args()
    report = HandlerReport()

    if not LogProcessor.is_valid_filename(args.report):
        print("Error: Invalid report filename")
        return

    with multiprocessing.Pool() as pool:
        results = pool.map(process_file, args.files)

    data = []
    for result in results:
        if result:
            data.extend(result)

    if not data:
        print("No valid log data found in any files")
        return

    report_data = report.generate(data)
    report.display(report_data)
    report.save(report_data, args.report)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()

import re
from typing import Callable, Iterable
from os import path


def validate_line(line: str) -> bool:
    """Checks if a line has exactly 5 elements"""
    return len(line.split()) == 5


def validate_date(date: str) -> bool:
    """Checks if the date is valid and follows the pattern DDDD-DD-DD"""
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattern, date):
        return True
    return False


def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    """Reads data from a file, validates each line and creates a report file"""
    report_file = 'report.txt'
    with open(filepath, 'r') as file, open(report_file, 'w') as report:
        for line in file:
            line = line.strip()
            validation_result = [v(line.split()[i]) for i, v in enumerate(validators)]
            if all(validation_result):
                continue
            else:
                invalid_reason = validators[validation_result.index(False)].__name__
                report.write(f"{line} {invalid_reason}\n")
    return path.abspath(report_file)
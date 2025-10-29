#!/usr/bin/env python3
"""
Advent of Code Day Creator

Usage: python create_day.py <year> <day>

This script creates a new day solution file in the specified year's python directory.
It generates a template with common imports and structure based on the year's utils.py.

Examples:
    python create_day.py 2024 13
    python create_day.py 2023 1
    python create_day.py 2022 25
"""

import argparse
import os
import sys
from pathlib import Path


TEMPLATE = """from utils import get_data
from utils import get_line_data
from utils import get_int_data
from utils import parse_grid
from utils import timeit
from utils import Point

import numpy
import itertools
import collections
import re


@timeit
def part_one(data):
    for line in data:
        pass


@timeit
def part_two(data):
    for line in data:
        pass


@timeit
def main(data):
    data = get_data("{day}")
    grid = parse_grid(data)
    data = get_line_data("{day}")
    data = get_int_data("{day}")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)

"""

def create_day_file(year, day):
    """Create a new day solution file for the specified year and day."""
    # Validate year
    if year < 2015 or year > 2030:
        print(f"Error: Year must be between 2015 and 2030.")
        return False

    # Validate day
    if day < 1 or day > 25:
        print(f"Error: Day must be between 1 and 25.")
        return False

    # Check if year directory exists
    year_dir = f"{year}/python"
    if not os.path.exists(year_dir):
        print(f"Error: Year {year} directory not found. Available years:")
        available_years = []
        for item in os.listdir('.'):
            if os.path.isdir(item) and item.isdigit() and len(item) == 4:
                available_years.append(int(item))
        for y in sorted(available_years):
            print(f"  {y}")
        return False

    # Format day with leading zero
    day_str = f"{day:02d}"
    file_path = f"{year_dir}/day{day_str}.py"

    # Check if file already exists
    if os.path.exists(file_path):
        print(f"Error: File {file_path} already exists.")
        return False

    # Replace the placeholder with the actual day
    python_script = TEMPLATE.replace("{day}", day_str)

    # Create the file
    try:
        with open(file_path, 'w') as f:
            f.write(python_script)
        print(f"Created {file_path}")
        return True
    except Exception as e:
        print(f"Error creating file: {e}")
        return False


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Create a new Advent of Code day solution file',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python create_day.py 2024 13
  python create_day.py 2023 1
  python create_day.py 2022 25
        """
    )

    parser.add_argument('year', type=int, help='Year (2015-2030)')
    parser.add_argument('day', type=int, help='Day (1-25)')

    args = parser.parse_args()

    success = create_day_file(args.year, args.day)
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""
Advent of Code Runner

Usage: python advent.py <year> <day>

This script allows you to run any Advent of Code solution from the root directory.
It dynamically imports and executes the appropriate day module.

Examples:
    python advent.py 2024 13
    python advent.py 2023 1
    python advent.py 2022 25
"""

import sys
import os
import importlib.util
from pathlib import Path


def find_available_years():
    """Find all available years in the repository."""
    years = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and item.isdigit() and len(item) == 4:
            years.append(int(item))
    return sorted(years)


def find_available_days(year):
    """Find all available days for a given year."""
    year_dir = f"{year}/python"
    if not os.path.exists(year_dir):
        return []

    days = []
    for item in os.listdir(year_dir):
        if item.startswith('day') and item.endswith('.py') and item != 'utils.py':
            day_num = item[3:-3]  # Remove 'day' prefix and '.py' suffix
            if day_num.isdigit():
                days.append(int(day_num))
    return sorted(days)


def run_day(year, day):
    """Run the specified day's solution."""
    # Validate year
    available_years = find_available_years()
    if year not in available_years:
        print(f"Error: Year {year} not found. Available years: {available_years}")
        return False

    # Validate day
    available_days = find_available_days(year)
    if day not in available_days:
        print(f"Error: Day {day} not found for year {year}. Available days: {available_days}")
        return False

    # Construct the module path
    module_path = f"{year}/python/day{day:02d}.py"

    if not os.path.exists(module_path):
        print(f"Error: Module file {module_path} not found.")
        return False

    try:
        # Temporarily change to the year's python directory
        original_cwd = os.getcwd()
        year_python_dir = f"{year}/python"
        os.chdir(year_python_dir)

        # Add the current directory to Python path for imports
        sys.path.insert(0, os.getcwd())

        # Load and execute the day module
        spec = importlib.util.spec_from_file_location(f"day{day:02d}", f"day{day:02d}.py")
        module = importlib.util.module_from_spec(spec)

        print(f"Running Advent of Code {year} Day {day}")
        print("=" * 40)

        # First execute the module to define all functions
        spec.loader.exec_module(module)
        
        # Then call the main function if it exists
        if hasattr(module, 'main'):
            module.main()

        print("=" * 40)
        print("Execution completed.")
    finally:
        # Always restore the original working directory
        os.chdir(original_cwd)

    return True


def main():
    """Main entry point for the script."""
    if len(sys.argv) != 3:
        print("Usage: python advent.py <year> <day>")
        print("\nAvailable years and days:")

        available_years = find_available_years()
        for year in available_years:
            days = find_available_days(year)
            if days:
                print(f"  {year}: days {min(days)}-{max(days)}")

        print(f"\nExamples:")
        print(f"  python advent.py 2024 13")
        print(f"  python advent.py 2023 1")
        return 1

    try:
        year = int(sys.argv[1])
        day = int(sys.argv[2])
    except ValueError:
        print("Error: Year and day must be integers.")
        return 1

    if year < 2015 or year > 2030:
        print("Error: Year must be between 2015 and 2030.")
        return 1

    if day < 1 or day > 25:
        print("Error: Day must be between 1 and 25.")
        return 1

    success = run_day(year, day)
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())

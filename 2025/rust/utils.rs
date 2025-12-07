// Utility functions for Advent of Code solutions

use std::fs;

pub fn get_data(day: &str) -> String {
    let file_path = format!("2025/inputs/input{}.txt", day);

    fs::read_to_string(&file_path)
        .unwrap_or_else(|_| {
            eprintln!("Warning: Could not read file {}. Returning empty string.", file_path);
            String::new()
        })
        .trim_end()
        .to_string()
}

pub fn get_line_data(day: &str) -> Vec<String> {
    get_data(day)
        .lines()
        .map(|s| s.to_string())
        .filter(|s| !s.is_empty())
        .collect()
}

pub fn get_nums_unsigned(s: &str) -> Vec<u64> {
    let mut nums = Vec::new();
    let mut current_num = String::new();

    for ch in s.chars() {
        if ch.is_ascii_digit() {
            current_num.push(ch);
        } else {
            if !current_num.is_empty() {
                if let Ok(num) = current_num.parse::<u64>() {
                    nums.push(num);
                }
                current_num.clear();
            }
        }
    }

    if !current_num.is_empty() {
        if let Ok(num) = current_num.parse::<u64>() {
            nums.push(num);
        }
    }

    nums
}

pub fn get_nums(s: &str) -> Vec<i64> {
    let mut nums = Vec::new();
    let mut current_num = String::new();
    let mut is_negative = false;

    for ch in s.chars() {
        if ch == '-' && current_num.is_empty() {
            is_negative = true;
        } else if ch.is_ascii_digit() {
            current_num.push(ch);
        } else {
            if !current_num.is_empty() {
                if let Ok(mut num) = current_num.parse::<i64>() {
                    if is_negative {
                        num = -num;
                    }
                    nums.push(num);
                }
                current_num.clear();
                is_negative = false;
            }
        }
    }

    if !current_num.is_empty() {
        if let Ok(mut num) = current_num.parse::<i64>() {
            if is_negative {
                num = -num;
            }
            nums.push(num);
        }
    }

    nums
}

pub fn rotated<T: Clone>(matrix: &[Vec<T>]) -> Vec<Vec<T>> {
    if matrix.is_empty() {
        return Vec::new();
    }

    let rows = matrix.len();
    let cols = matrix[0].len();
    let mut result = Vec::new();

    for c in 0..cols {
        let mut new_row = Vec::new();
        for r in (0..rows).rev() {
            new_row.push(matrix[r][c].clone());
        }
        result.push(new_row);
    }

    result
}

pub fn mult(nums: &[i64]) -> i64 {
    nums.iter().product()
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct Point {
    pub x: i32,
    pub y: i32,
}

impl Point {
    pub fn new(x: i32, y: i32) -> Self {
        Point { x, y }
    }

    pub fn neighbors_8(&self) -> Vec<Point> {
        vec![
            Point::new(self.x, self.y + 1),     // N
            Point::new(self.x + 1, self.y + 1), // NE
            Point::new(self.x + 1, self.y),     // E
            Point::new(self.x + 1, self.y - 1), // SE
            Point::new(self.x, self.y - 1),     // S
            Point::new(self.x - 1, self.y - 1), // SW
            Point::new(self.x - 1, self.y),     // W
            Point::new(self.x - 1, self.y + 1), // NW
        ]
    }
}

impl std::ops::Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point::new(self.x + other.x, self.y + other.y)
    }
}

pub fn parse_grid(data: &str, keep_values: Option<&str>) -> std::collections::HashMap<Point, char> {
    let mut grid = std::collections::HashMap::new();
    let lines: Vec<&str> = data.lines().collect();

    for (y, line) in lines.iter().enumerate() {
        for (x, ch) in line.chars().enumerate() {
            let point = Point::new(x as i32, y as i32);
            if let Some(keep) = keep_values {
                if keep.contains(ch) {
                    grid.insert(point, ch);
                }
            } else {
                grid.insert(point, ch);
            }
        }
    }

    grid
}

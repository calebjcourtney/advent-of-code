use crate::y2025::utils;
use itertools::Itertools;
use std::collections::HashSet;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct Point {
    x: i64,
    y: i64,
}

impl Point {
    fn new(x: i64, y: i64) -> Self {
        Point { x, y }
    }
}

struct Grid {
    points_set: HashSet<Point>,
    points_ordered: Vec<Point>,
    vertical_lines: Option<Vec<(i64, (i64, i64))>>,
    horizontal_lines: Option<Vec<((i64, i64), i64)>>,
}

impl Grid {
    fn new(data: &[String]) -> Self {
        let points_set: HashSet<Point> = data
            .iter()
            .map(|line| {
                let nums = utils::get_nums(line);
                Point::new(nums[0], nums[1])
            })
            .collect();

        let points_ordered: Vec<Point> = data
            .iter()
            .map(|line| {
                let nums = utils::get_nums(line);
                Point::new(nums[0], nums[1])
            })
            .collect();

        Grid {
            points_set,
            points_ordered,
            vertical_lines: None,
            horizontal_lines: None,
        }
    }

    fn area_between_points(p1: Point, p2: Point) -> i64 {
        ((p1.x - p2.x).abs() + 1) * ((p1.y - p2.y).abs() + 1)
    }

    fn build_line_segments(&mut self) {
        if self.vertical_lines.is_some() {
            return;
        }

        let mut vertical_lines = Vec::new();
        let mut horizontal_lines = Vec::new();
        let mut prev_point = self.points_ordered[self.points_ordered.len() - 1];

        for &point in &self.points_ordered {
            if prev_point.x == point.x {
                // Vertical line
                let y1 = prev_point.y;
                let y2 = point.y;
                let (y_start, y_end) = if y1 < y2 { (y1, y2) } else { (y2, y1) };
                vertical_lines.push((point.x, (y_start, y_end)));
            } else if prev_point.y == point.y {
                // Horizontal line
                let x1 = prev_point.x;
                let x2 = point.x;
                let (x_start, x_end) = if x1 < x2 { (x1, x2) } else { (x2, x1) };
                horizontal_lines.push(((x_start, x_end), point.y));
            }
            prev_point = point;
        }

        self.vertical_lines = Some(vertical_lines);
        self.horizontal_lines = Some(horizontal_lines);
    }

    fn check_lines_cross_rectangle(
        &self,
        x_min: i64,
        x_max: i64,
        y_min: i64,
        y_max: i64,
    ) -> bool {
        let vertical_lines = self.vertical_lines.as_ref().unwrap();
        let horizontal_lines = self.horizontal_lines.as_ref().unwrap();

        // Check vertical
        for &(line_x, (line_y_start, line_y_end)) in vertical_lines {
            if x_min < line_x && line_x < x_max {
                if (line_y_start <= y_min && y_min < line_y_end)
                    || (line_y_start < y_max && y_max <= line_y_end)
                {
                    return false;
                }
            }
        }

        // Check horizontal
        for &((line_x_start, line_x_end), line_y) in horizontal_lines {
            if y_min < line_y && line_y < y_max {
                if (line_x_start <= x_min && x_min < line_x_end)
                    || (line_x_start < x_max && x_max <= line_x_end)
                {
                    return false;
                }
            }
        }

        true
    }

    fn part_one(&self) -> i64 {
        self.points_set
            .iter()
            .combinations(2)
            .map(|v| Self::area_between_points(*v[0], *v[1]))
            .max()
            .unwrap_or(0)
    }

    fn part_two(&mut self) -> i64 {
        self.build_line_segments();

        let n = self.points_ordered.len();
        let mut areas_and_pairs: Vec<(i64, usize, usize)> = Vec::new();

        for i in 0..n {
            for j in (i + 1)..n {
                let area = Self::area_between_points(self.points_ordered[i], self.points_ordered[j]);
                areas_and_pairs.push((area, i, j));
            }
        }

        areas_and_pairs.sort_by(|a, b| b.0.cmp(&a.0));

        for (area, i, j) in areas_and_pairs {
            let p1 = self.points_ordered[i];
            let p2 = self.points_ordered[j];
            let (x_min, x_max) = if p1.x < p2.x { (p1.x, p2.x) } else { (p2.x, p1.x) };
            let (y_min, y_max) = if p1.y < p2.y { (p1.y, p2.y) } else { (p2.y, p1.y) };

            if self.check_lines_cross_rectangle(x_min, x_max, y_min, y_max) {
                return area;
            }
        }

        0
    }
}

pub fn main() {
    let data = utils::get_line_data("09");
    let mut grid = Grid::new(&data);
    println!("{}", grid.part_one());
    println!("{}", grid.part_two());
}


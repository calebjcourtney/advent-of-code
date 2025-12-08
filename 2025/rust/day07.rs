use crate::y2025::utils::{self, Point};
use std::collections::{HashMap, HashSet, VecDeque};

fn part_one(start: Point, grid: &HashMap<Point, char>) -> usize {
    let mut tachyon_splits = HashSet::new();
    let mut visited = HashSet::new();
    let mut current_points = VecDeque::new();
    current_points.push_back(start);

    while let Some(current_point) = current_points.pop_front() {
        if visited.contains(&current_point) {
            continue;
        }

        if !grid.contains_key(&current_point) {
            continue;
        }

        visited.insert(current_point);
        let cell = grid[&current_point];

        if cell == '^' {
            tachyon_splits.insert(current_point);
            let left = current_point + utils::W;
            let right = current_point + utils::E;
            if grid.contains_key(&left) {
                current_points.push_back(left);
            }
            if grid.contains_key(&right) {
                current_points.push_back(right);
            }
        } else if cell == '.' || cell == 'S' {
            let down = current_point + utils::N;
            if grid.contains_key(&down) {
                current_points.push_back(down);
            }
        }
    }

    tachyon_splits.len()
}

fn part_two(start: Point, grid: &HashMap<Point, char>) -> u64 {
    let max_y = grid.keys().map(|p| p.y).max().unwrap_or(0);
    let mut memo = HashMap::new();

    fn count_timelines(
        point: Point,
        max_y: i32,
        grid: &HashMap<Point, char>,
        memo: &mut HashMap<Point, u64>,
    ) -> u64 {
        if point.y >= max_y {
            return 1;
        }

        if let Some(&cached) = memo.get(&point) {
            return cached;
        }

        let down = point + utils::N;

        if !grid.contains_key(&down) {
            return 1;
        }

        let cell_below = grid[&down];

        let result = if cell_below == '^' {
            let left = down + utils::W;
            let right = down + utils::E;
            let mut result = 0;
            if grid.contains_key(&left) {
                result += count_timelines(left, max_y, grid, memo);
            } else {
                result += 1;
            }
            if grid.contains_key(&right) {
                result += count_timelines(right, max_y, grid, memo);
            } else {
                result += 1;
            }
            result
        } else {
            count_timelines(down, max_y, grid, memo)
        };

        memo.insert(point, result);
        result
    }

    count_timelines(start, max_y, grid, &mut memo)
}

pub fn main() {
    let data = utils::get_data("07");
    let grid = utils::parse_grid(&data, None);
    let start = grid
        .iter()
        .find(|(_, &v)| v == 'S')
        .map(|(&p, _)| p)
        .expect("No start point found");

    let p1_result = part_one(start, &grid);
    println!("{}", p1_result);

    let p2_result = part_two(start, &grid);
    println!("{}", p2_result);
}


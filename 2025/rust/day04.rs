use crate::y2025::utils;
use std::collections::HashMap;

fn count_neighbors(grid: &HashMap<utils::Point, char>, point: utils::Point) -> usize {
    point.neighbors_8()
        .iter()
        .filter(|&neighbor| grid.contains_key(neighbor))
        .count()
}

fn part_one(grid: &HashMap<utils::Point, usize>) -> usize {
    grid.values().filter(|&&v| v < 4).count()
}

fn part_two(mut grid: HashMap<utils::Point, usize>) -> usize {
    let mut total_removed = 0;
    let mut prev_removed = 0;

    loop {
        let points_to_remove: Vec<utils::Point> = grid
            .iter()
            .filter(|(_, &v)| v < 4)
            .map(|(&p, _)| p)
            .collect();

        for point in points_to_remove {
            total_removed += 1;
            grid.remove(&point);

            for neighbor in point.neighbors_8() {
                if let Some(count) = grid.get_mut(&neighbor) {
                    *count = count.saturating_sub(1);
                }
            }
        }

        if prev_removed == total_removed {
            return total_removed;
        }

        prev_removed = total_removed;
    }
}

pub fn main() {
    let data = utils::get_data("04");
    let char_grid = utils::parse_grid(&data, Some("@"));

    // Convert grid values to neighbor counts
    let mut grid: HashMap<utils::Point, usize> = HashMap::new();
    for point in char_grid.keys() {
        let count = count_neighbors(&char_grid, *point);
        grid.insert(*point, count);
    }

    let p1_result = part_one(&grid);
    println!("{}", p1_result);

    let p2_result = part_two(grid);
    println!("{}", p2_result);
}

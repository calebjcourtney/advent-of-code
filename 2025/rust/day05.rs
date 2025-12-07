use crate::y2025::utils;

#[derive(Clone)]
struct Range {
    start: i64,
    end: i64,
}

fn parse_data(data: &str) -> (Vec<Range>, Vec<i64>) {
    let sections: Vec<&str> = data.split("\n\n").collect();
    let range_lines: Vec<&str> = sections[0].lines().collect();

    let ingredient_ranges: Vec<Range> = range_lines
        .iter()
        .map(|line| {
            let parts: Vec<&str> = line.split('-').collect();
            let start: i64 = parts[0].parse().unwrap();
            let end: i64 = parts[1].parse().unwrap();
            Range { start, end: end + 1 }
        })
        .collect();

    let available_ingredient_ids: Vec<i64> = sections[1]
        .split_whitespace()
        .filter_map(|s| s.parse().ok())
        .collect();

    (ingredient_ranges, available_ingredient_ids)
}

fn merge_ranges(mut ingredient_ranges: Vec<Range>) -> Vec<Range> {
    ingredient_ranges.sort_by_key(|r| r.start);

    let mut idx = 0;
    while idx < ingredient_ranges.len().saturating_sub(1) {
        let current_end = ingredient_ranges[idx].end;
        let next_start = ingredient_ranges[idx + 1].start;

        if current_end - 1 >= next_start {
            let next_end = ingredient_ranges[idx + 1].end;
            ingredient_ranges[idx].end = current_end.max(next_end);
            ingredient_ranges.remove(idx + 1);
        } else {
            idx += 1;
        }
    }

    ingredient_ranges
}

fn part_one(ingredient_ranges: &[Range], available_ingredient_ids: &[i64]) -> usize {
    available_ingredient_ids
        .iter()
        .filter(|&&ingredient_id| {
            ingredient_ranges
                .iter()
                .any(|r| ingredient_id >= r.start && ingredient_id < r.end)
        })
        .count()
}

fn part_two(ingredient_ranges: &[Range]) -> i64 {
    ingredient_ranges.iter().map(|r| r.end - r.start).sum()
}

pub fn main() {
    let data = utils::get_data("05");
    let (ingredient_ranges, available_ingredient_ids) = parse_data(&data);
    let ingredient_ranges = merge_ranges(ingredient_ranges);

    let result_part_one = part_one(&ingredient_ranges, &available_ingredient_ids);
    println!("{}", result_part_one);

    let result_part_two = part_two(&ingredient_ranges);
    println!("{}", result_part_two);
}

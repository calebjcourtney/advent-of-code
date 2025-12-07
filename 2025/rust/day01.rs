use crate::y2025::utils;

pub fn main() {
    let data = utils::get_line_data("01");

    let mut p1 = 0i32;
    let mut p2 = 0i32;
    let mut pos: i32 = 50;

    for line in data {
        let nums: Vec<u32> = line
            .chars()
            .filter_map(|c| c.to_digit(10))
            .collect::<Vec<_>>();

        if nums.is_empty() {
            continue;
        }

        let num = nums.iter().fold(0i32, |acc, &d| acc * 10 + d as i32);

        let diff: i32 = if line.starts_with('R') { 1 } else { -1 };

        for _ in 0..num {
            pos = (pos + diff).rem_euclid(100);

            if pos == 0 {
                p2 += 1;
            }
        }

        if pos == 0 {
            p1 += 1;
        }
    }

    println!("{}", p1);
    println!("{}", p2);
}

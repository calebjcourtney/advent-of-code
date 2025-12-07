use crate::y2025::utils;

fn process_data(data: &str) -> Vec<(u64, u64)> {
    let nums = utils::get_nums_unsigned(data);
    nums.chunks_exact(2)
        .map(|chunk| (chunk[0], chunk[1]))
        .collect()
}

fn p1_invalid(num: u64) -> bool {
    let num_str = num.to_string();
    let len = num_str.len();

    if len % 2 != 0 {
        return false;
    }

    let half = len / 2;
    &num_str[..half] == &num_str[half..]
}

fn p2_invalid(num: u64) -> bool {
    let num_str = num.to_string();
    let len = num_str.len();

    for prefix_len in 1..=len / 2 {
        let prefix = &num_str[..prefix_len];

        if len % prefix_len == 0 {
            let repetitions = len / prefix_len;

            if repetitions >= 2 {
                let repeated = prefix.repeat(repetitions);
                if repeated == num_str {
                    return true;
                }
            }
        }
    }

    false
}

pub fn main() {
    let data = utils::get_data("02");
    let data = process_data(&data);

    let mut p1 = 0u64;
    let mut p2 = 0u64;

    for (low, high) in data {
        for num in low..=high {
            if p1_invalid(num) {
                p1 += num;
            }
            if p2_invalid(num) {
                p2 += num;
            }
        }
    }

    println!("{}", p1);
    println!("{}", p2);
}

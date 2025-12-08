#[path = "../2025/rust/utils.rs"]
mod utils;

#[path = "../2025/rust/day01.rs"]
mod day01;
#[path = "../2025/rust/day02.rs"]
mod day02;
#[path = "../2025/rust/day03.rs"]
mod day03;
#[path = "../2025/rust/day04.rs"]
mod day04;
#[path = "../2025/rust/day05.rs"]
mod day05;
#[path = "../2025/rust/day06.rs"]
mod day06;
#[path = "../2025/rust/day07.rs"]
mod day07;
#[path = "../2025/rust/day08.rs"]
mod day08;

pub fn run_day(day: u32) {
    match day {
        1 => day01::main(),
        2 => day02::main(),
        3 => day03::main(),
        4 => day04::main(),
        5 => day05::main(),
        6 => day06::main(),
        7 => day07::main(),
        8 => day08::main(),
        _ => {
            eprintln!("Error: Day {} not yet implemented for year 2025.", day);
            std::process::exit(1);
        }
    }
}

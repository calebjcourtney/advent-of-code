use clap::Parser;
use std::path::Path;

mod y2025;

#[derive(Parser, Debug)]
#[command(name = "advent")]
#[command(about = "Advent of Code Runner", long_about = None)]
struct Args {
    year: u32,
    day: u32,
}

fn main() {
    let args = Args::parse();

    if args.year < 2015 || args.year > 2030 {
        eprintln!("Error: Year must be between 2015 and 2030.");
        std::process::exit(1);
    }

    if args.day < 1 || args.day > 25 {
        eprintln!("Error: Day must be between 1 and 25.");
        std::process::exit(1);
    }

    let day_file = format!("{}/rust/day{:02}.rs", args.year, args.day);
    if !Path::new(&day_file).exists() {
        eprintln!("Error: File {} not found.", day_file);
        std::process::exit(1);
    }

    println!("Running Advent of Code {} Day {}", args.year, args.day);
    println!("{}", "=".repeat(40));

    match args.year {
        2025 => y2025::run_day(args.day),
        _ => {
            eprintln!("Error: Year {} not yet implemented.", args.year);
            std::process::exit(1);
        }
    }

    println!("{}", "=".repeat(40));
    println!("Execution completed.");
}

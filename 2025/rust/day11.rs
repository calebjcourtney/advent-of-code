use crate::y2025::utils;
use std::collections::HashMap;

type Graph = HashMap<String, Vec<String>>;

fn build_graph(data: &[String]) -> Graph {
    let mut graph = Graph::new();

    for line in data {
        if let Some((device, outputs)) = line.split_once(": ") {
            let device = device.trim().to_string();
            let outputs: Vec<String> = outputs
                .split_whitespace()
                .map(|s| s.trim().to_string())
                .collect();
            graph.insert(device, outputs);
        }
    }

    graph.entry("out".to_string()).or_insert_with(Vec::new);

    graph
}

fn count_paths(
    graph: &Graph,
    cache: &mut HashMap<(String, String, bool, bool), i64>,
    curr: &str,
    end: &str,
    has_visited_dac: bool,
    has_visited_fft: bool,
) -> i64 {
    let key = (curr.to_string(), end.to_string(), has_visited_dac, has_visited_fft);

    if let Some(&cached) = cache.get(&key) {
        return cached;
    }

    let has_visited_dac = has_visited_dac || curr == "fft";
    let has_visited_fft = has_visited_fft || curr == "dac";

    if curr == end {
        let result = if has_visited_dac && has_visited_fft { 1 } else { 0 };
        cache.insert(key, result);
        return result;
    }

    let result = graph
        .get(curr)
        .map(|neighbors| {
            neighbors
                .iter()
                .map(|neighbor| {
                    count_paths(graph, cache, neighbor, end, has_visited_dac, has_visited_fft)
                })
                .sum()
        })
        .unwrap_or(0);

    cache.insert(key, result);
    result
}

pub fn main() {
    let data = utils::get_line_data("11");
    let graph = build_graph(&data);

    let mut cache = HashMap::new();

    let part_one = count_paths(&graph, &mut cache, "you", "out", true, true);
    println!("{}", part_one);

    cache.clear();

    let part_two = count_paths(&graph, &mut cache, "svr", "out", false, false);
    println!("{}", part_two);
}

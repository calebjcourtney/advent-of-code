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
    cache: &mut HashMap<(String, String), i64>,
    start: &str,
    end: &str,
) -> i64 {
    let key = (start.to_string(), end.to_string());

    if let Some(&cached) = cache.get(&key) {
        return cached;
    }

    if start == end {
        cache.insert(key, 1);
        return 1;
    }

    if start == "out" {
        cache.insert(key, 0);
        return 0;
    }

    let result = graph
        .get(start)
        .map(|neighbors| {
            neighbors
                .iter()
                .map(|neighbor| count_paths(graph, cache, neighbor, end))
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

    let part_one = count_paths(&graph, &mut cache, "you", "out");
    println!("{}", part_one);

    let part_two = count_paths(&graph, &mut cache, "svr", "fft")
        * count_paths(&graph, &mut cache, "fft", "dac")
        * count_paths(&graph, &mut cache, "dac", "out")
        + count_paths(&graph, &mut cache, "svr", "dac")
            * count_paths(&graph, &mut cache, "dac", "fft")
            * count_paths(&graph, &mut cache, "fft", "out");
    println!("{}", part_two);
}

use crate::y2025::utils;
use itertools::Itertools;
use std::collections::{HashMap, HashSet};

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct Point3D {
    x: i64,
    y: i64,
    z: i64,
}

impl Point3D {
    fn new(x: i64, y: i64, z: i64) -> Self {
        Point3D { x, y, z }
    }

    fn distance(&self, other: &Point3D) -> f64 {
        let dx = (self.x - other.x) as f64;
        let dy = (self.y - other.y) as f64;
        let dz = (self.z - other.z) as f64;
        (dx * dx + dy * dy + dz * dz).sqrt()
    }
}

fn parse_data(data: &[String]) -> HashSet<Point3D> {
    let mut points = HashSet::new();
    for line in data {
        let nums = utils::get_nums(line);
        if nums.len() >= 3 {
            points.insert(Point3D::new(nums[0], nums[1], nums[2]));
        }
    }
    points
}

struct CircuitConnector {
    points: HashSet<Point3D>,
    parent: HashMap<Point3D, Point3D>,
    circuit_count: usize,
}

impl CircuitConnector {
    fn new(points: HashSet<Point3D>) -> Self {
        let parent: HashMap<Point3D, Point3D> = points.iter().map(|&p| (p, p)).collect();
        let circuit_count = points.len();
        CircuitConnector {
            points,
            parent,
            circuit_count,
        }
    }

    fn find(&mut self, point: Point3D) -> Point3D {
        if self.parent[&point] != point {
            let root = self.find(self.parent[&point]);
            self.parent.insert(point, root);
            root
        } else {
            point
        }
    }

    fn union(&mut self, p1: Point3D, p2: Point3D) -> bool {
        let root1 = self.find(p1);
        let root2 = self.find(p2);
        if root1 != root2 {
            self.parent.insert(root1, root2);
            self.circuit_count -= 1;
            true
        } else {
            false
        }
    }

    fn get_circuit_sizes(&mut self) -> Vec<usize> {
        let mut circuit_sizes: HashMap<Point3D, usize> = HashMap::new();
        let points: Vec<Point3D> = self.points.iter().copied().collect();
        for point in points {
            let root = self.find(point);
            *circuit_sizes.entry(root).or_insert(0) += 1;
        }
        let mut sizes: Vec<usize> = circuit_sizes.values().copied().collect();
        sizes.sort_by(|a, b| b.cmp(a));
        sizes
    }

    fn solve(&mut self) -> (i64, i64) {
        let mut pairs: Vec<(f64, Point3D, Point3D)> = Vec::new();
        for (p1, p2) in self.points.iter().combinations(2).map(|v| (*v[0], *v[1])) {
            let dist = p1.distance(&p2);
            pairs.push((dist, p1, p2));
        }

        pairs.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

        let target_pairs = if self.points.len() > 20 { 1000 } else { 10 };
        let mut part_one_result: Option<i64> = None;
        let mut part_two_result: Option<i64> = None;

        for (i, (_dist, p1, p2)) in pairs.iter().enumerate() {
            let was_connected = self.union(*p1, *p2);

            if i == target_pairs - 1 {
                let sizes = self.get_circuit_sizes();
                part_one_result = if sizes.len() >= 3 {
                    Some(sizes[0] as i64 * sizes[1] as i64 * sizes[2] as i64)
                } else if sizes.len() == 2 {
                    Some(sizes[0] as i64 * sizes[1] as i64)
                } else if sizes.len() == 1 {
                    Some(sizes[0] as i64)
                } else {
                    Some(0)
                };
            }

            if was_connected {
                if self.circuit_count == 1 {
                    part_two_result = Some(p1.x * p2.x);
                }
            }

            if part_one_result.is_some() && part_two_result.is_some() {
                return (part_one_result.unwrap(), part_two_result.unwrap());
            }
        }

        (
            part_one_result.unwrap_or(0),
            part_two_result.unwrap_or(0),
        )
    }
}

pub fn main() {
    let data = utils::get_line_data("08");
    let points = parse_data(&data);

    let mut connector = CircuitConnector::new(points);
    let (p1_result, p2_result) = connector.solve();
    println!("{}", p1_result);
    println!("{}", p2_result);
}


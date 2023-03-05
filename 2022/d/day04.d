import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;
import std.regex;


//def part_two(data: List[Tuple[Set, Set]]) -> int:
//    return sum(
//        bool(s1 & s2)
//        for (s1, s2) in data
//    )


struct Row
{
    int[] r1;
    int[] r2;

    bool contains() {
        auto intersection = setIntersection(r1, r2).array.sort!("a < b").array;
        return intersection == r1 || intersection == r2;
    }

    bool overlap() {
        return setIntersection(r1, r2).array.length > 0;
    }
}


Row parseLine(string line)
{
    auto parts = line.split(",");
    int[] r1 = parts[0].split("-").map!(x => to!int(x)).array;
    int[] r2 = parts[1].split("-").map!(x => to!int(x)).array;

    return Row(iota(r1[0], r1[1] + 1).array, iota(r2[0], r2[1] + 1).array);
}


Row[] readData()
{
    auto data = readText("../inputs/input04.txt");
    return map!(row => parseLine(row))(data.splitLines).array;
}


void main()
{
    auto data = readData();
    writeln(data.filter!(row => row.contains).array.length);
    writeln(data.filter!(row => row.overlap).array.length);
}
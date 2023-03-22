import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;


long[string] parseData(string data)
{
    long[string] sizes;

    string[] path;
    foreach(line; data.strip.split("\n"))
    {
        auto tokens = line.strip.split();
        if (line.strip() == "$ cd /")
            tokens[$-1] = "root";

        if (tokens[1] == "cd") {
            if (tokens[2] == "..") {
                path = path[0 .. $-1];
            }
            else {
                path ~= tokens[2];
            }
        }

        else if (tokens[0].isNumeric) {
            long size = tokens[0].to!long;
            foreach(i; 0..path.length+1) {
                if (!sizes.keys.canFind(path[0..i].join("/")))
                    sizes[path[0..i].join("/")] = 0;

                sizes[path[0..i].join("/")] += size;
            }
        }
    }

    return sizes;
}


long partOne(long[string] data)
{
    long total = 0;
    foreach(value; data.byValue()) {
        if (value <= 100_000) {
            total += value;
        }
    }

    return total;
}


long partTwo(long[string] data)
{
    long total = 1000000000000;
    long maxUsed = 70000000 - 30000000;
    long totalUsed = data["root"];
    long needToFree = totalUsed - maxUsed;
    foreach(value; data.byValue()) {
        if (value >= needToFree)
            total = min(total, value);
    }

    return total;
}


void main(string[] args)
{
    string data = readText("../inputs/input07.txt");
    long[string] parsedData = parseData(data);
    writeln(partOne(parsedData));
    writeln(partTwo(parsedData));
}

import std.stdio;
import std.algorithm;
import std.conv;
import std.string;
import std.array;
import std.file;


string[] getLineData(string fileName) {
    return fileName.readText().strip().splitter("\n").array();
}

string[] getNums() {
    return "0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine".split();
}

int[] partOne(string[] lines) {
    auto nums = lines.map!(line => filter!(c => c.to!(string).isNumeric)(line));
    int[] output;
    foreach (num; nums) {
        output ~= ("" ~ num.to!string[0] ~ num.to!string[$ - 1]).to!int;
    }

    return output;
}

struct Index {
    string digit;
    int position;
}

Index[] indices(string line) {
    Index[] idx;
    foreach (num; getNums()) {
        if (line.canFind(num)) {
            idx ~= Index(num, line.countUntil(num).to!int);
        }
    }

    idx.sort!((a, b) => a.position < b.position);
    return idx;
}

int partTwo(string[] lines) {
    int answer = 0;

    foreach (line; lines) {
        Index[] idx = indices(line);
        string first = idx[0].digit;
        string last = idx[$ - 1].digit;
        answer += to!int(to!string(getNums().countUntil(first) / 2) ~ to!string(getNums().countUntil(last) / 2));
    }

    return answer;
}

void main() {
    string[] data = getLineData("../inputs/input01.txt");
    writeln(sum(partOne(data)));
    writeln(partTwo(data));
}

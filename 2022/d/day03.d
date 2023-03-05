import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;


string[] readData()
{
    auto data = readText("../inputs/input03.txt");
    return data
        .split("\n")
        .filter!(x => x.length > 0)
        .array;
}


int val(string x) {
    string asciiLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    return to!int(asciiLetters.indexOf(x)) + 1;
}


string get_overlap_char(string line) {
    int len = to!int(line.length) / 2;
    string first = line[0..len];
    string second = line[len..$];

    return to!string(first.filter!(x => second.canFind(x)).array[0]);
}


int partOne(string[] data) {
    return data.map!(x => val(get_overlap_char(x))).sum;
}


int partTwo(string[] data) {
    int sum = 0;
    foreach (chunk; chunks(data, 3)) {
        string first = chunk[0];
        string second = chunk[1];
        string third = chunk[2];

        sum += val(first.filter!(x => second.canFind(x) && third.canFind(x)).array[0].to!string);
    }

    return sum;
}


void main()
{
    auto lineData = readData();

    writeln(partOne(lineData));
    writeln(partTwo(lineData));
}

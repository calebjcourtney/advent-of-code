import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;


int[] readIntData()
{
    int[] output;

    File file = File("../inputs/input01.txt", "r");

    while (!file.eof()) {
        string line = strip(file.readln());
        output ~= to!int(line);
    }

    return output;
}

void main()
{
    int[] lineData = readIntData();

    writeln(sum(zip(lineData, lineData.dropOne).map!"a[0] < a[1]"));
    writeln(sum(zip(lineData, lineData[3 .. $]).map!"a[0] < a[1]"));
}
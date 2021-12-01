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

    auto part1 = sum(zip(lineData, lineData.dropOne).map!"a[0] < a[1]");
    writeln(part1);

    auto summedData = zip(lineData, lineData.dropOne, lineData.dropOne.dropOne).map!"a[0] + a[1] + a[2]";

    auto part2 = sum(zip(summedData, summedData.dropOne).map!"a[0] < a[1]");
    writeln(part2);
}
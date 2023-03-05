import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;


int[] readData()
{
    int[] array;

    auto data = readText("../inputs/input01.txt");
    auto elf_data = data.split("\n\n");

    foreach (elf; elf_data) {
        array ~= elf.split("\n").map!(to!int).sum;
    }

    return array.sort!("a > b").array;
}


void main()
{
    int[] lineData = readData();

    writeln(lineData[0]);
    writeln(lineData[0 .. 3].sum);

}
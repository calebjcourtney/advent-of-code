import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;
import std.regex;


int solve(string data, int depth)
{
	foreach (count, record; data.enumerate()) {
		if (count >= depth)
		{
			auto slice = data[count - depth .. count].map!(n => to!string(n)).array;
			auto sortedSlice = slice.sort.array;
			if (sortedSlice.uniq.array.length == depth) {
				return count.to!int;
			}
		}
	}
	return -1;
}


void main()
{
	string data = readText("../inputs/input06.txt");
	writeln(solve(data, 4));
	writeln(solve(data, 14));
}

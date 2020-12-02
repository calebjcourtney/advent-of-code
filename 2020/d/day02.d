import utils;

import std.stdio;
import std.typecons;
import std.array;
import std.conv;
import std.algorithm;


void main()
{
    auto data = getLineData("02");
    writeln(partOne(data));
    writeln(partTwo(data));
}


int partOne(string[] data)
{
    int valid = 0;
    foreach (line; data)
    {
        Line parsed = parseLine(line);
        if ((parsed.password.count(parsed.letter) >= parsed.start) & (parsed.password.count(parsed.letter) <= parsed.end))
            valid += 1;
    }

    return valid;
}


int partTwo(string[] data)
{
    int valid = 0;
    foreach (line; data)
    {
        Line parsed = parseLine(line);
        if ((to!string(parsed.password[to!int(parsed.start) - 1]) == parsed.letter) ^ (to!string(parsed.password[to!int(parsed.end) - 1]) == parsed.letter))
            valid += 1;
    }

    return valid;
}

struct Line
{
    int start;
    int end;
    string letter;
    char[] password;
}


Line parseLine(string line)
{
    auto range = line.split()[0];
    string letter = to!string(line.split()[1][0]);
    char[] password = to!(char[])(line.split()[2]);

    int start = to!int(range.split("-")[0]);
    int end = to!int(range.split("-")[1]);

    return Line(start, end, letter, password);
}

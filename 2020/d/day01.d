import utils;

import std.stdio;
import std.algorithm;


void main()
{
    writeln(partOne(getIntData("01")));
    writeln(partTwo(getIntData("01")));
}


int partOne(int[] data)
{
    int output;
    foreach (a; data)
        foreach (b; data[1 .. $])
        {
            if (sum([a, b]) == 2020)
            {
                output = fold!((a, b) => a * b)([a, b]);
                return output;
            }
        }

    return output;
}


int partTwo(int[] data)
{
    int output;
    foreach (a; data)
        foreach (b; data[1 .. $])
            foreach (c; data[2 .. $])
            {
                if (sum([a, b, c]) == 2020)
                {
                    output = fold!((a, b) => a * b)([a, b, c]);
                    return output;
                }
            }

    return output;
}

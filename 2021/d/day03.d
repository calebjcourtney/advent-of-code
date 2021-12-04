import std.stdio;
import std.string;
import std.conv;
import std.algorithm;
import std.array;


void main()
{
    auto data = readData();

    int part_one = partOne(data);
    writeln(part_one);
    int part_two = partTwo(data);
    writeln(part_two);
}

int partOne (char[][] data) {
    char[] epsilon;
    char[] gamma;

    for (int i; i < data[0].length; ++i)
    {
        char common_val = mostCommon(data, i, false);
        char uncommon_val = (common_val == '1') ? '0' : '1';

        gamma ~= common_val;
        epsilon ~= uncommon_val;
    }

    auto epsilon_val = to!int(epsilon.to!(string), 2);
    auto gamma_val = to!int(gamma.to!(string), 2);

    return epsilon_val * gamma_val;
}


int partTwo (char[][] data)
{
    char[] oxygen = filterData(data, false);
    char[] co2 = filterData(data, true);

    return to!int(oxygen, 2) * to!int(co2, 2);
}


char mostCommon(char[][] data, int index, bool invert) {
    int t;
    int f;

    foreach (row; data)
    {
        if (row[index] == '1')
            ++t;
        else if (row[index] == '0')
            ++f;
    }

    if (t == f)
        return (invert) ? '0': '1';

    if (invert)
        swap(t, f);

    if (t >= f)
        return '1';
    else
        return '0';
}


char[] filterData(char[][] data, bool invert)
{
    int i;
    while (data.length >1)
    {
        auto common_val = mostCommon(data, i, invert);
        data = data.filter!(a => a[i] == common_val).array;
        ++i;
    }

    return data[0];
}


char[][] readData()
{
    char[][] output;

    File file = File("../inputs/input03.txt", "r");

    while (!file.eof()) {
        string line = strip(file.readln());
        output ~= to!(char[])(line);
    }

    return output;
}

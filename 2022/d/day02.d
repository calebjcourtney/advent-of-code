import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;


struct Row {
    string one;
    string two;
}


Row[] readData()
{
    Row[] array;

    auto data = readText("../inputs/input02.txt");
    foreach (row; data.split("\n")) {
        if (row == "")
            continue;

        auto r = row.split();
        array ~= Row(r[0], r[1]);
    }

    return array;
}


int score(string p2, int outcome)
{
    int rps_score = [
        "r": 1,
        "p": 2,
        "s": 3
    ][p2];

    return outcome + rps_score;
}


int partOne(Row[] lineData) {
    int total;

    string[string] p1_map = [
        "A": "r",
        "B": "p",
        "C": "s"
    ];

    string[string] p2_map = [
        "X": "r",
        "Y": "p",
        "Z": "s"
    ];

    string p1_val;
    string p2_val;
    int outcome;

    foreach (row; lineData)
    {
        p1_val = p1_map[row.one];
        p2_val = p2_map[row.two];

        if (
            (p1_val == "s" && p2_val == "r") ||
            (p1_val == "p" && p2_val == "s") ||
            (p1_val == "r" && p2_val == "p")
        )
        {
            outcome = 6;
        }

        else if (p1_val == p2_val)
            outcome = 3;

        else
            outcome = 0;

        total += score(p2_val, outcome);
    }

    return total;
}


int partTwo(Row[] lineData) {
    int total;

    string[string] p1_map = [
        "A": "r",
        "B": "p",
        "C": "s"
    ];

    int[string] outcome_map = [
        "X": 0,
        "Y": 3,
        "Z": 6
    ];

    string[string] win_map = [
        "r": "s",
        "p": "r",
        "s": "p"
    ];

    string[string] loss_map = [
        "r": "p",
        "s": "r",
        "p": "s"
    ];

    string p1_val;
    string p2_val;
    int outcome;

    foreach (row; lineData)
    {
        p1_val = p1_map[row.one];
        outcome = outcome_map[row.two];

        if (outcome == 3)
            p2_val = p1_val;
        else if (outcome == 6) {
            p2_val = loss_map[p1_val];
        }
        else if (outcome == 0) {
            p2_val = win_map[p1_val];
        }
        else
            assert (false);

        total += score(p2_val, outcome);
    }

    return total;
}


void main()
{
    auto lineData = readData();

    writeln(partOne(lineData));
    writeln(partTwo(lineData));
}
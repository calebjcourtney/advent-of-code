import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;
import std.regex;


struct Stack
{
    string[] crates;

    void add(string[] list) {
        crates ~= list;
    }

    void insert(string c) {
        crates = [c] ~ crates;
    }

    string[] drop(int c)
    {
        string[] output = crates[$-c..$];
        crates = crates[0..$-c];
        return output;
    }

    string top() {
        return crates[$-1];
    }
}


struct Instruction {
    int count;
    int source;
    int target;
}


Instruction parseInstructions(string line) {
    int[] results = line.matchAll(`\d+`).map!(a => to!int(a[0])).array;
    return Instruction(results[0], results[1], results[2]);
}


string partOne(Stack[int] stacks, Instruction[] instructions) {
    foreach (instruction; instructions) {
        auto crates = stacks[instruction.source].drop(instruction.count);
        crates.reverse.array;
        stacks[instruction.target].add(crates);
    }

    string output;
    foreach (i; 1 .. stacks.length.to!(int) + 1) {
        output ~= stacks[i].top();
    }

    return output;
}


string partTwo(Stack[int] stacks, Instruction[] instructions) {
    foreach (instruction; instructions) {
        auto crates = stacks[instruction.source].drop(instruction.count);
        stacks[instruction.target].add(crates);
    }

    string output;
    foreach (i; 1 .. stacks.length.to!(int) + 1) {
        output ~= stacks[i].top();
    }

    return output;
}


void main(string[] args)
{
    auto data = readText("../inputs/input05.txt");
    auto instructions = data.split("\n\n")[1].strip.split("\n").map!(a => parseInstructions(a)).array;

    Stack[int] stackData = [
        1: Stack(["G", "D", "V", "Z", "J", "S", "B"]),
        2: Stack(["Z", "S", "M", "G", "V", "P"]),
        3: Stack(["C", "L", "B", "S", "W", "T", "Q", "F"]),
        4: Stack(["H", "J", "G", "W", "M", "R", "V", "Q"]),
        5: Stack(["C", "L", "S", "N", "F", "M", "D"]),
        6: Stack(["R", "G", "C", "D"]),
        7: Stack(["H", "G", "T", "R", "J", "D", "S", "Q"]),
        8: Stack(["P", "F", "V"]),
        9: Stack(["D", "R", "S", "T", "J"])
    ];
    writeln(partOne(stackData, instructions));

    stackData = [
        1: Stack(["G", "D", "V", "Z", "J", "S", "B"]),
        2: Stack(["Z", "S", "M", "G", "V", "P"]),
        3: Stack(["C", "L", "B", "S", "W", "T", "Q", "F"]),
        4: Stack(["H", "J", "G", "W", "M", "R", "V", "Q"]),
        5: Stack(["C", "L", "S", "N", "F", "M", "D"]),
        6: Stack(["R", "G", "C", "D"]),
        7: Stack(["H", "G", "T", "R", "J", "D", "S", "Q"]),
        8: Stack(["P", "F", "V"]),
        9: Stack(["D", "R", "S", "T", "J"])
    ];
    writeln(partTwo(stackData, instructions));

}

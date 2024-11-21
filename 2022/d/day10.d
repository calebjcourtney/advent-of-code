import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;
import std.math;


struct Instruction {
    string statement;
    int amount;
}


Instruction parseLine(string line) {
    auto info = line.strip().split();
    if (info.length == 1)
    	return Instruction(info[0], 0);

    return Instruction(info[0], info[1].to!int);
}


int[] parseInstructions(string data)
{
	int x = 1;
	int[] output = [0];

	foreach (line; data.splitLines()) {
		Instruction inst = parseLine(line);
		if (inst.statement == "noop")
			output ~= x;

		else {
			output ~= x;
			output ~= x;
			x += inst.amount;
		}
	}

	return output;
}

int partOne(int[] instructions)
{
	int output;
	foreach (x, y; instructions.enumerate())
		if (x % 40 == 20)
			output += x * y;

	return output;
}


string partTwo(int[] instructions)
{
	string output = "";
	foreach (i; iota(1, instructions.length, 40)) {
		foreach(j; iota(40)) {
			if (abs(instructions[i + j] - j) <= 1)
				output ~= "##";
			else
				output ~= "  ";
		}

		output ~= "\n";
	}

	return output;
}


void main(string[] args)
{
    string data = readText("../inputs/input10.txt").strip();
    int[] instructions = parseInstructions(data);
    writeln(partOne(instructions));
    writeln(partTwo(instructions));
}

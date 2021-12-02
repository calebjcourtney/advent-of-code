import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;


struct Instruction {
    string direction;
    int magnitude;
}


Instruction[] readData()
{
    Instruction[] output;

    File file = File("../inputs/input02.txt", "r");

    while (!file.eof()) {
        string[] line = strip(file.readln()).split();

        auto instruction = Instruction();
        instruction.direction = to!string(line[0]);
        instruction.magnitude = line[1].to!int;

        output ~= instruction;
    }

    return output;
}


int partOne(Instruction[] data) {
    int horizontal;
    int vertical;
    foreach (instruction; data)
    {
        switch (instruction.direction)
        {
            case "forward": 
                horizontal += instruction.magnitude;
                break;

            case "down": 
                vertical += instruction.magnitude;
                break; 

            case "up":
                vertical -= instruction.magnitude;
                break;

            default:
                break;
        }
    }

    return horizontal * vertical;
}


class Submarine
{
    int horizontal;
    int vertical;
    int aim;

    void addInstruction(Instruction instruction)
    {
        switch (instruction.direction)
        {
            case "forward": 
                this.horizontal += instruction.magnitude;
                this.vertical += this.aim * instruction.magnitude;
                break;

                //self.horizontal += int(line.split()[1])
                //self.vertical += self.aim * int(line.split()[1])

            case "down": 
                this.aim += instruction.magnitude;
                break; 

            case "up":
                this.aim -= instruction.magnitude;
                break;

            default:
                break;
        }
    }

    int position()
    {
        return this.horizontal * this.vertical;
    }
}

int partTwo(Instruction[] data)
{
    auto submarine = new Submarine();
    foreach (instruction; data)
    {
        submarine.addInstruction(instruction);
    }

    return submarine.position();
}

void main()
{
    auto lineData = readData();

    writeln(partOne(lineData));
    writeln(partTwo(lineData));
}
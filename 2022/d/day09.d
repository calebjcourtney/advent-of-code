import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;
import std.math;


struct Instruction {
    string direction;
    int count;
}


Instruction parseLine(string line) {
    auto info = line.strip().split();
    return Instruction(info[0], info[1].to!int);
}


struct Point {
    int x;
    int y;

    size_t toHash() const @safe pure nothrow
    {
        size_t hash;
        foreach (val; [x, y])
            hash = (hash * 999) + val;

        return hash;
    }

    bool opEquals(ref const Point p) const @safe pure nothrow
    {
        return this.x == p.x && this.y == p.y;
    }
}


Point pointFromDirection(string direction) {
    return [
        "U": Point(0, 1),
        "D": Point(0, -1),
        "R": Point(1, 0),
        "L": Point(-1, 0)
    ][direction];
}


class Rope
{
    Point[] knots;
    Point[] tailVisits;

    this(int ropeLen)
    {
        foreach (i; iota(ropeLen))
            knots ~= Point(0, 0);

        tailVisits ~= Point(0, 0);
    }

    void moveHead(string direction)
    {
        Point point = pointFromDirection(direction);
        this.knots[0].x += point.x;
        this.knots[0].y += point.y;
    }

    Point distance(int index)
    {
        return Point(
            this.knots[index - 1].x - this.knots[index].x,
            this.knots[index - 1].y - this.knots[index].y
        );
    }

    void moveIndex(int index, string direction)
    {
        Point dist = this.distance(index);
        if (abs(dist.x) < 2 && abs(dist.y) < 2)
            return;

        int x = dist.x == 0 ? 0 : abs(dist.x) / dist.x;
        int y = dist.y == 0 ? 0 : abs(dist.y) / dist.y;

        this.knots[index].x += x;
        this.knots[index].y += y;

        if (index == this.knots.length - 1 && !this.tailVisits.canFind(Point(this.knots[index].x, this.knots[index].y)))
            this.tailVisits ~= Point(this.knots[index].x, this.knots[index].y);
    }

    void move(Instruction instruction)
    {
        foreach (_; iota(instruction.count)) {
            this.moveHead(instruction.direction);
            foreach (index; iota(1, this.knots.length))
                this.moveIndex(index.to!int, instruction.direction);
        }
    }
}


ulong solve(string data, int ropeLen) {
    Rope rope = new Rope(ropeLen);
    foreach (line; data.split("\n")) {
        Instruction instruction = parseLine(line);
        rope.move(instruction);
    }

    return rope.tailVisits.length;
}


void main(string[] args)
{
    string data = readText("../inputs/input09.txt").strip();
    writeln(solve(data, 2));
    writeln(solve(data, 10));
}
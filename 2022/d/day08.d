import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;


class Grid
{
	int[][] data;

	this(string info)
	{
		foreach(line; info.strip().split("\n"))
			data ~= line.map!(to!int).array;
	}

	bool northVisible(int x, int y)
	{
		if (y == 0)
			return true;

		foreach (yi; iota(0, y))
			if (this.data[y][x] <= this.data[yi][x])
				return false;

		return true;
	}

	bool southVisible(int x, int y)
	{
		if (y == this.data.length.to!int)
			return true;

		foreach (yi; iota(y + 1, this.data.length))
			if (this.data[y][x] <= this.data[yi][x])
				return false;

		return true;
	}

	bool westVisible(int x, int y)
	{
		if (x == 0)
			return true;

		foreach (xi; iota(0, x))
			if (this.data[y][x] <= this.data[y][xi])
				return false;

		return true;
	}

	bool eastVisible(int x, int y)
	{
		if (x == this.data[y].length)
			return true;

		foreach (xi; iota(x + 1, this.data[y].length)) {
			if (this.data[y][x] <= this.data[y][xi])
				return false;
		}

		return true;
	}

	bool isVisible(int x, int y)
	{
		return any([
			this.northVisible(x, y),
			this.southVisible(x, y),
			this.westVisible(x, y),
			this.eastVisible(x, y)
		]);
	}

	int visibleTrees() {
		int total;
		foreach(y; iota(0, this.data.length.to!int))
			foreach(x; iota(0, this.data[y].length.to!int))
				if (this.isVisible(x, y))
					total++;

		return total;
	}

	int northCount(int x, int y) {
		int count;
        foreach (yi; iota(y - 1, -1, -1)) {
            count += 1;
            if (this.data[yi][x] >= this.data[y][x])
                return count;
        }

        return count;
	}

	int southCount(int x, int y) {
		int count;
        foreach (yi; iota(y + 1, data.length)) {
            count += 1;
            if (this.data[yi][x] >= this.data[y][x])
                return count;
        }

        return count;
	}

	int westCount(int x, int y) {
		int count;
        foreach (xi; iota(x - 1, -1, -1)) {
            count += 1;
            if (this.data[y][xi] >= this.data[y][x])
                return count;
        }

        return count;
	}

	int eastCount(int x, int y) {
		int count;
        foreach (xi; iota(x + 1, data[y].length)) {
            count += 1;
            if (this.data[y][xi] >= this.data[y][x])
                return count;
        }

        return count;
	}

	int scenicScore(int x, int y) {
		int score = 1;
		score *= this.northCount(x, y);
		score *= this.southCount(x, y);
		score *= this.eastCount(x, y);
		score *= this.westCount(x, y);

		return score;
    }

    int bestScenicScore() {
        int top_score;
        foreach (y; iota(0, this.data.length)) {
            foreach (x; iota(this.data[0].length)) {
                int temp = this.scenicScore(x.to!int, y.to!int);
                top_score = (temp > top_score) ? temp : top_score;
            }
        }

        return top_score;
    }
}


void main(string[] args)
{
    string data = readText("../inputs/input08.txt").strip();
    auto grid = new Grid(data);
    writeln(grid.visibleTrees());
    writeln(grid.bestScenicScore());
}

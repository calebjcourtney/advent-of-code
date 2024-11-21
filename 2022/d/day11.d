import std.stdio;
import std.conv;
import std.string;
import std.range;
import std.algorithm;
import std.array;
import std.file;
import std.math;
import std.regex;

import utils;


struct Monkey
{
    int[] items;
    string[] operation;
    int test;
    int ifTrue;
    int ifFalse;
    int inspections = 0;
}


/*
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
*/
Monkey parseMonkey(string data)
{
    Monkey monkey = Monkey();
    monkey.items = data.matchAll(`Starting items: (.*)`).map!(a => a[1].split(", ").map!(a => a.to!int).array).array[0];
    monkey.operation = data.matchAll(`Operation: (.*)`).map!(a => a[1]).array[0].split()[2 .. $];
    monkey.test = data.matchAll(`Test: divisible by (\d+)`).map!(a => a[1].to!int).array[0];
    monkey.ifTrue = data.matchAll(`If true: throw to monkey (\d+)`).map!(a => a[1].to!int).array[0];
    monkey.ifFalse = data.matchAll(`If false: throw to monkey (\d+)`).map!(a => a[1].to!int).array[0];

    return monkey;
}


int runOperation(int value, string[] operation)
{
    int change;
    if (operation[2] == "old")
        change = value;
    else
        change = operation[2].to!int;

    int newVal;
    if (operation[1] == "*")
        newVal = value * change;

    if (operation[1] == "+")
        newVal = value + change;

    return newVal;
}


int partOne(Monkey[] monkeyData)
{
    foreach (c; iota(20)) {
        foreach(monkeyIndex; 0..monkeyData.length) {
            foreach (item; monkeyData[monkeyIndex.to!int].items) {
                monkeyData[monkeyIndex.to!int].inspections++;

                item = (runOperation(item, monkeyData[monkeyIndex.to!int].operation).to!int / 3).to!int;
                if (item % monkeyData[monkeyIndex.to!int].test == 0)
                    monkeyData[monkeyData[monkeyIndex.to!int].ifTrue].items ~= item;
                else
                    monkeyData[monkeyData[monkeyIndex.to!int].ifFalse].items ~= item;
            }
            monkeyData[monkeyIndex.to!int].items = [];
        }
    }
    int[] counts;
    foreach(monkey; monkeyData)
        counts ~= monkey.inspections;

    counts.sort();

    return counts[$-1] * counts[$-2];
}


unittest {
    string data = "Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1";

    Monkey[] monkeyData;
    foreach(monkeyNum, monkey; data.split("\n\n").enumerate())
        monkeyData ~= parseMonkey(monkey);

    assert (partOne(monkeyData) == (101 * 105));
}


int partOne(Monkey[] monkeyData)
{
    foreach (c; iota(20)) {
        foreach(monkeyIndex; 0..monkeyData.length) {
            foreach (item; monkeyData[monkeyIndex.to!int].items) {
                monkeyData[monkeyIndex.to!int].inspections++;

                item = runOperation(item, monkeyData[monkeyIndex.to!int].operation) / 3;
                if (item % monkeyData[monkeyIndex.to!int].test == 0)
                    monkeyData[monkeyData[monkeyIndex.to!int].ifTrue].items ~= item;
                else
                    monkeyData[monkeyData[monkeyIndex.to!int].ifFalse].items ~= item;
            }
            monkeyData[monkeyIndex.to!int].items = [];
        }
    }
    int[] counts;
    foreach(monkey; monkeyData)
        counts ~= monkey.inspections;

    counts.sort();

    return counts[$-1] * counts[$-2];
}


void main(string[] args)
{
    string data = readText("../inputs/input11.txt").strip();
    Monkey[] monkeyData;
    foreach(monkeyNum, monkey; data.split("\n\n").enumerate())
        monkeyData ~= parseMonkey(monkey);

    writeln("Part 1: ", partOne(monkeyData));

    monkeyData = [];
    foreach(monkeyNum, monkey; data.split("\n\n").enumerate())
        monkeyData ~= parseMonkey(monkey);

    writeln("Part 2: ", partTwo(monkeyData));
}

module utils;

import std.stdio;
import std.file;
import std.conv;
import std.array;
import std.algorithm;


string getData(string day)
{
    string input_dir = "../inputs";
    return readText(input_dir ~ "/" ~ "input" ~ day ~ ".txt").to!string;
}


string[] getLineData(string day)
{
    auto data = getData(day).split("\n");
    return filter!(a => a != "")(data).array;
}


int[] getIntData(string day)
{
    auto inData = getLineData(day);

    int[] outData;
    foreach(record; inData)
        outData ~= to!int(record);

    return outData;
}

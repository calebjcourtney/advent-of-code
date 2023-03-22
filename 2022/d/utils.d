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

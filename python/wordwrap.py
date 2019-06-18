def wrap(line, cols):
    if len(line) <= cols:
        return line
    first, remainder = get_break_point(line, cols)
    return first + "\n" + wrap(remainder, cols)

def get_break_point(line, cols):
    try:
        break_pt = line.rindex(" ", 0, cols + 1)
        return line[:break_pt], line[break_pt+1:]
    except ValueError:
        return line[:cols], line[cols:]
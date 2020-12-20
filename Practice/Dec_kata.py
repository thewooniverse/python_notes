

# simple pig latin - 5
# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

# my solution
def pig_it(text):
    split_ls = text.split(" ")
    new_ls = []

    for txt in split_ls:

        if txt.isalpha():
            new_text = txt[1:] + txt[0] + "ay"
            new_ls.append(new_text)

        else:
            new_ls.append(txt)

    return " ".join(e for e in new_ls)


# other's solution
import re


def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)
    # I really should learn re


# snail sort - 4
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/solutions/python/all/newest
# I'm actually pretty happy with the way this function works;


def snail(snail_map):
    if len(snail_map) < 2:  # for single line depth arrays
        return snail_map[0]

    def add_point(point):  # adds current point value and point to visited;

        result.append(snail_map[point[0]][point[1]])
        visited_points.append(point)

    visited_points = []
    result = []
    current_direction = 0
    current_point = [0, 0]  # point in terms of [depth, length]
    add_point(current_point)
    print(result)
    print(visited_points)

    def get_next_point(point, direction):
        if direction % 4 == 0:  # dir = right
            print("trying right")
            return [point[0], point[1] + 1]

        if direction % 4 == 1:  # dir = down
            print("trying down")
            return [point[0] + 1, point[1]]

        if direction % 4 == 2:  # dir = left
            print("trying left")
            if point[1] == 0:
                return point

            else:
                return [point[0], point[1] - 1]

        if direction % 4 == 3:  # dir = up
            print("trying up")
            if point[0] == 0:
                return point
            else:
                return [point[0] - 1, point[1]]

    while len(result) < (len(snail_map) ** 2):

        next_point = get_next_point(current_point, current_direction)

        if next_point == current_point:
            current_direction += 1

        elif next_point not in visited_points:
            try:

                # if successful, that is it, return with new current_point.
                add_point(next_point)
                print("added {0}".format(next_point))
                current_point = next_point

            except IndexError:  # likely index error, meaning we reached the end, so turn.
                current_direction += 1

        else:  # if the next_point is in visited points, loop will try again with current point, new dir.
            current_direction += 1

    return result


# Scrambiles - 5
# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/solutions/python

def scramble(s1, s2):
    char_count = {}
    for c in set(list(s2)):
        char_count[c] = s2.count(c)

    for char, count in char_count.items():
        if count > s1.count(char):
            return False

    return True

# simpler solution


def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

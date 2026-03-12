#!/usr/bin/env python3

import math


def distance_calculation(
        position: tuple[int, int, int], position_two: tuple[int, int, int]
   ) -> float:
    i: int = 0
    distance: int = 0
    while i < 3:
        distance += (position_two[i] - position[i])**2
        i += 1
    distance = float(math.sqrt(distance))
    return distance


def do_parsing(arr: str) -> tuple[int, int, int] | None:
    try:
        parsing_pos: list = arr.split(",")
        i: int = 0
        while i < 3:
            parsing_pos[i] = int(parsing_pos[i])
            i += 1
        parsing_pos: tuple[int, int, int] = tuple(parsing_pos)
        return parsing_pos
    except Exception as e:
        print(f"Error parsing coordinates:  {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    position: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {position}")
    position_two: tuple[int, int, int] = (0, 0, 0)
    x: float = distance_calculation(position, position_two)
    print(
            f"Distance between {position_two} and {position}: "
            f"{x: .2f}"
            )
    print()
    parsing: str = "3,4,0"
    print(f"Parsing coordinates: \"{parsing}\"")
    parsing_pos: tuple[int, int, int] = do_parsing(parsing)
    print(f"Parsing coordinates: {parsing_pos}")
    print(
            f"Distance between {position_two} and {parsing_pos}: "
            f"{distance_calculation(parsing_pos, position_two)}"
            )
    print()
    invalid_parse: str = "abc,def,ghi"
    print(f"Parsing invalid coordinates: {invalid_parse}")
    do_parsing(invalid_parse)
    print()
    print("Unpacking demonstration:")
    x, y, z = parsing_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates:  X={x}, Y={y}, Z={z}")

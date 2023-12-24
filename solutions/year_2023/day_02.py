import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def get_integer(regex, text):
    matches = re.findall(regex, text)
    if len(matches) > 0:
        return int(matches[0])
    return 0


@register_solution(2023, 2, 1)
def part_one(input_data: list[str]):
    answer = 0
    limit = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for line in input_data:
        [(game_number_str, game_draws_str)] = re.findall(r"^Game (\d+): (.*)$", line)

        draws = game_draws_str.split("; ")
        valid = True
        for draw in draws:
            red = get_integer(r"(\d+) red.*", draw)
            green = get_integer(r"(\d+) green.*", draw)
            blue = get_integer(r"(\d+) blue.*", draw)
            if red > limit["red"] or green > limit["green"] or blue > limit["blue"]:
                valid = False
                break

        if valid:
            game_number = int(game_number_str)
            answer += game_number

    if not answer:
        raise SolutionNotFoundError(2023, 2, 1)

    return answer


@register_solution(2023, 2, 2)
def part_two(input_data: list[str]):
    answer = 0

    for line in input_data:
        [(game_number_str, game_draws_str)] = re.findall(r"^Game (\d+): (.*)$", line)

        draws = game_draws_str.split("; ")
        red, green, blue = 0, 0, 0
        for draw in draws:
            red = max(red, get_integer(r"(\d+) red.*", draw))
            green = max(green, get_integer(r"(\d+) green.*", draw))
            blue = max(blue, get_integer(r"(\d+) blue.*", draw))

        answer += red * green * blue

    if not answer:
        raise SolutionNotFoundError(2023, 2, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 2)
    part_one(data)
    part_two(data)

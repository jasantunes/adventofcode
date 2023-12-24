import regex as re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def get_first_and_last_digits_as_number(line):
    digits_str = re.findall(r"\d", line)
    number_str = digits_str[0] + digits_str[-1]
    return int(number_str)


def get_first_and_last_digits_or_spelled_digits_as_number(line):
    digits_str = re.findall(
        r"(\d|zero|one|two|three|four|five|six|seven|eight|nine)",
        line,
        flags=re.IGNORECASE,
        overlapped=True,
    )

    for i in [0, len(digits_str) - 1]:
        m = digits_str[i]
        match m:
            case "zero":
                digits_str[i] = "0"
            case "one":
                digits_str[i] = "1"
            case "two":
                digits_str[i] = "2"
            case "three":
                digits_str[i] = "3"
            case "four":
                digits_str[i] = "4"
            case "five":
                digits_str[i] = "5"
            case "six":
                digits_str[i] = "6"
            case "seven":
                digits_str[i] = "7"
            case "eight":
                digits_str[i] = "8"
            case "nine":
                digits_str[i] = "9"

    number_str = digits_str[0] + digits_str[-1]
    return int(number_str)


@register_solution(2023, 1, 1)
def part_one(input_data: list[str]):
    answer = 0
    for line in input_data:
        number = get_first_and_last_digits_as_number(line)
        answer += number

    if not answer:
        raise SolutionNotFoundError(2023, 1, 1)

    return answer


@register_solution(2023, 1, 2)
def part_two(input_data: list[str]):
    answer = 0
    for line in input_data:
        number = get_first_and_last_digits_or_spelled_digits_as_number(line)
        answer += number

    if not answer:
        raise SolutionNotFoundError(2023, 1, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 1)
    part_one(data)
    part_two(data)

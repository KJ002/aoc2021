from typing import Iterator

def get_input_data(file: str = "data.txt") -> str:
    with open(file) as f:
        return f.read()

def parse_input_data(data: list[str]) -> list[int]:
    return [
        int(depth) for depth in data.split("\n")
        if all(char.isdigit() for char in depth) and len(depth)
    ]

def get_depth_pairs(data: list[int]) -> Iterator[tuple[int, int]]:
    for i in range(len(data)-1):
        yield (data[i], data[i+1])

def main() -> None:
    print(
        sum(
            1 for pair in get_depth_pairs(parse_input_data(get_input_data()))
            if pair[0] < pair[1]
        )
    )

if __name__ == '__main__':
    main()

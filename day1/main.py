def get_input_data(file: str = "data.txt") -> str:
    with open(file) as f:
        return f.read()

def parse_input_data(data: list[str]) -> list[int]:
    return [int(i) for i in data.split("\n") if all(char.isdigit() for char in i) and len(i)]

if __name__ == '__main__':
    print(parse_input_data(get_input_data()))

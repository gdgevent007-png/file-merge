# main.py
def read_file_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        # splitlines() handles different line endings and won't leave a trailing empty
        return f.read().splitlines()

def main():
    a = read_file_lines("part1.txt")
    b = read_file_lines("part2.txt")
    merged = a + b
    # count non-empty lines properly (strip whitespace)
    non_empty = [line for line in merged if line.strip() != ""]
    print(f"Merged {len(non_empty)} non-empty lines.")

if __name__ == "__main__":
    main()

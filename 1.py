import pandas as pd


def search_file(file_path, start_line, end_line, search_text):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return

    start_line = max(0, start_line - 1)  # Correct for 0-indexing
    end_line = min(end_line, len(lines))  # Don't exceed number of lines in file

    matched_lines = [(idx + 1, line.strip()) for idx, line in enumerate(lines) if
                     search_text in line and start_line <= idx < end_line]

    with open('results.txt', 'w') as file:
        for line_num, content in matched_lines:
            file.write(f"{line_num}: {content}\n")

    print("Results saved to results.txt in the current directory.")


if __name__ == "__main__":
    input_data = input("PATH START END TEXT: ").split(' ')
    if len(input_data) != 4:
        print("Invalid input. Please enter 4 arguments: path, start line, end line, and text to be matched.")
    else:
        path, start, end, text = input_data[0], int(input_data[1]), int(input_data[2]), input_data[3]
        search_file(path, start, end, text)

# Author: Maria Varzari

# Import csv module
import csv

# Valid range for an exam mark
MIN_MARK = 0
MAX_MARK = 200


def read_student_marks(file_name):
    """
    Read pupil names and marks from a CSV file into two parallel 1-D arrays.
    :param file_name: file to open
    :return: (names, marks) - parallel lists of pupil names and their marks
    """
    names = []
    marks = []
    # Open the CSV file and iterate through its rows
    with open(file_name) as file:
        reader = csv.reader(file)
        for row_number, row in enumerate(reader, start=1):
            try:
                name = row[0] + " " + row[1]
                mark = int(row[2])
            except (IndexError, ValueError):
                print(f"Warning: Skipping malformed row {row_number}: {row}")
                continue
            names.append(name)
            marks.append(mark)
    return names, marks


def find_top_pupil(names, marks):
    """
    Find the pupil(s) with the highest valid mark.
    :param names: 1-D array of pupil names
    :param marks: 1-D array of pupil marks, parallel to names
    :return: (top_pupils, top_mark) - names sharing the top mark, and that mark
    """
    top_mark = 0
    top_pupils = []

    for name, mark in zip(names, marks):
        if MIN_MARK <= mark <= MAX_MARK:
            # Update the top mark and top pupils if a higher mark is found
            if mark > top_mark:
                top_mark = mark
                top_pupils = [name]
            elif mark == top_mark:
                # Add pupil to list if they have the same top mark
                top_pupils.append(name)
        else:
            print(f"Warning: Invalid mark ({mark}) found for {name}. Mark should be in the range of {MIN_MARK} to {MAX_MARK}.")

    return top_pupils, top_mark


def save_top_pupils(file_name, top_pupils, top_mark):
    """
    Save the top pupil(s) and their mark to a CSV file.
    :param file_name: file to write
    :param top_pupils: list of pupil names with the top mark
    :param top_mark: the top mark achieved
    """
    with open(file_name, 'w', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(['Name', 'Mark'])
        for pupil in top_pupils:
            writer.writerow([pupil, top_mark])


if __name__ == "__main__":
    input_file_name = 'FileForStudents.csv'
    output_file_name = 'topStudent.csv'

    try:
        # Read student data from the input file
        student_names, student_marks = read_student_marks(input_file_name)
    except FileNotFoundError:
        print(f"Error: Could not find input file '{input_file_name}'.")
    else:
        # Find the top pupil(s) and the highest mark
        top_pupils, top_mark = find_top_pupil(student_names, student_marks)

        print("The pupil(s) with the highest mark is/are:")
        for pupil in top_pupils:
            print("Name:", pupil, ", Mark:", top_mark)

        # Save the top pupil(s) and their mark to the output file
        save_top_pupils(output_file_name, top_pupils, top_mark)

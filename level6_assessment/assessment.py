# Author: Maria Varzari

# Import csv module
import csv


# Function to read student marks from a CSV file
def readStudentMarks(fileName):
    students = []
    # Open the CSV file and iterate through its rows
    with open(fileName) as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0] + " " + row[1]
            mark = int(row[2])
            students.append((name, mark))
    return students


# Function to find the pupil(s) with the highest mark
def findTopPupil(students):
    topMark = 0
    topPupils = []

    for name, mark in students:
        if 0 <= mark <= 200:
            # Update the top mark and top pupils if a higher mark is found
            if mark > topMark:
                topMark = mark
                topPupils = [name]
            elif mark == topMark:
                # Add pupil to list if they have the same top mark
                topPupils.append(name)
        else:
            print(f"Warning: Invalid mark ({mark}) found for {name}. Mark should be in the range of 0 to 200.")

    return topPupils, topMark


# Function to save top pupils to a new CSV file
def saveTopPupils(fileName, topPupils, topMark):
    with open(fileName, 'w', newline='') as myNewFile:
        writer = csv.writer(myNewFile)
        writer.writerow(['Name', 'Mark'])
        for pupil in topPupils:
            writer.writerow([pupil, topMark])


inputFileName = 'FileForStudents.csv'
outputFileName = 'topStudent.csv'

# Read student data from the input file
students = readStudentMarks(inputFileName)
# Find the top pupil(s) and the highest mark
topPupils, topMark = findTopPupil(students)

print("The pupil(s) with the highest mark is/are:")
for pupil in topPupils:
    print("Name:", pupil, ", Mark:", topMark)

# Save the top pupil(s) and their mark to the output file
saveTopPupils(outputFileName, topPupils, topMark)



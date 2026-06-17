# Assessment Level 6 Python

## Top Pupil Mark Finder

Programming task for Outcome 2 of Software Design & Development (J27C76): read pupil
names and exam marks (0-200) from a CSV file, find the pupil(s) with the top mark,
display the result, and save it to a new CSV file.

### Project structure

- `level6_assessment/assessment.py` - the program
- `level6_assessment/FileForStudents.csv` - sample input data (50 pupils)
- `level6_assessment/topStudent.csv` - sample output produced by the program
- `docs/` - design and testing evidence (data-flow diagram, pseudocode, test plan, test log)

### Running it

```
cd level6_assessment
python assessment.py
```

Reads `FileForStudents.csv` from the current directory and writes the top pupil(s)
and their mark to `topStudent.csv`.

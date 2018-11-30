FILENAME = 'parts/computer-science/computer-networks.tex'

BEGIN_SUBSECTION = '\\subsection'
BEGIN_SUBSECTION_OF_INTEREST = '\\subsection{Solved course exercises}'
BEGIN_EXERCISE = '\\begin{Exercise}'
END_EXERCISE = '\\end{Exercise}'
BEGIN_ANSWER = '\\begin{Answer}'

with open(FILENAME) as file_handler:
    capturing = False
    exercises = []
    found_answer = False
    answered = []
    for line in file_handler:
        line = line.strip()
        if line == BEGIN_SUBSECTION_OF_INTEREST:
            capturing = True
            continue
        if capturing:
            if line.startswith(BEGIN_SUBSECTION):
                capturing = False
            elif line == BEGIN_EXERCISE:
                if len(answered) < len(exercises):
                    answered.append(found_answer)
                exercises.append(line)
                found_answer = False
            elif line == BEGIN_ANSWER:
                found_answer = True
    answer_count = answered.count(True)
    exercise_count = len(exercises)
    print('Found {} exercises. {} are answered.'.format(exercise_count, answer_count))
    print('Completion is {:.1f}%.'.format(100.0 * answer_count / exercise_count))

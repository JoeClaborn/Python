quizzes = 0
labs = 0
midterm = 0
final = 0
total_points = 0

# Get quiz grades here
for i in range(1, 11) :
    i = float(input(f"Please enter your points for quiz {i} (type -1 to skip): "))
    quizzes += i
    total_points += 1
    if (i == -1) :
        i -= -1
        total_points += 0
        break;
# Get lab grades here
for j in range(1, 11) :
    j = float(input(f"Please enter your points for lab {j} (type -1 to skip): "))
    labs += j
    total_points += 3
    if (j == -1) :
        j -= -1
        total_points += 0
        break;
# Get midterm grade here
for g in range(1) :
    midterm = float(input("Please enter your points for the midterm (type -1 to skip): "))
    total_points += 25
    if (g == -1) :
        g -= -1
        total_points += 0
        break;
# Get final grades here
for h in range(1) :
    final = float(input("Please enter your points for the final (type -1 to skip): "))
    total_points += 35
    if (h == -1) :
        h -= -1
        total_points += 0
        break;

total = quizzes + labs + midterm + final

print(f"Current grade: {100 * total / total_points:.2f} = {total} / {total_points}");
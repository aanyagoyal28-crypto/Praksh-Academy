#  # Question 3: Weekly Expense Analyzer

#     ## Problem Statement

#     - Accept expenses for 5 days using a `for` loop.
# - Print total, average and highest expense.

#     ### Sample Input

#     ```text
#     100
# 200
# 150
# 300
# 250
#     ```

#     ### Sample Output

#     ```text
#     Total = 1000
# Average = 200.0
# Highest = 300
#     ```
total = 0#assignment opertor
higher=0
for day in range(1,6):#for loop with range
    expense = int(input(f"Enter your day {day} expense = "))#print statmetn with formatting variable
    total+=expense#addition assignment operator
    if day == 1 or expense>higher: # conditional operator,if and comparison
        higher=expense#assignemnt variable
print(f"Total = {total}")
print(f"Average = {total/5}")
print(f"Higher = {higher}")

'''
expense = [1,4,9,3,6,8]

higher = 1
if expense>higher:(4>1),(4>4),(9>4),(3>9),(6>9),(8>9)
    higher = expense#4,4,9,9,9,9


'''
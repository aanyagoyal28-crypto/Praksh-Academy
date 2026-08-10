age = [34,12,56,12,45,78,12,9,7,5]

def age_checker(age):
    if age<18:
        return False
    else:
        return True
    
voter_list = filter(age_checker,age)

print(voter_list)

for people in voter_list:
    print(people)
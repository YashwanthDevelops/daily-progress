courses = ["DBMS", "CA", "MATHS", "FDS"]
courses.append("English")
print(courses)

courses2 = ["Art", "education"]
courses2.insert(0,"Arrear")
print(courses2)

# courses.append(courses2)
# print(courses)

courses.extend(courses2)
print(courses)

popped = courses.pop()
print(popped)

courses.reverse()
print(courses)

sortcourses = sorted(courses)
print(sortcourses)

nums = [1,2,3,4,5,6]
nums.sort(reverse = True)
print(nums)

print(min(nums))
print(max(nums))


for item in courses:
    print(item)

for index,course in enumerate(courses, start = 1):
    print(f"{index} is the index,{course} is the course")

course_str = ', '.join(courses)
print(course_str)

newlist = course_str.split(', ')
print(newlist)

empty_set = []
empty_set = set()
# 1:30:00 timestamp
# tuple =   collection which is ordered and unchangable used to group together related data

student = ("Marot", 21, "Female")
print(student.count("Marot"))
print(student.index("Female"))

for x in student:
    print(x)

if "Female" in student:
    print("Yo I'm female!")
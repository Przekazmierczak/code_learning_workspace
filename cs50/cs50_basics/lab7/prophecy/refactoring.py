from cs50 import SQL

db_old = SQL("sqlite:///roster.db")
db_new = SQL("sqlite:///roster_refactored.db")

# students = db_old.execute("SELECT student_name FROM students;")

# for student in students:
#     db_new.execute("INSERT INTO students(student_name) VALUES (?)", student["student_name"])

# print(db_new.execute('SELECT * FROM students;'))

# # db_new.execute("INSERT INTO houses(house, head) VALUES ('Gryffindor', 'Minerva McGonagall')")
# # db_new.execute("INSERT INTO houses(house, head) VALUES ('Slytherin', 'Severus Snape')")
# # db_new.execute("INSERT INTO houses(house, head) VALUES ('Ravenclaw', 'Filius Flitwick')")
# # db_new.execute("INSERT INTO houses(house, head) VALUES ('Hufflepuff', 'Pomona Sprout')")

# print(db_new.execute('SELECT * FROM houses;'))

# students_houses = db_old.execute("SELECT id, house FROM students;")

# for student_house in students_houses:
#     if student_house["house"] == "Gryffindor":
#         db_new.execute("INSERT INTO houses_assignments(student_id, house_id) VALUES (?, 1)", student_house["id"])
#     elif student_house["house"] == "Slytherin":
#         db_new.execute("INSERT INTO houses_assignments(student_id, house_id) VALUES (?, 2)", student_house["id"])
#     elif student_house["house"] == "Ravenclaw":
#         db_new.execute("INSERT INTO houses_assignments(student_id, house_id) VALUES (?, 3)", student_house["id"])
#     elif student_house["house"] == "Hufflepuff":
#         db_new.execute("INSERT INTO houses_assignments(student_id, house_id) VALUES (?, 4)", student_house["id"])

# print(db_new.execute('SELECT * FROM houses_assignments;'))
CREATE TABLE students (
    id INTEGER,
    student_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    id INTEGER,
    house TEXT,
    head TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses_assignments (
    student_id INTEGER,
    house_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(house_id) REFERENCES houses(id)
);

-- SELECT
-- 	student_name,
-- 	houses.house,
-- 	houses.head
-- FROM
-- 	students
-- 	INNER JOIN houses_assignments ON houses_assignments.student_id = students.id
-- 	INNER JOIN houses ON houses_assignments.house_id = houses.id;
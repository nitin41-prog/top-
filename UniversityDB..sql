CREATE DATABASE UniversityDB;
USE UniversityDB;

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    DepartmentName VARCHAR(100) NOT NULL
);

CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,
    CourseName VARCHAR(100) NOT NULL,
    StudentID INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
INSERT INTO Departments (DepartmentName) VALUES
('Computer Science'),
('Mechanical Engineering'),
('Electrical Engineering');

INSERT INTO Students (Name, Age, DepartmentID) VALUES
('Alice Johnson', 21, 1),
('Bob Smith', 22, 2),
('Charlie Brown', 20, 1),
('David White', 23, 3),
('Emma Watson', 21, 2);

INSERT INTO Courses (CourseName, StudentID) VALUES
('Database Management', 1),
('Operating Systems', 1),
('Thermodynamics', 2),
('Digital Circuits', 3),
('Artificial Intelligence', 1),
('Heat Transfer', 2),
('Power Systems', 4),
('Data Structures', 3),
('Fluid Mechanics', 5),
('Machine Learning', 1);

SELECT Students.StudentID, Students.Name, Students.Age, Departments.DepartmentName 
FROM Students 
JOIN Departments ON Students.DepartmentID = Departments.DepartmentID;
SELECT Students.Name 
FROM Students 
JOIN Courses ON Students.StudentID = Courses.StudentID 
WHERE Courses.CourseName = 'Artificial Intelligence';
SELECT Departments.DepartmentName, COUNT(Students.StudentID) AS StudentCount 
FROM Departments 
LEFT JOIN Students ON Departments.DepartmentID = Students.DepartmentID 
GROUP BY Departments.DepartmentName;
SELECT Courses.CourseName 
FROM Courses 
JOIN Students ON Courses.StudentID = Students.StudentID 
WHERE Students.Name = 'Alice Johnson';
SELECT Students.Name, COUNT(Courses.CourseID) AS CourseCount 
FROM Students 
JOIN Courses ON Students.StudentID = Courses.StudentID 
GROUP BY Students.StudentID 
HAVING CourseCount> 1;
SELECT Departments.DepartmentName, AVG(Students.Age) AS AvgAge 
FROM Departments 
JOIN Students ON Departments.DepartmentID = Students.DepartmentID 
GROUP BY Departments.DepartmentName;
SELECT Departments.DepartmentName 
FROM Departments 
JOIN Students ON Departments.DepartmentID = Students.DepartmentID 
GROUP BY Departments.DepartmentName 
ORDER BY COUNT(Students.StudentID) DESC 
LIMIT 1;
SELECT Students.Name 
FROM Students 
LEFT JOIN Courses ON Students.StudentID = Courses.StudentID 
WHERE Courses.StudentID IS NULL;
SELECT Students.Name, COUNT(Courses.CourseID) AS TotalCourses 
FROM Students 
LEFT JOIN Courses ON Students.StudentID = Courses.StudentID 
GROUP BY Students.StudentID;
SELECT Students.Name 
FROM Students 
JOIN Departments ON Students.DepartmentID = Departments.DepartmentID 
JOIN Courses ON Students.StudentID = Courses.StudentID 
WHERE Departments.DepartmentName = 'Computer Science' 
AND Courses.CourseName LIKE '%Data%';
SELECT Students.StudentID, Students.Name, Students.Age, Departments.DepartmentName 
FROM Students 
JOIN Departments ON Students.DepartmentID = Departments.DepartmentID;
SELECT Students.Name 
FROM Students 
JOIN Courses ON Students.StudentID = Courses.StudentID 
WHERE Courses.CourseName = 'Artificial Intelligence';
SELECT Departments.DepartmentName, COUNT(Students.StudentID) AS StudentCount 
FROM Departments 
LEFT JOIN Students ON Departments.DepartmentID = Students.DepartmentID 
GROUP BY Departments.DepartmentName;
SELECT Courses.CourseName 
FROM Courses 
JOIN Students ON Courses.StudentID = Students.StudentID 
WHERE Students.Name = 'Alice Johnson';
SELECT Students.Name, COUNT(Courses.CourseID) AS CourseCount 
FROM Students 
JOIN Courses ON Students.StudentID = Courses.StudentID 
GROUP BY Students.StudentID 
HAVING CourseCount> 1;
SELECT Departments.DepartmentName, AVG(Students.Age) AS AvgAge 
FROM Departments 
JOIN Students ON Departments.DepartmentID = Students.DepartmentID 
GROUP BY Departments.DepartmentName;
SELECT Departments.DepartmentName 
FROM Departments 
JOIN Students ON Departments.DepartmentID = Students.DepartmentID 
GROUP BY Departments.DepartmentName 
ORDER BY COUNT(Students.StudentID) DESC 
LIMIT 1;
SELECT Students.Name 
FROM Students 
LEFT JOIN Courses ON Students.StudentID = Courses.StudentID 
WHERE Courses.StudentID IS NULL;
SELECT Students.Name, COUNT(Courses.CourseID) AS TotalCourses 
FROM Students 
LEFT JOIN Courses ON Students.StudentID = Courses.StudentID 
GROUP BY Students.StudentID;
SELECT Students.Name 
FROM Students 
JOIN Departments ON Students.DepartmentID = Departments.DepartmentID 
JOIN Courses ON Students.StudentID = Courses.StudentID 
WHERE Departments.DepartmentName = 'Computer Science' 
AND Courses.CourseName LIKE '%Data%';

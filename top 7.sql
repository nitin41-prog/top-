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
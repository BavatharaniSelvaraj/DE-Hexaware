-- 1. Database Creation
CREATE DATABASE IF NOT EXISTS CompanyDB;
USE CompanyDB;

-- 2. Table Creation and Data Insertion
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;

CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Age INT,
    Salary DECIMAL(10, 2),
    DeptID INT,
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
);

-- 3. Insert Data
INSERT INTO Departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Sales');

INSERT INTO Employees VALUES
(101, 'Alice', 30, 60000.00, 1),
(102, 'Bob', 28, 75000.00, 2),
(103, 'Charlie', 25, 50000.00, 2),
(104, 'Diana', 35, 82000.00, 3),
(105, 'Eva', 29, 45000.00, NULL);

-- 4. Update Data
UPDATE Employees SET Salary = 65000.00 WHERE EmpID = 101;

-- 5. Delete Data
DELETE FROM Employees WHERE EmpID = 105;

-- 6. Retrieve Specific Attributes
SELECT EmpName, Salary FROM Employees;

-- 7. Retrieve Selected Rows
SELECT * FROM Employees WHERE Age > 30;

-- 8. Filtering Data: WHERE
SELECT * FROM Employees WHERE DeptID = 2;

-- 9. Filtering: IN, DISTINCT, AND, OR, BETWEEN, LIKE
SELECT * FROM Employees WHERE DeptID IN (1, 3);
SELECT DISTINCT DeptID FROM Employees;
SELECT * FROM Employees WHERE Age > 25 AND Salary < 70000;
SELECT * FROM Employees WHERE Age < 30 OR DeptID = 1;
SELECT * FROM Employees WHERE Age BETWEEN 25 AND 30;
SELECT * FROM Employees WHERE EmpName LIKE 'A%';

-- 10. Aliases
SELECT EmpName AS Name, Salary AS MonthlySalary FROM Employees;
SELECT e.EmpName, d.DeptName
FROM Employees e
JOIN Departments d ON e.DeptID = d.DeptID;

-- 11. String Functions
SELECT UPPER(EmpName) AS UpperName, LENGTH(EmpName) AS NameLength FROM Employees;

-- 12. Mathematical Functions
SELECT EmpName, ROUND(Salary * 1.1, 2) AS IncrementedSalary FROM Employees;

-- 13. Aggregate Functions
SELECT COUNT(*) AS TotalEmployees FROM Employees;
SELECT AVG(Salary) AS AvgSalary FROM Employees;
SELECT MAX(Salary) AS MaxSalary FROM Employees;
SELECT MIN(Salary) AS MinSalary FROM Employees;

-- 14. INNER JOIN
SELECT e.EmpName, d.DeptName
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID;

-- 15. LEFT JOIN
SELECT e.EmpName, d.DeptName
FROM Employees e
LEFT JOIN Departments d ON e.DeptID = d.DeptID;

-- 16. RIGHT JOIN
SELECT e.EmpName, d.DeptName
FROM Employees e
RIGHT JOIN Departments d ON e.DeptID = d.DeptID;

-- 17. FULL OUTER JOIN (Simulated)
SELECT e.EmpName, d.DeptName
FROM Employees e
LEFT JOIN Departments d ON e.DeptID = d.DeptID
UNION
SELECT e.EmpName, d.DeptName
FROM Employees e
RIGHT JOIN Departments d ON e.DeptID = d.DeptID;

-- 18. CROSS JOIN
SELECT e.EmpName, d.DeptName
FROM Employees e
CROSS JOIN Departments d;

-- 19. JOIN + GROUP BY + Aggregate
SELECT d.DeptName, COUNT(e.EmpID) AS EmpCount, AVG(e.Salary) AS AvgSal
FROM Employees e
JOIN Departments d ON e.DeptID = d.DeptID
GROUP BY d.DeptName;

-- 20. Equi Join
SELECT * FROM Employees e, Departments d
WHERE e.DeptID = d.DeptID;

-- 21. Self Join
SELECT e1.EmpName AS Employee1, e2.EmpName AS Employee2
FROM Employees e1
JOIN Employees e2 ON e1.DeptID = e2.DeptID AND e1.EmpID <> e2.EmpID;

-- 22. JOIN + GROUP BY + HAVING
SELECT d.DeptName, COUNT(e.EmpID) AS EmpCount
FROM Employees e
JOIN Departments d ON e.DeptID = d.DeptID
GROUP BY d.DeptName
HAVING COUNT(e.EmpID) >= 2;

-- 23. GROUPING SETS Simulation with UNION
SELECT DeptID, NULL AS
 AgeGroup, COUNT(*) AS Total
FROM Employees
GROUP BY DeptID
UNION
SELECT NULL, Age, COUNT(*)
FROM Employees
GROUP BY Age;
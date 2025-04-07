-- 01. Querying data
SELECT 
  LastName
FROM
  employees;

SELECT LastName, FirstName
FROM employees;

SELECT * FROM employees;

SELECT FirstName AS '이름'
FROM employees;

SELECT
  Name,
  Milliseconds / 60000 AS "재생 시간(분)"
FROM
  tracks;


-- 02. Sorting data
SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName;

SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

SELECT 
  Country, City
FROM 
  customers
ORDER BY 
  Country DESC, 
  City;

SELECT
  Name,
  Milliseconds / 60000 AS "재생시간(분)"
FROM
  tracks
ORDER BY
  "Milliseconds" DESC;

-- NULL 정렬 예시
SELECT 
  postalCode
FROM
  customers
ORDER BY
  postalCode DESC;


-- 03. Filtering data
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

SELECT 
  LastName, 
  FirstName,
  City
FROM 
  customers
WHERE 
  City = "Prague";

-- 04. Grouping data
SELECT 
  Country
FROM
  customers
GROUP BY
  Country;

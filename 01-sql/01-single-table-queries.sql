-- 01. Querying data
SELECT 
  LastName
FROM
  employees;

-- 02. Sorting data
SELECT 
  FirstName
FROM
  employees;

-- NULL 정렬 예시
SELECT 
  postalCode
FROM
  customers
ORDER BY
  postalCode;

-- 03. Filtering data
SELECT
  Country
FROM
  customers
ORDER BY
  Country;

-- 04. Grouping data
SELECT
  Country
FROM
  customers
GROUP BY
  Country;

### Forign Keys

What is a friegn key - Helps us to join two tables using their primary key.

- repeatition is allowed.
- can be null

![alt text](image.png)
![alt text](image-1.png)

Select Movies.\*, Boxoffice.movie_id

## Exercise 6 — Tasks

1. Find the domestic and international sales for each movie
2.
3. Show the sales numbers for each movie that did better internationally rather than domestically
   ```sql
   SELECT *
   FROM movies JOIN boxoffice
       ON movies.id = boxoffice.movie_id
   WHERE international_sales > domestic_sales;
   ```
4. List all the movies by their ratings in descending order
   ```sql
   select movies.title, boxoffice.rating from movies inner join boxoffice on movies.id = boxoffice.movie_id order by rating desc
   ```

Exercise 7 — Tasks

1. Find the list of all buildings that have employees
   ```sql
   select Distinct building from  Employees
   ```

````
2. Find the list of all buildings and their capacity
```sql
Select * from buildings;
````

3. List all buildings and the distinct employee roles in each building (including empty buildings)
   ```sql
   select distinct building_name, role
   from buildings
   left join employees
       on buildings.building_name = employees.building;
   ```

Exercise 8 — Tasks

1. Find the name and role of all employees who have not been assigned to a building
   ```sql
    select name, role from employees where building is null
   ```
2. Find the names of the buildings that hold no employees
   ```sql
   select building_name from buildings left join employees on building_name = building where name is null
   ```
   Exercise 9 — Tasks
3. List all movies and their combined sales in millions of dollars
   ```sql
    select title, (domestic_sales + international_sales) / 1000000 as millions
    from movies
    join boxofficeon movies.id = boxoffice.movie_id;
   ```
4. List all movies and their ratings in percent
   ```sql
    select title, (rating*10) as percent  from movies join boxoffice where id = movie_id
   ```
5. List all movies that were released on even number years
   ```sql
    SELECT title, year
    FROM movies
    WHERE year % 2 = 0;
   ```

Exercise 10 — Tasks

1. Find the longest time that an employee has been at the studio
   ```sql
    select name, max(years_employed) from employees
   ```
2. For each role, find the average number of years employed by employees in that role
   ```sql
    select role, avg(years_employed) from employees group by role
   ```
3. Find the total number of employee years worked in each building
   ```sql
    select building, sum(years_employed) from employees group by building
   ```

Exercise 11 — Tasks

1. Find the number of Artists in the studio (without a HAVING clause)
   ```sql
    select count(role) from employees where role = 'Artist'
   ```
2. Find the number of Employees of each role in the studio
   ```sql
    select role, count(role) from employees group by rol
   ```
3. Find the total number of years employed by all Engineers
   ```sql
    select sum(years_employed) from employees where role = 'Engineer'
   ```
   Exercise 12 — Tasks
4. Find the number of movies each director has directed

5. Find the total domestic and international sales that can be attributed to each director

## SQL Lesson 12: Order of execution of a Query

![alt text](image-2.png)
Exercise 12 — Tasks

1. Find the number of movies each director has directed
   ```sql
    select director, count(director) from movies group by director
   ```
2. Find the total domestic and international sales that can be attributed to each director
   ```sql
    select director, sum(domestic_sales)+sum(international_sales) as total_amount from movies inner join boxoffice on id=movie_id group by director
   ```

### SQL Lesson 13: Inserting rows

![alt text](image-3.png)

Exercise 13 — Tasks

1. Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)

   ```sql
    INSERT INTO movies VALUES (4, "Toy Story 4", "LVO", 2025, 95);
   ```

2. Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.
   ```sql
   INSERT INTO boxoffice VALUES (4, 8.7, 340000000, 270000000);
   ```

Exercise 14 — Tasks

1. The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
   ```sql
    update movies
    set director = 'John Lasseter'
    where id = 2
   ```
2. The year that Toy Story 2 was released is incorrect, it was actually released in 1999
   ```sql
   update movies
   set director = 'John Lasseter'
   where id = 2
   ```
3. Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich
   Stuck?
   ```sql
    update movies
    set Title = 'Toy Story 3', director = 'Lee Unkrich'
    where id = 11
   ```

![alt text](image-4.png)

## Delete

![alt text](image-5.png)

Exercise 15 — Tasks

1. This database is getting too big, lets remove all movies that were released before 2005.
   ```sql
    delete from movies where year < 2005
   ```
2. Andrew Stanton has also left the studio, so please remove all movies directed by him.
   ```sql
    delete from movies where director ='Andrew Stanton'
   ```

## Exercise 16 — Tasks

![alt text](image-6.png)

1. Create a new table named Database with the following columns:
   – Name A string (text) describing the name of the database
   – Version A number (floating point) of the latest version of this database
   – Download_count An integer count of the number of times this database was downloaded

```sql
    create table Database(
    Name text,
    Version float,
    Download_count integer
);
```

> DML (Data Manipulatation Language) - CRUD

> DDL (Data Definition Language) - manipulation of the table itself, create and delelte

- If Not Exist -> silently fail

- float (3 decimal), Double( 6 decimal), Real(12 decimals)

- Character(few letters, yes or nor/ male or female), Varchar(250 characters) text(patagraphs)

- Blob -> stores binary data, stores path of the image

---

in real life we make use of **primary key** and **autoincrement**

- Unique - null is allowed, can have multiple uniques in one table
- Not Null - there should be a value it cannot be null
- Check - check if a particular condition is meet before allowing a record in a database
- foreign key -

---

Create of the table is called the schema or the blueprint

---

```sql
create table Department(
    DepartmentID integer primary Key,
    DepartmentName varchar Not Null
);
```

## Exercise 17 — Tasks

1. Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.
   ```sql
    ALTER TABLE Movies
   ADD COLUMN Aspect_ratio FLOAT;
   ```
1. Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.
   ```sql
    ALTER TABLE Movies
   ADD COLUMN Language  Text DEFAULT 'English';
   ```

## Drop the table

![alt text](image-7.png)

1. We've sadly reached the end of our lessons, lets clean up by removing the Movies table
   ```sql
    drop table movies;
   ```
2. And drop the BoxOffice table as well

   ```sql

   ```

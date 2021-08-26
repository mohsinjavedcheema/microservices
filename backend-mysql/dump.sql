USE mydb;
CREATE TABLE students (
    id int NOT NULL,
    lastName varchar(255) NOT NULL,
    firstName varchar(255) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE instructors (
    id int NOT NULL,
    lastName varchar(255) NOT NULL,
    firstName varchar(255) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO students VALUES
(1, "Mesut", "Ozil"), 
(2, "Aaron", "Ramsey"),
(3, "Santi", "Cazorla"),
(4, "Bakoyo", "Saka"),
(5, "Hector", "Bellerin");
INSERT INTO instructors VALUES
(1, "Theirry", "Henry"),
(2, "Dennis", "Bergkemp"),
(3, "Patrick", "Viera"),
(4, "Tony", "Adams"),
(5, "Robert", "Pires");
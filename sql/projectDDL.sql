/*
DROP TABLE Tracker;
DROP TABLE StoreOrder;
DROP TABLE PublisherBook;
DROP TABLE AuthorBook;
DROP TABLE Author;
DROP TABLE UserOrder;
DROP TABLE Book;
DROP TABLE Publisher;
DROP TABLE RegisteredUser;
DROP TABLE BankAccount;
*/

/* 
Creating Tables for DATABASE
*/

CREATE TABLE BankAccount (
    number INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    balance NUMERIC(8,2) NOT NULL
);

CREATE TABLE RegisteredUser (
    email VARCHAR(70) PRIMARY KEY,
    fName VARCHAR(50) NOT NULL,
    lName VARCHAR(50) NOT NULL,
    password VARCHAR(20) NOT NULL,
    role VARCHAR(8) NOT NULL,
    streetNumber VARCHAR(8) NOT NULL,
    streetName VARCHAR(30) NOT NULL,
    postalCode VARCHAR(6) NOT NULL,
    province VARCHAR(30) NOT NULL,
    country VARCHAR(56) NOT NULL,
    city VARCHAR(30) NOT NULL,
	bankAccount INT UNIQUE,
    FOREIGN KEY (bankAccount)
        REFERENCES BankAccount (number) 
);

CREATE TABLE Publisher (
    email VARCHAR(70) PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    address VARCHAR(200) NOT NULL,
    phoneNumber VARCHAR(10) UNIQUE,
	bankAccount INT UNIQUE,
    FOREIGN KEY (bankAccount)
        REFERENCES bankaccount (number)
);

CREATE TABLE Book (
    ISBN VARCHAR(13) PRIMARY KEY,
    genre VARCHAR(30) NOT NULL,
    numPages INT NOT NULL,
    title VARCHAR(70) NOT NULL,
    numSold INT NOT NULL,
    numStock INT NOT NULL,
    buyPrice NUMERIC(8,2) NOT NULL,
    sellPrice NUMERIC(8,2) NOT NULL,
    year INT NOT NULL,
    percentage NUMERIC(5,2) NOT NULL
);


CREATE TABLE UserOrder (
    orderNumber INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cost NUMERIC(8,2) NOT NULL,
    quantity INT NOT NULL,
    date CHAR(10) NOT NULL,
    streetNumber VARCHAR(8) NOT NULL,
    streetName VARCHAR(30) NOT NULL,
    postalCode VARCHAR(6) NOT NULL,
    province VARCHAR(30) NOT NULL,
    city VARCHAR(30) NOT NULL,
    country VARCHAR(56) NOT NULL,
    creditCard CHAR(16) NOT NULL,
    CVV CHAR(3) NOT NULL, 
    expiry CHAR(5) NOT NULL,
	username VARCHAR(70) NOT NULL,
	ISBN VARCHAR(13) NOT NULL,
    FOREIGN KEY (username)
        REFERENCES RegisteredUser (email),
    FOREIGN KEY (ISBN)
        REFERENCES Book (ISBN)
);

CREATE TABLE Author (
    email VARCHAR(70) PRIMARY KEY,
    fName VARCHAR(50) NOT NULL,
    lName VARCHAR(50) NOT NULL
);

CREATE TABLE AuthorBook (
    authorID VARCHAR(70),
    ISBN VARCHAR(13),
    PRIMARY KEY(authorID, ISBN),
    FOREIGN KEY (authorID)
        REFERENCES Author (email),
    FOREIGN KEY (ISBN)
        REFERENCES Book (ISBN)
);

CREATE TABLE PublisherBook (
    publisherID VARCHAR(70),
    ISBN VARCHAR(13),
    PRIMARY KEY(publisherID, ISBN),
    FOREIGN KEY (publisherID)
        REFERENCES Publisher (email),
    FOREIGN KEY (ISBN)
        REFERENCES Book (ISBN)
);

CREATE TABLE StoreOrder (
    orderNumber INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    quantity INT NOT NULL,
    date CHAR(10) NOT NULL,
	ISBN VARCHAR(13) UNIQUE NOT NULL,
    FOREIGN KEY (ISBN)
        REFERENCES Book (ISBN)
);

CREATE TABLE Tracker (
    number INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    status VARCHAR(20) NOT NULL
);

/* BankAccount */
INSERT INTO BankAccount(balance)
VALUES  (4.72),
        (18.63),
        (11.19),
        (7.98),
        (4.18),
        (3243.85),
        (2398.10),
        (7123.50),
        (1432.36);

/* RegisteredUser */
INSERT INTO RegisteredUser
VALUES  ('matt@user.com', 'Matt', 'User', '123456', 'user', '1', 'Road Lane', 'A1B2C3', 'Ontario', 'Canada', 'Ottawa', 6),
        ('vincent@user.com', 'Vincent', 'User1', '9876', 'user', '2', 'Street Road', 'G4H5I6', 'Quebec', 'Canada', 'Quebec', 7),
        ('rachel@employee.com', 'Rachel', 'User2', '7172', 'employee', '3', 'Crescent Street', 'J8K9L2', 'British Columbia', 'Canada', 'Vancouver', 8),
        ('admin@employee.com', 'Admin', 'Employee', '0000', 'employee', '2', 'Boulevard Crescent', 'E2F7G1', 'Ontario', 'Canada', 'Toronto', 9);

/* Publisher */
INSERT INTO Publisher
VALUES  ('grandcentralpublishing@publishing.com', 'Grand Central Publishing', '237 Park Ave FI 16, New York, NY, 10017, United States', '2125227200', 1), 
        ('atriabooks@publishing.com', 'Atria Books', '1230 Avenue of the Americas Rm 13-052a, New York, NY, 10020, United States', '2126987566', 2),
        ('stmartinspublishinggroup@publishing.com', 'St. Martins Publishing Group', '120 Broadway New York, NY, 10271, United States', '2121234567', 3),
        ('littlebrownandcompany@publishing.com', 'Little, Brown And Company', '53 State St, Boston, MA 02109, United States', '6172270730', 4), 
        ('harpercollins@publishing.com', 'HarperCollins', '195 Broadway, New York, NY, 10007, United States', '2122077000', 5);

/* Book */
INSERT INTO Book 
VALUES  ('9781250145291', 'Thrillers', 400, 'A World of Curiosities: A Novel', 2, 10, 27.29, 39.99, 2022, 20.5),
        ('9781538724736', 'Thrillers', 336, 'Verity', 1, 8, 17.58, 22.99, 2021, 19.5),
        ('9781501110368', 'Romance', 384, 'It Ends with Us: A Novel', 4, 10, 15.24, 22.99, 2016, 20.0),
        ('9781501110344', 'Romance', 320, 'November 9: A Novel', 2, 13, 16.50, 22.99, 2015, 19.5),
        ('9780316505420', 'Mystery', 400, 'Desert Star: Signed Edition', 3, 7, 26.60, 38.00, 2022, 10),
        ('9781478948278', 'Crime', 464, 'Void Moon', 1, 10, 7.99, 12.99, 2017, 10),
        ('9780063215382', 'Crime', 416, 'The Guest List: A Novel', 3, 5, 8.99, 12.99, 2022, 15.5);

/* UserOrder */
INSERT INTO UserOrder(cost, quantity, date, streetNumber, streetName, postalCode, province, city, country, creditCard, CVV, expiry, username, ISBN)
VALUES  (12.99, 2, '12/07/2022', '1', 'Road Lane', 'A1B2C3', 'Ontario', 'Toronto', 'Canada', '1234567890123456', '123', '09/25', 'matt@user.com', '9780063215382'),
        (12.99, 1, '11/02/2022', '1', 'Road Lane', 'A1B2C3', 'Ontario', 'Toronto', 'Canada', '1234567890123456', '123', '09/25', 'matt@user.com', '9781478948278'),
        (12.99, 1, '05/05/2021', '2', 'Street Road', 'G4H5I6', 'Quebec', 'Quebec', 'Canada', '0987654321123456', '456', '23/24', 'vincent@user.com', '9780063215382'),
        (38.00, 3, '03/19/2021', '2', 'Street Road', 'G4H5I6', 'Quebec', 'Quebec', 'Canada', '0987654321123456', '456', '23/24', 'vincent@user.com', '9780316505420'),
        (22.99, 2, '11/02/2022', '1', 'Road Lane', 'A1B2C3', 'Ontario', 'Toronto', 'Canada', '1234567890123456', '123', '09/25', 'matt@user.com', '9781501110344'),
        (22.99, 4, '11/02/2022', '1', 'Road Lane', 'A1B2C3', 'Ontario', 'Toronto', 'Canada', '1234567890123456', '123', '09/25', 'matt@user.com', '9781501110368'),
        (22.99, 1, '11/02/2022', '1', 'Road Lane', 'A1B2C3', 'Ontario', 'Toronto', 'Canada', '1234567890123456', '123', '09/25', 'matt@user.com', '9781538724736'),
        (39.99, 2, '03/19/2021', '2', 'Street Road', 'G4H5I6', 'Quebec', 'Quebec', 'Canada', '0987654321123456', '456', '23/24', 'vincent@user.com', '9781250145291');

/* Author */
INSERT INTO Author
VALUES  ('louise@penny.com', 'Louise', 'Penny'),
        ('colleen@hoover.com', 'Colleen', 'Hoover'),
        ('michael@connelly.com', 'Michael', 'Connelly'),
        ('lucy@foley.com', 'Lucy', 'Foley');


/* AuthorBook */
INSERT INTO AuthorBook
VALUES  ('louise@penny.com', '9781250145291'),
        ('colleen@hoover.com', '9781501110368'),
        ('colleen@hoover.com', '9781501110344'),
        ('colleen@hoover.com', '9781538724736'),
        ('michael@connelly.com', '9780316505420'),
        ('michael@connelly.com', '9781478948278'),
        ('lucy@foley.com', '9780063215382');

/* PublisherBook */
INSERT INTO PublisherBook
VALUES  ('stmartinspublishinggroup@publishing.com', '9781250145291'),
        ('atriabooks@publishing.com', '9781501110368'),
        ('atriabooks@publishing.com', '9781501110344'),
        ('grandcentralpublishing@publishing.com', '9781538724736'),
        ('littlebrownandcompany@publishing.com', '9780316505420'),
        ('grandcentralpublishing@publishing.com', '9781478948278'),
        ('harpercollins@publishing.com', '9780063215382');

/* StoreOrder */
INSERT INTO StoreOrder(quantity, date, ISBN)
VALUES  (10, '08/13/2021', '9780316505420'),
        (8, '04/07/2020', '9780063215382'),
        (11, '06/12/2020', '9781478948278'),
        (15, '01/23/2021', '9781501110344'),
        (14, '11/04/2020', '9781501110368'),
        (9, '05/05/2021', '9781538724736'),
        (12, '01/01/2020', '9781250145291');

/* Tracker */
INSERT INTO Tracker(status)
VALUES  ('Delivered'),
        ('Delivered'),
        ('Delivered'),
        ('Delivered'),
        ('Delivered'),
        ('Delivered'),
        ('Delivered'),
        ('Delivered');
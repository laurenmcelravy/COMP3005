/* queries in the application that are run throughout
   not meant to be run on its own, this is just a record
   of all queries in the database 
   
   Most queries contain variable names*/


/* verifyUser*/
SELECT * FROM RegisteredUser WHERE email='user' AND password='password'; /*returns user with given username and password*/

/*registerUser*/
INSERT INTO BankAccount(balance) VALUES (0); /*inserts a bank account tuple with a balance of 0*/
SELECT MAX(number) FROM BankAccount; /*returns the largest number in the number column from bankaccount*/
INSERT INTO RegisteredUser VALUES ('username', 'fName', 'lName', 'password', 'user', 'streetNumber', 'streetName', 'postalCode', 'province', 'country', 'city', result[0][0]); /*inserts a tuple with the users information*/

/*salesVsExpenditures*/
SELECT Book.isbn, Book.title, Book.numsold, Book.numstock, Book.buyprice, Book.sellprice, Book.percentage FROM Book JOIN storeorder ON storeorder.isbn = Book.isbn; /*returns isbn, title, numsold, numstock, buyprice, sellprice, percentage of tuples from Book join storeorder where the isbn is the same */

/*addBook*/
SELECT isbn FROM Book; /*returns isbns from book*/
INSERT INTO Book VALUES ('isbn', 'genre', numPages, 'title', numSold, quantity, buyPrice, sellPrice, year, percentage); /*add a book to the Book relation*/
INSERT INTO StoreOrder(quantity, date, ISBN) VALUES (quantity, 'x.strftime("%x")', 'isbn'); /*add a tuple to the storeorder relation*/
SELECT email FROM Author; /*returns email from author*/
INSERT INTO Author VALUES ('emailA+', 'fName', 'lName'); /*add an author tuple into the author relation*/
SELECT email FROM Publisher; /*returns email from publisher*/
INSERT INTO BankAccount(balance) VALUES (0); /*add a bankaccount with balance value of 0*/
SELECT MAX(number) FROM BankAccount; /*returns the highest number from bankaccout*/
INSERT INTO Publisher VALUES ('emailP', 'name', 'address', 'phoneNumber', result[0][0]); /*add a new publisher */
INSERT INTO AuthorBook VALUES ('emailA', 'isbn');/* add a new author book tuple*/
INSERT INTO PublisherBook VALUES ('emailP', 'isbn');/* add a new publisher book tuple*/
INSERT INTO AuthorBook VALUES ('emailA', 'isbn');/* add a new author book tuple*/
INSERT INTO PublisherBook VALUES ('emailP', 'isbn');/* add a new publisher book*/

/*removeBook*/
SELECT numStock, isbn, title FROM Book;/* return numstock, isbn, title from book for each tuple */
UPDATE Book SET numStock=0 WHERE isbn='selection';/*update the book with the isbn that matches the selection*/

/*salesPerGenre*/
SELECT DISTINCT genre FROM Book;/* returns distinct genres from book*/
SELECT genre, numSold, sellPrice, percentage FROM Book WHERE genre='genres[i][0]';/* returns genre, numsold, sellprice and percentage from book where the genre matches */

/*salesPerAuthor*/
SELECT * FROM Author;/*returns all authors in author*/
SELECT * FROM Book, AuthorBook WHERE Book.isbn = AuthorBook.isbn AND AuthorBook.authorID='authors[i][0]';/* return tuples where Book JOIN AuthorBook where isbn matches and authorId matches given authorid*/

/*titleSearch*/
SELECT * FROM Book WHERE title='search';/*returns all books from book where title matches*/
SELECT authorID FROM AuthorBook WHERE isbn='matches[i][0]';/* returns all authorId from author book where isbn matches */
SELECT publisherID FROM PublisherBook WHERE isbn='matches[i][0]';/* returns publisher id from publisherbook where isbn matches*/

/*authorSearch*/
SELECT * FROM Author WHERE email='search' OR fname='search' OR lname='search';/*returns all authors where the email, faname or lname matches */
SELECT * FROM Book JOIN AuthorBook WHERE Book.isbn = AuthorBook.isbn AND AuthorBook.authorID='matches[i][0]';/*returns all tuples of Book JOIN AuthorBook where isbn's are equal and authorID matches given value*/
SELECT publisherID FROM PublisherBook WHERE isbn='books[j][0]';/*returns publisherID from publisherbook where isbn matches value*/

/*isbnSearch*/
SELECT * FROM Book WHERE isbn='search';/* returns books from Book where isbn matches value*/
SELECT authorID FROM AuthorBook WHERE isbn='matches[0][0]';/*returns authorID from Author book where isbn matches value*/
SELECT publisherID FROM PublisherBook WHERE isbn='matches[0][0]';/*returns publisherId from publisher book where isbn matches value*/

/*genreSearch*/
SELECT * FROM Book WHERE genre='search';/*return books from book where genre matches value*/
SELECT authorID FROM AuthorBook WHERE isbn='matches[i][0]';/*returns authorID from authorBook where isbn matches*/
SELECT publisherID FROM PublisherBook WHERE isbn='matches[i][0]';/*returns publisherID from publisherbook where isbn matches*/

/*yearSearch*/
SELECT * FROM Book WHERE year='search';/*returns book from book where year matches value*/
SELECT authorID FROM AuthorBook WHERE isbn='matches[i][0]';/*returns authorID from authorBook where isbn matches value*/
SELECT publisherID FROM PublisherBook WHERE isbn='matches[i][0]';/*returns publisherID from publisherbook where isbn matches value*/

/*trackOrder*/
SELECT orderNumber FROM UserOrder WHERE username='user[0][0]';/*returns ordernumber from userorder where username matches value*/
SELECT * FROM Tracker WHERE number=order;/* returns tuples from tracker where number matches value*/

/*checkout*/
SELECT * FROM Author, AuthorBook WHERE Author.email = AuthorBook.authorID AND AuthorBook.isbn='cart[i-1][0]';/*select all from Author JOIN authorbook where email and authorID matches and isbn matches value*/
INSERT INTO UserOrder(cost, quantity, date, streetNumber, streetName, postalCode, province, city, country, creditCard, CVV, expiry, username, ISBN) VALUES (cart[j][7], bookQuantity, 'date', 'streetNum', 'streetName', 'postalCode', 'province', 'city', 'country', 'creditCard', 'cvv', 'expiry', 'user[0][0]', 'cart[0][0]');/*add a new userorder to the database */
UPDATE Book SET numSold="+str(cart[j][4]+int(bookQuantity))+", numStock=cart[j][5]-bookQuantity WHERE isbn='cart[j][0]';/* update numsold and numstock from book where isbn matches value*/
INSERT INTO Tracker(status) VALUES ('Ordered');/*insert new tuple into tracker with status equal to ordered*/
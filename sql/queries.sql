/* queries in the application that are run throughout
   not meant to be run on its own, this is just a record
   of all queries in the database 
   
   Most queries contain variable names*/


/* verifyUser*/
SELECT * FROM RegisteredUser WHERE email='user' AND password='password'; /*user and password are provided by user*/

/*registerUser*/
INSERT INTO BankAccount(balance) VALUES (0);
SELECT MAX(number) FROM BankAccount
INSERT INTO RegisteredUser VALUES ('username', 'fName', 'lName', 'password', 'user', 'streetNumber', 'streetName', 'postalCode', 'province', 'country', 'city', result[0][0]);
UPDATE BankAccount SET balance=0 WHERE number=result[0][0];

/*salesVsExpenditures*/
SELECT Book.isbn, Book.title, Book.numsold, Book.numstock, Book.buyprice, Book.sellprice, Book.percentage FROM Book JOIN storeorder ON storeorder.isbn = Book.isbn;

/*addBook*/
SELECT isbn FROM Book
INSERT INTO Book VALUES ('isbn', 'genre', numPages, 'title', numSold, quantity, buyPrice, sellPrice, year, percentage);
INSERT INTO StoreOrder(quantity, date, ISBN) VALUES (quantity, 'x.strftime("%x")', 'isbn');
SELECT email FROM Author;
INSERT INTO Author VALUES ('emailA+', 'fName', 'lName');
SELECT email FROM Publisher;
INSERT INTO BankAccount(balance) VALUES (0);
SELECT MAX(number) FROM BankAccount;
INSERT INTO Publisher VALUES ('emailP', 'name', 'address', 'phoneNumber', result[0][0]);
INSERT INTO AuthorBook VALUES ('emailA', 'isbn');
INSERT INTO PublisherBook VALUES ('emailP', 'isbn');
INSERT INTO AuthorBook VALUES ('emailA', 'isbn');
INSERT INTO PublisherBook VALUES ('emailP', 'isbn');

/*removeBook*/
SELECT numStock, isbn, title FROM Book;
UPDATE Book SET numStock=0 WHERE isbn='selection';

/*salesPerGenre*/
SELECT DISTINCT genre FROM Book;
SELECT genre, numSold, sellPrice, percentage FROM Book WHERE genre='genres[i][0]';

/*salesPerAuthor*/
SELECT * FROM Author;
SELECT * FROM Book, AuthorBook WHERE Book.isbn = AuthorBook.isbn AND AuthorBook.authorID='authors[i][0]';

/*titleSearch*/
SELECT * FROM Book WHERE title='search';
SELECT authorID FROM AuthorBook WHERE isbn='matches[i][0]'
SELECT publisherID FROM PublisherBook WHERE isbn='matches[i][0]'

/*authorSearch*/
SELECT * FROM Author WHERE email='search' OR fname='search' OR lname='search'
SELECT * FROM Book, AuthorBook WHERE Book.isbn = AuthorBook.isbn AND AuthorBook.authorID='matches[i][0]'
SELECT publisherID FROM PublisherBook WHERE isbn='books[j][0]'

/*isbnSearch*/
SELECT * FROM Book WHERE isbn='search'
SELECT authorID FROM AuthorBook WHERE isbn='matches[0][0]'
SELECT publisherID FROM PublisherBook WHERE isbn='matches[0][0]'

/*genreSearch*/
SELECT * FROM Book WHERE genre='search'
SELECT authorID FROM AuthorBook WHERE isbn='matches[i][0]'
SELECT publisherID FROM PublisherBook WHERE isbn='matches[i][0]'

/*yearSearch*/
SELECT * FROM Book WHERE year='search'
SELECT authorID FROM AuthorBook WHERE isbn='matches[i][0]'
SELECT publisherID FROM PublisherBook WHERE isbn='matches[i][0]'

/*trackOrder*/
SELECT orderNumber FROM UserOrder WHERE username='user[0][0]'
SELECT * FROM Tracker WHERE number=order

/*checkout*/
SELECT * FROM Author, AuthorBook WHERE Author.email = AuthorBook.authorID AND AuthorBook.isbn='cart[i-1][0]'
INSERT INTO UserOrder(cost, quantity, date, streetNumber, streetName, postalCode, province, city, country, creditCard, CVV, expiry, username, ISBN) VALUES (cart[j][7], bookQuantity, 'date', 'streetNum', 'streetName', 'postalCode', 'province', 'city', 'country', 'creditCard', 'cvv', 'expiry', 'user[0][0]', 'cart[0][0]')
UPDATE Book SET numSold="+str(cart[j][4]+int(bookQuantity))+", numStock=cart[j][5]-bookQuantity WHERE isbn='cart[j][0]'
INSERT INTO Tracker(status) VALUES ('Ordered')
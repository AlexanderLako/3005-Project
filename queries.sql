USER QUERY STUFF


Gets tracking info for order_number
SELECT tracking_info
FROM order
WHERE order_num = 'PARAM'


checks if user exists, should have count of 1 if exists
SELECT COUNT(1)
FROM user
WHERE username = 'PARAM';

These queries help fill in info for order confirmation
SELECT billing_info
FROM user
WHERE username = 'PARAM';

SELECT shipping_info
FROM user
WHERE username = 'PARAM';



search keys

get the book with this name
SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher
WHERE book.bname = 'PARAM' AND publisher.email_addr = book.email_addr;

get the book with this ISBN
SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, pubisher
WHERE book.ISBN = 'PARAM' AND publisher.email_addr = book.email_addr;

gets all books that have this genre name
SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher, genre
WHERE book.email_addr = publisher.email_addr AND genre.ISBN = book.ISBN AND genre.gname = 'PARAM';

gets all books that have this author name
SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname,
FROM book, publisher, author
WHERE book.email_addr = publisher.email_addr AND author.ISBN = book.ISBN AND author.aname = 'PARAM';


USED IN CONJUNCTION WITH:

Gets the authors of a book
SELECT author.aname
FROM author, book
WHERE author.ISBN = book.ISBN AND book.ISBN = 'PARAM';

Gets the genres of a book
SELECT genre.gname
FROM genre, book
WHERE genre.ISBN = book.ISBN AND book.ISBN = 'PARAM';










OWNER QUERY STUFF

What is sale vs expenditure


Does the sale report by author
SELECT sum(book.quantity_sold), sum (book.quantity_sold * * book.price) AS revenue
FROM book, author
GROUP BY author

Does the sale report by genre
SELECT sum(book.quantity_sold), sum(book.quantity_sold * book.price) AS revenue
FROM book, genres
GROUP BY genre






UPDATING INFO STUFF
remember com.percent
UPDATE publisher
SET money_transferred = money_transferred + 'PRICE GOES HERE'
WHERE email_addr = 'EMAIL HERE'

UPDATE book
SET quantity_remaining = quantity_remainingd + 'PRICE GOES HERE'
WHERE ISBN = 'EMAIL HERE'

DELETE FROM book
WHERE ISBN = 'PARAM';

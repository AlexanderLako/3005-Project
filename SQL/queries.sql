
SELECT *
FROM store_user
WHERE username = %s;


SELECT tracking_info
FROM store_order
WHERE order_num =  %s;

SELECT author.aname
FROM author, book
WHERE author.ISBN = book.ISBN AND book.ISBN = %s AND book.available = 'true';

SELECT genre.gname
FROM genre, book
WHERE genre.ISBN = book.ISBN AND book.ISBN = %s AND book.available = 'true';


SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher
WHERE book.ISBN = %s AND publisher.email_addr = book.email_addr AND book.available = 'true';


SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher
WHERE book.bname = %s AND publisher.email_addr = book.email_addr AND book.available = 'true';


SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher, genre
WHERE book.email_addr = publisher.email_addr AND genre.ISBN = book.ISBN AND genre.gname = %s AND book.available = 'true';


SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher, author
WHERE book.email_addr = publisher.email_addr AND author.ISBN = book.ISBN AND author.aname = %s AND book.available = 'true';


SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher
WHERE publisher.email_addr = book.email_addr AND book.available = 'true';


SELECT quantity_remaining
FROM book
WHERE ISBN = %s;


SELECT max(order_num)
FROM store_order;


SELECT u_addr
FROM store_user
WHERE username = %s;


SELECT card_number
FROM store_user
WHERE username = %s;


SELECT *
FROM publisher
WHERE email_addr =  %s;


SELECT *
FROM book
WHERE ISBN = %s;

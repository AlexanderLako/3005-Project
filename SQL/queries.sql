/* Note that %s represents a parameter passed into the query */




/*Retrieves user information with given username from store_user*/
SELECT *
FROM store_user
WHERE username = %s;

/*Gets the tracking info from an order with the given order_num from store_order*/
SELECT tracking_info
FROM store_order
WHERE order_num =  %s;

/*Gets all the authors (their names) of a book with the given ISBN from the author relation*/
SELECT author.aname
FROM author, book
WHERE author.ISBN = book.ISBN AND book.ISBN = %s AND book.available = 'true';

/*Gets all the genres of a book with the given ISBN from the genre relation*/
SELECT genre.gname
FROM genre, book
WHERE genre.ISBN = book.ISBN AND book.ISBN = %s AND book.available = 'true';

/*Gets a book with the given ISBN and its publisher's name*/
SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher
WHERE book.ISBN = %s AND publisher.email_addr = book.email_addr AND book.available = 'true';

/*Gets books with the given name and their publisher's names*/
SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher
WHERE book.bname = %s AND publisher.email_addr = book.email_addr AND book.available = 'true';

/*Gets books with the given genre and their publisher's names*/
SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher, genre
WHERE book.email_addr = publisher.email_addr AND genre.ISBN = book.ISBN AND genre.gname = %s AND book.available = 'true';

/*Gets books with the given author name and its publisher's names*/
SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher, author
WHERE book.email_addr = publisher.email_addr AND author.ISBN = book.ISBN AND author.aname = %s AND book.available = 'true';

/*Gets all available books from the book relation along with their publisher's name*/
SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
FROM book, publisher
WHERE publisher.email_addr = book.email_addr AND book.available = 'true';

/*Gets the quantity remaining of the book with the given ISBN from the book relation*/
SELECT quantity_remaining
FROM book
WHERE ISBN = %s;

/*Gets the max order_num(which is the most recent order added due to the use of a sequence) from store_order*/
SELECT max(order_num)
FROM store_order;

/*Gets checks if the given order part already exists by getting all tuples with this primary key and checking array size is 0*/
SELECT *
FROM order_contains
WHERE ISBN = %s AND order_num = %s;

/*Gets the user address of the user with the given username from the store_user relation*/
SELECT u_addr
FROM store_user
WHERE username = %s;

/*Gets the card_number of the user with the given username from the store_user relation*/
SELECT card_number
FROM store_user
WHERE username = %s;

/* Queries the publisher and the amount they should be paid based on a book item in a user's cart */
SELECT (book.price * book.com_percentage) * %s, email_addr
FROM book
WHERE ISBN = %s;

/* Gets the revenue made grouped by genre */
SELECT gname, sum(revenue)
FROM (
    SELECT book.ISBN AS ISBN, genre.gname, ((book.price - book.price * book.com_percentage) * book.num_sold) AS revenue
    FROM book, genre
    WHERE book.ISBN = genre.ISBN
) rev_table
GROUP BY gname;

/*Gets the revenue grouped by author */
SELECT aname, sum(revenue)
FROM (
    SELECT book.ISBN AS ISBN, author.aname, ((book.price - book.price * book.com_percentage) * book.num_sold) AS revenue
    FROM book, author
    WHERE book.ISBN = author.ISBN
) rev_table
GROUP BY aname;

/*Get the publisher information with the given email address from the publisher relation*/
SELECT *
FROM publisher
WHERE email_addr =  %s;

/*Get the book information with the given ISBN from the book relation*/
SELECT *
FROM book
WHERE ISBN = %s;

/*Calculate and give the sales and expenditures from a sub-relation containing revenue and money_transfered from the book and publisher relations*/
SELECT sum(revenue) AS sales, sum(money_transfered) AS expenditures
FROM (
    SELECT ((book.price- book.price * book.com_percentage) * book.num_sold) AS revenue, publisher.money_transfered
    FROM book, publisher
    WHERE book.email_addr = publisher.email_addr
) sVe_table;


/* displays all the contents of an order to a user using an order number*/
SELECT isbn, quantity
FROM order_contains
WHERE order_num = %s;

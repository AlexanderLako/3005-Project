/*
Inserts email address, publisher name, address, and money transfered with the values below
*/
INSERT INTO publisher(email_addr, pname, address, money_transfered)
VALUES('bruh@bro.ca', 'White House', 'Trump', 0)
ON CONFLICT (email_addr) DO NOTHING;

/*
Inserts ISBN, quantity remaining, number sold, pages, price, book name, commission percentage, email address, and sets the available key with the values below
*/
INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available)
VALUES(1, 15, 0, 420, 69, 'Fifty_Shades', 0.25, 'bruh@bro.ca', 'true')
ON CONFLICT (ISBN) DO NOTHING;

/*
For the ISBN 1, insert the genre horror
*/
INSERT INTO genre(ISBN, gname)
VALUES(1, 'horror')
ON CONFLICT (ISBN, gname) DO NOTHING;

/*
For the ISBN 1, insert the genre kids animation
*/
INSERT INTO genre(ISBN, gname)
VALUES(1, 'kids animation')
ON CONFLICT (ISBN, gname) DO NOTHING;

/*
For the ISBN 1, insert the author Mista White
*/
INSERT INTO author(ISBN, aname)
VALUES(1, 'Mista White')
ON CONFLICT (ISBN, aname) DO NOTHING;

/*
Create a publisher with email, publisher name, address, and money transfered with the values below
*/
INSERT INTO publisher(email_addr, pname, address, money_transfered)
VALUES('ye@gmail.com', 'Kanye', 'Kim Ks', 0)
ON CONFLICT (email_addr) DO NOTHING;


/*
Create a book with the respected values below
*/
INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available)
VALUES(2, 15, 0, 420, 69, 'V Sauce Michael', 0.25, 'ye@gmail.com', 'true')
ON CONFLICT (ISBN) DO NOTHING;

/*
For the ISBN 2, insert the genre action
*/
INSERT INTO genre(ISBN, gname)
VALUES(2, 'action')
ON CONFLICT (ISBN, gname) DO NOTHING;

/*
For the ISBN 2, insert the genre anime
*/
INSERT INTO genre(ISBN, gname)
VALUES(2, 'anime')
ON CONFLICT (ISBN, gname) DO NOTHING;

/*
For the ISBN 2, insert the genre horror
*/
INSERT INTO genre(ISBN, gname)
VALUES(2, 'horror')
ON CONFLICT (ISBN, gname) DO NOTHING;

/*
For the ISBN 2, insert the author Kanye
*/
INSERT INTO author(ISBN, aname)
VALUES(2, 'Kanye')
ON CONFLICT (ISBN, aname) DO NOTHING;





/*
Insert 3 strings into order_contains
*/
INSERT INTO order_contains(ISBN, quantity, order_num)
VALUES(%s, %s, %s)


/*
update order_contains, set quantity to the quantity plus an amount, set order_num and ISBN to strings
*/
UPDATE order_contains
SET quantity = quantity + %s
WHERE order_num = %s AND ISBN = %s;


/*
Insert 4 strings into store_order
*/
INSERT INTO store_order(tracking_info, username, shipping_info, billing_info)
VALUES(%s, %s, %s, %s);

/*
Update book and set number sold being the amount sold from a books ISBN
*/
UPDATE book
SET num_sold = %s + (
  SELECT num_sold
  FROM book
  WHERE ISBN = %s
)
WHERE ISBN = %s;



/*
Update book and set quantity remaining being the quantity remaining from a books ISBN
*/
UPDATE book
SET quantity_remaining =  (
    SELECT quantity_remaining
    FROM book
    WHERE ISBN = %s
    ) - %s
WHERE ISBN = %s;

/*
Update publishers money transfered being the previous amount plus the new amount
*/
UPDATE publisher
SET money_transfered = money_transfered + %s
WHERE email_addr = %s;

/*
Sets a books initial quantity remaining to 20 + its current remaining amount
if the quantity falls below 10
*/
UPDATE book
SET quantity_remaining = 20 + quantity_remaining
WHERE quantity_remaining < 10;


/*
Insert 9 strings into book
*/
INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available)
VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s);

/*
Insert 2 strings into genre
On conflict where some new values match the old ones, do nothing
*/
INSERT INTO genre(ISBN, gname)
VALUES(%s, %s)
ON CONFLICT (ISBN, gname) DO NOTHING;

/*
insert 4 strings into publisher
if an email is the same, do nothing
*/
INSERT INTO publisher(email_addr, pname, address, money_transfered)
VALUES(%s, %s, %s, %s)
ON CONFLICT (email_addr) DO NOTHING;

/*
insert 2 strings into phone number
if the email and phone numbers are the same as previous values do nothing
*/
INSERT INTO phone_number(email_addr, phone_number)
VALUES(%s, %s)
ON CONFLICT (email_addr, phone_number) DO NOTHING;

/*
update a books (with given ISBN) availability to false
*/
UPDATE book
SET available = 'false'
WHERE ISBN = %s;

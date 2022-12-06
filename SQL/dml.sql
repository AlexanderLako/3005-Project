
INSERT INTO publisher(email_addr, pname, address, money_transfered)
VALUES('bruh@bro.ca', 'White House', 'Trump', 0)
ON CONFLICT (email_addr) DO NOTHING;

INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available)
VALUES(1, 15, 0, 420, 69, 'Fifty_Shades', 0.25, 'bruh@bro.ca', 'true')
ON CONFLICT (ISBN) DO NOTHING;

INSERT INTO genre(ISBN, gname)
VALUES(1, 'horror')
ON CONFLICT (ISBN, gname) DO NOTHING;

INSERT INTO genre(ISBN, gname)
VALUES(1, 'kids animation')
ON CONFLICT (ISBN, gname) DO NOTHING;

INSERT INTO author(ISBN, aname)
VALUES(1, 'Mista White')
ON CONFLICT (ISBN, aname) DO NOTHING;

INSERT INTO publisher(email_addr, pname, address, money_transfered)
VALUES('ye@gmail.com', 'Kanye', 'Kim Ks', 0)
ON CONFLICT (email_addr) DO NOTHING;



INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available)
VALUES(2, 15, 0, 420, 69, 'V Sauce Michael', 0.25, 'ye@gmail.com', 'true')
ON CONFLICT (ISBN) DO NOTHING;

INSERT INTO genre(ISBN, gname)
VALUES(2, 'action')
ON CONFLICT (ISBN, gname) DO NOTHING;

INSERT INTO genre(ISBN, gname)
VALUES(2, 'anime')
ON CONFLICT (ISBN, gname) DO NOTHING;

INSERT INTO genre(ISBN, gname)
VALUES(2, 'horror')
ON CONFLICT (ISBN, gname) DO NOTHING;

INSERT INTO author(ISBN, aname)
VALUES(2, 'Kanye')
ON CONFLICT (ISBN, aname) DO NOTHING;






INSERT INTO order_contains(ISBN, quantity, order_num)
VALUES(%s, %s, %s)



UPDATE order_contains
SET quantity = quantity + %s
WHERE order_num = %s AND ISBN = %s;



INSERT INTO store_order(tracking_info, username, shipping_info, billing_info)
VALUES(%s, %s, %s, %s);


UPDATE book
SET num_sold = %s + (
  SELECT num_sold
  FROM book
  WHERE ISBN = %s
)
WHERE ISBN = %s;




UPDATE book
SET quantity_remaining =  (
    SELECT quantity_remaining
    FROM book
    WHERE ISBN = %s
    ) - %s
WHERE ISBN = %s;



UPDATE book
SET quantity_remaining = 20 + quantity_remaining
WHERE quantity_remaining < 10;



INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available)
VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s);


INSERT INTO genre(ISBN, gname)
VALUES(%s, %s)
ON CONFLICT (ISBN, gname) DO NOTHING;


INSERT INTO publisher(email_addr, pname, address, money_transfered)
VALUES(%s, %s, %s, %s)
ON CONFLICT (email_addr) DO NOTHING;


INSERT INTO phone_number(email_addr, phone_number)
VALUES(%s, %s)
ON CONFLICT (email_addr, phone_number) DO NOTHING;


UPDATE book
SET available = 'false'
WHERE ISBN = %s;

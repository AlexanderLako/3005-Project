INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, name, price, com_percentage, email_addr)
VALUES();

INSERT INTO order(order_num, tracking_info, username, shipping_info, billing_info)
VALUES();

INSERT INTO user(username, tracking_info, billing_info);
VALUES();

INSERT INTO genre(ISBN, genre)
VALUES();

INSERT INTO author(ISBN, author)
VALUES();

INSERT INTO order_contains(order_num, ISBN, quantity)
VALUES();

DELETE FROM book
WHERE(ISBN = '');

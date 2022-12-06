/*
    Creates the store_user entity if it does not already exist
    It contains the primary key - username, and a card number and u_addr
*/

create table if NOT exists store_user
    (
      username varchar(50),
      u_addr varchar(50),
      card_number  varchar(50),
      primary key (username)
    );

/*
    Creates the store_order entity if it does not already exist
    It contains the primary key order_num, which is an INT that acts as a sequence
    This means it auto-increments each time a new tuple is added.
*/
create table if NOT exists store_order
    (
     order_num SERIAL,
     tracking_info  varchar(50),
     username       varchar(50),
     shipping_info  varchar(50),
     billing_info   char(50),
     primary key (order_num),
     foreign key (username) references store_user
    );


/*
    Creates the publisher entity if it does not already exist
    It contains the primary key - email_addr and attributes shown below
*/
create table if NOT exists publisher
  (
      email_addr  varchar(50),
      pname        varchar(50),
      address     varchar(50),
      money_transfered   NUMERIC(5, 2),
      primary key (email_addr)
  );



/*
    Creates the book entity if it does not already exist
    It contains the primary key - ISBN, with other attributes below
    Note that the available flag refers to whether it is in the catalogue or not
    The book references to a publisher's email addr
*/
create table if NOT exists book
  (
    ISBN  INT,
    quantity_remaining  INT,
    num_sold  int,
    pages     INT,
    price     float,
    bname      varchar(50),
    com_percentage  FLOAT,
    email_addr varchar(50) NOT NULL,
    available  varchar(50),
    primary key (ISBN),
    foreign key (email_addr) references publisher
  );


/*
    Creates the phone_number weak entity if it does not already exist
    It contains the primary key - (phone_number, email_addr)
*/
create table if NOT exists phone_number
  (
    email_addr  varchar(50),
    phone_number varchar(50),
    primary key (email_addr, phone_number),
    foreign key (email_addr) references publisher
  );


/*
    Creates the store_user weak entity if it does not already exist
    It contains the primary key - (ISBN, gname)
*/
create table if NOT exists genre
  (
    ISBN  INT,
    gname varchar(50),
    primary key (ISBN, gname),
    foreign key (ISBN) references book(ISBN)
  );


/*
    Creates the author weak entity if it does not already exist
    It contains the primary key - (ISBN, aname)
*/
create table if NOT exists author
  (
    ISBN  INT,
    aname varchar(50),
    primary key (ISBN, aname),
    foreign key (ISBN) references book(ISBN)
  );


/*
    Creates the order_contains relation if it does not already exist
    It contains the primary key (ISBN, order_num), and a quantity purchased for that book
*/
create table if NOT exists order_contains
  (
   order_num INT,
   ISBN      INT,
   quantity  INT,
   primary key (ISBN, order_num),
   foreign key (ISBN) references book(ISBN),
   foreign key (order_num) references store_order
  );

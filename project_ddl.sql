create table store_user
  (
    username varchar(15),
    tracking_info varchar(15),
    billing_info  varchar(15),
    primary key (username)
  );

create table store_order
  (
   order_num INT,
   tracking_info  varchar(15),
   username       varchar(15),
   shipping_info  varchar(15),
   billing_info   char(15),
   primary key (order_num),
   foreign key (username) references store_user
  );

create table publisher
  (
      email_addr  varchar(15),
      pname        varchar(15),
      address     varchar(15),
      money_transferred   NUMERIC(3, 2),
      primary key (email_addr)
  );

create table book
  (
    ISBN  INT,
    quantity_remaining  INT,
    num_sold  int,
    pages     INT,
    price     float,
    bname      varchar(15),
    com_percentage  FLOAT,
    email_addr varchar(15) NOT NULL,
    primary key (ISBN),
    foreign key (email_addr) references publisher
  );

create table phone_number
  (
    email_addr  varchar(15),
    phone_number varchar(10),
    primary key (email_addr, phone_number),
    foreign key (email_addr) references publisher
  );

create table genre
  (
    ISBN  INT,
    gname varchar(15),
    primary key (ISBN, gname),
    foreign key (ISBN) references book(ISBN)
  );

create table author
  (
    ISBN  INT,
    aname varchar(15),
    primary key (ISBN, aname),
    foreign key (ISBN) references book(ISBN)
  );

create table order_contains
  (
   order_num INT,
   ISBN      INT,
   quantity  INT,
   primary key (ISBN, order_num),
   foreign key (ISBN) references book(ISBN),
   foreign key (ISBN) references store_order
  );

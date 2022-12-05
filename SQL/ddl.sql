create table if NOT exists store_user
    (
      username varchar(15),
      u_addr varchar(15),
      card_number  varchar(15),
      primary key (username)
    );

create table if NOT exists store_order
    (
     order_num SERIAL,
     tracking_info  varchar(15),
     username       varchar(15),
     shipping_info  varchar(15),
     billing_info   char(15),
     primary key (order_num),
     foreign key (username) references store_user
    );

create table if NOT exists publisher
  (
      email_addr  varchar(15),
      pname        varchar(15),
      address     varchar(15),
      money_transfered   NUMERIC(3, 2),
      primary key (email_addr)
  );

create table if NOT exists book
  (
    ISBN  INT,
    quantity_remaining  INT,
    num_sold  int,
    pages     INT,
    price     float,
    bname      varchar(15),
    com_percentage  FLOAT,
    email_addr varchar(15) NOT NULL,
    available  varchar(15),
    primary key (ISBN),
    foreign key (email_addr) references publisher
  );

create table if NOT exists phone_number
  (
    email_addr  varchar(15),
    phone_number varchar(10),
    primary key (email_addr, phone_number),
    foreign key (email_addr) references publisher
  );

create table if NOT exists genre
  (
    ISBN  INT,
    gname varchar(15),
    primary key (ISBN, gname),
    foreign key (ISBN) references book(ISBN)
  );

create table if NOT exists author
  (
    ISBN  INT,
    aname varchar(15),
    primary key (ISBN, aname),
    foreign key (ISBN) references book(ISBN)
  );

create table if NOT exists order_contains
  (
   order_num INT,
   ISBN      INT,
   quantity  INT,
   primary key (ISBN, order_num),
   foreign key (ISBN) references book(ISBN),
   foreign key (ISBN) references store_order
  );

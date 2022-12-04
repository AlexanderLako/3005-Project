import psycopg2

# user code

SQLusername = "Alex"
SQLpassword = "3005"

SQLstring = "dbname=3005Project user={} password={}".format(SQLusername, SQLpassword)


conn = None
conn = psycopg2.connect(SQLstring)
conn.autocommit = True
cur = conn.cursor()

def connect():



    commands = (
      """
             create table if NOT exists store_user
        (
          username varchar(15),
          u_addr varchar(15),
          card_number  varchar(15),
          primary key (username)
        );
    """,
  """
  create table if NOT exists store_order
    (
     order_num INT,
     tracking_info  varchar(15),
     username       varchar(15),
     shipping_info  varchar(15),
     billing_info   char(15),
     primary key (order_num),
     foreign key (username) references store_user
    );
  """,
"""
create table if NOT exists publisher
  (
      email_addr  varchar(15),
      pname        varchar(15),
      address     varchar(15),
      money_transferred   NUMERIC(3, 2),
      primary key (email_addr)
  );
  """,
"""
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
    primary key (ISBN),
    foreign key (email_addr) references publisher
  );
  """,
"""
create table if NOT exists phone_number
  (
    email_addr  varchar(15),
    phone_number varchar(10),
    primary key (email_addr, phone_number),
    foreign key (email_addr) references publisher
  );
""",
"""
create table if NOT exists genre
  (
    ISBN  INT,
    gname varchar(15),
    primary key (ISBN, gname),
    foreign key (ISBN) references book(ISBN)
  );
  """,
"""
create table if NOT exists author
  (
    ISBN  INT,
    aname varchar(15),
    primary key (ISBN, aname),
    foreign key (ISBN) references book(ISBN)
  );
""",
"""
create table if NOT exists order_contains
  (
   order_num INT,
   ISBN      INT,
   quantity  INT,
   primary key (ISBN, order_num),
   foreign key (ISBN) references book(ISBN),
   foreign key (ISBN) references store_order
  );
  """
    )

    for command in commands:
            cur.execute(command)

    print("Connection in progress...")

    """ Connect to the PostgreSQL database server """
    #conn = None --------------------------------------------------------------------------------------
    # read connection parameters

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')


    # create a cursor


# execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)
    conn.commit()



def load_db():

    books = (
    """
        INSERT INTO publisher(email_addr, pname, address, money_transferred)
        VALUES('bruh@bro.ca', 'White House', 'Trump', 2.56);
    """,
    """
    INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr)
    VALUES(1, 15, 0, 420, 69, 'Fifty_Shades', 0.25, 'bruh@bro.ca');
    """,
      )

    for book in books:
        cur.execute(book,)

connect()
load_db()

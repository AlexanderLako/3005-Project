import psycopg2

# user code

SQLusername = "Brian"
SQLpassword = "Brian"

SQLstring = "dbname=test user={} password={}".format(SQLusername, SQLpassword)


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
         order_num SERIAL,
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
          money_transfered   NUMERIC(3, 2),
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
        available  varchar(15),
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
    INSERT INTO publisher(email_addr, pname, address, money_transfered)
    VALUES('bruh@bro.ca', 'White House', 'Trump', 0)
    ON CONFLICT (email_addr) DO NOTHING;
    """,
    """
    INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available)
    VALUES(1, 15, 0, 420, 69, 'Fifty_Shades', 0.25, 'bruh@bro.ca', 'true')
    ON CONFLICT (ISBN) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(1, 'horror')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(1, 'kids animation')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO author(ISBN, aname)
    VALUES(1, 'Mista White')
    ON CONFLICT (ISBN, aname) DO NOTHING;
    """,


    """
    INSERT INTO publisher(email_addr, pname, address, money_transfered)
    VALUES('ye@gmail.com', 'Kanye', 'Kim Ks', 0)
    ON CONFLICT (email_addr) DO NOTHING;
    """,
    """
    INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available)
    VALUES(2, 15, 0, 420, 69, 'V Sauce Michael', 0.25, 'ye@gmail.com', 'true')
    ON CONFLICT (ISBN) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(2, 'action')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(2, 'anime')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(2, 'horror')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO author(ISBN, aname)
    VALUES(2, 'Kanye')
    ON CONFLICT (ISBN, aname) DO NOTHING;
    """
  )

    for book in books:
        cur.execute(book,)

    query = "INSERT INTO publisher(email_addr, pname, address, money_transfered) VALUES(%s, %s, %s,%s)"
    vars = ("scary@gmail.com", "Scary Inc", "123 Scary Lane", "0")
    cur.execute(query, vars)

connect()
load_db()

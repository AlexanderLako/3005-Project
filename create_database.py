import psycopg2

# user code

SQLusername = "Brian"
SQLpassword = "3005"

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
          username varchar(50),
          u_addr varchar(50),
          card_number  varchar(50),
          primary key (username)
        );
    """,
    """
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
    """,
    """
    create table if NOT exists publisher
      (
          email_addr  varchar(50),
          pname        varchar(50),
          address     varchar(50),
          money_transfered   NUMERIC(10, 2),
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
        bname      varchar(50),
        com_percentage  FLOAT,
        email_addr varchar(50) NOT NULL,
        available  varchar(50),
        primary key (ISBN),
        foreign key (email_addr) references publisher
      );
      """,
    """
    create table if NOT exists phone_number
      (
        email_addr  varchar(50),
        phone_number varchar(50),
        primary key (email_addr, phone_number),
        foreign key (email_addr) references publisher
      );
    """,
    """
    create table if NOT exists genre
      (
        ISBN  INT,
        gname varchar(50),
        primary key (ISBN, gname),
        foreign key (ISBN) references book(ISBN)
      );
      """,
    """
    create table if NOT exists author
      (
        ISBN  INT,
        aname varchar(50),
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
       foreign key (order_num) references store_order
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
    VALUES(1, 15, 0, 420, 69, 'Fifty Shades of Grey', 0.25, 'bruh@bro.ca', 'true')
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
    """,


    """
    INSERT INTO publisher(email_addr, pname, address, money_transfered)
    VALUES('cwheezer@gmail.com', 'Carl Wheezer', 'Jimmys moms house', 0)
    ON CONFLICT (email_addr) DO NOTHING;
    """,
    """
    INSERT INTO phone_number(email_addr, phone_number)
    VALUES ('cwheezer@gmail.com', '613 123 123')
    ON CONFLICT (phone_number, email_addr) DO NOTHING;
    """,
    """
    INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available)
    VALUES(3, 15, 0, 123, 56, 'Why I Pull Up - A series', 0.20, 'cwheezer@gmail.com', 'true')
    ON CONFLICT (ISBN) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(3, 'autobiography')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(3, 'how-to')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(3, 'religious')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO author(ISBN, aname)
    VALUES(3, 'Carl Wheezer')
    ON CONFLICT (ISBN, aname) DO NOTHING;
    """,



    """
    INSERT INTO publisher(email_addr, pname, address, money_transfered)
    VALUES('jmama@gmail.com', 'Joseph Mama', 'Joe moms house', 0)
    ON CONFLICT (email_addr) DO NOTHING;
    """,
    """
    INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available)
    VALUES(4, 15, 0, 123, 60, 'Fifty Shades Darker', 0.3, 'jmama@gmail.com', 'true')
    ON CONFLICT (ISBN) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(4, 'fantasy')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(4, 'how-to')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO genre(ISBN, gname)
    VALUES(4, 'horror')
    ON CONFLICT (ISBN, gname) DO NOTHING;
    """,
    """
    INSERT INTO author(ISBN, aname)
    VALUES(4, 'Joseph Mama')
    ON CONFLICT (ISBN, aname) DO NOTHING;
    """,
    """
    INSERT INTO author(ISBN, aname)
    VALUES(4, 'Michael Wazowski')
    ON CONFLICT (ISBN, aname) DO NOTHING;
    """,



    """
    INSERT INTO store_user(username, u_addr, card_number)
    VALUES('Michael Wazowski', 'Monsters Inc.', '9876')
    ON CONFLICT(username) DO NOTHING;
    """,
    """
    INSERT INTO store_user(username, u_addr, card_number)
    VALUES('test_user', 'test_addr', 'test_card')
    ON CONFLICT(username) DO NOTHING;
    """
  )

    for book in books:
        cur.execute(book,)

    query = "INSERT INTO publisher(email_addr, pname, address, money_transfered) VALUES(%s, %s, %s,%s) ON CONFLICT(email_addr) DO NOTHING;"
    vars = ("scary@gmail.com", "Scary Inc", "123 Scary Lane", "0")
    cur.execute(query, vars)

connect()
load_db()

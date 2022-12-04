# remember in prompts, add the character number restrictions
# ex. billing info needs to be exactly 9 characters etc.

import psycopg2

# user code

SQLusername = "noah"
SQLpassword = "1234"

SQLstring = "dbname=comp3005 user={} password={}".format(SQLusername, SQLpassword)


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
  )
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
  )
""",
"""
create table if NOT exists publisher
  (
      email_addr  varchar(15),
      pname        varchar(15),
      address     varchar(15),
      money_transferred   NUMERIC(3, 2),
      primary key (email_addr)
  )
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
  )
  """,
"""
create table if NOT exists phone_number
  (
    email_addr  varchar(15),
    phone_number varchar(10),
    primary key (email_addr, phone_number),
    foreign key (email_addr) references publisher
  )
""",
"""
create table if NOT exists genre
  (
    ISBN  INT,
    gname varchar(15),
    primary key (ISBN, gname),
    foreign key (ISBN) references book(ISBN)
  )
  """,
"""
create table if NOT exists author
  (
    ISBN  INT,
    aname varchar(15),
    primary key (ISBN, aname),
    foreign key (ISBN) references book(ISBN)
  )
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
  )
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
    # disconnect()



def disconnect():
    # close the communication with the PostgreSQL
    cur.close()
    if conn is not None:
        conn.close()
        print('Database connection closed.')


# ask user to login or register, then brings up cart
def user_prompts():

    username = ""
    while (username == ""):
        user_prompt = int(input("\nEnter 1 to login or 2 to register: "))
        if user_prompt == 1:
            username = login()
        elif user_prompt == 2:
            username = register()
        else:
            print("invalid input\n")

    while True:
        print("\nEnter 1 to query an existing order")
        print("Enter 2 to make a purchase")
        print("Enter 3 to search catalogue by keyword")
        print("Enter 4 to logout")

        user_prompt = int(input("\nEnter here: "))
        if (user_prompt == 1):
            query_order()
        elif user_prompt == 2:
            user_cart(username)
        elif user_prompt == 3:
            search_catalogue()
        elif user_prompt == 4:
            return

# gets the location of order
def query_order():
    user_prompt = int(input("\nEnter order number: "))

    query = """
            SELECT tracking_info
            FROM order
            WHERE order_num =  %s;
            """
    cur.execute(query, user_prompt)

# check if user with given username exists
def user_exists(username):
    query = """
            SELECT *
            FROM store_user
            WHERE username = %s;
            """ 
    vars = (username,)
    cur.execute(query, vars)

    if cur.fetchone() == None:
        return False
    else:
        return True

def login():
    username = input("\nEnter registered username to login: ")

    if (not user_exists(username)):
        print("Username does not exist.")
        return ""
    else:
        return username

def register():
    username = input("\nEnter a new username to register: ")

    if (user_exists(username)):
        print("Username already exists.")
        return ""
    else:
        card = input("\nEnter a new card number: ")

        u_add = input("\nEnter an address: ")

        query = "INSERT INTO store_user(username, card_number, u_addr) VALUES(%s, %s, %s);"
        vars = (username, card, u_add)

        cur.execute(query, vars)

        return username




def search_catalogue():


    print("\nEnter 1 to search by ISBN")
    print("Enter 2 to search by book name")
    print("Enter 3 to search by genre")
    print("Enter 4 to search by author")
    print("Enter 5 to logout")

    user_prompt = int(input("\nEnter selection here: "))
    books = []
    if (user_prompt == 1):
        books = get_book_by_ISBN()
    elif user_prompt == 2:
        books = get_book_by_name()
    elif user_prompt == 3:
        books = get_books_by_genre()
    elif user_prompt == 4:
        books = get_books_by_author()
    else:
        print("\nInvalid input")


    # Gets the authors of a book
    # SELECT author.aname
    # FROM author, book
    # WHERE author.ISBN = book.ISBN AND book.ISBN = 'PARAM';
    #
    # Gets the genres of a book
    # SELECT genre.gname
    # FROM genre, book
    # WHERE genre.ISBN = book.ISBN AND book.ISBN = 'PARAM';

    print(books)
    # todo: outputs them here



# gets the while querying
def get_book_by_ISBN(ISBN):

    ISBN = input("\nEnter book ISBN: ")

    query = """
        SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
        FROM book, publisher
        WHERE book.ISBN = %s AND publisher.email_addr = book.email_addr;
    """, (ISBN)

    cur.execute(query)

    return

# gets the while querying
def get_book_by_name(bname):

    book_name = input("\nEnter book name: ")

    query = """
    SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    FROM book, publisher
    WHERE book.bname = %s AND publisher.email_addr = book.email_addr;
    """, (book_name)

    cur.execute(query)

    return

def get_books_by_genre():

    genre = input("\nEnter book genre: ")

    query ="""SELECT book.ISBN FROM book, publisher, genre WHERE book.email_addr = publisher.email_addr AND genre.ISBN = book.ISBN AND genre.gname = %s;"""
    vars = (genre,)
    cur.execute(query, vars)

    return cur.fetchone()


def get_books_by_author(genre):

    author = input("\nEnter author name: ")

    query = """
    SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname,
    FROM book, publisher, author
    WHERE book.email_addr = publisher.email_addr AND author.ISBN = book.ISBN AND author.aname = %s;
    """, (author)

    cur.execute(query)

    return


# prompts input for ISBN and quantity
def user_cart(username):
    cart[[]]
    while (input != -1):

        # maybe 2 inputs instead of one

        # SHOULD ALSO PROMPT for searching catalogue keywords and specific book by ISBN

        input = input("Enter ISBN and quantity (max 10) with space seperated:")

        # check for ISBN existence

        # if ok, add ISBN and quantity to cart and maybe change it to a map?

    checkout_cart(cart, username)


def checkout_cart(cart, username):

    addr = input("Enter addr for the order or -1 to use existing addr: ")

    if addr == -1:
        return   # todo get cart here

    card_num = input("Enter card num for the order or -1 to use existing addr: ")

    if card_num == -1:
        return   # todo get card-num here

    # todo update quantities of all bought items
    # update sales for those books
    # update tuples in publisher relation
    # add new order tuple to the order relation
    # add tuples (order_num, book) to order_contains relation









# owner code



# prompts for the owner
def owner_prompts():

    print("\nEnter 1 to add a book to the store")
    print("Enter 2 to remove a book from the store")
    print("Enter 3 to query reports from the store")

    owner_choice = int(input("\nEnter here: "))

    if owner_choice == 3:
        query_store_reports()
    elif owner_choice == 2:
        remove_book()
    elif owner_choice == 1:
        add_book()
    else:
        print("invalid input")


def query_store_reports():
    report_type = []
    # todo print query options

    print("\nEnter 1 to query sales vs. expenditure report")
    print("Enter 2 to query sales by genre")
    print("Enter 3 to query sales by author")

    owner_choice = int(input("\nEnter here: "))

    if owner_choice == 3:
        query_report("author")
    elif owner_choice == 2:
        query_report("genre")
    elif owner_choice == 1:
        return
    else:
        print("invalid input")

# queries reprt by keyowrd for owner
def query_report(type):
    return



# storeowner adding book to store
def add_book():
    genres = []
    genre = input("Enter genre (-1 when done): ")
    if (genre != -1):
        genres.append(genre)
    while (genre != -1):
        genre = input("Enter genre (-1 when done): ")
        if (genre != -1):
            genres.append(genre)

    authors = []
    author = input("Enter author (type nothing and press enter when done): ")
    if (author != ''):
        authors.append(genre)
    while (author != ''):
        author = input("Enter author (-1 when done): ")
        if (genre != ''):
            authors.append(genre)

    name = input("Enter book name: ")

    ISBN = input("Enter ISBN: ")

    publisher = input("Enter publisher email addr: ")

    com_percentage = input("Enter commission percentage: ")

    pages = input("Enter the number of pages in the book: ")

    num_sold = 0

    quantity = 15


    # todo add book entity based on these and what im missing

    # should also add/update publisher tuple?? and genre and author
    # iterate through list of authrors and genres to create new tuples

    print(name + " added to the store catologue")




def publisher_addition_prompts():
    return

# WB Publisher phone numbers?????


def update_publisher(addr):

    # check oif addr exists, then add publisher to entity relation

    # otherwise update?


    # wb phone number?/


    return



# this removes the book from the store
def remove_book():

    ISBN = input("Enter ISBN of book to remove it from store: ")


    # if ISBN does not exist print error, otherwise remove


    print("ISBN does not exist, removal failure")






# main loop
def main():

    connect()

    while (True):
        print("\nEnter 1 if you are a user")
        print("Enter 2 if you are an owner")
        print("Enter 3 if you wish to exit")
        user_type = int(input("\nEnter selection here: "))
        if user_type == 2:
            owner_prompts()
        elif user_type == 1:
            user_prompts()
        elif user_type == 3:
            break



if __name__ == "__main__":
    main()

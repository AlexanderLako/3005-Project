# remember in prompts, add the character number restrictions
# ex. billing info needs to be exactly 9 characters etc.

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
        user_prompt = input("\nEnter 1 to login or 2 to register: ")
        if user_prompt.isdigit() and int(user_prompt) == 1:
            username = login()
        elif user_prompt.isdigit() and int(user_prompt) == 2:
            username = register()
        else:
            print("invalid input\n")

    while True:
        print("\nEnter 1 to query an existing order")
        print("Enter 2 to make a purchase")
        print("Enter 3 to search catalogue by keyword")
        print("Enter 4 to logout")

        user_prompt = input("\nEnter here: ")
        if (user_prompt.isdigit() and int(user_prompt) == 1):
            query_order()
        elif user_prompt.isdigit() and int(user_prompt) == 2:
            user_cart(username)
        elif user_prompt.isdigit() and int(user_prompt) == 3:
            search_catalogue()
        elif user_prompt.isdigit() and int(user_prompt) == 4:
            return
        else:
            print("invalid input")

# gets the location of order
def query_order():
    user_prompt = int(input("\nEnter order number: "))

    query = """
            SELECT tracking_info
            FROM order
            WHERE order_num =  %s;
            """
    vars = (user_prompt,)
    cur.execute(query, vars)

    tracking_info = cur.fetchone()[0]
    print("Your order's tracking information is: " + tracking_info)

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



#to do: add print all books functionality
# do checks to make sure books are available
def search_catalogue():


    print("\nEnter 1 to search by ISBN")
    print("Enter 2 to search by book name")
    print("Enter 3 to search by genre")
    print("Enter 4 to search by author")
    print("Enter 5 to logout")

    user_prompt = input("\nEnter selection here: ")
    books = []
    if (user_prompt.isdigit() and int(user_prompt) == 1):
        ISBN = input("\nEnter book ISBN: ")
        books = get_book_by_ISBN(ISBN)
    elif user_prompt.isdigit() and int(user_prompt) == 2:
        book_name = input("\nEnter book name: ")
        books = get_book_by_name(book_name)
    elif user_prompt.isdigit() and int(user_prompt) == 3:
        genre = input("\nEnter book genre: ")
        books = get_books_by_genre(genre)
    elif user_prompt.isdigit() and int(user_prompt) == 4:
        author = input("\nEnter author name: ")
        books = get_books_by_author(author)
    else:
        print("\nInvalid input")
    
    for book in books:
        print('{:10}{:20}{:15}{:10}{:15}{:10}'.format("ISBN", "Name", "Price", "Pg Num", "Quantity", "Publish Name"))
        print('{:10}{:20}{:15}{:10}{:15}{:10}'.format(str(book[0]), str(book[1]), str(book[2]), str(book[3]), str(book[4]), str(book[5])))
        
        # get author names
        aQuery = """
        SELECT author.aname
        FROM author, book
        WHERE author.ISBN = book.ISBN AND book.ISBN = %s;
        """
        vars = (book[0], )
        cur.execute(aQuery, vars)
        authors = cur.fetchall()

        print("Authors:")
        for author in authors:
            print(str(author[0]))


        # get genres
        gQuery = """
        SELECT genre.gname
        FROM genre, book
        WHERE genre.ISBN = book.ISBN AND book.ISBN = %s;
        """
        cur.execute(gQuery, vars)
        genres = cur.fetchall()

        print("Genres:")
        for genre in genres:
            print(str(genre[0]))
        print("\n")



# gets the while querying
def get_book_by_ISBN(ISBN):

    query = """
        SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
        FROM book, publisher
        WHERE book.ISBN = %s AND publisher.email_addr = book.email_addr;
    """
    vars = (ISBN, )
    cur.execute(query, vars)

    return cur.fetchall()

# gets the while querying
def get_book_by_name(bname):

    query = """
    SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    FROM book, publisher
    WHERE book.bname = %s AND publisher.email_addr = book.email_addr;
    """
    vars = (bname,)
    cur.execute(query, vars)

    return cur.fetchall()

def get_books_by_genre(genre):

    query ="""
    SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    FROM book, publisher, genre
    WHERE book.email_addr = publisher.email_addr AND genre.ISBN = book.ISBN AND genre.gname = %s;
    """
    vars = (genre,)
    cur.execute(query, vars)

    return cur.fetchall()


def get_books_by_author(author_name):

    query = """
    SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    FROM book, publisher, author
    WHERE book.email_addr = publisher.email_addr AND author.ISBN = book.ISBN AND author.aname = %s;
    """
    vars = (author_name,)
    cur.execute(query, vars)

    return cur.fetchall()


# prompts input for ISBN and quantity
def user_cart(username):
    cart = []

    while (True):

        isbn = input("\nEnter ISBN: ")

        quantity = input("\nEnter quantity: ")

        query = """
                SELECT *
                FROM book
                WHERE ISBN = %s;
                """
        vars = (isbn,)
        cur.execute(query, vars)

        if cur.fetchone() == None:
            print("ISBN does not exist")
        else:
            order_part = (username, isbn, quantity)
            cart.append(order_part)

        print("\nEnter 1 to continue shopping: ")
        print("Enter 0 to checkout")
        continue_shopping = int(input(("Enter input here: ")))

        if (continue_shopping == 0):
            break

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

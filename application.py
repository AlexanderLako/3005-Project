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

    print("\nYou are now logged as " +username)

    #allows user to navigate the store
    while True:
        print("\nEnter 1 to query an existing order")
        print("Enter 2 to make a purchase")
        print("Enter 3 to search catalogue by keyword")
        print("Enter 0 to return to main menu")

        user_prompt = input("\nEnter here: ")
        if (user_prompt.isdigit() and int(user_prompt) == 1):
            query_order()
        elif user_prompt.isdigit() and int(user_prompt) == 2:
            user_cart(username)
        elif user_prompt.isdigit() and int(user_prompt) == 3:
            search_catalogue()
        elif user_prompt.isdigit() and int(user_prompt) == 0:
            return
        else:
            print("invalid input")

# gets the location of order
def query_order():
    user_prompt = int(input("\nEnter order number: "))

    query = """
            SELECT tracking_info
            FROM store_order
            WHERE order_num =  %s;
            """
    vars = (user_prompt,)
    cur.execute(query, vars)

    check = cur.fetchone()
    if (check == None):
        print("Order does not exist.")
        return

    tracking_info = check[0]

    display_order(user_prompt)

    print("Your order is currently in " + tracking_info)

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

#login prompt, login with username
def login():
    username = input("\nEnter registered username to login: ")

    if (not user_exists(username)):
        print("Username does not exist.")
        return ""
    else:
        return username

#register a user with their username, card, and address
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

#search catalogue for the user to search by many different options
def search_catalogue():


    print("\nEnter 1 to search by ISBN")
    print("Enter 2 to search by book name")
    print("Enter 3 to search by genre")
    print("Enter 4 to search by author")
    print("Enter 5 to see all available books")
    print("Enter 0 to go back")

    #based on user input, search based on criteria
    user_prompt = input("\nEnter selection here: ")
    books = []
    if user_prompt == '1':
        ISBN = input("\nEnter book ISBN: ")
        books = get_book_by_ISBN(ISBN)
    elif user_prompt == '2':
        book_name = input("\nEnter book name: ")
        books = get_book_by_name(book_name)
    elif user_prompt == '3':
        genre = input("\nEnter book genre: ")
        books = get_books_by_genre(genre)
    elif user_prompt == '4':
        author = input("\nEnter author name: ")
        books = get_books_by_author(author)
    elif user_prompt == '5':
        books = get_all_available_books()
    elif user_prompt == '0':
        return
    else:
        print("\nInvalid input")
        return

    print_books(books)

def print_books(books):
    for book in books:
        print('{:10}{:30}{:15}{:10}{:15}{:10}'.format("ISBN", "Name", "Price", "Pg Num", "Quantity", "Publish Name"))
        print('{:10}{:30}{:15}{:10}{:15}{:10}'.format(str(book[0]), str(book[1]), str(book[2]), str(book[3]), str(book[4]), str(book[5])))

        # get author names
        aQuery = """
        SELECT author.aname
        FROM author, book
        WHERE author.ISBN = book.ISBN AND book.ISBN = %s AND book.available = 'true';
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
        WHERE genre.ISBN = book.ISBN AND book.ISBN = %s AND book.available = 'true';
        """
        cur.execute(gQuery, vars)
        genres = cur.fetchall()

        print("Genres:")
        for genre in genres:
            print(str(genre[0]))
        print("\n")



# gets book by its ISBN
def get_book_by_ISBN(ISBN):

    query = """
        SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
        FROM book, publisher
        WHERE book.ISBN = %s AND publisher.email_addr = book.email_addr AND book.available = 'true';
    """
    vars = (ISBN, )
    cur.execute(query, vars)

    return cur.fetchall()

# gets the book name
def get_book_by_name(bname):

    query = """
    SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    FROM book, publisher
    WHERE book.bname = %s AND publisher.email_addr = book.email_addr AND book.available = 'true';
    """
    vars = (bname,)
    cur.execute(query, vars)

    return cur.fetchall()

#get all books with the desired genre
def get_books_by_genre(genre):

    query ="""
    SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    FROM book, publisher, genre
    WHERE book.email_addr = publisher.email_addr AND genre.ISBN = book.ISBN AND genre.gname = %s AND book.available = 'true';
    """
    vars = (genre,)
    cur.execute(query, vars)

    return cur.fetchall()

#get the books by author name
def get_books_by_author(author_name):

    query = """
    SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    FROM book, publisher, author
    WHERE book.email_addr = publisher.email_addr AND author.ISBN = book.ISBN AND author.aname = %s AND book.available = 'true';
    """
    vars = (author_name,)
    cur.execute(query, vars)

    return cur.fetchall()

#get all available books that are marked true
def get_all_available_books():
    query = """
    SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    FROM book, publisher
    WHERE publisher.email_addr = book.email_addr AND book.available = 'true';
    """
    cur.execute(query)

    return cur.fetchall()




# prompts input for ISBN and quantity
def user_cart(username):
    cart = []

    print_books(get_all_available_books())
    while (True):

        #get ISBN
        isbn = input("\nEnter ISBN: ")

        check_avail = """
                      SELECT available
                      FROM book
                      WHERE ISBN = %s;
                      """
        vars = (isbn,)
        cur.execute(check_avail, vars)
        is_avail = cur.fetchall()

        if not check_ISBN_exists(isbn):
            print("\nISBN does not exist. Please enter an existing ISBN")
            continue
        elif is_avail[0][0] == 'false':
            print("\nBook is currently unavailable (removed from store)")
            continue

        #enter the quantity of books you want to buy
        quantity = input("\nEnter quantity: ")
        if not quantity.isdigit():
            print("\nPlease enter a number")
            continue
        quantity_in_cart = 0
        for order_part in cart:
            if order_part[0] == isbn:
                quantity_in_cart += int(order_part[1])

        Qquery = """
                 SELECT quantity_remaining
                 FROM book
                 WHERE ISBN = %s;
                 """
        vars = (isbn,)
        cur.execute(Qquery, vars)
        q_in_stock = cur.fetchone()[0]

        #check if enough books are available to purchase
        if (quantity_in_cart + int(quantity)) > int(q_in_stock):
            print("Not enough of book #" + isbn + " in stock to add to cart")
            continue

        order_part = (isbn, quantity)
        cart.append(order_part)

        print("\nEnter 1 to continue shopping: ")
        print("Enter 0 to checkout")
        continue_shopping = input("\nEnter input here: ")

        if continue_shopping != '1':
            break
        else:
            print_books(get_all_available_books())

    checkout_cart(cart, username)

#checkout with the items in the users cart
def checkout_cart(cart, username):

    create_order(username)

    # gets the created order's order number
    # (most recently created order will have the highest order number)
    Qorder_num = """
                 SELECT max(order_num)
                 FROM store_order;
                 """

    cur.execute(Qorder_num,)
    order_num = cur.fetchone()[0]

    add_order_items(order_num, cart)

    update_book_quantities(cart)

    display_order(order_num)


# adds all items in the cart to the order_contains relation using the order number
def add_order_items(order_num, cart):
    ISBN_INDEX = 0
    QUANTITY_INDEX = 1

    #for each item in the cart first try to get the ISBN
    for order_part in cart:

        # queries the tuple with this particular candidate key for order_contains
        Qorder_part_exists = """
                             SELECT *
                             FROM order_contains
                             WHERE ISBN = %s AND order_num = %s;
                             """
        vars = (order_part[ISBN_INDEX], order_num)
        cur.execute(Qorder_part_exists, vars)

        check_part_exists = cur.fetchone()

        # checks if the (isbn, order_num) does not already exist. Insert if not exists
        if check_part_exists == None:
            Qorder_contains = """
                              INSERT INTO order_contains(ISBN, quantity, order_num)
                              VALUES(%s, %s, %s);
                              """
            vars = (order_part[ISBN_INDEX], order_part[QUANTITY_INDEX], order_num)

            cur.execute(Qorder_contains, vars)

        #update the order with a order number and the ISBN if already exists
        else:
            Qorder_contains = """
                              UPDATE order_contains
                              SET quantity = quantity + %s
                              WHERE order_num = %s AND ISBN = %s;
                              """
            vars = (order_part[QUANTITY_INDEX], order_num, order_part[ISBN_INDEX])

            cur.execute(Qorder_contains, vars)




#Create an order for a user
def create_order(username):
    addr = input("\nEnter addr for the order or 1 to use existing addr: ")

    #if the user enters '1', get their existing address
    if addr == '1':
        U_addr_query = """
                        SELECT u_addr
                        FROM store_user
                        WHERE username = %s;
                        """

        vars = (username,)
        cur.execute(U_addr_query, vars)
        addr = cur.fetchone()

    card_num = input("Enter card num for the order or 1 to use existing card: ")

    #if the user enters '1', get their existing card number
    if card_num == '1':
        U_card_query = """
                        SELECT card_number
                        FROM store_user
                        WHERE username = %s;
                        """

        vars = (username,)
        cur.execute(U_card_query, vars)
        card_num = cur.fetchone()

    #create a new store order with provided information
    new_order = """
                INSERT INTO store_order(tracking_info, username, shipping_info, billing_info)
                VALUES(%s, %s, %s, %s);
                """

    vars = ('Alabama', username, addr, card_num)
    cur.execute(new_order, vars)
    print("\nThank you for placing an order %s!" % (username))


#update the book quantities based on what the user ordered
def update_book_quantities(cart):

    quantity_index = 1
    isbn_index = 0

    #update the number of books sold for that specific book using ISBN
    for order_part in cart:
        update_num_sold = """
                          UPDATE book
                          SET num_sold = %s + (
                            SELECT num_sold
                            FROM book
                            WHERE ISBN = %s
                          )
                          WHERE ISBN = %s;
                          """
        vars = (order_part[quantity_index], order_part[isbn_index], order_part[isbn_index])

        cur.execute(update_num_sold, vars)

        #update the quantity remaining of a book using ISBN
        update_quantity_remain = """
                                UPDATE book
                                SET quantity_remaining =  (
                                    SELECT quantity_remaining
                                    FROM book
                                    WHERE ISBN = %s
                                    ) - %s
                                WHERE ISBN = %s;
                                """
        vars = (order_part[isbn_index], order_part[quantity_index], order_part[isbn_index])

        cur.execute(update_quantity_remain, vars)

        pay_publisher(order_part[isbn_index], order_part[quantity_index])

    restock_books()


# restocks all the books which have quantities below 10
def restock_books():

    Qrestock = """
               UPDATE book
               SET quantity_remaining = 20 + quantity_remaining
               WHERE quantity_remaining < 10;
               """
    cur.execute(Qrestock)



def pay_publisher(isbn, quantity):

    transfer_Q   = """
                   SELECT (book.price * book.com_percentage) * %s, email_addr
                   FROM book
                   WHERE ISBN = %s;
                   """
    vars = (quantity, isbn)
    cur.execute(transfer_Q, vars)

    transferQ_result = cur.fetchone()
    pub_email = transferQ_result[1]
    amt = transferQ_result[0]

    pay_pub = """
              UPDATE publisher
              SET money_transfered = money_transfered + %s
              WHERE email_addr = %s;
              """
    vars = (amt, pub_email)
    cur.execute(pay_pub, vars)


def display_order(order_num):
    q_order_num = """
                  SELECT isbn, quantity
                  FROM order_contains
                  WHERE order_num = %s;
                  """
    vars = (order_num,)
    cur.execute(q_order_num, vars)

    items = cur.fetchall()
    print("\nOrder number: " + str(order_num))
    print("\nISBN       quantity")
    for item in items:
        print("  " + str(item[0]) + "           " + str(item[1]))





# owner code



# prompts for the owner to add or remove book and get reports
def owner_prompts():

    while(True):
        print("\nEnter 1 to add a book to the store")
        print("Enter 2 to remove a book from the store")
        print("Enter 3 to query reports from the store")
        print("Enter 0 to return to main menu")

        owner_choice = input("\nEnter here: ")

        if owner_choice == '3':
            query_store_reports()
        elif owner_choice == '2':
            remove_book()
        elif owner_choice == '1':
            add_book()
        elif owner_choice == '0':
            break
        else:
            print("invalid input")


#Asks the owner which reports they want to see
# NOTE that these reports consider removed books as well
def query_store_reports():

    print("\nEnter 1 to query sales vs. expenditure report")
    print("Enter 2 to query sales by genre")
    print("Enter 3 to query sales by author")
    print("Enter 0 to return")

    owner_choice = input("\nEnter here: ")

    if owner_choice == '3':
        author_report = query_report_author()
        print('\n{:20}{:20}'.format("Author", "Revenue"))
        for report in author_report:
            print('{:20}{:20}'.format(str(report[0]), str(report[1])))

    elif owner_choice == '2':
        genre_report = query_report_genre()
        print('\n{:20}{:20}'.format("Genre", "Revenue"))
        for report in genre_report:
            print('{:20}{:20}'.format(str(report[0]), str(report[1])))

    elif owner_choice == '1':
        sVeReport = query_sale_v_expenditure()
        print('\n{:20}{:20}'.format("Sales", "Expenditures"))
        for report in sVeReport:
            print('{:20}{:20}'.format(str(report[0]), str(report[1])))
    elif owner_choice == '0':
        return
    else:
        print("invalid input")




def query_sale_v_expenditure():
    sEquery = """
        SELECT sum(revenue) AS sales, sum(money_transfered) AS expenditures
        FROM (
            SELECT ((book.price- book.price * book.com_percentage) * book.num_sold) AS revenue, publisher.money_transfered
            FROM book, publisher
            WHERE book.email_addr = publisher.email_addr
        ) sVe_table;
        """
    cur.execute(sEquery)

    return cur.fetchall()



# queries store sale reports for each genre
def query_report_genre():

    Gquery = """
             SELECT gname, sum(revenue)
             FROM (
                 SELECT book.ISBN AS ISBN, genre.gname, ((book.price - book.price * book.com_percentage) * book.num_sold) AS revenue
                 FROM book, genre
                 WHERE book.ISBN = genre.ISBN
             ) rev_table
             GROUP BY gname;
             """

    cur.execute(Gquery)

    return cur.fetchall()


# queries the amount the store has made by each author
def query_report_author():
    Aquery = """
             SELECT aname, sum(revenue)
             FROM (
                 SELECT book.ISBN AS ISBN, author.aname, ((book.price - book.price * book.com_percentage) * book.num_sold) AS revenue
                 FROM book, author
                 WHERE book.ISBN = author.ISBN
             ) rev_table
             GROUP BY aname;
             """

    cur.execute(Aquery)

    return cur.fetchall()



# storeowner adding book to store
def add_book():
    genres = []
    genre = 0

    ISBN = input("Enter ISBN: ")

    if check_ISBN_exists(ISBN):
        make_avail = """
                     UPDATE book
                     SET available = 'true'
                     WHERE ISBN = %s;
                     """
        vars = (ISBN,)
        cur.execute(make_avail, vars)
        print("\nISBN already exists, book has been re-added to the catalogue")
        return

    name = input("Enter book name: ")

    #allow user to enter multiple genres
    while True:

        genre = input("Enter genre (-1 when done): ")

        if(genre != "-1"):
            genres.append(genre)

        if (genre == "-1" and len(genres) > 0):
            break

    authors = []
    author = 0

    #allow user to enter multiple authors
    while True:

        author = input("Enter author (-1 when done): ")

        if(author != "-1"):
            authors.append(author)

        if (author == "-1" and len(authors) > 0):
            break


    publisher = input("Enter publisher email addr: ")
    query = """
            SELECT *
            FROM publisher
            WHERE email_addr =  %s;
            """
    vars = (publisher,)
    cur.execute(query, vars)

    #check to see if publisher email address already exists, if not create a new publisher with that email
    if cur.fetchone() == None:
        print("The publisher does not exist, please enter their information")
        update_publisher(publisher)

    com_percentage = 0.1
    pages = input("Enter the number of pages in the book: ")
    price = input("Enter the price of the book: ")
    num_sold = 0
    quantity = 15

    query = "INSERT INTO book(ISBN, quantity_remaining, num_sold, pages, price, bname, com_percentage, email_addr, available) VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s)"
    vars = (ISBN, quantity, num_sold, pages, price, name, com_percentage, publisher, 'true')
    cur.execute(query, vars)

    #insert each author and genre into their respected tables
    i = 0
    while i < len(authors):
        query = "INSERT INTO author(ISBN, aname) VALUES(%s, %s) ON CONFLICT (ISBN, aname) DO NOTHING;"
        vars = (ISBN, authors[i])
        cur.execute(query, vars)
        i+=1

    j = 0
    while j < len(genres):
        query = "INSERT INTO genre(ISBN, gname) VALUES(%s, %s) ON CONFLICT (ISBN, gname) DO NOTHING;"
        vars = (ISBN, genres[j])
        cur.execute(query, vars)
        j+=1

    print(name + " added to the store catologue")



#Update the publisher and their phone numbers
def update_publisher(addr):

    pname = input("Please enter publisher name: ")
    address = input("Enter publisher address: ")
    money_transfered = 0

    query = "INSERT INTO publisher(email_addr, pname, address, money_transfered) VALUES(%s, %s, %s, %s) ON CONFLICT (email_addr) DO NOTHING;"
    vars = (addr, pname, address, money_transfered)
    cur.execute(query, vars)

    phoneNumbers = []
    numbers = 0

    #let owner enter phone numbers and insert them into the table
    while True:

        numbers = input("Enter publisher phone number (-1 when done): ")

        if(numbers != "-1"):
            phoneNumbers.append(numbers)

        if (numbers == "-1" and len(phoneNumbers) > 0):
            break

    i = 0
    while i < len(phoneNumbers):
        query = "INSERT INTO phone_number(email_addr, phone_number) VALUES(%s, %s) ON CONFLICT (email_addr, phone_number) DO NOTHING;"
        vars = (addr, phoneNumbers[i])
        cur.execute(query, vars)
        i+=1

    return addr



# this "removes" the book from the store
# by setting the book's available attribute to 'false'
def remove_book():

    print_books(get_all_available_books())
    ISBN = input("\nEnter ISBN of book to remove it from store: ")

    if not check_ISBN_exists(ISBN):
        print("\nISBN does not exist, removal failure")
        return

    Qupdate_avail = """
                    UPDATE book
                    SET available = 'false'
                    WHERE ISBN = %s;
                    """
    vars = (ISBN,)

    cur.execute(Qupdate_avail, vars)

    print("\nBook " + ISBN + " is now removed from the catalogue")


# Checks to see whether the ISBN exists
# by checking to see whether any tuples are returned
def check_ISBN_exists(isbn):
        query = """
                SELECT *
                FROM book
                WHERE ISBN = %s;
                """
        vars = (isbn,)
        cur.execute(query, vars)

        if cur.fetchone() == None:
            return False

        return True


# main loop
def main():

    #connect to database
    connect()

    while (True):
        print("\nEnter 1 if you are a user")
        print("Enter 2 if you are an owner")
        print("Enter 0 if you wish to exit")
        user_type = input("\nEnter selection here: ")
        if user_type == '2':
            owner_prompts()
        elif user_type == '1':
            user_prompts()
        elif user_type == '0':
            disconnect()
            break




if __name__ == "__main__":
    main()

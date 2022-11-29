# remember in prompts, add the character number restrictions
# ex. billing info needs to be exactly 9 characters etc.



# user code


# ask user to login or register, then brings up cart
def user_prompts():

    user_prompt = int(input("\nEnter 1 to login or 2 to register: "))
    username = ""
    if user_prompt == 1:
        username = login()
    elif user_prompt == 2:
        username = register()

        # if user == False:
            # return
    else:
        print("invalid input\n")
        return

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

    # SELECT tracking_info
    # FROM order
    # WHERE order_num = 'PARAM'


def login():
    username = input("\nEnter registered username to login: ")

    # if does not exists, print error

    print("Username does not exist")

    return username

def register():
    username = input("\nEnter a new username to register: ")

    # if username exists, print error and return False
    #******
    print("Username already exists")

    billing_info = input("\nEnter a new card number: ")

    shipping_info = input("\nEnter an address: ")

    # INSERT INTO user(username, tracking_info, billing_info)
    # VALUES();

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


    # todo: outputs them here



# gets the while querying
def get_book_by_ISBN(ISBN):

    ISBN = input("\nEnter book ISBN: ")

    # SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    # FROM book, pubisher
    # WHERE book.ISBN = 'PARAM' AND publisher.email_addr = book.email_addr;

    return

# gets the while querying
def get_book_by_name(bname):

    book_name = input("\nEnter book name: ")

    # SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    # FROM book, publisher
    # WHERE book.bname = 'PARAM' AND publisher.email_addr = book.email_addr;

    return

def get_books_by_genre(genre):

    genre = input("\nEnter book genre: ")

    # SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname
    # FROM book, publisher, genre
    # WHERE book.email_addr = publisher.email_addr AND genre.ISBN = book.ISBN AND genre.gname = 'PARAM';

    return


def get_books_by_author(genre):

    author = input("\nEnter author name: ")

    # SELECT book.ISBN, book.bname, book.price, book.pages, book.quantity_remaining, publisher.pname,
    # FROM book, publisher, author
    # WHERE book.email_addr = publisher.email_addr AND author.ISBN = book.ISBN AND author.aname = 'PARAM';

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

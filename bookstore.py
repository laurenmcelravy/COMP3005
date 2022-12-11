import psycopg2
import datetime
from config import config

def queryBookstore(query):
    #queries database (DQL)

    connection = None
    #print("query")
    try: 
        params = config()
        connection = psycopg2.connect(**params)

        #create a cursor 
        cursor = connection.cursor()

        #execute query and get result
        cursor.execute(query)
        result = cursor.fetchall()
        
        cursor.close()
        return result
    except(Exception, psycopg2.DatabaseError) as error:
        #print(error)
        return(False)
    finally:
        if connection is not None:
            connection.close()

def manipulateBookstore(query):
    #queries database (DML)

    connection = None
    #print("query")
    try: 
        params = config()

        connection = psycopg2.connect(**params)

        #create a cursor 
        cursor = connection.cursor()

        #execute query and get result
        cursor.execute(query)

        connection.commit()

        cursor.close()
        return 
    except(Exception, psycopg2.DatabaseError) as error:
        #print(error)
        return(False)
    finally:
        if connection is not None:
            connection.close()

def verifyEmployee(user):
    #verify employee
    #check the role of the user 
    if user[4] == "employee":
        employee = True
    else:
        employee = False
    return employee 

def verifyUser(user, password):
    # query database to see if there is a user already 
    result = queryBookstore("SELECT * FROM RegisteredUser WHERE email='"+user+"' AND password='"+password+"'")
    return result

def registerUser():
    #registering a user 
    # adding them to the data base 
    print("---------------------------------------------------------")
    print("     REGISTERING USER")
    print()
    correct = False
    while correct == False:
        print("     User Registration")
        #get user input for registration
        username = input("     email (this will be your username): ")
        fName = input("     First Name: ")
        lName = input("     Last Name: ")
        password = input("     Password: ")
        address = input("     Full Address: ")
        print()
        print("     Please confirm the following information is correct.")
        print("---------------------------------------------------------")
        print("     username = "+username)
        print("     First Name = "+fName)
        print("     Last Name = "+lName)
        print("     password = "+password)
        print("     Full Address = "+address)
        print("---------------------------------------------------------")
        confirm = input(" Confirm Here (y for yes, any key to restart): ")
        if confirm == "y":
            correct = True
            if (verifyUser(username, password) != []):
                # check if the username and password is already in database 
                print()
                print("     There is already an account registered to that email.")
                print("     You will be logged into that account.")
            else:
                # if the usernaame and password do not exist, add user to database 
                manipulateBookstore("INSERT INTO BankAccount(balance) VALUES (0)")
                result = queryBookstore("SELECT MAX(number) FROM BankAccount")
                check = manipulateBookstore("INSERT INTO RegisteredUser VALUES ('"+username+"', '"+fName+"', '"+lName+"', '"+password+"', 'user', '"+address+"', "+str(result[0][0])+");")
                if (check == False):
                    #check for error
                    correct = False 
                    print("     An error occurred. Please try again.")
                    print()
        else:
            correct = False
        print()
    user = verifyUser(username, password) 
    return user

def salesVsExpenditures():
    results = queryBookstore("SELECT Book.isbn, Book.title, Book.numsold, Book.numstock, Book.buyprice, Book.sellprice, Book.percentage FROM Book JOIN storeorder ON storeorder.isbn = Book.isbn;")

    #print(len(results))
    sales = 0
    salesPercentage = 0
    expenditures = 0
    #isbn, title, numsold, numstock, buyprice, sellprice, percentage

    print("--------------------------------------------------------------")
    print("     SALES VS. EXPENDITURES REPORT PER BOOK")
    print()

    for i in range(0,len(results)):
        #print(results[i])
        sales += results[i][2] * results[i][5]
        expenditures += results[i][2] * results[i][4]
        salesPercentage += results[i][2] * results[i][6]

        print("     Book: " + str(results[i][1]))
        print("          Sales: " + str(results[i][2]*results[i][5]))
        print("          Sales minus Publisher's Percentage: " + str(results[i][2]*results[i][4]))
        print("          Expenditures: " + str(results[i][2]*results[i][6]))
        print("          Profits: " + str((results[i][2]*results[i][4]) - (results[i][2]*results[i][6])))
        print()

    print("--------------------------------------------------------------")
    print("     SALES VS. EXPENDITURES REPORT TOTAL")
    print("     Total Sales: "+str(sales))
    print("     Total Sales minus Publisher's Percentage: "+str(sales - salesPercentage))
    print("     Total Expenditures: "+str(expenditures))
    print("     Total Profits: " + str(salesPercentage-expenditures))
    print("--------------------------------------------------------------")
    print()
    return

def addBook():
    print("--------------------------------------------------------------")
    print("     ADD A NEW BOOK")
    print()
    x = datetime.datetime.now()
    
    #input information manually
    correct = False
    while correct == False :
        print("     Please Ensure You Have The Information On: ")
        print("     Book, Author and Publisher")
        print()
        print("     Book Information")
        isbn = input("          Book ISBN: ")
        genre = input("          Book Genre: ")
        numPages = input("          Number of Pages: ")
        title = input("          Book Title: ")
        numSold = 0
        quantity = input("          Quantity to Order: ")
        buyPrice = input("          Cost: ")
        sellPrice = input("          Price to Sell: ")
        year = input("          Year Book was Published: ")
        percentage = input("          Percentage owed: ")
        print()
        print("     Author Information")
        emailA = input("          Author's Email: ")
        fName = input("          Author's First Name: ")
        lName = input("          Author's Last Name: ")
        print()
        print("     Publisher Information")
        emailP = input("          Publisher's Email: ")
        name = input("          Publisher's Name: ")
        address = input("          Publisher's Address: ")
        phoneNumber = input("          Publisher's Phone Number: ")

        print()
        print("     Please confirm the following is correct.")
        print()
        print("     Book Information: "+isbn+" "+genre+" "+str(numPages)+" "+title+" "+str(numSold)+" "+str(quantity)+" "+str(buyPrice)+" "+str(sellPrice)+" "+str(year)+" "+str(percentage))
        print("     Author Information: "+emailA+" "+fName+" "+lName)
        print("     Publisher Information: "+emailP+" "+name+" "+address+" "+phoneNumber)
        print()
        confirm = input("     Is this information correct (y for Yes): ")
        print()
        if confirm == "y":
            correct = True
            #check for existing book
            eBooks = queryBookstore("SELECT isbn FROM Book")
            uBook = True
            for i in range(0, len(eBooks)):
                #print(eBooks[i][0])
                if isbn == eBooks[i][0]:
                    uBook = False
            if uBook == True:
                #unique book 
                check1 = manipulateBookstore("INSERT INTO Book VALUES ('"+isbn+"', '"+genre+"', "+str(numPages)+", '"+title+"', "+str(numSold)+", "+str(quantity)+", "+str(buyPrice)+", "+str(sellPrice)+", "+str(year)+", "+str(percentage)+")")
                check2 = manipulateBookstore("INSERT INTO StoreOrder(quantity, date, ISBN) VALUES ("+quantity+", '"+str(x.strftime("%x"))+"', '"+isbn+"')")
                if (check1==False or check2==False):
                    #check for errors 
                    correct = False
                    print("     An error occurred please try again.")
                    print()
                    break
            else:
                check10 = manipulateBookstore("UPDATE Book SET numStock="+quantity+"WHERE isbn='"+isbn+"'")
                if (check10 == False):
                    #check for errors 
                    correct = False
                    print("     An error occurred please try again.")
                    print()
                    break

            #check for existing author 
            authors = queryBookstore("SELECT email FROM Author")
            uAuthor = True
            for j in range(0, len(authors)):
                if emailA == authors[j][0]:
                    uAuthor = False
            if uAuthor == True:
                #unique author 
                check3 = manipulateBookstore("INSERT INTO Author VALUES ('"+emailA+"', '"+fName+"', '"+lName+"')")
                if (check3 == False):
                    #check for errors
                    correct = False
                    print("     An error occurred please try again.")
                    print()
                    break

            #check for existing publisher 
            publishers = queryBookstore("SELECT email FROM Publisher")
            uPublisher = True
            for k in range(0, len(publishers)):
                if emailP == publishers[k][0]:
                    uPublisher = False
            if uPublisher == True:
                #unique publisher 
                manipulateBookstore("INSERT INTO BankAccount(balance) VALUES (0)")
                result = queryBookstore("SELECT MAX(number) FROM BankAccount")
                check5 = manipulateBookstore("INSERT INTO Publisher VALUES ('"+emailP+"', '"+name+"', '"+address+"', '"+phoneNumber+"', "+str(result[0][0])+")")
                if (check5 == False):
                    #check for errors 
                    correct = False
                    print("     An error occurred please try again.")
                    print()
                    break

            if (uBook == False) :
                #not a unique book 
                if (uAuthor == True):
                    #unique author 
                    #add author book to database 
                    check6 = manipulateBookstore("INSERT INTO AuthorBook VALUES ('"+emailA+"', '"+isbn+"')")
                if (uPublisher == True):
                    #unique publisher 
                    #add publisher book 
                    check7 = manipulateBookstore("INSERT INTO PublisherBook VALUES ('"+emailP+"', '"+isbn+"')")
                if (check6 == False or check7 == False):
                    #check for errors 
                    correct = False
                    print("     An error occurred please try again.")
                    print()
                    break
            else :
                check8 = manipulateBookstore("INSERT INTO AuthorBook VALUES ('"+emailA+"', '"+isbn+"')")
                check9 = manipulateBookstore("INSERT INTO PublisherBook VALUES ('"+emailP+"', '"+isbn+"')")
                if (check8 == False or check9 == False):
                    #check for errors 
                    correct = False
                    print("     An error occurred please try again.")
                    print()
                    break           
            
        else:
            correct = False

    return 

def removeBook():
    print("----------------------------------------------------------------------------------")
    print("     REMOVE A BOOK FROM THE COLLECTION")
    print()
    print("     Current Books in the Store's Collection: ")
    print()

    books = queryBookstore("SELECT numStock, isbn, title FROM Book")
    for i in range(0, len(books)):
        if (books[i][0] != 0):
            print("          Stock: "+str(books[i][0])+" ISBN: "+str(books[i][1])+" Title: "+str(books[i][2]))
    print("----------------------------------------------------------------------------------")
    print()

    selection = input("     Enter the ISBN of the Book to be Removed: ")
    print()

    isbn = False 
    for j in range(0, len(books)):
        if (selection == books[j][1]):
            isbn = True

    if (isbn == True):
        manipulateBookstore("UPDATE Book SET numStock=0 WHERE isbn='"+selection+"'")
    return 
    
def salesPerGenre():
    genres = queryBookstore("SELECT DISTINCT genre FROM Book")
    print("--------------------------------------------------------------")
    print("     SALES PER GENRE REPORT")
    print()
    for i in range(0, len(genres)):
        books = queryBookstore("SELECT genre, numSold, sellPrice, percentage FROM Book WHERE genre='"+genres[i][0]+"'")
        print("          GENRE: "+genres[i][0])
        sales = 0
        percentage = 0
        for j in range(0, len(books)):
            sales += books[j][1]*books[j][2]
            percentage += books[j][1]*books[j][3]
        print("          Sales: "+str(sales-percentage))
        print()
    print("--------------------------------------------------------------")
    return 

def salesPerAuthor():
    authors = queryBookstore("SELECT * FROM Author")
    print("--------------------------------------------------------------")
    print("     SALES PER AUTHOR REPORT")
    print()
    for i in range(0, len(authors)):
        books = queryBookstore("SELECT * FROM Book JOIN AuthorBook ON Book.isbn = AuthorBook.isbn AND AuthorBook.authorID='"+authors[i][0]+"'")
        print("          AUTHOR: "+authors[i][1]+" "+authors[i][2])
        sales = 0
        percentage = 0
        for j in range(0, len(books)):
            sales = books[j][4]*books[j][7] 
            percentage = books[j][4]*books[j][9]       
        print("          SALES: "+str(sales-percentage))
        print()
    print("--------------------------------------------------------------")
    print()
    return

def titleSearch(cart):
    print("--------------------------------------------------------------")
    print("     SEARCH BY TITLE")
    print()
    search = input("     SEARCH: ")
    matches = queryBookstore("SELECT * FROM Book WHERE title='"+search+"'")
    print()
    
    if matches!=[] :
        for i in range (0, len(matches)):
            if (matches[i][5] != 0):
                author = queryBookstore("SELECT authorID FROM AuthorBook WHERE isbn='"+matches[i][0]+"'")
                publisher = queryBookstore("SELECT publisherID FROM PublisherBook WHERE isbn='"+matches[i][0]+"'")
                print("          "+matches[i][0]+": | TITLE: "+matches[i][3]+"| AUTHOR: "+author[0][0]+"| NUMBER OF PAGES: "+str(matches[i][2])+"| GENRE: "+matches[i][1]+"| PUBLISHER: "+publisher[0][0])
                print("               Available Copies: "+str(matches[i][5])+" Priced at: "+str(matches[i][7]))
                print()

        isbn = input("          Add to Cart (Enter isbn # or any key to continue): ")
        print()
        for j in range(0, len(matches)):
            if (isbn == matches[j][0]):
                cart.append(matches[j])
    else:
        print("     No search results.")
        print()
    
    return 

def authorSearch(cart):
    print("--------------------------------------------------------------")
    print("     SEARCH BY AUTHOR")
    print()
    search = input("          SEARCH (using email, first name, last name): ")
    print()

    matches = queryBookstore("SELECT * FROM Author WHERE email='"+search+"' OR fname='"+search+"' OR lname='"+search+"'")
    
    if matches!=[] :
        for i in range (0, len(matches)):
            books = queryBookstore("SELECT * FROM Book JOIN AuthorBook WHERE Book.isbn = AuthorBook.isbn AND AuthorBook.authorID='"+matches[i][0]+"'")
            
            for j in range(0, len(books)):

                if (books[j][4] != 0):
                    publisher = queryBookstore("SELECT publisherID FROM PublisherBook WHERE isbn='"+books[j][0]+"'")
                    print("          "+books[j][0]+": | TITLE: "+books[j][3]+"| AUTHOR: "+matches[i][0]+"| NUMBER OF PAGES: "+str(books[j][2])+"| GENRE: "+books[j][1]+"| PUBLISHER"+publisher[0][0])
                    print("               Available Copies: "+str(books[0][5]))
                    print()
        
        isbn = input("          Add to Cart (Enter isbn # or any key to continue): ")
        print()
        for k in range(0, len(books)):
            if (isbn == books[k][0]):
                cart.append(books[k])

    else:
        print("     No search results.")
        print()

    return 

def isbnSearch(cart):
    print("--------------------------------------------------------------")
    print("     SEARCH BY ISBN")
    print()
    search = input("          SEARCH: ")
    matches = queryBookstore("SELECT * FROM Book WHERE isbn='"+search+"'")
    print()
    
    if matches!=[] :
        if (matches[0][5] != 0):
            author = queryBookstore("SELECT authorID FROM AuthorBook WHERE isbn='"+matches[0][0]+"'")
            publisher = queryBookstore("SELECT publisherID FROM PublisherBook WHERE isbn='"+matches[0][0]+"'")
            print("          "+matches[0][0]+": | TITLE: "+matches[0][3]+"| AUTHOR: "+author[0][0]+"| NUMBER OF PAGES: "+str(matches[0][2])+"| GENRE: "+matches[0][1]+"| PUBLISHER"+publisher[0][0])
            print("               Available Copies: "+str(matches[0][5]))
            print()

        isbn = input("          Add to Cart (Enter isbn # or any key to continue): ")
        print()
        for j in range(0, len(matches)):
            if (isbn == matches[j][0]):
                cart.append(matches[j])
    else:
        print("     No search results.")
        print()
    
    return 

def genreSearch(cart):
    print("--------------------------------------------------------------")
    print("     SEARCH BY GENRE")
    print()
    search = input("          SEARCH: ")
    matches = queryBookstore("SELECT * FROM Book WHERE genre='"+search+"'")
    print()
    if matches!=[] :
        for i in range(0, len(matches)):
            if (matches[i][5] != 0):
                author = queryBookstore("SELECT authorID FROM AuthorBook WHERE isbn='"+matches[i][0]+"'")
                publisher = queryBookstore("SELECT publisherID FROM PublisherBook WHERE isbn='"+matches[i][0]+"'")
                print("          "+matches[i][0]+": | TITLE: "+matches[i][3]+"| AUTHOR: "+author[0][0]+"| NUMBER OF PAGES: "+str(matches[i][2])+"| GENRE: "+matches[i][1]+"| PUBLISHER"+publisher[0][0])
                print("               Available Copies: "+str(matches[i][5]))
                print()

        isbn = input("          Add to Cart (Enter isbn # or any key to continue): ")
        print()
        for j in range(0, len(matches)):
            if (isbn == matches[j][0]):
                cart.append(matches[j])
    else:
        print("     No search results.")
        print()
    
    return  

def yearSearch(cart):
    print("--------------------------------------------------------------")
    print("     SEARCH BY PUBLISHED YEAR")
    print()
    search = input("          SEARCH: ")
    matches = queryBookstore("SELECT * FROM Book WHERE year='"+search+"'")
    print()
    if matches!=[] :
        for i in range(0, len(matches)):
            if (matches[i][5] != 0):
                author = queryBookstore("SELECT authorID FROM AuthorBook WHERE isbn='"+matches[i][0]+"'")
                publisher = queryBookstore("SELECT publisherID FROM PublisherBook WHERE isbn='"+matches[i][0]+"'")
                print("          "+matches[i][0]+": | TITLE: "+matches[i][3]+" | AUTHOR: "+author[0][0]+" | NUMBER OF PAGES: "+str(matches[i][2])+" | GENRE: "+matches[i][1]+" | PUBLISHER"+publisher[0][0])
                print("               Available Copies: "+str(matches[i][5]))
                print()

        isbn = input("          Add to Cart (Enter isbn # or any key to continue): ")
        print()
        for j in range(0, len(matches)):
            if (isbn == matches[j][0]):
                cart.append(matches[j])
    else:
        print("     No search results.")
        print()
    
    return  

def trackOrder(user):
    print("--------------------------------------------------------------")
    print("     TRACK YOUR ORDER ")
    print()
    order = input("     Order Number: ")
    print()
    userOrders = queryBookstore("SELECT orderNumber FROM UserOrder WHERE username='"+user[0][0]+"'")
    result = queryBookstore("SELECT * FROM Tracker WHERE number="+order)
    if result ==[]:
        print("     There is no order with that number.")
    else: 
        owner = False 
        for i in range(0, len(userOrders)):
            if (int(order) == userOrders[i][0]):
                owner = True
        if owner == False:
            print("     "+user[0][0]+" did not place this order.")
            print("     Please enter an order you placed.")
        else:
            print("     Order "+str(result[0][0])+" Status is "+result[0][1])
    print()
    return 

def checkout(user, cart):
    print("--------------------------------------------------------------")
    print("     CART: ")
    print()
    if (cart == []):
        print("     There are no items in your cart.")
        ("--------------------------------------------------------------")
        print()
    else :  
        x = datetime.datetime.now()
        for i in range(1, len(cart)+1):
            author = queryBookstore("SELECT * FROM Author JOIN AuthorBook ON Author.email = AuthorBook.authorID AND AuthorBook.isbn='"+cart[i-1][0]+"'")
            print("     "+str(i)+". "+cart[i-1][3]+"  BY "+author[0][1]+" "+author[0][2]+" A "+cart[i-1][1]+" NOVEL")
            print("          Price: "+str(cart[i-1][7]))
            print()
        
        #get order information 
        order = False
        while order == False:
            print("     Billing/Shipping Information")
            date = x.strftime("%x")
            address = input("     Full Address: ")
            print()

            print("     Payment Information")
            creditCard = input("     Credit Card Number: ")
            cvv = input("     CVV: ")
            expiry = input("     expiry: ")
            print()

            correct = input("     Please confirm the above is correct (y for yes): ")
            if correct == "y":
                order = True
            
        if order == True:
            bookQuantity = 0
            for j in range(0, len(cart)):
                print()
                possible = False
                while possible == False:
                    bookQuantity = input("     Quantity of "+cart[j][3]+": ")
                    if (int(bookQuantity) <= int(cart[j][5])):
                        possible = True
                        break
                    else:
                        print("     Please Try Again. ")
                        print("     Quantity Requested is More than Available.")
                        print()
                if possible == True:
                    #place user order 
                    check1 = manipulateBookstore("INSERT INTO UserOrder(cost, quantity, date, address, creditCard, CVV, expiry, username, ISBN) VALUES ("+str(cart[j][7])+", "+bookQuantity+", '"+date+"', '"+address+"', '"+creditCard+"', '"+cvv+"', '"+expiry+"', '"+user[0][0]+"', '"+cart[0][0]+"')")
                    if (check1 == False):
                        print("     An error occurred please try again.")
                        print()
                        return cart
                    #update book 
                    check2 = manipulateBookstore("UPDATE Book SET numSold="+str(cart[j][4]+int(bookQuantity))+", numStock="+str(cart[j][5]-int(bookQuantity))+" WHERE isbn='"+cart[j][0]+"'")
                    if (check2 == False):
                        print("     An error occurred please try again.")
                        print()
                        return cart                        
                    #make tracker 
                    check3 = manipulateBookstore("INSERT INTO Tracker(status) VALUES ('Ordered')")
                    if (check3 == False):
                        print("     An error occurred please try again.")
                        print()
                        return cart
                    bookQuantity = 0
                    print()
                    print("--------------------------------------------------------------")
                    print("     Thank You!")
                    print("--------------------------------------------------------------")
                    print()
                
            cart =  []
        return cart 

#main
x = datetime.datetime.now()
print("--------------------------------------------------------------")
print("---------                Look Inna Book              ---------")
print("-----                 THE ONLINE BOOKSTORE               -----")
print("---                                                        ---")
print("     New user? Please Register")
print("     Have you shopped with us before? Please Login")
print("     Look Inna Book employee(s) please enter")
print("     your login")
print()
print("     "+ x.strftime("%x"))
print()

register = input("     Are you Registered? (Enter y for Yes): ")
print()

if (register == "y"):
    username = input("     username: ")
    password = input("     password: ")
    print()

    # verify user 
    currentUser = verifyUser(username, password)

    if (currentUser == []):
        print("     You are not a registered User please register now :)")
        currentUser = registerUser()
else:
    currentUser = registerUser()

# check for employee or user
if (verifyEmployee(currentUser[0]) == True):
    print("--------------------------------------------------------------")
    print("            WELCOME Look Inna Book EMPLOYEE!")
    print()
    employeeQuit = False
    while (employeeQuit == False):
        print("     (1) Sales VS. Expenditures Report ")
        print("     (2) Add NEW BOOK ")
        print("     (3) Remove BOOK ")
        print("     (4) Sales per genre Report ")
        print("     (5) Sales per author Report ")
        print("     (6) Exit ")
        print()
        request = input("     Enter request: ")
        print()
        if (request == "1"):
            salesVsExpenditures()
        elif (request == "2"):
            addBook()
        elif (request == "3"):
            removeBook()
        elif (request == "4"):
            salesPerGenre()
        elif (request == "5"):
            salesPerAuthor()
        elif (request == "6"):
            employeeQuit = True
        else:
            print ("     Please enter an option (1-6): ")
else:
    cart = []
    userQuit = False
    while (userQuit == False):
        print("     (1) Search by TITLE ")
        print("     (2) Search by AUTHOR ")
        print("     (3) Search by ISBN ")
        print("     (4) Search by GENRE ")
        print("     (5) Search by YEAR ")
        print("     (6) Track Order ")
        print("     (7) Checkout")
        print("     (8) Exit ")
        print()
        request = input ("Enter request: ")
        print()
        if (request == "1"):
            titleSearch(cart)
        elif (request == "2"):
            authorSearch(cart)
        elif (request == "3"):
            isbnSearch(cart)
        elif (request == "4"):
            genreSearch(cart)
        elif (request == "5"):
            yearSearch(cart)
        elif (request == "6"):
            trackOrder(currentUser)
        elif (request == "7"):
            cart = checkout(currentUser, cart)
        elif (request == "8"):
            userQuit = True
        else:
            print("     Please enter an option (1-8): ")
            print()



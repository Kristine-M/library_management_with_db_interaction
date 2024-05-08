
import book
import user
import author
import user
import menu
import genre
import error_handle
import borrow_book

lib_user = user.User()
lib_authors = author.Author()
borrow = borrow_book.Borrow_Book()
new_book = book.Book()
menu.print_main_menu()
user_input = error_handle.main_menu_valid_input()


    
while (user_input != 5):
    if user_input == 1:
        menu.print_book_op()
        inner_input = error_handle.main_menu_valid_input()
    
        if inner_input == 1:
            
            title = input("Title of the book you want to add: ")
            authr = input("Author ID of the book you want to add: ")
            isbn = input("ISBN of the book you want to add: ")
            pub_date = input("Publication date of the book you want to add (format YYYY-MM-DD): ")
            genre_id= input("Genre ID of the book you want to add: ")
            
           

            new_book.add_book(title, authr, genre_id, isbn, pub_date, 1)
            new_book.display()
        
        elif inner_input == 2:
            
            lib_user.display()
            user_id = input("What is your user ID? ")
            new_book.display()
            book_id = input("What is the book ID you want to borrow? ")
            
            can_borrow = borrow.check_avail(book_id)
            
            if can_borrow:
                borrow_date = input("Enter today's date (format YYYY-MM-DD): ")
                borrow.borrow_book(user_id, book_id, borrow_date)
        
        elif inner_input == 3:
            
            borrow.display()
            id = input("What is the id of your borrowed book order? ")
            new_book.display()
            book_id = input("What is the id of your book? ")
            return_date = input("Enter today's date (format YYYY-MM-DD): ")
            
            borrow.return_book(id, book_id, return_date)
            
        elif inner_input == 4:
            title = input("Title of the book you want to find: ")
            new_book.find_book(title)
        
        elif inner_input == 5:
            print("Here is the current library collection")
            new_book.display()
            
    elif user_input == 2:
        menu.print_user_op()
        inner_input = error_handle.valid_input()
        
        if inner_input == 1:
      
            name = input("What is the name of the user you want to add? ")
            id = input("What is the library ID? ")
            lib_user.add_user(name, id)
            
        elif inner_input == 2:
            name = input("What is the name of the user you want to view? ")
            lib_user.display_detail(name)
            
        elif inner_input == 3:
            print("Here are all the library users")
            lib_user.display()
            
    elif user_input == 3:
        menu.print_author_op()
        inner_input = error_handle.valid_input()
        
        if inner_input == 1:
            name = input("What is the name of the author you want to add? ")
            bio = input("Give a brief description of the author? ")
            lib_authors.add_author(name, bio)
            
        elif inner_input == 2:
            name = input("What is the name of the author you want to view? ")
            lib_authors.display_detail(name)
            
        elif inner_input == 3:
            print("Here are all the library authors")
            lib_authors.display()
            
    elif user_input == 4:
        menu.print_genre_op()
        inner_input = error_handle.valid_input()
        genre_list = genre.Genre()
        
        if inner_input == 1:
            name = input("What is the genre you want to add? ")
            descrip = input("Give a brief description of the genre? ")
            category = input("What is the category of the genre? ")
            genre_list.add_genre(name, descrip, category)
            
        elif inner_input == 2:
            name = input("What is the genre you want to view? ")
            genre_list.display_detail(name)
            
        elif inner_input == 3:
            print("Here are all the library genres")
            genre_list.display()
            

    menu.print_main_menu()           
    user_input = error_handle.main_menu_valid_input()
    
print("Thank you for visiting the library!")


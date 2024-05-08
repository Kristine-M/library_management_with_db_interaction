from connect_mysql import connect_database

class Borrow_Book():
    
    
    def __init__(self):
        self.user_id = "Empty"
        self.book_id = "Empty"
        self.borrow_date = "Empty"
        self.return_date = "Empty"
        
    def check_avail(self, book_id):
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor()
                
                to_find = (book_id, ) #book info
                
                query = "SELECT * FROM books WHERE id = %s AND availability = 1"
                #rule ^ for action on the table
                
                cursor.execute(query, to_find) #executes the rule with the book info
                # conn.commit()
                
                found = cursor.fetchall() #list of matched data
                
                if found:
                    print("Book is available to borrow")
                    
                    return True
                else:
                    print("Book is currently borrowed")
                    return False
                
            except Exception as e:
                print(f"Error: {e}") #prints errors
                return None
            
            finally:
                cursor.close()
                conn.close()
                
        
    def borrow_book(self, user_id, book_id, borrow_date):
        
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor()
                
                update_status = (user_id, book_id, borrow_date) #status info
                
                query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
                #rule ^ for action on the table
                
                cursor.execute(query, update_status) #executes the rule with the status info
                conn.commit()
                
                book = (book_id,)
                query = "UPDATE books SET availability = 0 WHERE id = %s"
                #rule ^ for action on the table
                
                cursor.execute(query, book) #executes the rule with the new status info
                conn.commit()
                print("You borrowed a book!")
                return conn
                
            except Exception as e:
                print(f"Error: {e}") #prints errors
                return None
            
            finally:
                cursor.close()
                conn.close()
                
                
    def return_book(self, id, book_id, return_date):
        
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor()
                
                update_status = (return_date, id) #new status info
                
                query = "UPDATE borrowed_books SET return_date = %s WHERE id = %s"
                #rule ^ for action on the table
                
                cursor.execute(query, update_status) #executes the rule with the new status info
                conn.commit()
                
                book = (book_id,)
                query = "UPDATE books SET availability = 1 WHERE id = %s"
                #rule ^ for action on the table
                
                cursor.execute(query, book) #executes the rule with the new status info
                conn.commit()
                print("You borrowed a book!")
                return conn
                
            except Exception as e:
                print(f"Error: {e}") #prints errors
                return None
            
            finally:
                cursor.close()
                conn.close()
                
    def display(self):
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor() #look through the table
                
                query = "SELECT * FROM borrowed_book" #rule
                
                cursor.execute(query) #goes and look through the table with the rule
                
                for row in cursor.fetchall(): #prints the found data
                    print(row)
                    
            finally:
                cursor.close()
                conn.close()
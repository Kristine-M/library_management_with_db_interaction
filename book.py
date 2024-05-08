from connect_mysql import connect_database

class Book():
    
    
    def __init__(self):
        self.__title = "Empty"
        self.__author = "Empty"
        self.__isbn = "Empty"
        self.__pub_date = "Empty"
        self.__genre = "Empty"
        self.__avail = 1
    
    def set_title(self, title):
        
        self.__title = title
    
    def set_author(self, author):
        
        self.__author = author
    
    def set_title(self, title):
        
        self.__title = title
    
    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    def set_pub_date(self, date):
        self.__pub_date = date
        
    def set_genre(self, genre):
        self.__genre = genre
        
    def get_title(self):
        
        return self.__title
    
    def get_author(self):
        
        return self.__author
    
    def get_genre(self):
        
        return self.__genre
    
    def get_isbn(self):
        
        return self.__isbn
    
    def get_date(self):
        
        return self.__pub_date
    
    def get_avail(self):
        return self.__avail
    
    def add_book(self, title, author_id, genre_id, isbn, publication_date, availability):
        
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor()
                
                new_book = (title, author_id, genre_id, isbn, publication_date, availability) #new member info
                
                query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"
                #rule ^ for action on the table
                
                cursor.execute(query, new_book) #executes the rule with the new book info
                conn.commit()
                
                print("New book added")
                return conn
                
            except Exception as e:
                print(f"Error: {e}") #prints errors
                return None
            
            finally:
                cursor.close()
                conn.close()
                
    def find_book(self, title):
        
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor()
                
                to_find = (title, ) #book info
                
                query = "SELECT * FROM books WHERE title = %s"
                #rule ^ for action on the table
                
                cursor.execute(query, to_find) #executes the rule with the new book info
                # conn.commit()
                
                found = cursor.fetchall() #list of matched data
                
                if found:
                    print("Book found")
                    for row in found: #prints the found data
                        print(row)
                    return conn
                else:
                    print("Book not found")
                
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
                
                query = "SELECT * FROM books" #rule
                
                cursor.execute(query) #goes and look through the table with the rule
                
                for row in cursor.fetchall(): #prints the found data
                    print(row)
                    
            finally:
                cursor.close()
                conn.close()
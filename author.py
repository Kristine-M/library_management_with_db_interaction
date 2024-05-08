from connect_mysql import connect_database

class Author:
    
    def __init__(self):
        self.name = "Empty"
        self.biography = "Empty"
    
    def add_author(self, author_to_add, bio):
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor()
                
                new_author = (author_to_add, bio) #new member info
                
                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
                #rule ^ for action on the table
                
                cursor.execute(query, new_author) #executes the rule with the new member info
                conn.commit()
                
                print("New author added")
                return conn
                
            except Exception as e:
                print(f"Error: {e}") #prints errors
                return None
            
            finally:
                cursor.close()
                conn.close()
        
        # if author_to_add in self.authors:
        #     print("Author already added")
        # else:
        #     self.authors[author_to_add] = bio
    
    def display_detail(self, name):
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor() #look through the table
                
                author_detail = (name,)
                query = "SELECT * FROM authors WHERE name = %s" #rule
                
                cursor.execute(query, author_detail) #goes and look through the table with the rule
                
                for row in cursor.fetchall(): #prints the found data
                    print(row)
                    
            finally:
                cursor.close()
                conn.close()
        # if name not in self.authors:
        #     print("This author is not in the added in the library database yet")
        # else:
        #     print(self.authors[name])
        
    def display(self):
        
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor() #look through the table
                
                query = "SELECT * FROM authors" #rule
                
                cursor.execute(query) #goes and look through the table with the rule
                
                for row in cursor.fetchall(): #prints the found data
                    print(row)
                    
            finally:
                cursor.close()
                conn.close()
        # print(self.authors)
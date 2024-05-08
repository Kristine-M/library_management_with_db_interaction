from connect_mysql import connect_database

class Genre:
    
    def __init__(self):
        self.name = "Empty"
        self.description = "Empty"
        self.category = "Empty"
    
    def add_genre(self, genre_to_add, description, category):
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor()
                
                new_genre = (genre_to_add, description, category) #new member info
                
                query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
                #rule ^ for action on the table
                
                cursor.execute(query, new_genre) #executes the rule with the new member info
                conn.commit()
                
                print("New genre added")
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
                
                genre_detail = (name,)
                query = "SELECT * FROM genres WHERE name = %s" #rule
                
                cursor.execute(query, genre_detail) #goes and look through the table with the rule
                
                found = cursor.fetchall()
                
                if found:
                    for row in cursor.fetchall(): #prints the found data
                        print(row)
                else:
                    print("No genre data")
                    
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
                
                query = "SELECT * FROM genres" #rule
                
                cursor.execute(query) #goes and look through the table with the rule
                
                for row in cursor.fetchall(): #prints the found data
                    print(row)
                    
            finally:
                cursor.close()
                conn.close()
        # print(self.authors)
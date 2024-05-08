from connect_mysql import connect_database

class User:
    
    def __init__(self):
        self.name = "Empty"
        self.library_id = "Empty"
        
    
    def add_user(self, name, library_id):
        conn = connect_database()
        if conn is not None:
            try: 
                cursor = conn.cursor()
                
                new_user = (name, library_id) #new member info
                
                query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
                #rule ^ for action on the table
                
                cursor.execute(query, new_user) #executes the rule with the new member info
                conn.commit()
                
                print("New user added")
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
                
                user_detail = (name,)
                query = "SELECT * FROM users WHERE name = %s" #rule
                
                cursor.execute(query, user_detail) #goes and look through the table with the rule
                
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
                
                query = "SELECT * FROM users" #rule
                
                cursor.execute(query) #goes and look through the table with the rule
                found = cursor.fetchall()
                
                if found:
                    for row in cursor.fetchall(): #prints the found data
                        print(row)
                else:
                    print("No user data")
                
                    
            finally:
                cursor.close()
                conn.close()
        # print(self.authors)
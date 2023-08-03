import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("p3.db")
        self.cursor = self.connection.cursor()
        self.create_user()

    def create_user(self):
        self.cursor.execute("""
            create table if not exists user(
                id integer primary key,
                name varchar ,
                age integer ,
                phone_number varchar ,
                email varchar,
                photo varchar 
            )
        """)
        self.connection.commit()

    def add_user(self, name, age, phone_number, email, photo):
        self.cursor.execute("""
            insert into user (name, age, phone_number, email, photo)
            values (?, ?, ?, ?, ?)
        """, (name, age, phone_number, email, photo))
        self.connection.commit()

    def all_user(self):
        self.cursor.execute(f"""
            SELECT * from user
        """)
        return self.cursor.fetchall()


    def get_user(self, id):
        self.cursor.execute("""
            select * from user where id=?
        """, (id,))
        return self.cursor.fetchone()

    # def update_user(self, id, name, age, phone_number, email, photo):
    #     self.cursor.execute("""
    #         update user set name=?, age=?, phone_number=?, email=?, photo=?
    #         where id=?
    #     """, (name, age, phone_number, email, photo, id))
    #     self.connection.commit()

    def update_user_name(self, id, name):
        self.cursor.execute("""
            update user set name=? where id=?
        """, (name, id))
        self.connection.commit()

    def update_user_age(self, id, age):
        self.cursor.execute("""
            update user set age=? where id=?
        """, (age, id))
        self.connection.commit()

    def update_user_phone(self, id, phone_number):
        self.cursor.execute("""
            update user set phone_number=? where id=?
        """, (phone_number, id))
        self.connection.commit()

    def update_user_email(self, id, email):
        self.cursor.execute("""
            update user set email=? where id=?
        """, (email, id))
        self.connection.commit()

    def update_user_photo(self, id, photo):
        self.cursor.execute("""
            update user set photo=? where id=?
        """, (photo, id))
        self.connection.commit()

    def delete_user(self, id):
        self.cursor.execute("""
            delete from user where id=?
        """, (id,))
        self.connection.commit()




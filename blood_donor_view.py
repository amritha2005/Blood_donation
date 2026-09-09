import mysql.connector
import datetime

class BloodDonorManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Amrithasuku@123",
            database="blood_db"
        )
        print("Connection Successfully")




    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """
                INSERT INTO donor(name, blood_group, phone, city, last_donation)
                VALUES(%s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Donor added Successfully...")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM donor"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for data in records:
                print(data)

        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM donor WHERE donor_id=%s"

            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            if record == None:
                print("Donor not found!")
            else:
                print(record)

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM donor WHERE donor_id=%s"

            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            if record != None:

                query = "DELETE FROM donor WHERE donor_id=%s"

                self.cursor.execute(query, values)

                self.connection.commit()

                print("Donor deleted Successfully...!")

            else:
                print("Donor not found")

        except Exception as e:
            print(e)

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM donor WHERE donor_id=%s"

            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            return record

        except Exception as e:
            return None
    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id=id)        #check whether the record exists
            if record != None:                     #if a record is found, record will not be none
                self.cursor = self.connection.cursor()
                placeholder = ""                   # creates an empty string
                # this variable will be used to construct the SET part of the SQL query
                for k in kwargs:
                    placeholder += k + "=%s ,"     #Build the SET condition
                    # SET name ="%s",city="%s",blood_group="%s"..etc
                    placeholder = placeholder.rstrip(" , ")    # Removes the last comma
                    query = f"update donor set {placeholder} where id = %s"
                    values = [v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Donor details updated successfully")
                else:
                    print("donor not found")
        except Exception as e:
            print(e)




donor_instance = BloodDonorManager()

# donor_instance.post(
#     name="Anu",
#     blood_group="AB-",
#     phone="987555550",
#     city="Alappuzha",
#     last_donation=datetime.datetime.today()
# )

# donor_instance.get()

# donor_instance.retrieve(id=1)

donor_instance.delete(id=3)

donor_instance.get()
# donor_instance.put(id=1)
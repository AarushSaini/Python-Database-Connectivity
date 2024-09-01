import mysql.connector

def connect_to_database(config):
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            return connection
        else:
            print("Error connecting to the database.")
            return None
    except mysql.connector.Error as e:
        print("Error connecting to the database: ", str(e))
        return None

def insert_record(connection):
    try:
        Id = int(input("Enter Player ID: "))
        name = input("Enter Player Name: ")
        salary = float(input("Enter Player Salary: "))
        teamname = input("Enter Team Name: ")
        sport = input("Enter the Player Sport: ")
        orgname = input("Enter the Organization Name: ")

        sql = "INSERT INTO Player(Id, name, salary, teamname, sport, orgname) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (Id, name, salary, teamname, sport, orgname)

        with connection.cursor() as cursor:
            cursor.execute(sql, values)
            connection.commit()

        print("\nRecord inserted successfully!")
    except ValueError:
        print("Invalid input. Please enter the correct data types.")
    except Exception as e:
        print("Error inserting record: ", str(e))

def display_records(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Player")
            records = cursor.fetchall()

        if records:
            print("\nPlayer Records:")
            for record in records:
                print(record)
        else:
            print("\nNo records found in the 'Player' table.")
    except Exception as e:
        print("Error fetching records: ", str(e))

def search_record(connection):
    try:
        Id = int(input("Enter Player ID to search: "))
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Player WHERE Id = %s", (Id,))
            record = cursor.fetchone()

        if record:
            print("\nPlayer Record:")
            print(record)
        else:
            print(f"\nNo record found with Player ID {Id}")
    except ValueError:
        print("Invalid input. Please enter a valid Player ID.")
    except Exception as e:
        print(f"Error searching record: {str(e)}")

def update_record(connection):
    try:
        Id = int(input("Enter Player ID to update: "))
        salary = float(input("Enter updated Player Salary: "))
        with connection.cursor() as cursor:
            cursor.execute("UPDATE Player SET salary = %s WHERE Id = %s", (salary, Id))
            connection.commit()

        if cursor.rowcount > 0:
            print("\nRecord updated successfully!")
        else:
            print(f"No record found with Player ID {Id}")
    except ValueError:
        print("Invalid input. Please enter valid data types.")
    except Exception as e:
        print("Error updating record: ", str(e))

def delete_record(connection):
    try:
        Id = int(input("Enter Player ID to delete: "))
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Player WHERE Id = %s", (Id,))
            connection.commit()

        if cursor.rowcount > 0:
            print("\nRecord deleted successfully!")
        else:
            print(f"\nNo record found with Player ID {Id}")
    except ValueError:
        print("Invalid input. Please enter a valid Player ID.")
    except Exception as e:
        print("Error deleting record: ", str(e))

def main():
    config = {
        "host": "localhost",
        "user": "root",
        "password": "PASSWORD",
        "database": "DATABASE NAME"
    }

    connection = connect_to_database(config)
    if connection:
        try:
            while True:
                print('-' * 80)
                print("1. Insert Record")
                print("2. Display Records")
                print("3. Search Record")
                print("4. Update Record")
                print("5. Delete Record")
                print("6. Exit \n")

                choice = input("Enter your choice (1-6): ")
                print(" ")

                if choice == "1":
                    insert_record(connection)

                elif choice == "2":
                    display_records(connection)

                elif choice == "3":
                    search_record(connection)

                elif choice == "4":
                    update_record(connection)

                elif choice == "5":
                    delete_record(connection)

                elif choice == "6":
                    print("Exiting the program.")
                    break

                else:
                    print("Invalid choice. Please select a valid option.")

        finally:
            connection.close()

if __name__ == "__main__":
    main()

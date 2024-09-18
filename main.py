import sqlite3
import csv
connection = sqlite3.connect('quizdata1.db')
cursor = connection.cursor()

insert_query = """
INSERT INTO people (first_name, last_name, state_code, shirt_or_hat, age, quiz_points, city, team)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);
"""

new_person = ("Walter", "John", "NY", "hat", "30", "93", "Buffalo",  "Baffled Badgers")

cursor.execute(insert_query, new_person)
connection.commit()

query = """
    SELECT * FROM people;
    """


cursor.execute(query)
results = cursor.fetchall()

csv_file = 'people_data.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    column_names = [description[0] for description in cursor.description]
    writer.writerow(column_names)
    
    writer.writerows(results)
    
print(f"People data saved to {csv_file}")

# for row in results:
#     print(row)
    
connection.close()
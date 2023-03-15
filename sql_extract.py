import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# Select the password values from the auth_user table
c.execute('SELECT password FROM auth_user')

# Write the passwords to a file in John the Ripper format
with open('passwords.txt', 'w') as f:
    for row in c.fetchall():
        password = row[0]
        f.write(password + '\n')

# Close the database connection
conn.close()
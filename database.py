import sqlite3 as sql

conn = sql.connect('customer.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMER(identity integer, password text, balance real)")

conn.commit()
conn.close()

def insert(identity, password, balance):
    conn = sql.connect('customer.db')
    cursor = conn.cursor()

    add_command = "INSERT INTO CUSTOMER VALUES {}"
    data = (identity, password, balance)
    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()

def search_customer(identity, password):
    conn = sql.connect('customer.db')
    cursor = conn.cursor()
    search_command = "SELECT * FROM CUSTOMER WHERE identity = '{}' AND password = '{}'"
    cursor.execute(search_command.format(identity, password))

    customer = cursor.fetchone()
    conn.close()

    return customer

def balance_inquiry(identity):
    conn = sql.connect('customer.db')
    cursor = conn.cursor()

    inquiry_command = "SELECT balance FROM CUSTOMER WHERE identity = '{}'"
    cursor.execute(inquiry_command.format(identity))

    balance = cursor.fetchone()
    conn.close()

    return balance

def add_balance(amount, identity):
    conn = sql.connect('customer.db')
    cursor = conn.cursor()

    add_balance_command = "UPDATE CUSTOMER SET balance = balance + ? WHERE identity = ?"
    cursor.execute(add_balance_command, (amount, identity))

    conn.commit()
    conn.close()

def reduce_balance(amount, identity):
    conn = sql.connect('customer.db')
    cursor = conn.cursor()

    red_balance_command = "UPDATE CUSTOMER SET balance = balance - ? WHERE identity = ?"
    cursor.execute(red_balance_command, (amount, identity))

    conn.commit()
    conn.close()

def send_money(sender_identity, receiver_identity, amount):
    conn = sql.connect('customer.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE CUSTOMER SET balance = balance - ? WHERE identity = ?", (amount, sender_identity))
    cursor.execute("UPDATE CUSTOMER SET balance = balance + ? WHERE identity = ?", (amount, receiver_identity))

    conn.commit()
    conn.close()

def search_customer_for_sending(identity):
    conn = sql.connect('customer.db')
    cursor = conn.cursor()

    search_command = "SELECT * FROM CUSTOMER WHERE identity = '{}'"
    cursor.execute(search_command.format(identity))

    customer = cursor.fetchone()
    conn.close()

    return customer

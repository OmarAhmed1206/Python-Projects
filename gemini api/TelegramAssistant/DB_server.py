import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=TelegramAssistant;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()

print("DB Connected")


def create_users(telegram_id, first_name, username):
    cursor.execute("""
        INSERT INTO Users
        (TelegramID, FirstName, UserName)
        VALUES (?, ?, ?)
    """, telegram_id, first_name, username)
    connection.commit()


def get_users(telegram_id):
    cursor.execute("""
        SELECT *
        FROM Users
        WHERE TelegramID = ?
    """, telegram_id)
    return cursor.fetchone()


def add_message(user_id, role, message):
    cursor.execute("""
        INSERT INTO Conversations
        (UserID, Role_, Message_)
        VALUES (?, ?, ?)
    """, user_id, role, message)
    connection.commit()


def get_history(user_id):
    cursor.execute("""
        SELECT TOP (100)
            Role_, Message_
        FROM Conversations
        WHERE UserID = ?
        ORDER BY ConversationID DESC
    """, user_id)

    rows = cursor.fetchall()
    return list(reversed(rows))


def clear_history(user_id):
    cursor.execute("""
        DELETE FROM Conversations
        WHERE UserID = ?
    """, user_id)
    connection.commit()
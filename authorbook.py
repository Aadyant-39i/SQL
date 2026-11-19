import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')

conn.execute("""CREATE TABLE author (
    author_id   INTEGER PRIMARY KEY,
    author_name TEXT NOT NULL UNIQUE
)""")

conn.execute("""CREATE TABLE book (
    book_id    INTEGER PRIMARY KEY,
    book_title TEXT NOT NULL,
    author_id  INTEGER
)""")

conn.executemany("INSERT INTO author VALUES (?, ?)", [
    (1, 'Roald Dahl'), (2, 'J.K. Rowling'),
    (3, 'Rick Riordan'), (4, 'Jeff Kinney'),
    (5, 'Dav Pilkey'), (6, 'Lemony Snicket'),
])

conn.executemany("INSERT INTO book VALUES (?, ?, ?)", [
    (1, 'Charlie and the Chocolate Factory', 1),
    (2, 'James and the Giant Peach', 1),
    (3, 'Harry Potter and the Philosopher\'s Stone', 2),
    (4, 'Harry Potter and the Chamber of Secrets', 2),
    (5, 'Lightning Thief', 3),
    (6, 'The Sea of Monsters', 3),
    (7, 'Diary of a Wimpy Kid', 4),
    (8, 'Diary of a Wimpy Kid: Fight or Flight', 4),
    (9, 'Dog Man: The Scarlet Shredder', 5),
    (10, 'Captain Underpants and the Perilous Plot of Professor Poopypants', 5)
])
conn.commit()
authors = pd.read_sql("SELECT * FROM author", conn)
books = pd.read_sql("SELECT * FROM book", conn)
print(authors)
print(books)

inner = pd.read_sql("SELECT author.author_name, book.book_title "
                    "FROM author INNER JOIN book ON author.author_id = book.author_id",
                    conn)
print("INNER JOIN - authors matched with their books: ")
print(inner)
print()

left = pd.read_sql("SELECT author.author_name, book.book_title"
                   "FROM authorLEFT JOIN book ON author.author_id = book.author_id",
                   conn)
print("LEFT JOIN - all authors, null for authors with no books: ")
print(left)
print()

cross = pd.read_sql("SELECT author.author_name, book.book_title "
                    "FROM author CROSS JOIN book WHERE author.author_id <= 2",
                    conn)
print("CROSS JOIN - First two authors paired with every book: ")
print(cross)
print()

union = pd.read_sql("SELECT author_name AS name, 'Author' AS type FROM author"
                    "UNION"
                    "SELECT book_title AS name, 'Book' AS type FROM book",
                    conn)
print("UNION - all author names and book titles combined: ")
print(union)
print()


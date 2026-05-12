import json
import os
from CompiledFiles.libraryVisitor import libraryVisitor

BOOKS_FILE = os.path.join(os.path.dirname(__file__), 'books.json')
USERS_FILE = os.path.join(os.path.dirname(__file__), 'users.json')


def load_books():
    with open(BOOKS_FILE, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=4)

def load_users():
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)


class LibraryVisitor(libraryVisitor):

    def __init__(self):
        self.error = None
        self.current_user = None
        self.current_role = None

    # ── guards ──────────────────────────────────────────────────────

    def _require_login(self):
        if not self.current_user:
            self.error = "You must be logged in. Use: login <username> <password>"
            return False
        return True

    def _require_admin(self):
        if not self._require_login():
            return False
        if self.current_role != 'admin':
            self.error = "Admin privileges required for this command."
            return False
        return True

    def _find_book(self, books, book_id):
        book_id = book_id.upper()
        for b in books:
            if b['id'].upper() == book_id:
                return b
        return None

    # ── program ─────────────────────────────────────────────────────

    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitTitlePhrase(self, ctx):
        return ' '.join(w.getText() for w in ctx.WORD())

    # ── register ────────────────────────────────────────────────────

    def visitRegisterUser(self, ctx):
        words = ctx.WORD()
        username = words[0].getText()
        password = words[1].getText()
        users = load_users()
        if username in users:
            self.error = f"Username '{username}' is already taken."
            return None
        users[username] = {"password": password, "role": "user", "borrowed": []}
        save_users(users)
        return f"✅ Registered! Welcome, {username}. You can now login."

    # ── login ───────────────────────────────────────────────────────

    def visitLoginUser(self, ctx):
        words = ctx.WORD()
        username = words[0].getText()
        password = words[1].getText()
        users = load_users()
        if username not in users:
            self.error = f"User '{username}' not found."
            return None
        if users[username]['password'] != password:
            self.error = "Incorrect password."
            return None
        self.current_user = username
        self.current_role = users[username]['role']
        tag = " [ADMIN]" if self.current_role == 'admin' else ""
        return f"✅ Logged in as {username}{tag}."

    # ── logout ──────────────────────────────────────────────────────

    def visitLogoutUser(self, ctx):
        if not self.current_user:
            self.error = "You are not currently logged in."
            return None
        name = self.current_user
        self.current_user = None
        self.current_role = None
        return f" Goodbye, {name}. Logged out."

    # ── borrow ──────────────────────────────────────────────────────

    def visitBorrowBook(self, ctx):
        if not self._require_login():
            return None
        book_id = ctx.BOOKID().getText().upper()
        books   = load_books()
        users   = load_users()
        book    = self._find_book(books, book_id)
        if not book:
            self.error = f"Book ID '{book_id}' does not exist."
            return None
        if not book['available']:
            self.error = f"'{book['title']}' is currently borrowed by someone else."
            return None
        user_data = users[self.current_user]
        if book_id in user_data['borrowed']:
            self.error = f"You already have '{book['title']}' borrowed."
            return None
        if len(user_data['borrowed']) >= 3:
            self.error = "Borrow limit reached (max 3 books). Please return a book first."
            return None
        book['available'] = False
        user_data['borrowed'].append(book_id)
        save_books(books)
        save_users(users)
        return f"📖 You borrowed '{book['title']}' by {book['author']}. (ID: {book_id})"

    # ── return ──────────────────────────────────────────────────────

    def visitReturnBook(self, ctx):
        if not self._require_login():
            return None
        book_id   = ctx.BOOKID().getText().upper()
        books     = load_books()
        users     = load_users()
        user_data = users[self.current_user]
        if book_id not in user_data['borrowed']:
            self.error = f"You have not borrowed '{book_id}'."
            return None
        book = self._find_book(books, book_id)
        book['available'] = True
        user_data['borrowed'].remove(book_id)
        save_books(books)
        save_users(users)
        return f"✅ Returned '{book['title']}'. Thank you!"

    # ── list books ──────────────────────────────────────────────────

    def visitListBooks(self, ctx):
        books = load_books()
        if not books:
            return "No books in the library."
        lines = ["📚 Library Catalogue:",
                 f"{'ID':<8} {'Title':<42} {'Author':<25} Status",
                 "-" * 85]
        for b in books:
            status = "Available" if b['available'] else "Borrowed"
            lines.append(f"{b['id']:<8} {b['title']:<42} {b['author']:<25} {status}")
        return "\n".join(lines)

    # ── search ──────────────────────────────────────────────────────

    def visitSearchBook(self, ctx):
        term    = self.visitTitlePhrase(ctx.titlePhrase()).lower()
        books   = load_books()
        results = [b for b in books
                   if term in b['title'].lower() or term in b['author'].lower()]
        if not results:
            return f"No books found matching '{term}'."
        lines = [f"🔍 Results for '{term}':",
                 f"{'ID':<8} {'Title':<42} {'Author':<25} Status",
                 "-" * 85]
        for b in results:
            status = "Available" if b['available'] else "Borrowed"
            lines.append(f"{b['id']:<8} {b['title']:<42} {b['author']:<25} {status}")
        return "\n".join(lines)

    # ── view borrowed ───────────────────────────────────────────────

    def visitViewBorrowed(self, ctx):
        if not self._require_login():
            return None
        users     = load_users()
        books     = load_books()
        borrowed  = users[self.current_user]['borrowed']
        if not borrowed:
            return "You have no books currently borrowed."
        lines = [f" Books borrowed by {self.current_user}:"]
        for bid in borrowed:
            b = self._find_book(books, bid)
            lines.append(f"  • [{bid}] {b['title']} — {b['author']}" if b else f"  • [{bid}]")
        return "\n".join(lines)

    # ── admin: add book ─────────────────────────────────────────────

    def visitAddBook(self, ctx):
        if not self._require_admin():
            return None
        book_id    = ctx.BOOKID().getText().upper()
        raw_phrase = self.visitTitlePhrase(ctx.titlePhrase())
        # Support "Title by Author" pattern
        if ' by ' in raw_phrase:
            parts  = raw_phrase.split(' by ', 1)
            title  = parts[0].strip()
            author = parts[1].strip()
        else:
            title  = raw_phrase.strip()
            author = "Unknown"
        books = load_books()
        if self._find_book(books, book_id):
            self.error = f"Book ID '{book_id}' already exists."
            return None
        books.append({"id": book_id, "title": title, "author": author, "available": True})
        save_books(books)
        return f"✅ Added [{book_id}] '{title}' by {author}."

    # ── admin: remove book ──────────────────────────────────────────

    def visitRemoveBook(self, ctx):
        if not self._require_admin():
            return None
        book_id = ctx.BOOKID().getText().upper()
        books   = load_books()
        book    = self._find_book(books, book_id)
        if not book:
            self.error = f"Book '{book_id}' does not exist."
            return None
        if not book['available']:
            self.error = f"Cannot remove '{book['title']}' — it is currently borrowed."
            return None
        books = [b for b in books if b['id'].upper() != book_id]
        save_books(books)
        return f"  Removed [{book_id}] '{book['title']}'."

    # ── admin: list users ───────────────────────────────────────────

    def visitListUsers(self, ctx):
        if not self._require_admin():
            return None
        users = load_users()
        lines = [" Registered Users:",
                 f"{'Username':<20} {'Role':<10} Borrowed",
                 "-" * 40]
        for uname, data in users.items():
            lines.append(f"{uname:<20} {data['role']:<10} {len(data['borrowed'])}")
        return "\n".join(lines)

    # ── admin: view user ────────────────────────────────────────────

    def visitViewUser(self, ctx):
        if not self._require_admin():
            return None
        username = ctx.WORD().getText()
        users    = load_users()
        if username not in users:
            self.error = f"User '{username}' not found."
            return None
        data  = users[username]
        books = load_books()
        lines = [f" User: {username}",
                 f"   Role    : {data['role']}",
                 f"   Borrowed: {len(data['borrowed'])} book(s)"]
        for bid in data['borrowed']:
            b = self._find_book(books, bid)
            lines.append(f"     • [{bid}] {b['title']}" if b else f"     • [{bid}]")
        return "\n".join(lines)

# ── AI smart search ─────────────────────────────────────────────

    def ai_search_books(self, query):
        books = load_books()
        q = query.lower()

        results = []

        for b in books:
            title = str(b.get('title', '')).lower()
            author = str(b.get('author', '')).lower()
            topic = str(b.get('topic', '')).lower()
            publisher = str(b.get('publisher', '')).lower()
            year = str(b.get('year', '')).lower()

            score = 0

            if q in title:
                score += 5

            if q in author:
                score += 5

            if q in topic:
                score += 4

            if q in publisher:
                score += 3

            if q in year:
                score += 2

            # keyword matching
            words = q.split()

            for word in words:
                if word in title:
                    score += 2
                if word in author:
                    score += 2
                if word in topic:
                    score += 1
                if word in publisher:
                    score += 1
                if word in year:
                    score += 1

            if score > 0:
                results.append((score, b))

        results.sort(reverse=True, key=lambda x: x[0])

        if not results:
            return f"AI Assistant: No books found for '{query}'."

        lines = [f"AI Assistant Results for '{query}':", ""]

        for score, b in results:
            status = "Available" if b['available'] else "Borrowed"

            lines.append(
                f"[{b['id']}] {b['title']}\n"
                f"  Author: {b['author']}\n"
                f"  Topic: {b.get('topic', 'Unknown')}\n"
                f"  Publisher: {b.get('publisher', 'Unknown')}\n"
                f"  Year: {b.get('year', 'Unknown')}\n"
                f"  Status: {status}\n"
            )

        return "\n".join(lines)

    # ── help ────────────────────────────────────────────────────────

    def visitHelpCmd(self, ctx):
        return (
            "╔══════════════════════════════════════════════════════════╗\n"
            "║              LIBRARY SYSTEM — COMMAND HELP               ║\n"
            "╠══════════════════════════════════════════════════════════╣\n"
            "║  USER COMMANDS                                           ║\n"
            "║  register <username> <password>  — Create an account     ║\n"
            "║  login    <username> <password>  — Log in                ║\n"
            "║  logout                          — Log out               ║\n"
            "║  list books                      — Show all books        ║\n"
            "║  search <term or title words>    — Search title/author   ║\n"
            "║  borrow <BookID>                 — Borrow a book (max 3) ║\n"
            "║  return <BookID>                 — Return a book         ║\n"
            "║  view borrowed                   — Your borrowed books   ║\n"
            "╠══════════════════════════════════════════════════════════╣\n"
            "║  ADMIN COMMANDS (login: admin / admin123)                ║\n"
            "║  add <BookID> <Title by Author>  — Add a new book        ║\n"
            "║  remove <BookID>                 — Remove a book         ║\n"
            "║  list users                      — Show all users        ║\n"
            "║  view <username>                 — View user details     ║\n"
            "╚══════════════════════════════════════════════════════════╝"
        )

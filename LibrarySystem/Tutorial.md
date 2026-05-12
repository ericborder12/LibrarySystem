# Library Management System — Tutorial

## Overview
A chatbox-style Library Management System built with ANTLR4 + Python + Tkinter.
Evolved from the PPL shopping-cart project — same architecture, new domain.

## Project Structure
```
LibrarySystem/
├── library.g4          ← ANTLR4 grammar (the language spec)
├── library.py          ← Main entry point (gen / run / gui)
├── library_gui.py      ← Tkinter GUI
├── handle_input.py     ← Parse + dispatch one command string
├── LibraryVisitor.py   ← All business logic (visitor pattern)
├── books.json          ← Book catalogue (persistent)
├── users.json          ← User accounts (persistent)
└── CompiledFiles/      ← ANTLR-generated lexer/parser (Python)
    ├── libraryLexer.py
    ├── libraryParser.py
    └── libraryVisitor.py
```

## Setup

### 1. Install Python dependencies
```
pip install antlr4-python3-runtime==4.11
```
> Match the runtime version to your ANTLR jar version.

### 2. Compile the grammar (only needed if you modify library.g4)
Edit the `ANTLR_JAR` path in `library.py` to point to your jar, then:
```
python library.py gen
```

### 3. Run

**GUI mode (recommended):**
```
python library.py gui
```

**CLI mode:**
```
python library.py run
```

---

## Commands Reference

### User Commands
| Command | Description |
|---|---|
| `register <username> <password>` | Create a new user account |
| `login <username> <password>` | Log in |
| `logout` | Log out |
| `list books` | Show full catalogue with availability |
| `search <words>` | Search by title or author keywords |
| `borrow <BookID>` | Borrow a book (max 3 at a time) |
| `return <BookID>` | Return a borrowed book |
| `view borrowed` | See all books you have borrowed |
| `help` | Show command reference |

### Admin Commands (login: admin / admin123)
| Command | Description |
|---|---|
| `add <BookID> <Title by Author>` | Add a new book to catalogue |
| `remove <BookID>` | Remove a book (only if not borrowed) |
| `list users` | Show all registered users |
| `view <username>` | See a user's borrowed books |

### Book ID Format
Book IDs start with `B` followed by digits, e.g. `B001`, `B012`, `B099`.

---

## Example Session

```
[guest]>> register alice mypassword
✅ Registered! Welcome, alice. You can now login.

[guest]>> login alice mypassword
✅ Logged in as alice.

[alice]>> list books
📚 Library Catalogue:
ID       Title                          Author                    Status
...

[alice]>> borrow B003
📖 You borrowed 'Introduction to Algorithms' by Thomas H. Cormen. (ID: B003)

[alice]>> view borrowed
📋 Books borrowed by alice:
  • [B003] Introduction to Algorithms — Thomas H. Cormen

[alice]>> return B003
✅ Returned 'Introduction to Algorithms'. Thank you!

[alice]>> logout
👋 Goodbye, alice. Logged out.

[guest]>> login admin admin123
✅ Logged in as admin [ADMIN].

[admin]>> add B099 Deep Learning by Ian Goodfellow
✅ Added [B099] 'Deep Learning' by Ian Goodfellow.

[admin]>> list users
👥 Registered Users:
Username             Role       Borrowed
admin                admin      0
alice                user       0

[admin]>> view alice
👤 User: alice
   Role    : user
   Borrowed: 0 book(s)
```

---

## Grammar Design (library.g4)

The ANTLR4 grammar uses **labeled alternatives** for clean visitor dispatch:

```antlr
command
    : REGISTER WORD WORD    # registerUser
    | LOGIN    WORD WORD    # loginUser
    | LOGOUT                # logoutUser
    | BORROW   BOOKID       # borrowBook
    | ...
    ;

BOOKID : [Bb][0-9]+ ;
WORD   : [a-zA-Z0-9!@#$%^&*_\-]+ ;
```

Keywords are defined before `WORD` so ANTLR's longest-match rule
ensures `login` is a LOGIN token, not a WORD.

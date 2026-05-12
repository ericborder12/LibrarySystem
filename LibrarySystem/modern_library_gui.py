import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from LibraryVisitor import LibraryVisitor
from library import handle_input
from helpers import load_books


# ============================================================
# Modern Library GUI
# ============================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ModernLibraryGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI Library Management System")
        self.geometry("1400x800")
        self.minsize(1200, 700)

        self.visitor = LibraryVisitor()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._build_sidebar()
        self._build_main_area()
        self._load_books()

    # ========================================================
    # Sidebar
    # ========================================================

    def _build_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(10, weight=1)

        title = ctk.CTkLabel(
            self.sidebar,
            text="📚 Library System",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(pady=(30, 20))

        buttons = [
            ("📖 All Books", self._load_books),
            ("🔍 Search", self.focus_search),
            ("📥 Borrow", self.borrow_selected),
            ("📤 Return", self.return_selected),
            ("🤖 AI Assistant", self.focus_ai),
            ("🔄 Refresh", self._load_books),
        ]

        for text, command in buttons:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                command=command,
                height=45,
                font=("Segoe UI", 15)
            )
            btn.pack(fill="x", padx=20, pady=8)

        footer = ctk.CTkLabel(
            self.sidebar,
            text="Modern UI Redesign",
            font=("Segoe UI", 12),
            text_color="gray"
        )
        footer.pack(side="bottom", pady=20)

    # ========================================================
    # Main Area
    # ========================================================

    def _build_main_area(self):
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nswe")

        self.main_frame.grid_columnconfigure(0, weight=3)
        self.main_frame.grid_columnconfigure(1, weight=2)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self.main_frame, height=90)
        header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=20)
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text="Library Dashboard",
            font=("Segoe UI", 30, "bold")
        )
        title.grid(row=0, column=0, sticky="w", padx=20, pady=20)

        # Search section
        left_panel = ctk.CTkFrame(self.main_frame)
        left_panel.grid(row=1, column=0, sticky="nswe", padx=(20, 10), pady=(0, 20))

        search_frame = ctk.CTkFrame(left_panel)
        search_frame.pack(fill="x", padx=20, pady=20)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Search by title, author, topic, year, publisher...",
            height=45,
            font=("Segoe UI", 15)
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(10, 10), pady=10)
        self.search_entry.bind("<Return>", lambda e: self.search_books())

        search_btn = ctk.CTkButton(
            search_frame,
            text="Search",
            width=120,
            height=45,
            command=self.search_books
        )
        search_btn.pack(side="right", padx=(0, 10), pady=10)

        # Table
        table_frame = ctk.CTkFrame(left_panel)
        table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        columns = (
            "ID",
            "Title",
            "Author",
            "Topic",
            "Publisher",
            "Year",
            "Status"
        )

        self.book_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=20
        )

        for col in columns:
            self.book_table.heading(col, text=col)
            self.book_table.column(col, anchor="center", width=120)

        self.book_table.column("Title", width=250)
        self.book_table.column("Author", width=180)
        self.book_table.column("Topic", width=200)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.book_table.yview)
        self.book_table.configure(yscrollcommand=scrollbar.set)

        self.book_table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Right panel
        right_panel = ctk.CTkFrame(self.main_frame)
        right_panel.grid(row=1, column=1, sticky="nswe", padx=(10, 20), pady=(0, 20))

        # AI Assistant
        ai_title = ctk.CTkLabel(
            right_panel,
            text="🤖 AI Assistant",
            font=("Segoe UI", 24, "bold")
        )
        ai_title.pack(anchor="w", padx=20, pady=(20, 10))

        self.chat_box = ctk.CTkTextbox(
            right_panel,
            height=450,
            font=("Consolas", 14)
        )
        self.chat_box.pack(fill="both", expand=True, padx=20, pady=10)

        self.chat_box.insert("end", "🤖 Welcome to the AI Library Assistant!\n\n")
        self.chat_box.insert("end", "Try:\n")
        self.chat_box.insert("end", "• fantasy books\n")
        self.chat_box.insert("end", "• books by Tolkien\n")
        self.chat_box.insert("end", "• programming 2008\n")
        self.chat_box.insert("end", "• publisher Pearson\n\n")

        ai_input_frame = ctk.CTkFrame(right_panel)
        ai_input_frame.pack(fill="x", padx=20, pady=(0, 20))

        self.ai_entry = ctk.CTkEntry(
            ai_input_frame,
            placeholder_text="Ask the AI assistant...",
            height=45,
            font=("Segoe UI", 14)
        )
        self.ai_entry.pack(side="left", fill="x", expand=True, padx=(10, 10), pady=10)
        self.ai_entry.bind("<Return>", lambda e: self.ai_search())

        send_btn = ctk.CTkButton(
            ai_input_frame,
            text="Send",
            width=100,
            height=45,
            command=self.ai_search
        )
        send_btn.pack(side="right", padx=(0, 10), pady=10)

    # ========================================================
    # Load Books
    # ========================================================

    def _load_books(self):
        for row in self.book_table.get_children():
            self.book_table.delete(row)

        try:
            books = load_books()

            for book in books:
                status = "Available" if book.get("available", True) else "Borrowed"

                self.book_table.insert(
                    "",
                    "end",
                    values=(
                        book.get("id", "N/A"),
                        book.get("title", "N/A"),
                        book.get("author", "N/A"),
                        book.get("topic", "Unknown"),
                        book.get("publisher", "Unknown"),
                        book.get("year", "Unknown"),
                        status
                    )
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ========================================================
    # Search
    # ========================================================

    def search_books(self):
        query = self.search_entry.get().strip().lower()

        if not query:
            self._load_books()
            return

        for row in self.book_table.get_children():
            self.book_table.delete(row)

        books = load_books()

        for book in books:
            searchable = " ".join([
                str(book.get("title", "")),
                str(book.get("author", "")),
                str(book.get("topic", "")),
                str(book.get("publisher", "")),
                str(book.get("year", ""))
            ]).lower()

            if query in searchable:
                status = "Available" if book.get("available", True) else "Borrowed"

                self.book_table.insert(
                    "",
                    "end",
                    values=(
                        book.get("id", "N/A"),
                        book.get("title", "N/A"),
                        book.get("author", "N/A"),
                        book.get("topic", "Unknown"),
                        book.get("publisher", "Unknown"),
                        book.get("year", "Unknown"),
                        status
                    )
                )

    # ========================================================
    # Borrow Book
    # ========================================================

    def borrow_selected(self):
        selected = self.book_table.selection()

        if not selected:
            messagebox.showwarning("Warning", "Please select a book.")
            return

        item = self.book_table.item(selected[0])
        book_id = item["values"][0]

        command = f"borrow {book_id}"

        try:
            result, error = handle_input(command, self.visitor)

            if error:
                messagebox.showerror("Error", error)
            else:
                messagebox.showinfo("Success", result)
                self._load_books()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ========================================================
    # Return Book
    # ========================================================

    def return_selected(self):
        selected = self.book_table.selection()

        if not selected:
            messagebox.showwarning("Warning", "Please select a book.")
            return

        item = self.book_table.item(selected[0])
        book_id = item["values"][0]

        command = f"return {book_id}"

        try:
            result, error = handle_input(command, self.visitor)

            if error:
                messagebox.showerror("Error", error)
            else:
                messagebox.showinfo("Success", result)
                self._load_books()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ========================================================
    # AI Search
    # ========================================================

    def ai_search(self):
        query = self.ai_entry.get().strip()

        if not query:
            return

        self.chat_box.insert("end", f"🧑 You: {query}\n\n")

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
            self.chat_box.insert(
                "end",
                "🤖 No books found. Try another keyword.\n\n"
            )
        else:
            self.chat_box.insert("end", "🤖 Recommended Books:\n\n")

            for score, b in results[:10]:
                status = "Available" if b.get("available", True) else "Borrowed"

                response = (
                    f"📘 {b.get('title', 'Unknown')}\n"
                    f"Author: {b.get('author', 'Unknown')}\n"
                    f"Topic: {b.get('topic', 'Unknown')}\n"
                    f"Publisher: {b.get('publisher', 'Unknown')}\n"
                    f"Year: {b.get('year', 'Unknown')}\n"
                    f"Status: {status}\n\n"
                )

                self.chat_box.insert("end", response)

        self.chat_box.see("end")
        self.ai_entry.delete(0, "end")

    # ========================================================
    # Helpers
    # ========================================================

    def focus_search(self):
        self.search_entry.focus()

    def focus_ai(self):
        self.ai_entry.focus()


# ============================================================
# Run GUI
# ============================================================

if __name__ == "__main__":
    app = ModernLibraryGUI()
    app.mainloop()

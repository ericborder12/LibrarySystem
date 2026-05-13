import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from LibraryVisitor import LibraryVisitor, load_books
from handle_input import handle_input


# ============================================================
# Modern Library GUI 
# ============================================================

# Use Deep Dark theme for a high-end look
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ModernLibraryGUI(ctk.CTk):
    """
    Main Application class. 
    Redesigned for a professional look while maintaining original backend logic.
    """
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("AI Library Management System")
        self.geometry("1400x800")
        self.minsize(1200, 700)
        self.configure(fg_color="#0f0f12") # Deep dark background

        # Backend Engine Initialization
        self.visitor = LibraryVisitor()
        # Bypass default auth for GUI testing
        self.visitor.current_user = "admin"
        self.visitor.current_role = "admin"

        # Main Layout: Sidebar (fixed) | Workspace (expanding)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Apply flat dark styling to the native Treeview
        self._setup_table_style()

        # Build UI Modules
        self._build_sidebar()
        self._build_main_area()
        self._load_books()

    def _setup_table_style(self):
        """Custom style to make the standard Treeview look modern and dark."""
        style = ttk.Style(self)
        style.theme_use("default")
        
        style.configure("Treeview",
                        background="#1a1a21",
                        foreground="#d1d1d6",
                        rowheight=40,
                        fieldbackground="#1a1a21",
                        borderwidth=0,
                        font=("Segoe UI", 11))
                        
        style.map('Treeview', background=[('selected', '#2563eb')])
        
        style.configure("Treeview.Heading",
                        background="#25252e",
                        foreground="#ffffff",
                        borderwidth=0,
                        font=("Segoe UI", 12, "bold"))
        style.map("Treeview.Heading", background=[('active', '#2f2f3d')])

    # ========================================================
    # Sidebar 
    # ========================================================

    def _build_sidebar(self):
        """Sidebar with navigation only. Borrow/Return moved to main area."""
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0, fg_color="#1a1a21")
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(10, weight=1)

        title = ctk.CTkLabel(
            self.sidebar,
            text="📚 Library Hub",
            font=("Segoe UI", 26, "bold")
        )
        title.pack(pady=(40, 30))
        buttons = [
            ("📖 All Books", self._load_books),
            ("🔍 Search ", self.focus_search),
            ("🤖 AI Assistant", self.focus_ai),
            ("🔄 Refresh Data", self._load_books),
        ]
        for text, command in buttons:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                command=command,
                height=45,
                corner_radius=8,
                font=("Segoe UI", 14, "bold"), # Fixed: Removed "medium"
                fg_color="transparent",
                text_color="#a1a1aa",
                hover_color="#2f2f3d",
                anchor="w"
            )
            btn.pack(fill="x", padx=15, pady=5)
        footer = ctk.CTkLabel(
            self.sidebar,
            text="System Online",
            font=("Segoe UI", 11, "bold"),
            text_color="#4b4b57"
        )
        footer.pack(side="bottom", pady=25)

    # ========================================================
    # Main Area 
    # ========================================================

    def _build_main_area(self):
        """The core dashboard containing search, the book table, and AI chat."""
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nswe")
        self.main_frame.grid_columnconfigure(0, weight=3)
        self.main_frame.grid_columnconfigure(1, weight=2)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header = ctk.CTkFrame(self.main_frame, height=80, fg_color="transparent")
        header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=25, pady=(20, 0))

        title = ctk.CTkLabel(
            header,
            text="Catalog Dashboard",
            font=("Segoe UI", 30, "bold")
        )
        title.pack(side="left", pady=10)

        left_panel = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        left_panel.grid(row=1, column=0, sticky="nswe", padx=(25, 12), pady=(10, 25))

        search_frame = ctk.CTkFrame(left_panel, corner_radius=10, fg_color="#1a1a21")
        search_frame.pack(fill="x", pady=(0, 15))

        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="🔍 Search title, author, topic, year...",
            height=45,
            border_width=0,
            fg_color="transparent",
            font=("Segoe UI", 14)
        )
        self.search_entry.pack(fill="x", expand=True, padx=15, pady=5)
        self.search_entry.bind("<Return>", lambda e: self.search_books())

        table_card = ctk.CTkFrame(left_panel, corner_radius=10, fg_color="#1a1a21")
        table_card.pack(fill="both", expand=True)

        columns = ("ID", "Title", "Author", "Topic", "Publisher", "Year", "Status")
        self.book_table = ttk.Treeview(table_card, columns=columns, show="headings", style="Treeview")

        for col in columns:
            self.book_table.heading(col, text=col)
            self.book_table.column(col, anchor="center", width=100)

        self.book_table.column("ID", width=60, stretch=False)
        self.book_table.column("Title", width=220, anchor="w")
        self.book_table.column("Author", width=140, anchor="w")
        self.book_table.column("Status", width=90, stretch=False)

        scrollbar = ttk.Scrollbar(table_card, orient="vertical", command=self.book_table.yview)
        self.book_table.configure(yscrollcommand=scrollbar.set)

        self.book_table.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)

        action_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
        action_frame.pack(fill="x", pady=(15, 0))

        self.borrow_btn = ctk.CTkButton(
            action_frame,
            text="📥 Borrow Book",
            height=45,
            corner_radius=8,
            fg_color="#059669", 
            hover_color="#047857",
            command=self.borrow_selected,
            font=("Segoe UI", 14, "bold")
        )
        self.borrow_btn.pack(side="left", expand=True, fill="x", padx=(0, 10))

        self.return_btn = ctk.CTkButton(
            action_frame,
            text="📤 Return Book",
            height=45,
            corner_radius=8,
            fg_color="#374151", 
            hover_color="#1f2937",
            command=self.return_selected,
            font=("Segoe UI", 14, "bold")
        )
        self.return_btn.pack(side="left", expand=True, fill="x")

        right_panel = ctk.CTkFrame(self.main_frame, corner_radius=10, fg_color="#1a1a21")
        right_panel.grid(row=1, column=1, sticky="nswe", padx=(12, 25), pady=(10, 25))

        ai_title = ctk.CTkLabel(
            right_panel,
            text="🤖 AI Intelligent Assistant",
            font=("Segoe UI", 22, "bold")
        )
        ai_title.pack(anchor="w", padx=20, pady=(20, 10))

        self.chat_box = ctk.CTkTextbox(
            right_panel,
            font=("Consolas", 13),
            wrap="word",
            fg_color="#0f0f12",
            border_width=0
        )
        self.chat_box.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        self.chat_box.insert("end", "🤖 Engine Status: Ready.\n\n")
        self.chat_box.insert("end", "Try searching contextual keywords like 'fantasy', 'Tolkien', or 'programming'.\n\n")

        ai_input_frame = ctk.CTkFrame(right_panel, fg_color="transparent")
        ai_input_frame.pack(fill="x", padx=20, pady=(0, 20))

        self.ai_entry = ctk.CTkEntry(
            ai_input_frame,
            placeholder_text="Ask logic engine...",
            height=45,
            corner_radius=8,
            fg_color="#0f0f12",
            border_color="#2f2f3d",
            font=("Segoe UI", 13)
        )
        self.ai_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.ai_entry.bind("<Return>", lambda e: self.ai_search())

        send_btn = ctk.CTkButton(
            ai_input_frame,
            text="Send",
            width=70,
            height=45,
            corner_radius=8,
            command=self.ai_search,
            font=("Segoe UI", 13, "bold")
        )
        send_btn.pack(side="right")

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
                self.book_table.insert("", "end", values=(
                    book.get("id", "N/A"), book.get("title", "N/A"), book.get("author", "N/A"),
                    book.get("topic", "Unknown"), book.get("publisher", "Unknown"), book.get("year", "Unknown"), status
                ))
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
            searchable = " ".join([str(book.get(k, "")) for k in ["title", "author", "topic", "publisher", "year"]]).lower()
            if query in searchable:
                status = "Available" if book.get("available", True) else "Borrowed"
                self.book_table.insert("", "end", values=(
                    book.get("id", "N/A"), book.get("title", "N/A"), book.get("author", "N/A"),
                    book.get("topic", "Unknown"), book.get("publisher", "Unknown"), book.get("year", "Unknown"), status
                ))
                
    # ========================================================
    # Borrow Book
    # ========================================================

    def borrow_selected(self):
        selected = self.book_table.selection()
        if not selected:
            messagebox.showwarning("Selection Required", "Please select a book from the table first.")
            return
        book_id = self.book_table.item(selected[0])["values"][0]
        try:
            result, error = handle_input(f"borrow {book_id}", self.visitor)
            if error: messagebox.showerror("Denied", error)
            else: 
                messagebox.showinfo("Success", result)
                self._load_books()
        except Exception as e: messagebox.showerror("System Error", str(e))
        
    # ========================================================
    # Return Book
    # ========================================================
    
    def return_selected(self):
        selected = self.book_table.selection()
        if not selected:
            messagebox.showwarning("Selection Required", "Please select a book from the table first.")
            return
        book_id = self.book_table.item(selected[0])["values"][0]
        try:
            result, error = handle_input(f"return {book_id}", self.visitor)
            if error: messagebox.showerror("Denied", error)
            else: 
                messagebox.showinfo("Success", result)
                self._load_books()
        except Exception as e: messagebox.showerror("System Error", str(e))
        
    # ========================================================
    # AI Search
    # ========================================================
    
    def ai_search(self):
        query = self.ai_entry.get().strip()
        if not query: return
        self.chat_box.insert("end", f"🧑 You: {query}\n\n")
        books = load_books()
        q = query.lower()
        results = []
        for b in books:
            score = 0
            search_str = " ".join([str(b.get(k, "")) for k in ["title", "author", "topic", "publisher", "year"]]).lower()
            if q in search_str: score += 5
            words = q.split()
            for word in words:
                if word in search_str: score += 1
            if score > 0: results.append((score, b))
        results.sort(reverse=True, key=lambda x: x[0])
        if not results:
            self.chat_box.insert("end", "🤖 AI: No books found. Try another keyword.\n\n")
        else:
            self.chat_box.insert("end", "🤖 Recommended Matches:\n\n")
            for score, b in results[:5]:
                status = "Available" if b.get("available", True) else "Borrowed"
                self.chat_box.insert("end", f"📘 {b.get('title')} | {b.get('author')} ({status})\n\n")
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
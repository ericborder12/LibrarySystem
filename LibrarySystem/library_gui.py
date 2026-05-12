import tkinter as tk
from tkinter import scrolledtext, font as tkfont
from handle_input import handle_input
from LibraryVisitor import LibraryVisitor


# ──────────────────────────────────────────────────────────────────────────────
#  Colour palette
# ──────────────────────────────────────────────────────────────────────────────
BG_DARK    = "#0f1117"
BG_PANEL   = "#1a1d27"
BG_INPUT   = "#1f2233"
ACCENT     = "#4f8ef7"
ACCENT2    = "#7c5cbf"
SUCCESS    = "#3ecf6e"
ERROR      = "#f76f6f"
WARNING    = "#f7c94f"
TEXT_MAIN  = "#e8eaf0"
TEXT_DIM   = "#6b7280"
TEXT_USER  = "#a5c8ff"
TEXT_BOT   = "#c3f0a8"
TEXT_ERR   = "#ffaaaa"
TEXT_INFO  = "#ffd580"
BORDER     = "#2d3148"


class LibraryGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("860x640")
        self.root.minsize(700, 480)
        self.root.configure(bg=BG_DARK)

        self.visitor = LibraryVisitor()

        self._build_fonts()
        self._build_ui()
        self._welcome()

    # ── fonts ─────────────────────────────────────────────────────────────────

    def _build_fonts(self):
        self.font_mono  = tkfont.Font(family="Courier New", size=11)
        self.font_ui    = tkfont.Font(family="Segoe UI",    size=11)
        self.font_bold  = tkfont.Font(family="Segoe UI",    size=11, weight="bold")
        self.font_title = tkfont.Font(family="Segoe UI",    size=13, weight="bold")
        self.font_small = tkfont.Font(family="Segoe UI",    size=9)

    # ── layout ────────────────────────────────────────────────────────────────

    def _build_ui(self):
        # ── header ────────────────────────────────────────────────────────────
        header = tk.Frame(self.root, bg=BG_PANEL, height=52)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)

        tk.Label(header, text="📚", font=("Segoe UI Emoji", 20),
                 bg=BG_PANEL, fg=ACCENT).pack(side=tk.LEFT, padx=(16, 6), pady=8)
        tk.Label(header, text="Library Management System",
                 font=self.font_title, bg=BG_PANEL, fg=TEXT_MAIN).pack(side=tk.LEFT, pady=8)

        self.status_label = tk.Label(header, text="● Guest",
                                     font=self.font_small, bg=BG_PANEL, fg=TEXT_DIM)
        self.status_label.pack(side=tk.RIGHT, padx=16)

        # ── divider ──────────────────────────────────────────────────────────
        tk.Frame(self.root, bg=BORDER, height=1).pack(fill=tk.X)

        # ── main area ─────────────────────────────────────────────────────────
        main = tk.Frame(self.root, bg=BG_DARK)
        main.pack(fill=tk.BOTH, expand=True)

        # sidebar
        sidebar = tk.Frame(main, bg=BG_PANEL, width=180)
        sidebar.pack(fill=tk.Y, side=tk.LEFT)
        sidebar.pack_propagate(False)
        self._build_sidebar(sidebar)

        tk.Frame(main, bg=BORDER, width=1).pack(fill=tk.Y, side=tk.LEFT)

        # chat area
        chat_frame = tk.Frame(main, bg=BG_DARK)
        chat_frame.pack(fill=tk.BOTH, expand=True)
        self._build_chat(chat_frame)

    def _build_sidebar(self, parent):
        tk.Label(parent, text="QUICK COMMANDS", font=self.font_small,
                 bg=BG_PANEL, fg=TEXT_DIM).pack(pady=(14, 4), padx=10, anchor="w")

        cmds = [
            ("📋 List Books",    "list books"),
            ("🔍 Search...",     "search "),
            ("🤖 AI Search",     "ai fantasy books"),
            ("📖 My Borrowed",   "view borrowed"),
            ("❓ Help",          "help"),
            ("", ""),
            ("👤 Register",      "register <user> <pass>"),
            ("🔑 Login",         "login <user> <pass>"),
            ("🚪 Logout",        "logout"),
            ("", ""),
            ("➕ Add Book",      "add B0XX \"Title by Author\""),
            ("🗑️  Remove Book",  "remove B0XX"),
            ("👥 List Users",    "list users"),
        ]

        for label, cmd in cmds:
            if label == "":
                tk.Frame(parent, bg=BORDER, height=1).pack(fill=tk.X, padx=8, pady=4)
                continue
            btn = tk.Button(
                parent, text=label, anchor="w",
                font=self.font_small, bg=BG_PANEL, fg=TEXT_MAIN,
                activebackground=BG_INPUT, activeforeground=ACCENT,
                relief=tk.FLAT, cursor="hand2", bd=0,
                command=lambda c=cmd: self._quick_cmd(c)
            )
            btn.pack(fill=tk.X, padx=6, pady=1, ipady=4)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=BG_INPUT))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=BG_PANEL))

    def _build_chat(self, parent):
        # output area
        self.output = scrolledtext.ScrolledText(
            parent, wrap=tk.WORD, state="disabled",
            font=self.font_mono, bg=BG_DARK, fg=TEXT_MAIN,
            insertbackground=ACCENT, selectbackground=ACCENT2,
            relief=tk.FLAT, padx=14, pady=10,
            bd=0
        )
        self.output.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

        # configure text tags
        self.output.tag_config("user",    foreground=TEXT_USER)
        self.output.tag_config("bot",     foreground=TEXT_BOT)
        self.output.tag_config("error",   foreground=TEXT_ERR)
        self.output.tag_config("info",    foreground=TEXT_INFO)
        self.output.tag_config("dim",     foreground=TEXT_DIM)
        self.output.tag_config("success", foreground=SUCCESS)
        self.output.tag_config("header",  foreground=ACCENT,  font=self.font_bold)

        # ── input bar ─────────────────────────────────────────────────────────
        tk.Frame(parent, bg=BORDER, height=1).pack(fill=tk.X)
        bar = tk.Frame(parent, bg=BG_INPUT, height=50)
        bar.pack(fill=tk.X)
        bar.pack_propagate(False)

        self.prompt_label = tk.Label(bar, text="[guest]>>", font=self.font_mono,
                                     bg=BG_INPUT, fg=ACCENT)
        self.prompt_label.pack(side=tk.LEFT, padx=(12, 4))

        self.entry = tk.Entry(bar, font=self.font_mono, bg=BG_INPUT, fg=TEXT_MAIN,
                              insertbackground=TEXT_MAIN, relief=tk.FLAT, bd=0)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", self._on_enter)
        self.entry.bind("<Up>",     self._history_up)
        self.entry.bind("<Down>",   self._history_down)
        self.entry.focus_set()

        send_btn = tk.Button(bar, text="Send ⏎", font=self.font_small,
                             bg=ACCENT, fg="white", activebackground=ACCENT2,
                             relief=tk.FLAT, cursor="hand2", bd=0,
                             command=self._send)
        send_btn.pack(side=tk.RIGHT, padx=10, pady=8, ipadx=8)

        self._history = []
        self._hist_idx = -1

    # ── helpers ───────────────────────────────────────────────────────────────

    def _welcome(self):
        self._append("╔══════════════════════════════════════════╗\n", "header")
        self._append("║     Welcome to Library Management System ║\n", "header")
        self._append("╚══════════════════════════════════════════╝\n", "header")
        self._append("Type ", "dim")
        self._append("help", "info")
        self._append(" to see all commands.\n", "dim")
        self._append("Default admin login: ", "dim")
        self._append("admin / admin123\n\n", "info")

    def _append(self, text: str, tag: str = ""):
        self.output.configure(state="normal")
        if tag:
            self.output.insert(tk.END, text, tag)
        else:
            self.output.insert(tk.END, text)
        self.output.configure(state="disabled")
        self.output.see(tk.END)

    def _print_result(self, result: str):
        """Color-code result lines by first character."""
        for line in result.split("\n"):
            stripped = line
            if stripped.startswith("✅") or stripped.startswith("📖") or stripped.startswith("👋"):
                self._append(line + "\n", "success")
            elif stripped.startswith("❌"):
                self._append(line + "\n", "error")
            elif stripped.startswith("╔") or stripped.startswith("╠") or stripped.startswith("╚") or stripped.startswith("║"):
                self._append(line + "\n", "header")
            elif stripped.startswith("─") or stripped.startswith("━"):
                self._append(line + "\n", "dim")
            else:
                self._append(line + "\n", "bot")

    def _update_status(self):
        if self.visitor.current_user:
            role = self.visitor.current_role
            color = WARNING if role == "admin" else SUCCESS
            self.status_label.config(
                text=f"● {self.visitor.current_user} ({role})", fg=color)
            self.prompt_label.config(text=f"[{self.visitor.current_user}]>>")
        else:
            self.status_label.config(text="● Guest", fg=TEXT_DIM)
            self.prompt_label.config(text="[guest]>>")

    def _quick_cmd(self, cmd: str):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, cmd)
        self.entry.focus_set()
        # If no placeholders, send immediately
        if "<" not in cmd and cmd.strip() not in ("", "search "):
            self._send()

    def _history_up(self, event):
        if self._history and self._hist_idx < len(self._history) - 1:
            self._hist_idx += 1
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self._history[-(self._hist_idx + 1)])

    def _history_down(self, event):
        if self._hist_idx > 0:
            self._hist_idx -= 1
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self._history[-(self._hist_idx + 1)])
        else:
            self._hist_idx = -1
            self.entry.delete(0, tk.END)

    # ── send ──────────────────────────────────────────────────────────────────

    def _on_enter(self, event):
        self._send()

    def _send(self):
        text = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        if not text:
            return

        # history
        self._history.append(text)
        self._hist_idx = -1

        # echo user input
        self._append(f"\n[{self.visitor.current_user or 'guest'}]>> ", "dim")
        self._append(text + "\n", "user")

        if text.lower() in ("exit", "quit"):
            self.root.quit()
            return

        # AI assistant mode
        if text.lower().startswith("ai "):
            query = text[3:].strip()
            result = self.visitor.ai_search_books(query)
            error = None
        else:
            result, error = handle_input(text, self.visitor)
        self._update_status()

        if error:
            self._append(f"❌ {error}\n", "error")
        elif result is not None:
            self._print_result(result)


def launch():
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()


if __name__ == "__main__":
    launch()

grammar library;

program: command EOF;

command
    : REGISTER WORD WORD                   # registerUser
    | LOGIN    WORD WORD                   # loginUser
    | LOGOUT                               # logoutUser
    | BORROW   BOOKID                      # borrowBook
    | RETURN   BOOKID                      # returnBook
    | VIEW BORROWED                        # viewBorrowed
    | LIST BOOKS                           # listBooks
    | LIST USERS                           # listUsers
    | SEARCH   titlePhrase                 # searchBook
    | ADD      BOOKID titlePhrase          # addBook
    | REMOVE   BOOKID                      # removeBook
    | VIEW     WORD                        # viewUser
    | HELP                                 # helpCmd
    ;

titlePhrase : WORD+ ;

// Keywords first
REGISTER : 'register' ;
LOGIN    : 'login'    ;
LOGOUT   : 'logout'   ;
BORROW   : 'borrow'   ;
RETURN   : 'return'   ;
VIEW     : 'view'     ;
BORROWED : 'borrowed' ;
LIST     : 'list'     ;
BOOKS    : 'books'    ;
USERS    : 'users'    ;
SEARCH   : 'search'   ;
ADD      : 'add'      ;
REMOVE   : 'remove'   ;
HELP     : 'help'     ;

// Book IDs: B/b followed by digits
BOOKID : [Bb][0-9]+ ;

// Generic word: letters, digits, special chars — no spaces
WORD : [a-zA-Z0-9!@#$%^&*_\-]+ ;

WS : [ \t\r\n]+ -> skip ;

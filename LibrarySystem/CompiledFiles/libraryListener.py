# Generated from library.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .libraryParser import libraryParser
else:
    from libraryParser import libraryParser

# This class defines a complete listener for a parse tree produced by libraryParser.
class libraryListener(ParseTreeListener):

    # Enter a parse tree produced by libraryParser#program.
    def enterProgram(self, ctx:libraryParser.ProgramContext):
        pass

    # Exit a parse tree produced by libraryParser#program.
    def exitProgram(self, ctx:libraryParser.ProgramContext):
        pass


    # Enter a parse tree produced by libraryParser#registerUser.
    def enterRegisterUser(self, ctx:libraryParser.RegisterUserContext):
        pass

    # Exit a parse tree produced by libraryParser#registerUser.
    def exitRegisterUser(self, ctx:libraryParser.RegisterUserContext):
        pass


    # Enter a parse tree produced by libraryParser#loginUser.
    def enterLoginUser(self, ctx:libraryParser.LoginUserContext):
        pass

    # Exit a parse tree produced by libraryParser#loginUser.
    def exitLoginUser(self, ctx:libraryParser.LoginUserContext):
        pass


    # Enter a parse tree produced by libraryParser#logoutUser.
    def enterLogoutUser(self, ctx:libraryParser.LogoutUserContext):
        pass

    # Exit a parse tree produced by libraryParser#logoutUser.
    def exitLogoutUser(self, ctx:libraryParser.LogoutUserContext):
        pass


    # Enter a parse tree produced by libraryParser#borrowBook.
    def enterBorrowBook(self, ctx:libraryParser.BorrowBookContext):
        pass

    # Exit a parse tree produced by libraryParser#borrowBook.
    def exitBorrowBook(self, ctx:libraryParser.BorrowBookContext):
        pass


    # Enter a parse tree produced by libraryParser#returnBook.
    def enterReturnBook(self, ctx:libraryParser.ReturnBookContext):
        pass

    # Exit a parse tree produced by libraryParser#returnBook.
    def exitReturnBook(self, ctx:libraryParser.ReturnBookContext):
        pass


    # Enter a parse tree produced by libraryParser#viewBorrowed.
    def enterViewBorrowed(self, ctx:libraryParser.ViewBorrowedContext):
        pass

    # Exit a parse tree produced by libraryParser#viewBorrowed.
    def exitViewBorrowed(self, ctx:libraryParser.ViewBorrowedContext):
        pass


    # Enter a parse tree produced by libraryParser#listBooks.
    def enterListBooks(self, ctx:libraryParser.ListBooksContext):
        pass

    # Exit a parse tree produced by libraryParser#listBooks.
    def exitListBooks(self, ctx:libraryParser.ListBooksContext):
        pass


    # Enter a parse tree produced by libraryParser#listUsers.
    def enterListUsers(self, ctx:libraryParser.ListUsersContext):
        pass

    # Exit a parse tree produced by libraryParser#listUsers.
    def exitListUsers(self, ctx:libraryParser.ListUsersContext):
        pass


    # Enter a parse tree produced by libraryParser#searchBook.
    def enterSearchBook(self, ctx:libraryParser.SearchBookContext):
        pass

    # Exit a parse tree produced by libraryParser#searchBook.
    def exitSearchBook(self, ctx:libraryParser.SearchBookContext):
        pass


    # Enter a parse tree produced by libraryParser#addBook.
    def enterAddBook(self, ctx:libraryParser.AddBookContext):
        pass

    # Exit a parse tree produced by libraryParser#addBook.
    def exitAddBook(self, ctx:libraryParser.AddBookContext):
        pass


    # Enter a parse tree produced by libraryParser#removeBook.
    def enterRemoveBook(self, ctx:libraryParser.RemoveBookContext):
        pass

    # Exit a parse tree produced by libraryParser#removeBook.
    def exitRemoveBook(self, ctx:libraryParser.RemoveBookContext):
        pass


    # Enter a parse tree produced by libraryParser#viewUser.
    def enterViewUser(self, ctx:libraryParser.ViewUserContext):
        pass

    # Exit a parse tree produced by libraryParser#viewUser.
    def exitViewUser(self, ctx:libraryParser.ViewUserContext):
        pass


    # Enter a parse tree produced by libraryParser#helpCmd.
    def enterHelpCmd(self, ctx:libraryParser.HelpCmdContext):
        pass

    # Exit a parse tree produced by libraryParser#helpCmd.
    def exitHelpCmd(self, ctx:libraryParser.HelpCmdContext):
        pass


    # Enter a parse tree produced by libraryParser#titlePhrase.
    def enterTitlePhrase(self, ctx:libraryParser.TitlePhraseContext):
        pass

    # Exit a parse tree produced by libraryParser#titlePhrase.
    def exitTitlePhrase(self, ctx:libraryParser.TitlePhraseContext):
        pass



del libraryParser
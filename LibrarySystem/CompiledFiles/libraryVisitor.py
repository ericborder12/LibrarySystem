# Generated from library.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .libraryParser import libraryParser
else:
    from libraryParser import libraryParser

# This class defines a complete generic visitor for a parse tree produced by libraryParser.

class libraryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by libraryParser#program.
    def visitProgram(self, ctx:libraryParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#registerUser.
    def visitRegisterUser(self, ctx:libraryParser.RegisterUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#loginUser.
    def visitLoginUser(self, ctx:libraryParser.LoginUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#logoutUser.
    def visitLogoutUser(self, ctx:libraryParser.LogoutUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#borrowBook.
    def visitBorrowBook(self, ctx:libraryParser.BorrowBookContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#returnBook.
    def visitReturnBook(self, ctx:libraryParser.ReturnBookContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#viewBorrowed.
    def visitViewBorrowed(self, ctx:libraryParser.ViewBorrowedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#listBooks.
    def visitListBooks(self, ctx:libraryParser.ListBooksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#listUsers.
    def visitListUsers(self, ctx:libraryParser.ListUsersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#searchBook.
    def visitSearchBook(self, ctx:libraryParser.SearchBookContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#addBook.
    def visitAddBook(self, ctx:libraryParser.AddBookContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#removeBook.
    def visitRemoveBook(self, ctx:libraryParser.RemoveBookContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#viewUser.
    def visitViewUser(self, ctx:libraryParser.ViewUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#helpCmd.
    def visitHelpCmd(self, ctx:libraryParser.HelpCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by libraryParser#titlePhrase.
    def visitTitlePhrase(self, ctx:libraryParser.TitlePhraseContext):
        return self.visitChildren(ctx)



del libraryParser
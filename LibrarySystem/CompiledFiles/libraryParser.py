# Generated from library.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\'\n\3\3\4\6")
        buf.write("\4*\n\4\r\4\16\4+\3\4\2\2\5\2\4\6\2\2\2\67\2\b\3\2\2\2")
        buf.write("\4&\3\2\2\2\6)\3\2\2\2\b\t\5\4\3\2\t\n\7\2\2\3\n\3\3\2")
        buf.write("\2\2\13\f\7\3\2\2\f\r\7\22\2\2\r\'\7\22\2\2\16\17\7\4")
        buf.write("\2\2\17\20\7\22\2\2\20\'\7\22\2\2\21\'\7\5\2\2\22\23\7")
        buf.write("\6\2\2\23\'\7\21\2\2\24\25\7\7\2\2\25\'\7\21\2\2\26\27")
        buf.write("\7\b\2\2\27\'\7\t\2\2\30\31\7\n\2\2\31\'\7\13\2\2\32\33")
        buf.write("\7\n\2\2\33\'\7\f\2\2\34\35\7\r\2\2\35\'\5\6\4\2\36\37")
        buf.write("\7\16\2\2\37 \7\21\2\2 \'\5\6\4\2!\"\7\17\2\2\"\'\7\21")
        buf.write("\2\2#$\7\b\2\2$\'\7\22\2\2%\'\7\20\2\2&\13\3\2\2\2&\16")
        buf.write("\3\2\2\2&\21\3\2\2\2&\22\3\2\2\2&\24\3\2\2\2&\26\3\2\2")
        buf.write("\2&\30\3\2\2\2&\32\3\2\2\2&\34\3\2\2\2&\36\3\2\2\2&!\3")
        buf.write("\2\2\2&#\3\2\2\2&%\3\2\2\2\'\5\3\2\2\2(*\7\22\2\2)(\3")
        buf.write("\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\7\3\2\2\2\4&+")
        return buf.getvalue()


class libraryParser ( Parser ):

    grammarFileName = "library.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'register'", "'login'", "'logout'", "'borrow'", 
                     "'return'", "'view'", "'borrowed'", "'list'", "'books'", 
                     "'users'", "'search'", "'add'", "'remove'", "'help'" ]

    symbolicNames = [ "<INVALID>", "REGISTER", "LOGIN", "LOGOUT", "BORROW", 
                      "RETURN", "VIEW", "BORROWED", "LIST", "BOOKS", "USERS", 
                      "SEARCH", "ADD", "REMOVE", "HELP", "BOOKID", "WORD", 
                      "WS" ]

    RULE_program = 0
    RULE_command = 1
    RULE_titlePhrase = 2

    ruleNames =  [ "program", "command", "titlePhrase" ]

    EOF = Token.EOF
    REGISTER=1
    LOGIN=2
    LOGOUT=3
    BORROW=4
    RETURN=5
    VIEW=6
    BORROWED=7
    LIST=8
    BOOKS=9
    USERS=10
    SEARCH=11
    ADD=12
    REMOVE=13
    HELP=14
    BOOKID=15
    WORD=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(libraryParser.CommandContext,0)


        def EOF(self):
            return self.getToken(libraryParser.EOF, 0)

        def getRuleIndex(self):
            return libraryParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = libraryParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.command()
            self.state = 7
            self.match(libraryParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return libraryParser.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ListBooksContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIST(self):
            return self.getToken(libraryParser.LIST, 0)
        def BOOKS(self):
            return self.getToken(libraryParser.BOOKS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListBooks" ):
                listener.enterListBooks(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListBooks" ):
                listener.exitListBooks(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListBooks" ):
                return visitor.visitListBooks(self)
            else:
                return visitor.visitChildren(self)


    class ViewBorrowedContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VIEW(self):
            return self.getToken(libraryParser.VIEW, 0)
        def BORROWED(self):
            return self.getToken(libraryParser.BORROWED, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterViewBorrowed" ):
                listener.enterViewBorrowed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitViewBorrowed" ):
                listener.exitViewBorrowed(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitViewBorrowed" ):
                return visitor.visitViewBorrowed(self)
            else:
                return visitor.visitChildren(self)


    class AddBookContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(libraryParser.ADD, 0)
        def BOOKID(self):
            return self.getToken(libraryParser.BOOKID, 0)
        def titlePhrase(self):
            return self.getTypedRuleContext(libraryParser.TitlePhraseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddBook" ):
                listener.enterAddBook(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddBook" ):
                listener.exitAddBook(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddBook" ):
                return visitor.visitAddBook(self)
            else:
                return visitor.visitChildren(self)


    class SearchBookContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEARCH(self):
            return self.getToken(libraryParser.SEARCH, 0)
        def titlePhrase(self):
            return self.getTypedRuleContext(libraryParser.TitlePhraseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearchBook" ):
                listener.enterSearchBook(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearchBook" ):
                listener.exitSearchBook(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSearchBook" ):
                return visitor.visitSearchBook(self)
            else:
                return visitor.visitChildren(self)


    class LoginUserContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOGIN(self):
            return self.getToken(libraryParser.LOGIN, 0)
        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(libraryParser.WORD)
            else:
                return self.getToken(libraryParser.WORD, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoginUser" ):
                listener.enterLoginUser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoginUser" ):
                listener.exitLoginUser(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoginUser" ):
                return visitor.visitLoginUser(self)
            else:
                return visitor.visitChildren(self)


    class BorrowBookContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BORROW(self):
            return self.getToken(libraryParser.BORROW, 0)
        def BOOKID(self):
            return self.getToken(libraryParser.BOOKID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBorrowBook" ):
                listener.enterBorrowBook(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBorrowBook" ):
                listener.exitBorrowBook(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBorrowBook" ):
                return visitor.visitBorrowBook(self)
            else:
                return visitor.visitChildren(self)


    class ReturnBookContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(libraryParser.RETURN, 0)
        def BOOKID(self):
            return self.getToken(libraryParser.BOOKID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnBook" ):
                listener.enterReturnBook(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnBook" ):
                listener.exitReturnBook(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnBook" ):
                return visitor.visitReturnBook(self)
            else:
                return visitor.visitChildren(self)


    class LogoutUserContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOGOUT(self):
            return self.getToken(libraryParser.LOGOUT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogoutUser" ):
                listener.enterLogoutUser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogoutUser" ):
                listener.exitLogoutUser(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogoutUser" ):
                return visitor.visitLogoutUser(self)
            else:
                return visitor.visitChildren(self)


    class ListUsersContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIST(self):
            return self.getToken(libraryParser.LIST, 0)
        def USERS(self):
            return self.getToken(libraryParser.USERS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListUsers" ):
                listener.enterListUsers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListUsers" ):
                listener.exitListUsers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListUsers" ):
                return visitor.visitListUsers(self)
            else:
                return visitor.visitChildren(self)


    class ViewUserContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VIEW(self):
            return self.getToken(libraryParser.VIEW, 0)
        def WORD(self):
            return self.getToken(libraryParser.WORD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterViewUser" ):
                listener.enterViewUser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitViewUser" ):
                listener.exitViewUser(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitViewUser" ):
                return visitor.visitViewUser(self)
            else:
                return visitor.visitChildren(self)


    class RegisterUserContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REGISTER(self):
            return self.getToken(libraryParser.REGISTER, 0)
        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(libraryParser.WORD)
            else:
                return self.getToken(libraryParser.WORD, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegisterUser" ):
                listener.enterRegisterUser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegisterUser" ):
                listener.exitRegisterUser(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegisterUser" ):
                return visitor.visitRegisterUser(self)
            else:
                return visitor.visitChildren(self)


    class HelpCmdContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HELP(self):
            return self.getToken(libraryParser.HELP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelpCmd" ):
                listener.enterHelpCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelpCmd" ):
                listener.exitHelpCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelpCmd" ):
                return visitor.visitHelpCmd(self)
            else:
                return visitor.visitChildren(self)


    class RemoveBookContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a libraryParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REMOVE(self):
            return self.getToken(libraryParser.REMOVE, 0)
        def BOOKID(self):
            return self.getToken(libraryParser.BOOKID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemoveBook" ):
                listener.enterRemoveBook(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemoveBook" ):
                listener.exitRemoveBook(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemoveBook" ):
                return visitor.visitRemoveBook(self)
            else:
                return visitor.visitChildren(self)



    def command(self):

        localctx = libraryParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = libraryParser.RegisterUserContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                self.match(libraryParser.REGISTER)
                self.state = 10
                self.match(libraryParser.WORD)
                self.state = 11
                self.match(libraryParser.WORD)
                pass

            elif la_ == 2:
                localctx = libraryParser.LoginUserContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(libraryParser.LOGIN)
                self.state = 13
                self.match(libraryParser.WORD)
                self.state = 14
                self.match(libraryParser.WORD)
                pass

            elif la_ == 3:
                localctx = libraryParser.LogoutUserContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(libraryParser.LOGOUT)
                pass

            elif la_ == 4:
                localctx = libraryParser.BorrowBookContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 16
                self.match(libraryParser.BORROW)
                self.state = 17
                self.match(libraryParser.BOOKID)
                pass

            elif la_ == 5:
                localctx = libraryParser.ReturnBookContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 18
                self.match(libraryParser.RETURN)
                self.state = 19
                self.match(libraryParser.BOOKID)
                pass

            elif la_ == 6:
                localctx = libraryParser.ViewBorrowedContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 20
                self.match(libraryParser.VIEW)
                self.state = 21
                self.match(libraryParser.BORROWED)
                pass

            elif la_ == 7:
                localctx = libraryParser.ListBooksContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 22
                self.match(libraryParser.LIST)
                self.state = 23
                self.match(libraryParser.BOOKS)
                pass

            elif la_ == 8:
                localctx = libraryParser.ListUsersContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 24
                self.match(libraryParser.LIST)
                self.state = 25
                self.match(libraryParser.USERS)
                pass

            elif la_ == 9:
                localctx = libraryParser.SearchBookContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 26
                self.match(libraryParser.SEARCH)
                self.state = 27
                self.titlePhrase()
                pass

            elif la_ == 10:
                localctx = libraryParser.AddBookContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 28
                self.match(libraryParser.ADD)
                self.state = 29
                self.match(libraryParser.BOOKID)
                self.state = 30
                self.titlePhrase()
                pass

            elif la_ == 11:
                localctx = libraryParser.RemoveBookContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 31
                self.match(libraryParser.REMOVE)
                self.state = 32
                self.match(libraryParser.BOOKID)
                pass

            elif la_ == 12:
                localctx = libraryParser.ViewUserContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 33
                self.match(libraryParser.VIEW)
                self.state = 34
                self.match(libraryParser.WORD)
                pass

            elif la_ == 13:
                localctx = libraryParser.HelpCmdContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 35
                self.match(libraryParser.HELP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitlePhraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(libraryParser.WORD)
            else:
                return self.getToken(libraryParser.WORD, i)

        def getRuleIndex(self):
            return libraryParser.RULE_titlePhrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitlePhrase" ):
                listener.enterTitlePhrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitlePhrase" ):
                listener.exitTitlePhrase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTitlePhrase" ):
                return visitor.visitTitlePhrase(self)
            else:
                return visitor.visitChildren(self)




    def titlePhrase(self):

        localctx = libraryParser.TitlePhraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_titlePhrase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.match(libraryParser.WORD)
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==libraryParser.WORD):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






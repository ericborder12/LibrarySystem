from CompiledFiles.libraryLexer  import libraryLexer
from CompiledFiles.libraryParser import libraryParser
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener


class _SilentErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, col, msg, e):
        raise SyntaxError(msg)


def handle_input(user_input: str, visitor):
    """
    Parse user_input with ANTLR and execute via visitor.
    Returns a (result_string, error_string) tuple.
    visitor is shared across calls so session state (login) persists.
    """
    try:
        stream = InputStream(user_input.strip())
        lexer  = libraryLexer(stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(_SilentErrorListener())

        tokens = CommonTokenStream(lexer)
        parser = libraryParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(_SilentErrorListener())

        tree   = parser.program()
        result = visitor.visit(tree)

        if visitor.error:
            err = visitor.error
            visitor.error = None
            return None, err

        return result, None

    except SyntaxError:
        return None, "Unrecognised command — type 'help' for a list of commands."
    except Exception as e:
        return None, str(e)

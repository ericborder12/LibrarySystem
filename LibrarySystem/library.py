import sys
import os
import subprocess

DIR       = os.path.dirname(os.path.abspath(__file__))
# ── Update this path to your local ANTLR jar ──────────────────────
ANTLR_JAR = 'C:/antlr/antlr4-4.9.2-complete.jar'
CPL_DEST  = 'CompiledFiles'
SRC       = 'library.g4'


def print_usage():
    print('python library.py gen   — compile grammar (run once)')
    print('python library.py run   — start CLI mode')
    print('python library.py gui   — start GUI mode')


def print_break():
    print('-' * 55)


def generate_antlr():
    print('ANTLR4 compiling grammar...')
    subprocess.run([
        'java', '-jar', ANTLR_JAR,
        '-o', CPL_DEST,
        '-visitor', '-no-listener',
        '-Dlanguage=Python3',
        SRC
    ], cwd=DIR)
    print('Done. Compiled files written to:', CPL_DEST)


def run():
    from CompiledFiles.libraryLexer  import libraryLexer
    from CompiledFiles.libraryParser import libraryParser
    from antlr4 import InputStream, CommonTokenStream
    from antlr4.error.ErrorListener import ErrorListener
    from LibraryVisitor import LibraryVisitor

    class SilentErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, col, msg, e):
            raise SyntaxError(msg)

    visitor = LibraryVisitor()

    print('╔══════════════════════════════════════════╗')
    print('║       LIBRARY MANAGEMENT SYSTEM          ║')
    print('║  Type "help" for commands, "exit" to quit║')
    print('╚══════════════════════════════════════════╝')
    print('  Default admin: admin / admin123\n')

    while True:
        try:
            prompt = f"[{visitor.current_user or 'guest'}]>> "
            user_input = input(prompt).strip()
            if not user_input:
                continue
            if user_input.lower() in ('exit', 'quit'):
                print("Goodbye!")
                break

            stream = InputStream(user_input)
            lexer  = libraryLexer(stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(SilentErrorListener())

            tokens = CommonTokenStream(lexer)
            parser = libraryParser(tokens)
            parser.removeErrorListeners()
            parser.addErrorListener(SilentErrorListener())

            tree   = parser.program()
            result = visitor.visit(tree)

            if visitor.error:
                print(f"Error: {visitor.error}")
                visitor.error = None
            elif result is not None:
                print(result)

        except SyntaxError:
            print("Unrecognised command — type 'help' for a list of commands.")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def main(argv):
    print_break()
    if len(argv) < 1:
        print_usage()
    elif argv[0] == 'gen':
        generate_antlr()
    elif argv[0] == 'run':
        run()
    elif argv[0] == 'gui':
        import library_gui
        library_gui.launch()
    else:
        print_usage()
    print_break()


if __name__ == '__main__':
    main(sys.argv[1:])

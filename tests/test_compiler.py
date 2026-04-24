import io
import sys
import tempfile
import os
import unittest
from pathlib import Path

# Add src directory to path to import braython package
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from braython import Compiler


class TestCompilerPortuguese(unittest.TestCase):
    def setUp(self):
        self.compiler = Compiler()

    def _compile(self, code):
        return self.compiler.compile(code, 'pt')

    def test_print(self):
        self.assertEqual(self._compile('escreva("hello")'), 'print("hello")')

    def test_variable_assignment(self):
        self.assertEqual(self._compile('deixe x = 10'), 'x = 10')

    def test_if(self):
        self.assertEqual(self._compile('se x > 0:'), 'if x > 0:')

    def test_else_without_accent(self):
        self.assertEqual(self._compile('senao:'), 'else:')

    def test_else_with_accent(self):
        self.assertEqual(self._compile('senão:'), 'else:')

    def test_elif_without_accent(self):
        self.assertEqual(self._compile('senao_se x == 0:'), 'elif x == 0:')

    def test_elif_with_accent(self):
        self.assertEqual(self._compile('senão_se x == 0:'), 'elif x == 0:')

    def test_while(self):
        self.assertEqual(self._compile('enquanto x > 0:'), 'while x > 0:')

    def test_for_in_range(self):
        self.assertEqual(self._compile('para i em alcance(10):'), 'for i in range(10):')

    def test_range_standalone(self):
        self.assertEqual(self._compile('alcance(1, 4)'), 'range(1, 4)')

    def test_in_operator(self):
        self.assertEqual(self._compile('x em lista'), 'x in lista')

    def test_def_without_accent(self):
        self.assertEqual(self._compile('funcao foo():'), 'def foo():')

    def test_def_with_accent(self):
        self.assertEqual(self._compile('função foo():'), 'def foo():')

    def test_return(self):
        self.assertEqual(self._compile('retorna x'), 'return x')

    def test_true(self):
        self.assertEqual(self._compile('verdadeiro'), 'True')

    def test_false(self):
        self.assertEqual(self._compile('falso'), 'False')

    def test_none(self):
        self.assertEqual(self._compile('nulo'), 'None')

    def test_continue(self):
        self.assertEqual(self._compile('continua'), 'continue')

    def test_break(self):
        self.assertEqual(self._compile('quebra'), 'break')

    def test_or_operator(self):
        self.assertEqual(self._compile('x ou y'), 'x or y')

    def test_and_operator(self):
        self.assertEqual(self._compile('x e y'), 'x and y')

    def test_import(self):
        self.assertEqual(self._compile('importar re'), 'import re')

    def test_from_import(self):
        self.assertEqual(self._compile('de enum importar Enum'), 'from enum import Enum')

    def test_enum_class(self):
        self.assertEqual(self._compile('class Foo(Enumeracao):'), 'class Foo(Enum):')

    def test_enum_module(self):
        self.assertEqual(self._compile('enumeracao'), 'enum')

    def test_enum_from_import(self):
        self.assertEqual(self._compile('de enumeracao importar Enumeracao, auto'),
                         'from enum import Enum, auto')

    def test_comment_preserved(self):
        self.assertEqual(self._compile('# senao enquanto se'), '# senao enquanto se')

    def test_string_not_translated(self):
        self.assertEqual(self._compile('escreva("senao enquanto se")'),
                         'print("senao enquanto se")')

    def test_indentation_preserved(self):
        code = 'se x > 0:\n    escreva("sim")'
        expected = 'if x > 0:\n    print("sim")'
        self.assertEqual(self._compile(code), expected)

    def test_exemplo_basico(self):
        example_path = Path(__file__).parent.parent / 'examples' / 'exemplo_basico.py'
        with open(example_path, 'r', encoding='utf-8') as f:
            code = f.read()
        result = self._compile(code)
        self.assertIn('print("Olá, Mundo!")', result)
        self.assertIn('x = 10', result)
        self.assertIn('if y > z:', result)
        self.assertIn('else:', result)

    def test_lexer_compiles(self):
        lexer_path = Path(__file__).parent.parent / 'src' / 'braython' / 'lexer.py'
        with open(lexer_path, 'r', encoding='utf-8') as f:
            code = f.read()
        result = self._compile(code)
        self.assertIn('import re', result)
        self.assertIn('from enum import Enum, auto', result)
        self.assertIn('class TipoToken(Enum):', result)
        self.assertIn('while ', result)
        self.assertIn('if ', result)
        self.assertIn('elif ', result)
        # Verify compiled code is valid Python
        import ast
        ast.parse(result)


class TestCompilerSpanish(unittest.TestCase):
    def setUp(self):
        self.compiler = Compiler()

    def _compile(self, code):
        return self.compiler.compile(code, 'es')

    def test_print(self):
        self.assertEqual(self._compile('escribe("hello")'), 'print("hello")')

    def test_variable_assignment(self):
        self.assertEqual(self._compile('deja x = 10'), 'x = 10')

    def test_if(self):
        self.assertEqual(self._compile('si x > 0:'), 'if x > 0:')

    def test_else(self):
        self.assertEqual(self._compile('sino:'), 'else:')

    def test_elif(self):
        self.assertEqual(self._compile('sino_si x == 0:'), 'elif x == 0:')

    def test_while(self):
        self.assertEqual(self._compile('mientras x > 0:'), 'while x > 0:')

    def test_for_in_range(self):
        self.assertEqual(self._compile('para i en rango(10):'), 'for i in range(10):')

    def test_range_standalone(self):
        self.assertEqual(self._compile('rango(1, 4)'), 'range(1, 4)')

    def test_in_operator(self):
        self.assertEqual(self._compile('x en lista'), 'x in lista')

    def test_def_without_accent(self):
        self.assertEqual(self._compile('funcion foo():'), 'def foo():')

    def test_def_with_accent(self):
        self.assertEqual(self._compile('función foo():'), 'def foo():')

    def test_return(self):
        self.assertEqual(self._compile('retorna x'), 'return x')

    def test_true(self):
        self.assertEqual(self._compile('verdadero'), 'True')

    def test_false(self):
        self.assertEqual(self._compile('falso'), 'False')

    def test_none(self):
        self.assertEqual(self._compile('nulo'), 'None')

    def test_continue(self):
        self.assertEqual(self._compile('continua'), 'continue')

    def test_break(self):
        self.assertEqual(self._compile('rompe'), 'break')

    def test_comment_preserved(self):
        self.assertEqual(self._compile('# sino mientras si'), '# sino mientras si')

    def test_string_not_translated(self):
        self.assertEqual(self._compile('escribe("sino mientras si")'),
                         'print("sino mientras si")')


class TestCompilerMisc(unittest.TestCase):
    def setUp(self):
        self.compiler = Compiler()

    def test_unsupported_language(self):
        with self.assertRaises(ValueError):
            self.compiler.compile('foo', 'fr')

    def test_compile_to_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False,
                                        encoding='utf-8') as f:
            f.write('escreva("hello")\n')
            tmp_in = f.name
        tmp_out = tmp_in + '_out.py'
        try:
            self.compiler.compile_to_file(tmp_in, tmp_out, 'pt')
            with open(tmp_out, encoding='utf-8') as f:
                self.assertEqual(f.read(), 'print("hello")\n')
        finally:
            os.unlink(tmp_in)
            if os.path.exists(tmp_out):
                os.unlink(tmp_out)

    def test_compile_and_run(self):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            self.compiler.compile_and_run('escreva("ok")', 'pt')
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        self.assertEqual(output, 'ok\n')


if __name__ == '__main__':
    unittest.main()

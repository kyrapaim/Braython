# Braython — Portuguese/Spanish to Python Compiler

Braython is a compiler that lets you write simple programs in Portuguese or Spanish and translates them to Python automatically.

## Project Structure

```
Braython/
├── lexer.py           # Tokenizes Portuguese/Spanish source code
├── parser.py          # AST parser (placeholder for future use)
├── compiler.py        # Main compiler that orchestrates lexer → translator → Python
├── exemplo_basico.py  # Basic example: variables, conditionals
├── exemplo_avancado.py # Advanced example: functions, loops
├── run.py             # Simple runner script
└── README.md          # This file
```

## Setup

### Requirements
- Python 3.6+
- No external dependencies (uses only Python standard library)

### Installation

1. Clone or download all files to a directory:
   ```bash
   git clone <repo-url>
   cd Braython
   ```

2. Ensure all files are in the same directory:
   - `lexer.py`
   - `parser.py`
   - `compiler.py`
   - Examples (optional): `exemplo_basico.py`, `exemplo_avancado.py`

## Usage

### Method 1: Run Examples

```bash
python exemplo_basico.py
python exemplo_avancado.py
```

### Method 2: Use the Runner Script

```bash
python run.py
```

Then select which example to run.

### Method 3: Write Your Own Code

Create a Python script:

```python
from compiler import Compiler

code = '''
escreva("Olá, Mundo!")
deixe x = 10
escreva(x + 5)
'''

Compiler().compile_and_run(code, 'pt')
```

Run it:
```bash
python seu_programa.py
```

### Method 4: Compile to a File

```python
from compiler import Compiler

# Compile Portuguese to Python file
Compiler().compile_to_file('programa.br', 'programa.py', 'pt')
```

Then run the generated Python:
```bash
python programa.py
```

## Portuguese Keywords

| Portuguese | English | Python |
|-----------|---------|--------|
| `escreva()` | write/print | `print()` |
| `deixe` | let | variable assignment |
| `se` | if | `if` |
| `senao` | else | `else` |
| `para ... em alcance()` | for...in range() | `for...in range()` |
| `funcao` | function | `def` |
| `retorna` | return | `return` |
| `verdadeiro` | true | `True` |
| `falso` | false | `False` |
| `nulo` | null | `None` |

## Examples

### Basic Example
```python
escreva("Olá, Mundo!")

deixe x = 10
deixe y = x + 5

se y > 10:
    escreva("Maior que 10")
senao:
    escreva("Menor ou igual a 10")
```

### With Functions
```python
funcao saudacao(nome):
    escreva("Olá, " + nome)

saudacao("Maria")
```

### With Loops
```python
para i em alcance(1, 5):
    escreva(i)
```

## Troubleshooting

**Error: "ModuleNotFoundError: No module named 'lexer'"**
- Ensure `lexer.py` is in the same directory as `compiler.py`
- Run from the Braython directory: `cd Braython && python script.py`

**Error: "SyntaxError" in Portuguese source**
- Check that you're using correct Portuguese keywords
- Don't run `.br` files directly with Python — pass them through `Compiler`

**Program doesn't print anything**
- Use `escreva()` instead of `print()`
- Wrap strings in quotes: `escreva("texto")`

## Next Steps

- Improve expression parsing (nested calls, complex operators)
- Add Spanish language support
- Build a REPL (interactive shell)
- Add error messages in Portuguese/Spanish

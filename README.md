# Braython — Portuguese/Spanish to Python Compiler

Braython is a compiler that lets you write simple programs in Portuguese or Spanish and translates them to Python automatically.

## Project Structure

This project follows industry-standard Python project organization:

```
braython/
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
├── src/
│   └── braython/               # Main package
│       ├── __init__.py         # Package initialization
│       ├── compiler.py         # Main compiler orchestrator
│       ├── lexer.py            # Tokenizer for Portuguese/Spanish
│       ├── parser.py           # AST parser
│       ├── messages.py         # Localized messages and translations
│       └── gui/
│           ├── __init__.py     # GUI package initialization
│           └── web_gui.py      # Web interface
├── tests/
│   ├── __init__.py
│   └── test_compiler.py        # Unit tests
├── examples/
│   ├── __init__.py
│   ├── exemplo_basico.py       # Basic example: variables, conditionals
│   ├── exemplo_pratico.py      # Practical example: grade calculator
│   └── interactive.py          # Interactive terminal interface
├── scripts/
│   └── run.py                  # Simple runner script
├── templates/
│   └── index.html              # Web GUI HTML template
└── docs/
    └── portuguese_guide/       # Portuguese language guide
```

## Setup

### Requirements
- Python 3.6+
- No external dependencies (uses only Python standard library)

### Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd braython
   ```

2. Install in development mode (optional, for pip integration):
   ```bash
   pip install -e .
   ```

## Usage

### Method 1: Run Examples

```bash
cd examples
python exemplo_basico.py
python exemplo_pratico.py
python interactive.py
```

### Method 2: Use the Runner Script

```bash
python scripts/run.py
```

Then select which example to run.

### Method 3: Write Your Own Code

Create a Python script:

```python
import sys
from pathlib import Path

# Add src to path to import braython
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from braython import Compiler

code = '''
escreva("Olá, Mundo!")
deixe x = 10
escreva(x + 5)
'''

Compiler().compile_and_run(code, 'pt')
```

### Method 4: Compile to a File

```python
from braython import Compiler

# Compile Portuguese to Python file
Compiler().compile_to_file('programa.br', 'programa.py', 'pt')
```

Then run the generated Python:
```bash
python programa.py
```

### Method 5: Web GUI

Run the web interface:
```bash
cd src/braython/gui
python web_gui.py
```

Then open your browser to `http://localhost:8000`

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

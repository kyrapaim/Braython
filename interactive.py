#!/usr/bin/env python3
"""
Braython Interactive - Simple terminal interface
Just press the play button in VS Code to run this!
"""

from compiler import Compiler
from messages import msg
import sys

def clear_screen():
    """Clear terminal screen"""
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    """Print welcome header"""
    print("\n" + "="*60)
    print("  BRAYTHON - Compilador Português/Espanhol → Python")
    print("="*60 + "\n")

def print_menu():
    """Print language menu"""
    print("Selecione o idioma:")
    print("  1) Português")
    print("  2) Español")
    print("  0) Sair\n")

def get_language_choice():
    """Get language from user"""
    while True:
        print_menu()
        choice = input("Escolha (0-2): ").strip()
        if choice == '1':
            return 'pt', 'Português'
        elif choice == '2':
            return 'es', 'Español'
        elif choice == '0':
            print("\n" + msg('bye', 'pt'))
            sys.exit(0)
        else:
            clear_screen()
            print_header()
            # Show invalid option in Portuguese since language not selected yet
            print(f"❌ {msg('invalid_option', 'pt')}\n")

def get_code(language_name):
    """Get code from user"""
    print(f"\n{'='*60}")
    print(f"  Digite seu código em {language_name}")
    print(f"  (termine digitando 010 em uma nova linha)")
    print("  Comandos: :show | :edit N <conteudo> | :insert N <conteudo> | :delete N | :clear")
    print("  Ex.: :edit 2 print(\"oi\") | :insert 1 x = 10\n")
    print(f"{'='*60}\n")
    
    lines = []
    while True:
        try:
            line = input(f"[{len(lines) + 1}] ")
            if line.strip() == '010':
                break

            stripped = line.strip()
            if stripped.startswith(':'):
                parts = stripped.split(' ', 2)
                command = parts[0].lower()

                if command == ':show':
                    if not lines:
                        print("(código vazio)")
                    else:
                        print("\nCódigo atual:")
                        for index, content in enumerate(lines, start=1):
                            print(f"{index:>3}: {content}")
                        print()
                    continue

                if command == ':clear':
                    lines.clear()
                    print("Código limpo.")
                    continue

                if command in (':edit', ':insert', ':delete'):
                    if len(parts) < 2:
                        print("Uso inválido. Exemplo: :edit 3 print(\"olá\")")
                        continue

                    try:
                        target = int(parts[1])
                    except ValueError:
                        print("Número da linha inválido.")
                        continue

                    if command == ':delete':
                        if target < 1 or target > len(lines):
                            print("Linha fora do intervalo.")
                            continue
                        lines.pop(target - 1)
                        print(f"Linha {target} removida.")
                        continue

                    new_text = parts[2] if len(parts) > 2 else ''

                    if command == ':edit':
                        if target < 1 or target > len(lines):
                            print("Linha fora do intervalo.")
                            continue
                        lines[target - 1] = new_text
                        print(f"Linha {target} atualizada.")
                        continue

                    if command == ':insert':
                        if target < 1 or target > len(lines) + 1:
                            print("Linha fora do intervalo para inserção.")
                            continue
                        lines.insert(target - 1, new_text)
                        print(f"Linha inserida na posição {target}.")
                        continue

                print("Comando desconhecido.")
                continue

            lines.append(line)
        except EOFError:
            break
    
    return '\n'.join(lines)

def run_code(code, language, language_name):
    """Run the code"""
    print(f"\n{'='*60}")
    print(f"  Executando código em {language_name}...")
    print(f"{'='*60}\n")
    
    compiler = Compiler()
    try:
        compiler.compile_and_run(code, language)
    except Exception as e:
        # Rare: compile_and_run itself raised; show localized label then raw error
        print(f"\n❌ {msg('runtime_error', language)}: {e}")

    # If the compiler captured a runtime exception, show raw error then translation
    if compiler.last_exception is not None:
        e = compiler.last_exception
        print(f"\n❌ {msg('runtime_error', language)}: {e}")
        if compiler.last_translated:
            print(f"{compiler.last_translated}")
    
    print(f"\n{'='*60}")

def show_translation(code, language):
    """Show translated Python code"""
    print(f"\n{'='*60}")
    print(f"  Código Traduzido para Python:")
    print(f"{'='*60}\n")
    
    compiler = Compiler()
    try:
        translated = compiler.compile(code, language)
        print(translated)
    except Exception as e:
        print(f"❌ Erro na tradução: {e}")
    
    print(f"\n{'='*60}")

def main():
    """Main interactive loop"""
    clear_screen()
    
    while True:
        print_header()
        
        # Get language
        language, language_name = get_language_choice()
        clear_screen()
        print_header()
        
        # Get code
        code = get_code(language_name)
        
        if not code.strip():
            clear_screen()
            print_header()
            print(f"⚠️  {msg('no_code', language)}\n")
            input(msg('menu_prompt', language))
            clear_screen()
            continue
        
        # Run or translate
        clear_screen()
        print_header()
        print("O que deseja fazer?\n")
        print("  1) Executar o código")
        print("  2) Ver a tradução para Python")
        print("  0) Voltar ao menu principal\n")
        
        action = input("Escolha (0-2): ").strip()
        
        clear_screen()
        print_header()
        
        if action == '1':
            run_code(code, language, language_name)
        elif action == '2':
            show_translation(code, language)
        elif action == '0':
            clear_screen()
            continue
        else:
            print("❌ Opção inválida.\n")
        
        input("\nPressione ENTER para continuar...")
        clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Até logo!")
        sys.exit(0)

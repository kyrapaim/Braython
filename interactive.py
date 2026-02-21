#!/usr/bin/env python3
"""
Braython Interactive - Simple terminal interface
Just press the play button in VS Code to run this!
"""

from compiler import Compiler
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
            print("\nAté logo!")
            sys.exit(0)
        else:
            clear_screen()
            print_header()
            print("❌ Opção inválida. Tente novamente.\n")

def get_code(language_name):
    """Get code from user"""
    print(f"\n{'='*60}")
    print(f"  Digite seu código em {language_name}")
    print(f"  (termine com uma linha vazia)\n")
    print(f"{'='*60}\n")
    
    lines = []
    while True:
        try:
            line = input()
            if not line:
                break
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
        print(f"\n❌ Erro: {e}")
    
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
            print("⚠️  Nenhum código foi digitado.\n")
            input("Pressione ENTER para continuar...")
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

#!/usr/bin/env python3
"""
Braython GUI - Interactive interface for the Braython compiler.
Write code in Portuguese or Spanish, compile, and run it instantly.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from compiler import Compiler
import sys
from io import StringIO

class BraythonGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Braython - Compilador Português/Espanhol → Python")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")
        
        self.compiler = Compiler()
        self.current_language = tk.StringVar(value='pt')
        
        self._create_welcome_screen()
        
    def _create_welcome_screen(self):
        """Create the initial welcome screen"""
        self.welcome_frame = tk.Frame(self.root, bg="#2c3e50")
        self.welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(
            self.welcome_frame,
            text="Braython",
            font=("Helvetica", 48, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title.pack(pady=30)
        
        # Subtitle
        subtitle = tk.Label(
            self.welcome_frame,
            text="Compilador Português/Espanhol → Python",
            font=("Helvetica", 16),
            bg="#2c3e50",
            fg="#3498db"
        )
        subtitle.pack(pady=10)
        
        # Description
        desc = tk.Label(
            self.welcome_frame,
            text="Escreva código em Português ou Espanhol\ne deixe o Braython traduzir para Python",
            font=("Helvetica", 12),
            bg="#2c3e50",
            fg="#bdc3c7",
            justify=tk.CENTER
        )
        desc.pack(pady=20)
        
        # Start button
        start_btn = tk.Button(
            self.welcome_frame,
            text="Começar",
            font=("Helvetica", 14, "bold"),
            bg="#3498db",
            fg="white",
            padx=40,
            pady=15,
            command=self._show_editor,
            relief=tk.FLAT,
            cursor="hand2"
        )
        start_btn.pack(pady=40)
        
        # Footer
        footer = tk.Label(
            self.welcome_frame,
            text="Sem dependências externas • Python 3.6+",
            font=("Helvetica", 10),
            bg="#2c3e50",
            fg="#7f8c8d"
        )
        footer.pack(side=tk.BOTTOM, pady=20)
    
    def _show_editor(self):
        """Replace welcome screen with the code editor"""
        self.welcome_frame.destroy()
        self._create_editor_screen()
    
    def _create_editor_screen(self):
        """Create the main editor interface"""
        # Top control bar
        control_frame = tk.Frame(self.root, bg="#34495e", height=60)
        control_frame.pack(fill=tk.X, padx=0, pady=0)
        
        # Language selection
        lang_frame = tk.Frame(control_frame, bg="#34495e")
        lang_frame.pack(side=tk.LEFT, padx=20, pady=10)
        
        lang_label = tk.Label(lang_frame, text="Idioma:", font=("Helvetica", 11, "bold"), bg="#34495e", fg="white")
        lang_label.pack(side=tk.LEFT, padx=(0, 10))
        
        pt_radio = tk.Radiobutton(
            lang_frame,
            text="Português",
            variable=self.current_language,
            value='pt',
            bg="#34495e",
            fg="white",
            selectcolor="#3498db",
            font=("Helvetica", 10),
            activebackground="#34495e",
            activeforeground="#3498db"
        )
        pt_radio.pack(side=tk.LEFT, padx=5)
        
        es_radio = tk.Radiobutton(
            lang_frame,
            text="Español",
            variable=self.current_language,
            value='es',
            bg="#34495e",
            fg="white",
            selectcolor="#3498db",
            font=("Helvetica", 10),
            activebackground="#34495e",
            activeforeground="#3498db"
        )
        es_radio.pack(side=tk.LEFT, padx=5)
        
        # Buttons
        button_frame = tk.Frame(control_frame, bg="#34495e")
        button_frame.pack(side=tk.RIGHT, padx=20, pady=10)
        
        compile_btn = tk.Button(
            button_frame,
            text="▶ Executar",
            font=("Helvetica", 11, "bold"),
            bg="#27ae60",
            fg="white",
            padx=15,
            pady=8,
            command=self._compile_and_run,
            relief=tk.FLAT,
            cursor="hand2"
        )
        compile_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="Limpar",
            font=("Helvetica", 11),
            bg="#e74c3c",
            fg="white",
            padx=15,
            pady=8,
            command=self._clear_all,
            relief=tk.FLAT,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Main content area
        content_frame = tk.Frame(self.root, bg="#ecf0f1")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Input label
        input_label = tk.Label(content_frame, text="Seu Código:", font=("Helvetica", 12, "bold"), bg="#ecf0f1", fg="#2c3e50")
        input_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Code input
        self.code_input = scrolledtext.ScrolledText(
            content_frame,
            height=15,
            font=("Courier", 11),
            bg="white",
            fg="#2c3e50",
            insertbackground="#3498db",
            relief=tk.FLAT,
            borderwidth=1
        )
        self.code_input.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.code_input.insert('1.0', "# Digite seu código aqui\nescreva(\"Olá, Mundo!\")")
        
        # Output label
        output_label = tk.Label(content_frame, text="Saída:", font=("Helvetica", 12, "bold"), bg="#ecf0f1", fg="#2c3e50")
        output_label.pack(anchor=tk.W, pady=(10, 5))
        
        # Output display
        self.output_display = scrolledtext.ScrolledText(
            content_frame,
            height=8,
            font=("Courier", 10),
            bg="#2c3e50",
            fg="#2ecc71",
            relief=tk.FLAT,
            borderwidth=1,
            state=tk.DISABLED
        )
        self.output_display.pack(fill=tk.BOTH, expand=True)
    
    def _compile_and_run(self):
        """Compile and run the code"""
        code = self.code_input.get('1.0', tk.END)
        language = self.current_language.get()
        
        if not code.strip():
            messagebox.showwarning("Aviso", "Por favor, digite algum código!")
            return
        
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = output_buffer = StringIO()
        
        try:
            self.compiler.compile_and_run(code, language)
            output = output_buffer.getvalue()
        except Exception as e:
            output = f"Erro: {str(e)}"
        finally:
            sys.stdout = old_stdout
        
        # Display output
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete('1.0', tk.END)
        self.output_display.insert('1.0', output if output else "(Sem saída)")
        self.output_display.config(state=tk.DISABLED)
    
    def _clear_all(self):
        """Clear code and output"""
        self.code_input.delete('1.0', tk.END)
        self.output_display.config(state=tk.NORMAL)
        self.output_display.delete('1.0', tk.END)
        self.output_display.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = BraythonGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

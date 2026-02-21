from translator import Translator


class Compiler:
    def __init__(self):
        self._translator = Translator()

    def compile(self, code: str, language: str) -> str:
        """ Convert code from Portuguese/Spanish to Python. """
        return self._translator.translate(code, language)

    def compile_and_run(self, code: str, language: str):
        """ Compile the code and execute the generated Python."""
        python_code = self.compile(code, language)
        exec(python_code)  # Caution: Using exec can be dangerous with untrusted input

    def compile_to_file(self, input_file: str, output_file: str, language: str):
        """ Read code from input_file, compile it, and save to output_file. """
        with open(input_file, 'r') as infile:
            code = infile.read()
        python_code = self.compile(code, language)
        with open(output_file, 'w') as outfile:
            outfile.write(python_code)

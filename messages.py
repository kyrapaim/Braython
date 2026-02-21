EXCEPTION_TYPE_TRANSLATIONS = {
    'pt': {
        'NameError': 'NomeNãoDefinido',
        'TypeError': 'TipoInválido',
        'SyntaxError': 'ErroDeSintaxe',
        'ZeroDivisionError': 'DivisãoPorZero',
        'IndexError': 'ÍndiceForaDoIntervalo',
        'KeyError': 'ChaveNãoEncontrada',
        'AttributeError': 'AtributoInexistente',
        'ValueError': 'ValorInválido',
        'Exception': 'Exceção',
    },
    'es': {
        'NameError': 'NombreNoDefinido',
        'TypeError': 'TipoInválido',
        'SyntaxError': 'ErrorDeSintaxis',
        'ZeroDivisionError': 'DivisiónPorCero',
        'IndexError': 'ÍndiceFueraDeRango',
        'KeyError': 'ClaveNoEncontrada',
        'AttributeError': 'AtributoInexistente',
        'ValueError': 'ValorInválido',
        'Exception': 'Excepción',
    }
}

def exception_type_label(exc: Exception, lang: str = 'pt') -> str:
    t = type(exc).__name__
    return EXCEPTION_TYPE_TRANSLATIONS.get(lang, EXCEPTION_TYPE_TRANSLATIONS['pt']).get(t, t)

MESSAGES = {
    'pt': {
        'no_code': 'Nenhum código foi digitado.',
        'runtime_error': 'Erro na execução',
        'invalid_option': 'Opção inválida. Tente novamente.',
        'bye': 'Até logo!',
        'prompt_language': 'Selecione o idioma:',
        'menu_prompt': 'Escolha (0-2): '
        ,
        'error_occurred': 'Ocorreu um erro durante a execução.',
        'post_error_option1': '1) Sair para o menu',
        'post_error_option2': '2) Voltar ao código para editar',
        'choose_post_error': 'Escolha (1/2): ',
        'enter_edit_mode': 'Entrando no modo de edição. Comandos: :show | :edit N <conteudo> | :insert N <conteudo> | :delete N | :clear | :done',
        'code_empty': '(código vazio)',
        'code_cleared': 'Código limpo.',
        'invalid_usage': 'Uso inválido. Ex.: :edit 3 print("oi")',
        'invalid_line_number': 'Número da linha inválido.',
        'line_out_of_range': 'Linha fora do intervalo.',
        'line_removed': 'Linha {n} removida.',
        'line_updated': 'Linha {n} atualizada.',
        'line_inserted': 'Linha inserida na posição {n}.',
        'unknown_command': 'Comando desconhecido.'
    },
    'es': {
        'no_code': 'No se ingresó código.',
        'runtime_error': 'Error al ejecutar',
        'invalid_option': 'Opción inválida. Intente nuevamente.',
        'bye': '¡Hasta luego!',
        'prompt_language': 'Seleccione el idioma:',
        'menu_prompt': 'Elija (0-2): '
        ,
        'error_occurred': 'Ocurrió un error durante la ejecución.',
        'post_error_option1': '1) Salir al menú',
        'post_error_option2': '2) Volver al código para editar',
        'choose_post_error': 'Elija (1/2): ',
        'enter_edit_mode': 'Entrando en modo de edición. Comandos: :show | :edit N <contenido> | :insert N <contenido> | :delete N | :clear | :done',
        'code_empty': '(código vacío)',
        'code_cleared': 'Código limpiado.',
        'invalid_usage': 'Uso inválido. Ej.: :edit 3 print("hola")',
        'invalid_line_number': 'Número de línea inválido.',
        'line_out_of_range': 'Línea fuera del rango.',
        'line_removed': 'Línea {n} eliminada.',
        'line_updated': 'Línea {n} actualizada.',
        'line_inserted': 'Línea insertada en la posición {n}.',
        'unknown_command': 'Comando desconocido.'
    }
}


def msg(key: str, lang: str = 'pt') -> str:
    """Return localized message for key and language (fallback to pt)."""
    return MESSAGES.get(lang, MESSAGES['pt']).get(key, MESSAGES['pt'].get(key, key))


def translate_exception(exc: Exception, lang: str = 'pt') -> str | None:
    """Attempt to translate common exception messages into the target language.

    Currently handles NameError patterns like "name 'x' is not defined".
    Returns a translated string or None if no translation available.
    """
    import re

    text = str(exc)
    # NameError: name 'foo' is not defined
    m = re.match(r"name '(.+)' is not defined", text)
    if m:
        ident = m.group(1)
        if lang == 'es':
            return f"'{ident}' no está definido"
        else:
            # default to Portuguese
            return f"'{ident}' não está definido"
    # SyntaxError
    if 'invalid syntax' in text.lower():
        return 'Error de sintaxis' if lang == 'es' else 'Erro de sintaxe'

    # ZeroDivisionError
    if 'division by zero' in text.lower() or 'division by 0' in text.lower():
        return 'División por cero' if lang == 'es' else 'Divisão por zero'

    # IndexError: list index out of range
    if 'list index out of range' in text.lower() or 'index out of range' in text.lower():
        return 'Índice fuera del rango' if lang == 'es' else 'Índice fora do intervalo'

    # KeyError: 'key'
    mkey = re.match(r"KeyError: ?(?:'|\")?(.*?)(?:'|\")?$", text)
    if mkey:
        key = mkey.group(1)
        if lang == 'es':
            return f"'{key}' no se encontró"
        else:
            return f"'{key}' não foi encontrado"

    # AttributeError: object has no attribute 'x'
    matt = re.search(r"attribute '(.+)'", text)
    if matt:
        attr = matt.group(1)
        if lang == 'es':
            return f"El atributo '{attr}' no existe en el objeto"
        else:
            return f"O atributo '{attr}' não existe no objeto"

    # TypeError: unsupported operand type(s)
    if 'unsupported operand type' in text.lower() or 'unsupported operand type(s)' in text.lower():
        return 'Operación con tipos incompatibles' if lang == 'es' else 'Operação com tipos incompatíveis'

    # ValueError generic
    if 'valueerror' in text.lower() or 'invalid literal' in text.lower() or 'could not convert' in text.lower():
        return 'Valor inválido' if lang == 'es' else 'Valor inválido'

    # Fallback: no translation available
    return None

MESSAGES = {
    'pt': {
        'no_code': 'Nenhum código foi digitado.',
        'runtime_error': 'Erro na execução',
        'invalid_option': 'Opção inválida. Tente novamente.',
        'bye': 'Até logo!',
        'prompt_language': 'Selecione o idioma:',
        'menu_prompt': 'Escolha (0-2): '
    },
    'es': {
        'no_code': 'No se ingresó código.',
        'runtime_error': 'Error al ejecutar',
        'invalid_option': 'Opción inválida. Intente nuevamente.',
        'bye': '¡Hasta luego!',
        'prompt_language': 'Seleccione el idioma:',
        'menu_prompt': 'Elija (0-2): '
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

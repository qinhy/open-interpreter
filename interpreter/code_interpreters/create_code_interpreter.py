from .language_map import language_map

def create_code_interpreter(language,user=''):
    # Case in-sensitive
    language = language.lower()

    try:
        CodeInterpreter = language_map[language]
        return CodeInterpreter(user=user)
    except KeyError:
        raise ValueError(f"Unknown or unsupported language: {language}")

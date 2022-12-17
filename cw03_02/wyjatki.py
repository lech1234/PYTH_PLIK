class BirthYearError(Exception):
    """
    Własna dedykowana klasa wyjątku, sygnalizująca, że podany rok urodzenia pochodzi z przyszłości.
    """
    def __init__(self):
        super().__init__('....... Rok urodzenia jeszcze nie nadszedł')


class NoValueError(Exception):
    """
    Własna dedykowana klasa wyjątku, sygnalizująca, że podany atrybut nie może być pusty.
    """
    def __init__(self, attr_name):
        super().__init__(f'....... Atrybut \'{attr_name}\' nie może być pusty')

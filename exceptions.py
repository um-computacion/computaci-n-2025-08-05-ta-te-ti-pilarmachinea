class PosOcupadaException(Exception):
    """Se lanza cuando se intenta ocupar una posición ya ocupada en el tablero."""
    pass

class PosInvalidaException(Exception):
    """Se lanza cuando las coordenadas están fuera del rango permitido (0-2)."""
    pass

class FichaInvalidaException(Exception):
    """Se lanza cuando se intenta crear un jugador con una ficha que no es 'X' ni '0'."""
    pass


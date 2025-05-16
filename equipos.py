class Equipo:
    def __init__(self):
        pass
    
    def AgregarEquipo(self, numero_parte, tipo, descripcion):
        self.__numero_parte = numero_parte
        self.__tipo = tipo
        self.__descripcion = descripcion

    @property
    def _numero_parte(self):
        return self.__numero_parte

    @_numero_parte.setter
    def _numero_parte(self, value):
        self.__numero_parte = value

    @property
    def _tipo(self):
        return self.__tipo

    @_tipo.setter
    def _tipo(self, value):
        self.__tipo = value

    @property
    def _descripcion(self):
        return self.__descripcion

    @_descripcion.setter
    def _descripcion(self, value):
        self.__descripcion = value

    def __str__(self):
        return f"Numero de Parte: {self._numero_parte} \nTipo de Equipo : {self._tipo} \nDescripcion    : {self._descripcion}\n{"-" * 30}"
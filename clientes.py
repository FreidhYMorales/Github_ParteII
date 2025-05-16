class Cliente:
    def __init__(self):
        pass
    def AgregarCliente(self, apellido, nombre, telefono):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__equipo = list() #[]
        print("-" * 30)
        print("Cliente Creado Exitosamente!!")

    @property
    def _equipo(self):
        return self.__equipo

    @_equipo.setter
    def _equipo(self, value):
        self.__equipo = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    def get_equipo(self):
        return self.equipo

    def set_equipo(self, value):
        self.equipo = value

    
    def AgregarEquipoCliente(self, equipo):
        self._equipo.append(equipo)
    
    def MostrarEquipos(self):
        for i in self._equipo:
            print(i)
        
    def __str__(self):
        return f"Nombre  : {self._nombre} \nApellido: {self._apellido} \nTelefono: {self._telefono} \n{"-" * 30}"
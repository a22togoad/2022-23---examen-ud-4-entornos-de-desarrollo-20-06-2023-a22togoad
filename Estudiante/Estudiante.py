"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Adrián Torres Gómez
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""
class Persona:
    """
    Se trata de la clase persona.
    """
    def __init__(self, nif, nombre, apellidos):
        """
        Constructor de la clase persona.
        :param nif: NIF de la persona correspondiente.
        :param nombre: Nombre de la persona.
        :param apellidos: Apellidos de la persona.
        """
        self.nif = nif;
        self.nombre = nombre;
        self.apellidos = apellidos;

class Estudiante(Persona):
    """
    Clase Estudiante, hija de la clase Persona.
    """
    nif = "11111111Z";
    curso = "Primaria";
    nombre = "Nombre";
    apellidos = "Apellidos";

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Constructor de la clase Estudiante.
        :param nif: NIF del Estudiante proveniente de Persona.
        :param curso: Curso al que pertenece el estudiante.
        :param nombre: Nombre del estudiante.
        :param apellidos: Apellidos del estudiante.
        """
        Persona.__init__(self)
        self.nif = nif;
        self.curso = curso;
        self.nombre = nombre;
        self.apellidos = apellidos;

    @property
    def nif(self):
        """
        NIF.
        :return: Recoge el NIF del estudiante.
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        Establece el NIF.
        :param value: Valor del NIF del estudiante.
        :return: NIF.
        """
        self.__nif = value

    @property
    def curso(self):
        """
        Curso.
        :return: Recoge el curso del estudiante.
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Establece el curso del alumno.
        :param value: Valor del curso.
        :return: Curso.
        """
        self.__curso = value

    @property
    def nombre(self):
        """
        Nombre
        :return: Recoge el nombre del estudiante.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Establece el nombre del estudiante.
        :param value: Valor del nombre.
        :return: Nombre.
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """
        Apellidos.
        :return: Recoge los apellidos del estudiante.
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        Establece los apellidos del estudiante.
        :param value: Valor de los apellidos del estudiante.
        :return: Apellidos.
        """
        self.__apellidos = value


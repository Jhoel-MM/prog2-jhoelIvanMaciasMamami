class Libro:
  """
  Clase que representa un libro con sus atributos principales.
  """

  def __init__(self, titulo, autor, isbn, paginas):
      """
      Constructor de la clase Libro.

      Args:
          titulo (str): Título del libro
          autor (str): Autor del libro
          isbn (str): ISBN del libro
          paginas (int): Número de páginas del libro
      """
      self.titulo = titulo
      self.autor = autor
      self.isbn = isbn
      self.paginas = paginas
      self.disponible = True

  def mostrar_info(self):
      """
      Método que imprime todos los atributos del libro de forma clara y formateada.
      """
      print("=" * 50)
      print("INFORMACIÓN DEL LIBRO")
      print("=" * 50)
      print(f"Título: {self.titulo}")
      print(f"Autor: {self.autor}")
      print(f"ISBN: {self.isbn}")
      print(f"Páginas: {self.paginas}")
      print(f"Disponible: {'Sí' if self.disponible else 'No'}")
      print("=" * 50)

  def prestar_libro(self):
      """
      Cambia el estado del libro a no disponible si está disponible,
      sino informa que ya está prestado.
      """
      if self.disponible:
          self.disponible = False
          print(f"El libro '{self.titulo}' ha sido prestado.")
      else:
          print(f"El libro '{self.titulo}' ya está prestado.")

  def devolver_libro(self):
      """
      Cambia el estado del libro a disponible si estaba prestado,
      sino informa que ya estaba disponible.
      """
      if not self.disponible:
          self.disponible = True
          print(f"El libro '{self.titulo}' ha sido devuelto y está disponible.")
      else:
          print(f"El libro '{self.titulo}' ya estaba disponible.")


# Ejemplo de uso
if __name__ == "__main__":
  # Crear dos libros
  libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-3-14-046401-7", 120)
  libro2 = Libro("Raza de Bronce", "Alcides Arguedas", "978-99905-2-213-9", 250)

  # Acceder y mostrar algunos atributos directamente
  print(f"\nEl autor del primer libro es: {libro1.autor}")
  print(f"El ISBN del segundo libro es: {libro2.isbn}")

  # Mostrar info completa
  print("\n--- Mostrando información completa ---")
  libro1.mostrar_info()
  libro2.mostrar_info()

  # Probar métodos de préstamo y devolución
  print("\n--- Probando métodos prestar_libro y devolver_libro ---")
  libro1.prestar_libro()  # Debería prestar el libro
  libro1.prestar_libro()  # Ya está prestado
  libro1.devolver_libro() # Devuelve el libro
  libro1.devolver_libro() # Ya está disponible

  libro2.prestar_libro()
  libro2.mostrar_info()

  print("\nFin del programa")
  print("Jhoel Ivan Macias Mamani")

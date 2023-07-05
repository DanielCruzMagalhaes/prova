from blog import Blog
import datetime

class Postagem(Blog):
  
  def __init__(self,__id,titulo ,texto ,dataDePublicacao):
        self.id = __id
        self.titulo = titulo
        self.texto = texto
        self.dataDePublicacao = dataDePublicacao
        

       
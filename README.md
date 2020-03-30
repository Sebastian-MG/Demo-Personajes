# Demo-Personajes
### Juan Sebastian Mancera Gaitan 20171020047 
### Pedro Enrique Barrera 20171020057
### Felipe corredor 20171020056

### El ejecutable del juego es el archivo Demojuego.py o tambien DemoOrda.py mientras se definia el proyecto.



##### Modulo Clases juego: Se crean dos clases:

-Clase Escudo: Posee los atributos Material y Sprites con sus respectivos metodos getter y setter

-Clase Personaje:  Posee los atributos Tipo,Escudo,Sprites y Ruido con sus respectivos metodos getter y setter.

![Cljuego](https://github.com/Sebastian-MG/Demo-Personajes/blob/master/UML/Clase-Juego.jpg)

##### Modulo Builder: 

-Se crea una clase padre llamada Builder_Sprites con atributos estaticos, Sprites y Plano .

-Se crea la clase padre Builder_Ruido con sus metodos sobreescribibles, y un hijo para la clase que sobreescribe el metodo de su Padre para llenar el atributo sonidos que hereda de la clase padre Builder_Ruido.

-Se crean los setters y getters respectivos para Plano y solo el get para Sprites, los setters no ya que  no se modifican los Sprites dentro de las clases hijas.

-Se crea el Metodo Build_Sprite y Build_Plano que sera sobreescrito por los hijos.

-Build_Sprite_Personaje hereda a Build_Sprites y sobreescribe el  método Build_Sprite haciendo sus propias dos direcciones para el personaje, tambien sobreescribe el método Build_Plano haciendo que sea el Plano 1 para la clase, posee un metodo constructor en el que se settea el tipo de personaje a crear.

![Builder](https://github.com/Sebastian-MG/Demo-Personajes/blob/master/UML/Builder.png)

##### Módulo Factory:

-Se crea la clase Padre Absrtract Factory con tres clases hijas




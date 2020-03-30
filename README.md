# Demo-Personajes
### Juan Sebastian Mancera Gaitan 20171020047 
### Pedro Enrique Barrera 20171020057
### Felipe corredor 20171020056

### El ejecutable del juego es el archivo Demojuego.py o tambien DemoOrda.py mientras se definia el proyecto.
### Juego realizado en Python 3 junto a las siguientes librerias:

Pygame
GC
Os
tkinter
Pil
enum
copy
functools
math
random

##### Modulo Clases juego: 

En este modulo se construyen las dos clases base para el resto de la version: Clase Escudo y Clase Personaje con sus propios metodos y atributos, estas comparten el atributo de tener sprites sin embargo la interpretacion sera diferente.

![Cljuego](https://github.com/Sebastian-MG/Demo-Personajes/blob/master/UML/Clase-Juego.jpg)

##### Modulo Builder: 


-Se crean las dos clases padre: Builder_Sprite y Builder_Ruido cada una con sus métodos sobreescribibles, se crean dos hijos del builder Sprite, cada uno sobreescribe el método  para la creacion del constructor  de diferente manera acudiendo  a diferentes direcciones en el proyecto.

-Se crea un hijo para Builder_Ruido que sobreescribe el metodo de su padre, para llenar el atributo Sonidos que hereda de la clase Build_Ruido.

![Builder](https://github.com/Sebastian-MG/Demo-Personajes/blob/master/UML/Builder.png)

##### Módulo Factory:

-Se crea la clase Padre Absrtract Factory la cual contiene un personaje vacion y metodos sobreescribibles, se crean tres clases hijas cada una con un constructor independiente que inicializa el personaje heredado del padre, le asigna un tipo y asigna los sprites y sonidos correspondientes segun los metodos correspondientes.

-Cada clase hija sobreescribe los metodos de la clase padre para crear un Builder correspondiente al tipo de Personaje de cada hija, luego lo asigna al Personaje, lugo crea un tipo de sonido correspondiente a cada clase hija y se lo asigna al personaje propio.


![Factory](https://github.com/Sebastian-MG/Demo-Personajes/blob/master/UML/fact.png)

#### Módulo Prototype

-Se crea la clase padre Prototype que contiene un personaje Padre vacio y un metodo de clonado, se crean tres clases hijas que completan el atributo Personaje heredado con lo que devuelva una Fabrica del módulo Factory luego se crea un getter para el personaje heredado y se sobreescribe el método copy para realizar una copia profunda (deep copy) del personaje heredado.

-Se crea un Objeto Factoria el cual es un objetyo abstracto que contiene todos los prototipos del módulo, se crean los getters únicos para cada uno de los prototipos en el objeto factoria.


![Proto](https://github.com/Sebastian-MG/Demo-Personajes/blob/master/UML/Proy.png)


##### Módulo DemoJuego y  DemoOrda:

Se crea la clase PersJugable que hereda de Sprite de pygame y se le introduce un personaje traido del Modulo Prototype, se definen los metodos para que al ejecutarse la clase funcione para la creacion de un personaje el cual el usuario pueda desplazar.

.Se crea una clase PersNPC que hereda del PersJugable con un método llamado existir que lo hace independiente del usuario.

-Se crea metodo main en el cual se inicializa una ventana de Pygame, se traen los objetos Prototype del Object Factory, se incializa un personaje jugable con uno de los objetos de factoria y se crea un array de personajes aleatorios del Object Factory, se realiza el dibujado en pantalla de este y se programan eventos para que el  usuario pueda desplazar de izquierda a derecha al objeto jugable y que reproduzca sonidos y que los demas objetos del array lo persigan dibujandose esto en pantalla. 

![Demojuego](https://github.com/Sebastian-MG/Demo-Personajes/blob/master/UML/DemoJUego.png)




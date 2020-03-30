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

![Demojuego](https://github.com/Sebastian-MG/Demo-Personajes/blob/master/UML/Clase-Juego.jpg


![DemoOr](https://github.com/Sebastian-MG/Demo-Personajes/blob/master/UML/DemoJUego.png)

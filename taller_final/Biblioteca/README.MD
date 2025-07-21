# **Sistema Gestor para Bibliotecas**

Esta aplicacion fue realizada con la intencion de gestionar actividades en una biblioteca por mediode un CLI (Interfaz de Lineas de Comando). Presenta tanto funcionalidades CRUD (Crear, Leer, Actualizar, Eliminar) para la gestion de libros y usuario, como servicio de gestion de prestamo y multas.

## Cómo ejecutar el programa

- Clonar el repositorio:

    [Github Repo](https://github.com/Juan-Wills/Python_2847248.git)

    `git clone https://github.com/Juan-Wills/Python_2847248.git`

- Ingresar a la carpeta del projecto:

    `cd taller_final/Biblioteca`

- Ejecutar el programa:

    `python main.py`


## Dependencias requeridas

- Instalar dependencias:

    `pip install -r requirements.txt`

>Para mas informacion revisar el documento "requirements.txt" e ir a la documentacion de cada dependencia.

## Navegar la aplicacion

Al momento de ejecutar el programa se mostrara el menu principal, 
despues se debera elegir alguna de las opciones disponibles enumeradas por medio de su indice.

![img main.py menu](imgs%20MD/main%20menu.jpg)

Una vez elegida alguna opcion, se redirigira a alguna de las siguientes vistas:

**Libros**
        
![img book main menu](imgs%20MD/book%20main%20menu.jpg)

**Usuario**

![img user main menu](imgs%20MD/user%20main%20menu.jpg)

**Prestamo y Devoluciones**

![img loan main menu](imgs%20MD/loan%20main%20menu.jpg)

**Multas**

![img fine main menu](imgs%20MD/multa%20main%20menu.jpg)

### Libros y Usuario

Debido a que la estructura de usuarios y libros resulta ser similar, se explicaran sus funcionalidades de manera conjunta.

#### Agregar nuevo registro

El usuario debera llenar los campos con las caracteristicas del "sujeto" (libro o usuario) que desea ingresar.

- Caso de libro:

    ![img add book (filled fields)](imgs%20MD/add%20book%20(details).jpg)

- Caso de usuario:
    
    ![img add user (filled fields)](imgs%20MD/add%20user%20(details).jpg)

Despues de llenar los campos, se mostrara una vista previa de las caracteristicas del nuevo "sujeto" y se debera confirmar su creacion para ser agregados en la base de datos.

- Caso de libro:
    
    ![img add book (filled fields)](imgs%20MD/add%20book%20(confirm).jpg)

- Caso de usuario:
    
    ![img add user (filled fields)](imgs%20MD/add%20user%20(details).jpg)

En caso de rechazarlo se volvera al menu.

#### Buscar por categoria

El usuario debera elegir la caracteristica (categoria) por la cual desea filtrar los resultados de busqueda.

En caso de elegir la opcion 'Ver todos', no se realizara ningun filtro y se mostraran todos los registro en la base de datos.

- Caso libro:
    
    ![img find book (all)](imgs%20MD/find%20book%20(all).jpg)

- Caso usuario:

    ![img find user (all)](imgs%20MD/find%20user%20(all).jpg)

En caso de elegir cualquier otra opcion, el usuario debera ingresar la informacion respecto a la categoria de busqueda.

Por ejemplo: 

Categoria: correo, Informacion: jane@example.com

- Caso libro:
    
    ![img find book (spec)](imgs%20MD/find%20book%20(specific).jpg)

- Caso usuario:
    
    ![img find user (spec)](imgs%20MD/find%20user%20(specific).jpg)

#### Actualizar registro

El usuario debera elegir una categoria de busqueda para el "sujeto" que desea actualizar. 
Si se encuentra mas de una coincidencia, el programa pedira al que se utilice otro criterio de busqueda como por ejemplo un id.

Al encontrar el resultado, mostrara las caracteristicas del mismo en pantalla.

- Caso libro:
    
    ![img upd book (find)](imgs%20MD/update%20book%20(find).jpg)

- Caso usuario:
    
    ![img upd user (find)](imgs%20MD/update%20user%20(find).jpg)

Se pedira al usuario que seleccione al caracteristica que desea modificar, seguido de esto debera llenar un campo con la nueva informacion.

- Caso libro:
    
    ![img upd book (upd info)](imgs%20MD/update%20book%20(category).jpg)

- Caso usuario:
    
    ![img upd user (upd info)](imgs%20MD/update%20user%20(update%20info).jpg)

Por ultimo, debera confirmar los cambios para guardarlos las modificaciones.

- Caso libro:
    
    ![img upd book (confirm)](imgs%20MD/update%20book%20(confirm).jpg)

- Caso usuario:
    
    ![img upd user (confirm)](imgs%20MD/update%20user%20(confirm).jpg)

En caso de rechazarlos se volvera al menu.

#### Eliminar
El usuario debera ingresar el id del 'sujeto' a eliminar. Si se desea ingresar mas de un id estos deberan estar separados por una coma.

- Caso libro:
    
    ![img upd book (confirm)](imgs%20MD/delete%20book.jpg)

- Caso usuario:
    
    ![img upd user (confirm)](imgs%20MD/delete%20user.jpg)

Por ultimo, se debera confirmar la eliminacion de/los "sujetos", en caso de rechazarlos se volvera al menu.

### Prestamos y Multas
Para realizar un prestamo se necesita que haya al menos un registro de cada "sujeto" (libro y usuario) y que el libro a prestar se encuentre disponible.

#### Crear presatamo


## Decisiones de diseño tomadas

Explica las elecciones clave de diseño, arquitectura, tecnologías o algoritmos que se hicieron durante el desarrollo del proyecto y por qué se tomaron esas decisiones.

- ![Decisión de Diseño 1](imgs%20MD/): Breve explicación de la decisión y la razón detrás de ella (por ejemplo, "Se eligió React para la interfaz de usuario debido a su ecosistema robusto y su enfoque basado en componentes para una UI escalable.").

- ![Decisión de Diseño 2](imgs%20MD/): Justificación de por qué se prefirió esta opción sobre otras alternativas (por ejemplo, "Se optó por una base de datos NoSQL para manejar datos no estructurados y permitir una escalabilidad horizontal más sencilla.").

- ![Decisión de Diseño 3](imgs%20MD/): Cualquier compromiso o consideración importante (por ejemplo, "Se priorizó la velocidad de desarrollo sobre la optimización extrema del rendimiento en la fase inicial.")

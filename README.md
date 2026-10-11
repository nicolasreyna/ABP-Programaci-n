Somos el grupo "SINERGIA DIGITAL" de la universidad ISPC de cordoba. 


En este proyecto construimos la interfaz de una app con Tkinter y TTK, una base de datos relacional y funcional en SQlite Ademas se incorporó OS que es un módulo de la biblioteca estándar de Python y en este proyecto se utilizo para construir correctamente la ruta hacia el archivo de imagen (os.path.join(carpeta_proyecto, "LOGO APP.png"))

La APP, incluye un sistema de gestión de almacen total, donde estan modulos de compra, venta, cliente, vendedores.

En primer lugar, se utilizaron Frames para dividir cada tabla en los archivos de doble tabla como AbpAplicacion.py y CicloDeCompras.py y para los de una tabla tmb se utilizaron frames. Main.py, Ventas.py y vendedor.py. Se utilizaron comboboxes, treeviews, Notebook para pestañas dentro de la aplicacion, donde se puede acceder a cada seccion de la aplicacion. Se dividio en funciones, para mejor legibilidad y mantenimiento de codigo. En los botones se agregaron, agregar_*, modificar_*, borrar_*. Despues se agrego mini funciones como cargar tabla para cargar la tabla en DB, con otra mini funcion llamada id_siguiente() que integra el autoincrement de SQlite en python, haciendo que por cada registro que haya, sacar el maximo de esa lista y devolver +1, si no hay devuelve id=1. Hay otra funcion llamada campo que es el entry. 

Seguimos Ahora con la carpeta Base De Datos, Aqui se realizaron 3 cosas claves. El __init_.py hace que la carpeta base de datos se vuelva en un paquete modularizado para que python lo extraya. Despues se creo el archivo conexion.py, donde se establece la base de datos y se crea si no existe, tambien se define un obtener_conexion para los archivos que utilicen la base de datos y necesiten enviar aquellos datos a esa base de datos. Por ultimo al final del archivo conexion.py, se define una funcion que se llama crear_tabla() que se ejecutara en main.py, por si se detecta que las tablas que se supone que deberian estar NO estan, las carga igual. POR ULTIMO, todos los archivos como cliente_db.py se relacionan directamente con lo que se ve en la interfaz, los datos y los atributos estan todos vinculados, ademas de que integrados a los botones de cada uno de los botones de la interfaz, estableciendo una conexion total entre todas las tablas. 

*ACLARACION, hay cosas por terminar y pulir, por ejemplo que el id_cliente  aun borrando los registros siga incrementando, osea si se borra un cliente con ID=2, tecnicamente el proximo deberia tener el ID=2 porque ese ID no esta ocupado, en cambio la aplicacion muestra ID=3, asumiendo que hay un ID=2. 



Para ejecutar la aplicacion, se tiene que dirigir a Main.py y simplemente correrlo desde allí. La contraseña es 1234. 

*IMPORTANTE, LA APLICACION ESTA SUJETA A FOREIGN KEYS = ON, POR ENDE SI SE BORRA UN REGISTRO Y ESTA SUJETO A OTRA TABLA COMO UNA CLAVE FORAÑEA, NO TE VA A DEJAR BORRARLA Y DESPUES SE TE BLOQUEA ACCESO. PARA SOLUCIONARLO, SOLAMENTE ABRIR Y CERRAR APLICACION.


Se procuró a que todos los miembros pudiesen constribuir al proyecto, incluyendo commits de los colaboradores, Benjamin Morgado, Fiamma Tissera, Guido Mandile y el creador del repositorio, Nicolas Reyna.


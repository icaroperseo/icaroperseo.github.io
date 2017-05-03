##################################
Contenedores cifrados en GNU/Linux
##################################

:date: 2017-04-07 01:35:07
:modified: 2016-05-03 03:01
:tags: How to, Privacidad, Contenedores
:category: GNU/Linux
:slug: contenedores-cifrados-en-gnu-linux
:authors: Icaro Perseo
:summary: ctmg es un bash script que permite la creación de contenedores cifrados valiéndose exclusivamente de utilidades estándar del sistema, lo cual evita tener que recurrir al uso de aplicaciones externas.

.. ----------------------------------------------------------------------------
.. role:: kbd
.. ----------------------------------------------------------------------------

.. image:: images/lock_usb_pen_drive.jpeg
    :alt: Logotipo pen drive USB
    :align: center
    :class: img-thumbnail

`ctmg <https://git.zx2c4.com/ctmg/about/>`__ es un gestor de archivos contenedores cifrados para sistemas GNU/Linux, escrito en el lenguaje de comandos *bash*, el cual hace uso exclusivamente de `cryptsetup <https://gitlab.com/cryptsetup/cryptsetup>`__ además de `otras utilidades estándar del sistema de archivos <https://es.wikipedia.org/wiki/E2fsprogs>`__.

Este *script* crea archivos contenedores a partir de un nombre y tamaño dado para posteriormente asignarle de forma automática la extensión ``.ct``. Durante el proceso de creación del contenedor se le pedirá al usuario introducir la contraseña de *root* y una **frase contraseña**, la cual será solicitada cada vez que se desee acceder al contenido del archivo. Una vez creado el archivo contenedor es posible realizar diversos tipos de operaciones, mismas que se detallan a continuación.

***************
Funcionalidades
***************

-  ``n`` \| ``new`` \| ``create``: crea un nuevo archivo contenedor, dependiendo del tamaño que se le haya designado. Es importante señalar que el tamaño de los archivos contenedores cambia de forma dinámica durante su vida útil, es decir que no se reserva de forma predeterminada la totalidad del espacio asignado para el archivo contenedor, optimizando o modificando su tamaño en relación de su propio contenido sin exceder, en ningún momento, el limite establecido. Si este característica le resulta indeseable, es posible modificar su comportamiento para que realice lo contrario, para ello tendrá que recurrir a la documentación oficial.
-  ``d`` \| ``del`` \| ``delete``: elimina, de forma permanente, un archivo contenedor al igual que su directorio temporal.
-  ``o`` \| ``open``: abre un archivo contenedor existente. Lo anterior creará un directorio temporal, con el mismo nombre del archivo contenedor, y copiará el contenido del archivo hacia este último.
-  ``c`` \| ``close``: cierra un contenedor. Esto eliminará el directorio temporal, su contenido será guardado dentro del archivo contenedor antes de realizar esta operación.
-  ``l`` \| ``list``: lista todos los directorios temporales existentes.
-  ``h`` \| ``help`` \| ``-h`` \| ``--help``: muestra un breve resumen sobre cómo utilizar *ctmg*.

Ejemplos de uso
===============

Crear un nuevo contenedor
-------------------------

.. code-block:: bash

    ctmg new foo 100MiB

Donde:

-  ``foo``: nombre que se le dará al nuevo archivo contenedor.
-  ``100MiB``: tamaño designado para el nuevo contenedor, 100 megabytes en este caso.

Abrir un archivo contenedor
---------------------------

.. code-block:: bash

    ctmg open foo

.. class:: well

    :label-info:`Información:` Una vez abierto el archivo es posible copiar, mover, crear o manipular archivos y directorios en su interior durante el periodo de tiempo que permanezca montado dicho contenedor.

Cerrar un archivo contenedor
----------------------------

.. code-block:: bash

    ctmg close foo

.. class:: well

    :label-info:`Información:` Recurra a la página oficial del proyecto para mayor información, ejecute: :kbd:`ctmg h` o bien: :kbd:`man ctmg` para aquellas distribuciones derivadas de *Arch Linux*, incluyendo a esta última.

***********
Instalación
***********

Es posible encontrar un paquete de instalación para *Arch Linux* y derivadas al recurrir al repositorio *AUR*, por ejemplo:

.. code-block:: bash

    sudo yaourt -S ctmg

Asimismo, existe un paquete para *Gentoo Linux* y derivadas, para ello basta con ejecutar el siguiente comando como *superusuario*:

.. code-block:: bash

    emerge ctmg

Para el resto de distribuciones GNU/Linux resulta necesario instalar las equivalencias a los siguientes paquetes: *cryptsetup*, *e2fsprogs*, *sudo*, *coreutils*; `descargar ctmg <https://git.zx2c4.com/ctmg/snapshot/ctmg-1.2.tar.xz>`__ desde el repositorio oficial, descomprimir su contenido y una vez se ha accedido al directorio en cuestión, desde la terminal ejecutar como *root*:

.. code-block:: bash

    make install

**********************
Consideraciones de uso
**********************

-  Resulta imperativo el poder acceder al sistema como superusuario.
-  *ctmg* es útil para mantener la privacidad de la información más no garantiza la autenticidad de la misma. Si alguna persona manipula de forma intencional el archivo *.ct* es muy posible que resulte comprometida la integridad y/o veracidad de los datos almacenados en el interior del contenedor.
-  Actualmente solo es posible utilizar *ctmg* en sistemas *Linux-like*.

*******************
Alternativas a ctmg
*******************

-  `Tomb <https://www.dyne.org/software/tomb/>`__
-  `VeraCrypt <https://veracrypt.codeplex.com/>`__
-  `SiriKali <https://mhogomchungu.github.io/sirikali/>`__
-  `Cryptkeeper <http://tom.noflag.org.uk/cryptkeeper.html>`__

.. alert:: **Notas finales:** El hecho de poder emplear exclusivamente utilidades estándar aunado a la rapidez de ejecución y facilidad de uso que brinda *ctmg* lo convierte en un verdadero *must to have*. Las carencias de portabilidad que *ctmg* presenta se pueden compensar cabalmente por sus propias virtudes. Para finalizar, si tuviera que citar una alternativa ideal al mismo diría que *tomb* es la opción a elegir con total seguridad.
    :type: success

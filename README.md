# TiendaLaGenerica
App creada para administrar varios aspectos de un negocio, como clientes, ventas, reportes, reportes a gran escala, proveedores, etc.
Utiliza Python, javascript, html, css para funcionar, con ciertas apps de python que hay que previamente instalar, y hay otras apps que vienen con el programa
y que hay que correr de forma sincronica utilizando el runserver de django como:
- (puerto 8001)micproductos: https://github.com/Leal31/micproductos 
- (puerto 8002)micclientes: https://github.com/Leal31/micclientes
- (puerto 8003)micproveedores : https://github.com/Leal31/micproveedores
- (puerto 8004)micventas : https://github.com/bryanes13/micventas
- (puerto 8005)micconsolidado : https://github.com/AngelMelo03/micconsolidado

- Si se desea correr la app de forma remota
Pasos a seguir:
- Tener python3
- Tener mongodb
- Tener pip que va con python3
- Descargar o clonar el repositorio
- Dentro de la carpeta del repositorio se abre una terminal y se hara el siguiente comando:
  - pip install -r requirements.txt
  Eso hara que se instalen todos los programas que utiliza el programa para funcionar
- Manualmente dentro de cada microservicio mencionado anteriormente se ejecutara "python manage.py migrate" eso hara que se creen automaticamente las bases
de datos dentro de mongodb
- luego se correran los 5 microservicios en los puertos especificados con "python manage.py runserver puerto" a la misma vez(la pagina principal no esta sujeta
a un puerto en especifico
- podras correr sin problema la pagina

# Project_m

## Pasos seguidos:

- Se ha creado un entorno virtual,  en este caso mediante
	pip install virtualenv
 
- Se creado y activado el entorno virtual ‘env_site’
- En el entorno virtual se ha instalado django
- Se ha iniciado el proyecto_m
  
Se inicia el servidor  mediante mange.py  que pertenece a django, al cual podemos acceder mediante la Url:

	http://127.0.0.1:8000/
### Estructura inicial

Para crear la estructura inicial se ha instalado django rest frameworks,  que es un complemento de django para desarrollar apis de forma rápida y que además proporciona una interfaz gráfica, (a través de de las vistas que tiene implementadas), facilitando de este modo hacer pruebas.

En el archivo setting.py del proyecto se añade a las aplicaciones instaladas del “rest_framework” para que se pueda utilizar desde django.

Una vez instalado DRF mediante manage.py inicializamos una api vacía, para el proyecto, esto, crea la carpeta api, y se debe añadir a las aplicaciones instaladas del archivo settings.py, “api.apps.ApiConfig”.


### Modelo
Para la creación del modelo Crearemos un modelo de producto. La API utilizará este modelo para realizar las operaciones de CRUD.

	name = models.CharField(max_length=255, unique=True)
	
		* unique → no permite que se repitan los nombres

	detail = models.CharField(max_length=255)

	creation_date = models.DateTimeField(auto_now_add=True)
	
		* auto_now_add →  añade la fecha solo cuando se crea ***

	update_date = models.DateTimeField(auto_now=True)
		
		* auto_now → añade la fecha cuando se actualiza

### Serializadores
A continuación  se han de crear los serializadores, en api/serializer.py.
DRF  se encargan de la serialización y deserialización de datos y leer y escribir en  base de datos.

Se utiliza el ModelSerializer mapeando el producto que además de serializar y deserializar,  permite,  crear, actualizar  y  borrar.

### Vistas
Crear vistas: 
 en apis/views.py se crean tres vistas.

Lista:  
	ProductList(generics.ListAPIView)

Creación: 
	ProductCreate(generics.CreateAPIView)

Detalle:
	ProductDetail(generics.RetrieveUpdateDestroyAPIView)

### URLS
Por último  queda indicar la ruta de los end points correspondientes a cada vista. en 
api/urls.py 

urlpatterns:

	path('', ProductList.as_view()), → Para ver los productos
		se accede  accede directamente  con la url: http://127.0.0.1:8000/

	path('create', ProductCreate.as_view()), → Para crear productos
		se accede  accede directamente  con la url: http://127.0.0.1:8000/create
		
	path('<int:pk>', ProductDetail.as_view()), → Para actualizar y borrar productos.
		se accede  accede directamente  con la url: http://127.0.0.1:8000/(pk del producto)


y product/urls.py indicamos que mire las url de la api.

urlpatterns:
	
	path('', include('api.urls'))

Para arrancar el servicio en local.

	source env_site/bin/activate
	./manage.py runserver



### Docker 
#### crear imagen:

	docker build -t project_m .

#### arrancar un contenedor la la imagen:
	docker run -it -p 8000:8000 project_m


### Instrucciones

#### Cómo listar productos

	curl --location --request GET 'http://127.0.0.1:8000/'

#### Crear producto

	curl --location --request POST 'http://127.0.0.1:8000/create' \
	--header 'Content-Type: application/json' \
	--data-raw '{
   		"name": "product_name",
   		"detail": "product detail"
		}'

#### Actualizar producto

	curl --location --request PUT 'http://127.0.0.1:8000/<pk>' \
	--header 'Content-Type: application/json' \
	--data-raw '{
   		"name": "product_name_updated",
   		"detail": "product detail"
	}'

#### Borrar producto
	
	curl --location --request DELETE 'http://127.0.0.1:8000/<pk>'

#### Ver detalle del producto
	
	curl --location --request GET 'http://127.0.0.1:8000/<pk>'

# Conclusiones - Tarea T02.04

La implementación de pruebas unitarias al Sistema de Gestión Académica (SGA) 
permitió verificar de manera sistemática el correcto funcionamiento de cada 
componente del backend desarrollado en la tarea anterior. Utilizando Pytest y 
Coverage.py como frameworks principales, se lograron 120 pruebas distribuidas 
en cuatro niveles: modelos, repositorios, servicios y controladores.

El análisis de cobertura alcanzó el 89% del código, superando ampliamente el 
60% requerido. Los módulos de modelos y servicios alcanzaron el 100% de 
cobertura, mientras que repositorios llegó al 99%. Esto demuestra que las 
pruebas cubren prácticamente todos los escenarios posibles del sistema.

La experiencia de escribir pruebas unitarias evidenció la importancia de diseñar 
código testeable desde el inicio. La arquitectura modelo/repositorio/servicio/ 
controlador facilitó enormemente la creación de pruebas aisladas para cada capa, 
ya que cada componente tiene responsabilidades bien definidas.

El uso de fixtures en Pytest para limpiar la base de datos entre pruebas garantizó 
la independencia de cada test, evitando efectos secundarios. Además, el TestClient 
de FastAPI permitió simular peticiones HTTP reales sin necesidad de levantar el 
servidor, agilizando la ejecución de las pruebas.

En conclusión, las pruebas unitarias son una práctica fundamental en el desarrollo 
de software de calidad, ya que detectan errores tempranamente y documentan el 
comportamiento esperado del sistema.
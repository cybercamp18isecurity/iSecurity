# WebServer de iSecurity

Backend de iSecurity que contiene los diversos Endpoints de la aplicación, que consumirán la app de Google Home y el Front End.

### Instalación

### Configuración

Para configurarlo, sólamente tenemos que fijar las credenciales de la instancia de Elasticsearch que usemos en el archivo de `src/configuration.ini`.

Este archivo tiene la siguiente estructura:
```ini
[elasticsearch]
host = ip_host
port = 9200 #default
user = usuario
password = password
```

Se incluye un ejemplo en `src/configuration.example.ini`
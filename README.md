## IntelligentSecurity
IntelligentSecurity is a free software project that allows you to keep track of the security status of an organization in a simple and intuitive way using different devices, such as your smartphone or google home.

## Main components and system architecture
The system architecture is shown below.

![Alt text](doc/images/network_diagram.png?raw=true "Network")

- **Analysis server**: Receive information from all hosts on the network and from network devices. It is formed by the following technologies:
  - **Elastic Search**: https://www.elastic.co
  - **iSecurityDetection**: https://github.com/cybercamp18isecurity/iSecurityDetection

- **Mobile app & other devices**: It allows users without technical knowledge of cybersecurity to interact with the security status of their organization through touch on the screen of their smartphone or through the voice. Supported technologies:
  - **Mobile App**: https://github.com/cybercamp18isecurity/iSecurityApp
  - **Google Home Assistant**: https://github.com/cybercamp18isecurity/iSecurityAssistant


*For more information about each of the components, visit the specific readme of the project*

## Installation

## Repositorios:
- Front End (Asistente): https://github.com/cybercamp18isecurity/iSecurityAssistant
- Back End (Esqueleto): https://github.com/cybercamp18isecurity/iSecurityWebService
- Elasticsearch sdk: https://github.com/cybercamp18isecurity/elasticsearch_sdk
- iSecurity Detector: https://github.com/cybercamp18isecurity/iSecurityDetection


# WebServer de iSecurity

Backend de iSecurity que contiene los diversos Endpoints de la aplicación, que consumirán la app de Google Home y el Front End.

### Instalación

# TODO: DOCKER

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

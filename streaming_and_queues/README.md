Usaremos [pulsar](https://pulsar.apache.org/) para experimentar con streaming y colas de mensajes.

## Prerrequisitos
Se requiere de java 17 o superior y una instalación de python con el [cliente de pulsar](https://pypi.org/project/pulsar-client/).

## Instalaciones
1. Instalar pulsar:
```bash
curl -LO "https://www.apache.org/dyn/closer.lua/pulsar/pulsar-4.0.2/apache-pulsar-4.0.2-bin.tar.gz?action=download"
tar xvfz apache-pulsar-4.0.2-bin.tar.gz
cd apache-pulsar-4.0.2
ls -1F
```

2. Iniciar servidor standalone:
```bash
bin/pulsar standalone
```

Pulsar debe haberse iniciado correctamento.
- Broker en localhost:6650
- Servicio en localhost:8080

3. En caso de no contar con el cliente de python:
```python
pip install pulsar-client
```
Ahora puede correr los scripts del proyecto.

## Miscelánea
Para revisar estadísticas de tópicos:
```bash
pulsar-admin topics stats my-topic
```

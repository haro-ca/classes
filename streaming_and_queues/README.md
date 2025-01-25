Usaremos pulsar para experimentar con streaming y colas de mensajes.

Prerrequisito: java 17 o superior

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

Ahora puede correr los scripts del proyecto.

Para revisar estadísticas de tópicos:
```bash
pulsar-admin topics stats my-topic
```

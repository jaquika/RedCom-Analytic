# RedCom Analytic

## Simulador avanzado de red de comunicaciones con análisis de tráfico

**RedCom Analytic** es un simulador académico de redes de comunicaciones **LAN/WAN** desarrollado en Python. El sistema permite configurar topologías de red, parametrizar enlaces, simular el tránsito de paquetes, detectar congestión, calcular métricas de rendimiento, generar gráficas estadísticas y almacenar resultados históricos en una base de datos SQLite.

El proyecto integra principios de **Programación Orientada a Objetos**, análisis de datos con **Pandas** y **NumPy**, visualización con **Matplotlib**, persistencia de información con **SQLite** y validación mediante **pruebas unitarias con Pytest**.

---

## Índice

1. [Descripción general](#descripción-general)
2. [Objetivo del proyecto](#objetivo-del-proyecto)
3. [Alcance del sistema](#alcance-del-sistema)
4. [Requisitos técnicos implementados](#requisitos-técnicos-implementados)
5. [Arquitectura del proyecto](#arquitectura-del-proyecto)
6. [Estructura de carpetas](#estructura-de-carpetas)
7. [Funcionamiento del sistema](#funcionamiento-del-sistema)
8. [Instalación](#instalación)
9. [Ejecución](#ejecución)
10. [Métricas calculadas](#métricas-calculadas)
11. [Análisis de datos](#análisis-de-datos)
12. [Gráficas generadas](#gráficas-generadas)
13. [Base de datos SQLite](#base-de-datos-sqlite)
14. [Pruebas unitarias](#pruebas-unitarias)
15. [Resultados de ejemplo](#resultados-de-ejemplo)
16. [Limitaciones](#limitaciones)
17. [Trabajos futuros](#trabajos-futuros)
18. [Información académica](#información-académica)
19. [Autoría](#autoría)

---

## Descripción general

El sistema **RedCom Analytic** fue diseñado como una herramienta académica para representar de manera simplificada el comportamiento de una red de comunicaciones. A través de una interfaz por consola, el usuario puede configurar redes **LAN** o **WAN**, establecer parámetros de transmisión y ejecutar simulaciones de envío de paquetes.

Durante la simulación, el sistema registra eventos relacionados con el tráfico de red, identifica paquetes recibidos o perdidos, detecta situaciones de congestión y calcula indicadores de rendimiento. Posteriormente, los resultados pueden ser exportados, analizados estadísticamente y visualizados mediante gráficas.

Este proyecto permite relacionar conceptos de programación, análisis de datos y telecomunicaciones en un solo sistema funcional.

---

## Objetivo del proyecto

Desarrollar un simulador académico de redes de comunicaciones **LAN/WAN** que permita analizar el comportamiento del tráfico mediante el envío de paquetes, la detección de congestión, el cálculo de métricas de rendimiento, la generación de gráficas estadísticas y el almacenamiento de resultados históricos.

---

## Alcance del sistema

El sistema permite:

- Configurar redes LAN y WAN.
- Crear nodos de red como hosts, routers y switches.
- Definir enlaces con parámetros de velocidad, latencia, pérdida y capacidad de cola.
- Simular el envío de paquetes entre un origen y un destino.
- Detectar paquetes perdidos durante la transmisión.
- Detectar congestión en enlaces de red.
- Registrar eventos de la simulación.
- Calcular métricas de rendimiento.
- Exportar resultados en formato CSV.
- Analizar resultados con Pandas y NumPy.
- Generar gráficas con Matplotlib.
- Almacenar resultados históricos en SQLite.
- Ejecutar pruebas unitarias con Pytest.
- Generar evidencia del funcionamiento del sistema.

---

## Requisitos técnicos implementados

| Requisito | Implementación en el proyecto |
|---|---|
| Programación Orientada a Objetos | Clases para nodos, hosts, routers, switches, enlaces, paquetes y redes |
| Herencia | Las clases `Host`, `Router` y `Switch` heredan de la clase base `Nodo` |
| Encapsulamiento | Cada clase administra sus propios atributos y comportamientos |
| Polimorfismo | Los dispositivos de red comparten una estructura base y especializan su comportamiento |
| Abstracción | La clase `Nodo` representa características comunes de los dispositivos de red |
| Simulación de paquetes | El motor ejecuta el envío de paquetes entre nodos |
| Detección de congestión | Se evalúa la cola de paquetes frente a la capacidad del enlace |
| Análisis de datos | Procesamiento con Pandas y NumPy |
| Visualización | Gráficas estadísticas con Matplotlib |
| Persistencia | Resultados almacenados en SQLite |
| Pruebas unitarias | Validación de módulos mediante Pytest |
| Exportación | Resultados en CSV y archivos de evidencia |

---

## Arquitectura del proyecto

El proyecto sigue una **arquitectura modular orientada a objetos**. Cada carpeta agrupa responsabilidades específicas del sistema, lo que facilita la organización, mantenimiento y escalabilidad del código.

| Módulo | Responsabilidad |
|---|---|
| `modelos/` | Define las clases principales del sistema |
| `simulacion/` | Contiene la lógica de tráfico, congestión, eventos y métricas |
| `analisis/` | Procesa datos, genera estadísticas, gráficas y reportes |
| `base_datos/` | Gestiona la conexión y almacenamiento en SQLite |
| `interfaz/` | Administra el menú y la interacción por consola |
| `utils/` | Contiene funciones auxiliares, logs y validaciones |
| `tests/` | Incluye pruebas unitarias del sistema |
| `data/` | Almacena la base de datos y resultados persistentes |
| `exports/` | Guarda archivos CSV, gráficas e informes |
| `logs/` | Registra eventos del sistema |

---

## Estructura de carpetas

```text
RedCom-Analytic/
│
├── main.py
│
├── modelos/
│   ├── nodo.py
│   ├── host.py
│   ├── router.py
│   ├── switch.py
│   ├── enlace.py
│   ├── paquete.py
│   ├── red.py
│   ├── red_lan.py
│   ├── red_wan.py
│   └── simulacion.py
│
├── simulacion/
│   ├── trafico.py
│   ├── congestion.py
│   ├── eventos.py
│   └── metricas.py
│
├── analisis/
│   ├── estadisticas.py
│   ├── graficas.py
│   └── reportes.py
│
├── base_datos/
│   ├── conexion_sqlite.py
│   ├── guardar_resultados.py
│   └── historial.py
│
├── interfaz/
│   ├── menu.py
│   ├── configuracion_lan.py
│   ├── configuracion_wan.py
│   ├── visualizacion.py
│   └── panel_resultados.py
│
├── utils/
│   ├── logs.py
│   ├── validaciones.py
│   └── helpers.py
│
├── data/
│   └── simulaciones.db
│
├── exports/
│   ├── csv/
│   ├── pdf/
│   └── graficas/
│
├── logs/
│   └── eventos_redcom.txt
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

## Funcionamiento del sistema

El flujo general del sistema es el siguiente:

```text
Inicio del sistema
        ↓
Preparación del entorno
        ↓
Menú principal
        ↓
Configuración de red LAN o WAN
        ↓
Parametrización de enlaces
        ↓
Ejecución de simulación
        ↓
Envío de paquetes
        ↓
Detección de pérdida y congestión
        ↓
Cálculo de métricas
        ↓
Exportación de resultados
        ↓
Análisis con Pandas y NumPy
        ↓
Generación de gráficas
        ↓
Almacenamiento en SQLite
```

El archivo `main.py` funciona como punto de entrada del sistema. Desde este archivo se prepara el entorno, se registra el inicio del programa y se ejecuta el menú principal.

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/jaquika/RedCom-Analytic.git
```

### 2. Ingresar a la carpeta del proyecto

```bash
cd RedCom-Analytic
```

### 3. Crear el entorno virtual con uv

```bash
uv venv
```

### 4. Activar el entorno virtual en Windows PowerShell

```powershell
.\\.venv\\Scripts\\Activate.ps1
```

Si PowerShell bloquea la activación del entorno, ejecutar:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Luego volver a activar:

```powershell
.\\.venv\\Scripts\\Activate.ps1
```

### 5. Instalar dependencias

```bash
uv pip install -r requirements.txt
```

---

## Ejecución

Para ejecutar el sistema:

```bash
uv run python main.py
```

También puede ejecutarse con el entorno virtual activado:

```bash
python main.py
```

Al iniciar, el sistema muestra un menú en consola desde el cual se puede configurar una red, ejecutar simulaciones, exportar resultados, generar gráficas y consultar el historial almacenado.

---

## Menú principal del sistema

```text
1. Configurar red LAN
2. Configurar red WAN
3. Ejecutar simulación
4. Exportar resultados CSV
5. Analizar resultados con Pandas y NumPy
6. Generar gráficas con Matplotlib
7. Ver historial SQLite
8. Salir
```

---

## Métricas calculadas

| Métrica | Descripción |
|---|---|
| Paquetes enviados | Cantidad total de paquetes generados en la simulación |
| Paquetes recibidos | Cantidad de paquetes que llegaron correctamente al destino |
| Paquetes perdidos | Cantidad de paquetes descartados durante la transmisión |
| Tasa de pérdida | Porcentaje de paquetes perdidos respecto al total enviado |
| Latencia promedio | Tiempo promedio de transmisión de los paquetes recibidos |
| Throughput | Rendimiento efectivo de la red |
| Eventos de congestión | Cantidad de momentos en los que la cola superó su capacidad |

---

## Detección de congestión

La congestión se detecta cuando la cantidad de paquetes acumulados en la cola de un enlace supera la capacidad máxima definida para dicho enlace.

```text
Si cola_paquetes > capacidad_cola:
        existe congestión
```

Este criterio permite representar de forma simplificada el comportamiento de una red saturada, donde el exceso de tráfico puede incrementar la latencia y provocar pérdida de paquetes.

---

## Análisis de datos

El sistema utiliza **Pandas** y **NumPy** para procesar los resultados exportados en CSV. Este análisis permite calcular estadísticas adicionales, como:

- Latencia mínima.
- Latencia máxima.
- Latencia promedio.
- Desviación estándar de latencia.
- Cantidad de paquetes recibidos.
- Cantidad de paquetes perdidos.
- Eventos de congestión.

El análisis de datos permite interpretar el comportamiento de la red de forma más precisa y fundamentada.

---

## Gráficas generadas

El sistema genera gráficas estadísticas mediante **Matplotlib**. Estas se almacenan automáticamente en la carpeta:

```text
exports/graficas/
```

| Archivo | Descripción |
|---|---|
| `01_latencia_por_paquete.png` | Muestra la evolución de la latencia por paquete |
| `02_paquetes_recibidos_vs_perdidos.png` | Compara paquetes recibidos y perdidos |
| `03_congestion_por_paquete.png` | Representa los eventos de congestión detectados |
| `04_histograma_latencia.png` | Muestra la distribución de valores de latencia |
| `05_comparacion_escenarios.png` | Compara escenarios LAN y WAN |

Estas visualizaciones complementan el análisis numérico y permiten interpretar mejor el rendimiento de la red.

---

## Base de datos SQLite

El proyecto utiliza **SQLite** para almacenar resultados históricos de las simulaciones.

La base de datos se genera automáticamente en:

```text
data/simulaciones.db
```

Esta base permite registrar y consultar información como:

- Tipo de red simulada.
- Paquetes enviados.
- Paquetes recibidos.
- Paquetes perdidos.
- Tasa de pérdida.
- Latencia promedio.
- Throughput.
- Eventos de congestión.
- Fecha de simulación.

SQLite fue seleccionado por ser una base de datos ligera, local y adecuada para proyectos académicos desarrollados en Python.

---

## Archivos generados por el sistema

Durante la ejecución, el sistema puede generar los siguientes archivos:

```text
logs/eventos_redcom.txt
exports/csv/resultados_simulacion.csv
exports/graficas/
data/simulaciones.db
```

Estos archivos sirven como evidencia del funcionamiento del simulador y pueden utilizarse en el informe del proyecto.

---

## Pruebas unitarias

El proyecto incluye pruebas unitarias mediante **Pytest**. Estas pruebas permiten verificar el funcionamiento de los principales módulos del sistema, como la creación de nodos, redes, enlaces, simulaciones, congestión y métricas.

Para ejecutar las pruebas:

```bash
uv run pytest
```

También puede utilizarse:

```bash
python -m pytest
```

Las pruebas unitarias contribuyen a validar la estabilidad del sistema y permiten comprobar que sus componentes principales funcionan correctamente.

---

## Resultados de ejemplo

Durante una simulación de prueba se obtuvieron los siguientes resultados:

```text
Paquetes enviados: 20
Paquetes recibidos: 13
Paquetes perdidos: 7
Tasa de pérdida: 35.0 %
Latencia promedio: 30.55 ms
Throughput: 65.0 Mbps
Eventos de congestión: 10
```

Estos resultados muestran que el sistema logra registrar el tráfico de paquetes, detectar pérdidas, calcular la latencia promedio, estimar el throughput e identificar eventos de congestión.

---

## Interpretación de resultados

Los resultados permiten analizar el comportamiento de una red simulada bajo determinadas condiciones de transmisión. Una mayor pérdida de paquetes reduce el rendimiento efectivo de la red. Asimismo, los eventos de congestión pueden provocar incremento de latencia y mayor probabilidad de pérdida.

Por ello, **RedCom Analytic** permite observar de forma práctica cómo los parámetros de red influyen en el desempeño de una comunicación LAN/WAN.

---

## Evidencia del proyecto

El repositorio contiene evidencia generada por el sistema, como:

- Archivos de resultados en CSV.
- Gráficas estadísticas.
- Base de datos SQLite.
- Logs de eventos.
- Pruebas unitarias.
- Código fuente estructurado.

Estos elementos respaldan el funcionamiento del simulador y su relación con los requisitos del proyecto final.

---

## Buenas prácticas aplicadas

En el desarrollo del sistema se aplicaron las siguientes prácticas:

- Separación del código en módulos.
- Uso de Programación Orientada a Objetos.
- Organización por responsabilidades.
- Registro de eventos.
- Persistencia de datos.
- Análisis estadístico.
- Visualización de resultados.
- Pruebas unitarias.
- Uso de entorno virtual.
- Archivo `requirements.txt` para dependencias.

---

## Limitaciones

El sistema representa una simulación académica simplificada. Por lo tanto:

- No captura tráfico real de red.
- No implementa protocolos avanzados como TCP, UDP, OSPF o BGP.
- No utiliza interfaces gráficas avanzadas.
- No realiza simulación en tiempo real con dispositivos físicos.
- Los valores de pérdida, latencia y congestión son simulados.

A pesar de estas limitaciones, el sistema cumple con el objetivo académico de representar el comportamiento básico del tráfico en redes LAN/WAN.

---

## Trabajos futuros

Como mejoras futuras se podrían implementar:

- Interfaz gráfica web con Reflex, Flask o Django.
- Simulación de protocolos de red.
- Comparación avanzada entre múltiples escenarios.
- Exportación de reportes en PDF con mayor detalle.
- Panel visual de métricas en tiempo real.
- Integración con bases de datos externas.
- Mayor cobertura de pruebas unitarias.
- Simulación de tráfico con diferentes tipos de paquetes.
- Incorporación de rutas dinámicas y tablas de enrutamiento más completas.

---

## Requisitos del sistema

Dependencias principales:

```text
pandas
numpy
matplotlib
pytest
```

Estas dependencias se encuentran registradas en el archivo:

```text
requirements.txt
```

---

## Comandos principales

| Acción | Comando |
|---|---|
| Crear entorno virtual | `uv venv` |
| Activar entorno en Windows | `.\\.venv\\Scripts\\Activate.ps1` |
| Instalar dependencias | `uv pip install -r requirements.txt` |
| Ejecutar sistema | `uv run python main.py` |
| Ejecutar pruebas | `uv run pytest` |

---

## Información académica

**Proyecto:** RedCom Analytic  
**Título:** Simulador avanzado de red de comunicaciones con análisis de tráfico  
**Curso:** Lenguaje de Programación II  
**Área:** Ingeniería de Telecomunicaciones  
**Tipo:** Proyecto académico  
**Lenguaje:** Python  

---

## Repositorio

```text
https://github.com/jaquika/RedCom-Analytic
```

---

## Autoría

Proyecto desarrollado con fines académicos para la aplicación de Programación Orientada a Objetos, simulación de redes, análisis de datos y visualización estadística en Python.


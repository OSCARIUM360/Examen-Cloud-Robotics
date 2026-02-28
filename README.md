# Examen Práctico: Cloud Robotics - UEES

## 1. Diseño de Arquitectura (Cloud - Edge - Robot)

[cite_start]Esta arquitectura ha sido diseñada para garantizar la continuidad operativa ante fallos de red y asegurar un estado seguro del robot en todo momento[cite: 7, 8, 9].

### 1.1 Diagrama de Arquitectura

```mermaid
graph TD
    subgraph "Nivel Robot (Local)"
        A[Sensores/Actuadores] --- B[Controlador de Seguridad]
        B --- C{Parada de Emergencia}
        style C fill:#f96,stroke:#333,stroke-width:2px
    end

    subgraph "Nivel Edge (Gateway/Frontera)"
        D[Edge Gateway Principal]
        E[Edge Gateway Failover]
        D <-->|Sincronización| E
    end

    subgraph "Nivel Cloud (Supervisión/Analítica)"
        F[Broker MQTT / IoT Core]
        G[Base de Datos Telemetría]
        H[Dashboard de Analítica]
        F --> G
        F --> H
    end

    %% Flujos
    B <==>|Prioridad Alta: Control| D
    D ==>|Prioridad Media: Telemetría| F
    
    classDef critical fill:#f9f,stroke:#333,stroke-width:2px;
    class B,D critical;

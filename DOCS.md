\# QNV 2030 HPC Architecture - API \& Module Documentation



This document provides technical specifications and usage guidelines for the core modules powering the Qatar National Vision 2030 High-Performance Computing and Cardio-Neural Digital Twin framework.



\---



\## 1. Spatial-Temporal Logging Engine (`python\_logger2.py`)

Provides microsecond-level precision state logging with zero cumulative drift ($< 6.44\\,\\mu\\text{s}$).



\### Class: `SpatialTemporalLogger`

```python

from python\_logger2 import SpatialTemporalLogger



logger = SpatialTemporalLogger(

&#x20;   project="QNV\_HPC\_Infrastructure",

&#x20;   node="HPC\_NODE\_GRC\_QATAR\_01",

&#x20;   log\_path="/var/log/qnv\_hpc\_telemetry.log",

&#x20;   golden\_sync\_enabled=True

)


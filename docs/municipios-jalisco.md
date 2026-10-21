# Municipios de Jalisco para el sistema

Este documento define la estructura base recomendada para municipalizar el cumplimiento del sistema en Jalisco.

## Municipios iniciales

Se recomienda iniciar con estos municipios:

- Guadalajara
- Zapopan
- Tonalá
- Tlaquepaque
- El Salto
- Tlajomulco de Zúñiga
- Puerto Vallarta
- Lagos de Moreno
- Ocotlán
- Tepatitlán

## Datos mínimos requeridos por municipio

Cada municipio debe contar con:

- nombre
- estado
- autoridad de protección civil
- autoridad de bomberos
- reglamento interno
- versión del reglamento
- responsable local
- contacto institucional
- documentos de referencia

## Ejemplo de definición de municipio

```json
{
  "name": "Guadalajara",
  "state": "Jalisco",
  "authority_protection_civil": "Protección Civil de Guadalajara",
  "authority_bomberos": "Bomberos Guadalajara",
  "regulation_reference": "Reglamento Interno de Protección Civil",
  "regulation_version": "2024"
}
```

## Programas internos recomendados por municipio

Para cada municipio, se recomienda al menos:

- Programa Interno de Brigada contra Incendios
- Programa de Evacuación
- Programa de Inspección
- Programa de Mantenimiento
- Programa de Capacitación
- Programa de Simulacros
- Programa de Respuesta Rápida
- Programa de Coordinación con Bomberos

## Requisitos mínimos del municipio

Se recomienda evaluar estos puntos:

1. Inspección documental y física
2. Registro de mantenimiento
3. Señalización de evacuación
4. Rutas de salida funcionales
5. Capacitaciones internas
6. Brigada contra incendios
7. Simulacro de evacuación
8. Mantenimiento de instalaciones eléctricas
9. Mantenimiento de equipos contra incendios
10. Coordinación con Protección Civil y Bomberos

## Reglas clave para cada municipio

El sistema debe permitir diferentes requisitos según el municipio, porque:

- no todos los municipios usan el mismo reglamento
- la autoridad local puede variar
- la vigencia del programa puede diferir
- la obligación local puede ser mayor o menor
- la forma de evaluar puede ser distinta

## Rúbrica mínima de evaluación

Cada requisito puede evaluarse como:

- compliant
- partial
- non_compliant
- unknown

## Recomendación

La mayor calidad del sistema se logra cuando cada municipio tiene:
- su propio catálogo de requisitos
- su propio programa interno
- sus responsables
- su historial de cumplimiento
- sus documentos regulatorios

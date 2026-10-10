# Plan Instagram +impactoIA: 8 piezas

Formato: sin cara a cámara (texto en pantalla, capturas de chat, voz en off, placas).
Palabra clave principal: TURNOS. Las otras (RECEPCIÓN, DEMO, CASO, EMPLEADO) se usan donde el destino del DM es distinto.
Números permitidos: solo los del caso Cardiología Hiskin (abril de 2026), siempre atribuidos.
Fuente de verdad: base "Gestión de contenido" en Notion (Status, Palabra Clave, Mensaje DM, caption, Guión, Fecha de publicación).

## Palabras clave y destino del DM

| Palabra clave | Destino del DM |
|---|---|
| TURNOS | WhatsApp 11 7650 5000 (https://wa.me/541176505000) |
| RECEPCIÓN | Diagnóstico: https://masimpactoia.com/es-ar/diagnostico |
| DEMO | Demo en vivo: https://cal.com/masimpactoia/solicita-tu-demo |
| CASO | Caso Cardiología Hiskin: https://masimpactoia.com/es-ar/recursos/caso-cardiologia-hiskin |
| EMPLEADO | Cotización: https://masimpactoia.com/es-ar/cotizacion |

## Piezas

| # | Formato | Gancho | Título | Palabra clave | Objetivo de comunicación y CTA | Estado en Notion |
|---|---|---|---|---|---|---|
| 1 | Reel | #14 The Callout | Tu paciente escribió a las 22:00. Le contestás mañana. | TURNOS | Hacer visible el costo de los mensajes que esperan horas: el paciente se molesta y agenda en otro lado. CTA: comentar TURNOS. | pendiente (14/10) |
| 2 | Reel (planeado como carrusel) | | 3 cosas que tu recepción hace a mano y no debería | RECEPCIÓN | Mostrar que turnos, reprogramaciones y obras sociales se pueden delegar. CTA: comentar RECEPCIÓN para recibir el diagnóstico. | programado |
| 3 | Reel | #18 Cold Open Demo | Agendar un turno por WhatsApp en menos de 1 minuto | DEMO | Mostrar un Empleado IA atendiendo a un paciente y agendando en tiempo real. CTA: comentar DEMO. | publicado (9/10) |
| 4 | Reel | #22 Contrarian Flip | El problema de tu clínica no es tu recepcionista | TURNOS | Poner el foco en el volumen y los horarios, no en el equipo. CTA: comentar TURNOS. | pendiente (16/10) |
| 5 | Reel | #23 The Statistic | 6.205 mensajes en un mes. 960 en un solo día. | CASO | Credibilidad con un número verificable del caso Cardiología Hiskin (8 sedes, abril de 2026). CTA: comentar CASO. | pendiente (19/10) |
| 6 | Carrusel (oferta) | | De cero a un Empleado IA en 3 pasos | EMPLEADO | Explicar la implementación sin fricción: nos contás, lo entrenamos y conectamos, lo ponemos a trabajar, con 14 días de correcciones. CTA: comentar EMPLEADO. | pendiente (21/10) |
| 7 | Reel | #12 The Objection | "Mis pacientes no quieren hablar con una IA" | DEMO | Responder la objeción principal: deriva a una persona cuando corresponde y entiende audios. CTA: comentar DEMO. | pendiente (23/10) |
| 8 | Reel | #21 Mid-Sentence Start | Domingo, 23:35. Un paciente pide turno para una resonancia. | TURNOS | Mostrar cómo un Empleado IA atiende pacientes las 24 horas, todos los días, sin feriados, sin licencias ni vacaciones. Escena simulada, avisarlo en el reel. CTA: comentar TURNOS. | pendiente (26/10) |

Stories sugeridas: pregunta "¿Cuántos mensajes quedan sin responder cuando cerrás?" y encuesta "¿Tu clínica contesta mensajes fuera de horario?".

## Cómo corre en n8n

- Generación: lunes, miércoles y viernes a la 01:00 toma una fila "pendiente" de Instagram, arma el reel o carrusel y pide aprobación por Telegram. Respeta el caption y el guión ya cargados.
- Publicación: filas "programado" con fecha de publicación llegada; lunes, miércoles y viernes a las 13:00 y 20:00.
- Engagement: el flujo "IA Instagram_DM y COMENTARIOS" responde a la palabra clave con el DM de Notion y una respuesta pública en voseo. Anti-duplicados con Redis.

## Reglas

- Todo en voseo y con acentos.
- No usar el "63% de los consumidores usa asistentes IA" sin fuente.
- Corregir en Instagram el caption del reel del 6/10 (tiene "6-9 hashtags:" filtrado).
- Al final, comparar en Metricool: alcance, comentarios con palabra clave, guardados y compartidos.

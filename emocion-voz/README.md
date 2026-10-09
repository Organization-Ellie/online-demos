# Mini-demo: emoción en la voz

Salida de un prototipo que estima la emoción en la voz de una persona participante durante una respuesta de entrevista, y una app de Streamlit que la muestra.

## Contenido

| Archivo | Para qué sirve |
|---|---|
| `data/curva_ejemplo.csv` | Un extracto de 45 s: una fila por ventana de 3 s (paso 1.5 s), con la probabilidad de las 9 clases, cruda (`p_*`) y suavizada (`s_*`) |
| `data/resumen_preguntas.csv` | Una fila por respuesta (42, de 6 sesiones identificadas solo por número): número de ventanas, **% de ventanas por emoción** (`pct_*`) y la emoción más frecuente. La más frecuente puede ocultar una presencia importante de otra emoción, por eso se usa la distribución completa |
| `app.py` | App de Streamlit: `streamlit run app.py` |

**No se incluye audio.** Contiene la voz de una persona participante y no está confirmado que el consentimiento informado cubra publicarla. Para verlo con audio en local, copiar el archivo a `data/audio_ejemplo.wav` (el `.gitignore` impide subirlo por error).

## Cómo se obtuvo

Se excluye la voz del robot que lee la pregunta y la del entrevistador; solo se analiza lo que dice el sujeto. Modelo: emotion2vec+ base, preentrenado, 9 clases, sin ajuste con datos propios. La probabilidad suavizada es el promedio de las últimas 5 ventanas (solo pasado, como en tiempo real).

## Límites que deben constar si esto se muestra

- **Resultado preliminar, sin validar con etiquetas humanas.** No hay medida de precisión ni matriz de confusión.
- El modelo no está entrenado para español ni para voz espontánea de personas mayores; puede confundir sollozos con otras emociones.
- El extracto se eligió entre 42 respuestas por mostrar una tendencia clara: es un ejemplo ilustrativo, no una muestra aleatoria.
- El fin de la voz del robot se detectó automáticamente; solo una parte de las 42 respuestas se verificó a mano.

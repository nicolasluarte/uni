---
title: Laboratorio de Neurofisología celular y de sistemas (Claudio Peréz Leighton)
author: Nicolás Luarte
output: beamer_presentation
csl: /home/nicoluarte/apa.csl
---

# Agenda

# Pregunta de investigación central
- Vínculo entre función neural y comportamiento
- Variable independiente es de caracter 'biológico'
- Variable dependiente de caracter 'comportamiento'
- o viceversa
- Existen multiples métodos de investigación

# Inhibir o extinguir una función neuronal
- Estudios de lesiones
- Estimulación magnetica/eléctrica
- Manipulación de neuro-transmisores
- Entre otras

# Aumentar una función neuronal
- Estimulación eléctrica
- Optogenetica
- facilitación de la actividad neuronal

# Observando el vínculo
En el laboratorio se observan multiples 'direccionalidades' derivadas de la pregunta central

Mi presentación evaluara 3 de ellas y sus respectivas técnicas

- Aumentar/inhibir la función neural y observar cambios en el comportamiento
- Definir, dado un fenotipo de comportamiento, la dinámica neuronal
- Definir variables contextuales que modulan el comportamiento, tener un fenotipo de comportamiento dado y observar la dinámica neuronal

# El laboratorio en especifico
- La pregunta en general, como se mencionó anteriormente, es el vínculo entre función neuronal y comportamiento
- La función neuronal de interés especifico es la orexina
- Las medidas de comportamiento corresponden a las relacionadas con el balance calorico
	- Actividad física espontanéa
	- Comportamiento de ingesta
	- Gasto energetico
	- Entre otras relacionadas
- Adicionalmente la pregunta incluye modulación del vínculo comportamiento-función-neuronal por elementos contextuales

# Técnicas asociadas a manipulación de la función neuronal y observar cambios en el comportamiento
La orexina es un neuropeptido, para el cual se ha vínculado la función de regulación de 'arousal', apetito, actividad física espontanea, actividad exploratoria, entre otras [@Z7PJ2NBV#Mavanji_Etal_2015]

@Z7PJ2NBV#Mavanji_Etal_2015 estudiaron la actividad  el sistema neuronal de orexina en el área ventrolateral pre-optica para el control del gasto energetico

# Técnicas asociadas a manipulación de la función neuronal y observar cambios en el comportamiento

- Manipulación de la función neuronal (variable independiente)
	- Inyección de orexina-A
	- Inyección de antagonista del receptor 2 de orexina (OX2R)

- Observar modificaciones en el comportamiento (variable dependiente)
	- Registro de los estados de comportamiento
		- NREM
		- REM
		- 'active wakefulness'
		- 'quiet wakefulness'
	- Registro de la actividad física espontanea

# Técnicas asociadas a manipulación de la función neuronal y observar cambios en el comportamiento

EL problema acá es observar el efecto de la orexina-A (función neuronal) sobre los registros de comportamientos anteriormente mencionados, para ello, lógicamente, es necesario saber el estado de comportamiento presente

# Determinación de estado de comportamiento bajo polisomnografía
- Se realiza implantación de un transmisor capaz de enviar señales con información de EEG y EMG
- Se realiza una transformada de Fourier a los datos obtenidos, utilizando un ancho de 'bin' determinado
- Se utilizad la banda delta, ya que es un marcador del 'sleep drive' (probabilidad de consumar el sueño en cualquier punto dado)
- Se evaluan el movimiento ocular rápido
- Entre otras medidas
- La información anterior es agregada y presentada a un evaluador para determinar el estado de comportamiento presente, dada dicha información

Para revisión de criterios especificos ver [@KILDFJME#Mavanji_Etal_2010]

# Medición de la actividad física espontanea
La actividad física espontanea (SPA) es aquél tipo de actividad no-estructurada de baja intensidad (estar de pie, movimiento de manos y pies, deambular, etc) [@5VILKIIC#Teske_Etal_2014]

- Para su medición se ocupan cajas especialmente diseñadas con haces infrarojos en los ejes x e y
- El eje z, para ratones, se ubica 2.5 cm por sobre el suelo y permite medir elevaciones del animal
- Gracias a lo anterior se puede medir el tiempo deambulando y tiempo 'de pie'
- Ambas medición dan un índice que estima el SPA

# Medición de la actividad física espontanea
![Comparación de grupos utilizando SPA](images/spa_measurement.png){ width=30% }

Comparación mediante 't-test' del SPA para ratones 'resistentes a la obesidad' (OR) y ratones Sprague-Dawley (SD)

# Segmentación de la actividad física espontanea

Una de los problemas que podría surgir para evaluar la SPA, es que las medidas de comportamiento sean redundantes y por ende no se este registrando apropiadamente la señal, por ejemplo, si la deambulación y pararse verticalmente es redundante o son medidas complementarias

# Segmentación de la actividad física espontanea

- Para lo anterior se puede utilizar una técnica de reducción de dimensionalidad tal como 'principal component analysis' (PCA)
- PCA nos entrega 'componentes' correspondientes a fuentes de variabilidad no-correlacionadas
- El primer componente da cuenta de la mayor cantidad de variabilidad de los datos, el segundo de la segunda mayor cantidad y así
- Adicionalmente, esto nos permite calcular los 'factor loadings':
	- Correlación entre las variables originales y cada uno de los componentes
	- Porcentaje de la varianza en la variable original explicado por un componente determinado
- Con ellos podemos determinar si distintos 'comportamientos' provienen de la misma o distinta fuente de variabilidad

# Ejemplo de hallazgo con la técnica anterior
![Análisis con PCA](images/pca.png){ width=70% }

Se observan las correlaciones de cada variable original con cada componente. Las correlaciones para medidas de 'deambulación' son altas para el componente 1, mientras que las de 'verticalidad' correlacionan sustancialmente con los componentes 2 y 3 [@5VILKIIC#Teske_Etal_2014]


# Técnicas dónde, dado un fenotipo de comportamiento, se observa la dinámica neuronal
En este tipo de problemas se cuenta con algún fenotipo de comportamiento, por ejemplo, ratones de altos y bajos niveles de actividad. Y luego se observa la modificación del comportamiento (SPA) por inyección de orexina-A en diferentes áreas

# Técnicas dónde, dado un fenotipo de comportamiento, se observa la estuctura neuronal

PCR

# Técnicas para evaluar interacción de elementos contextuales, comportamiento y función neuronal

Desarrollo de preferencia

# Conclusiones generales sobre las técnicas presentadas



# Preguntas frecuentes (FAQ)

**Agencia Tributaria**

Recopilación de preguntas y respuestas en relación a los Sistemas Informáticos de Facturación y VERI\*FACTU (Actualizadas a 5 de diciembre de 2025).

## Índice

- Cuestiones generales: objeto
- Cuestiones generales: conceptos y definiciones
- Cuestiones generales: ámbitos de aplicación
- Cuestiones generales: cumplimiento y delegación
- Características y requisitos de los sistemas informáticos de facturación (SIF): recursos necesarios, uso múltiple
- Características y requisitos de los SIF: capacidad de remisión, certificados, etc.
- Características y requisitos de los SIF: integridad e inalterabilidad
- Características y requisitos de los SIF: trazabilidad
- Características y requisitos de los SIF: conservación, accesibilidad y legibilidad
- Características y requisitos de los SIF: registro de eventos.
- Registros de facturación: alta
- Registros de facturación: anulación
- Huella o «hash»
- Firma
- Certificación de los sistemas informáticos: declaración responsable
- Sistemas VERI\*FACTU (Sistemas de emisión de facturas verificables)
- Posibilidad de remisión de información de la factura por parte de su receptor. Representación gráfica a incluir en la factura. Código QR. Frase «VERI\*FACTU».
- Procedimientos de facturación
- Colaboración social
- Glosario de abreviaturas

---

# Cuestiones generales: objeto

## ¿Qué es VERI\*FACTU (o el reglamento VERI\*FACTU y el Real Decreto 1007/2023 de VERI\*FACTU)?

En general, los términos VERI\*FACTU o reglamento VERI\*FACTU son formas abreviadas, coloquiales y significativas –aunque inexactas– de referirse al reglamento que establece los requisitos que deben adoptar los sistemas y programas informáticos o electrónicos que soporten los procesos de facturación de empresarios y profesionales, y la estandarización de formatos de los registros de facturación, aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

Este reglamento desarrolla parcialmente el artículo 29.2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria (LGT), introducido por la «ley antifraude» (Ley 11/2021, de 9 de julio), en lo que se refiere a sistemas y programas informáticos o electrónicos que soporten los procesos de facturación (denominados abreviadamente sistemas informáticos de facturación o SIF) de quienes desarrollen actividades económicas, es decir, de empresarios y profesionales.

Este reglamento y el real decreto que lo aprueba imponen una serie de requisitos a los sistemas informáticos que se utilicen para expedir facturas, con el objetivo de evitar o dificultar y detectar que se pueda cometer fraude en ese proceso.

Resumidamente, obligan a que esos SIF, en el momento de expedición de la factura, generen y guarden o remitan a la Agencia Tributaria un resumen de la factura –llamado registro de facturación– que lleva incorporada una serie de medidas de seguridad y control, como son la huella digital de sus datos, la inclusión de información del anterior registro generado (lo que permite verificar que no hay omisiones) y, en su caso, la firma electrónica del emisor del mismo. Asimismo, obligan a los SIF a que incluyan un código QR en la factura expedida, cuya lectura (por ejemplo, con la cámara de un teléfono móvil) permite a quien reciba dicha factura remitir fácilmente ciertos datos de la misma a la Agencia Tributaria, para su posible verificación.

Por último, cabe señalar que el término VERI\*FACTU con el que se suele conocer tanto a este reglamento como al real decreto que lo aprueba proviene del nombre de uno de los 2 tipos de SIF contemplados por el reglamento que se puede utilizar para cumplir con esta normativa y cuya característica más destacada es que remiten a la Agencia Tributaria un resumen estructurado de los datos de cada factura (denominado registro de facturación de alta) en el mismo momento de su expedición.

**Normativa/Doctrina**:

- Artículo 2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria.
- Real Decreto 1007/2023, de 5 de diciembre, por el que se aprueba el reglamento que establece los requisitos que deben adoptar los sistemas y programas informáticos o electrónicos que soporten los procesos de facturación de empresarios y profesionales, y la estandarización de formatos de los registros de facturación (RRSIF).

## ¿Por qué se ha aprobado el reglamento que establece los requisitos de los sistemas informáticos de facturación?

Además de lo que se comenta al respecto en otras preguntas frecuentes relacionadas (1.1, …), la exigencia del cumplimiento de ciertos requisitos de seguridad y control a los sistemas informáticos de facturación (SIF) como una medida más de lucha contra el fraude fiscal se ha venido aplicando desde hace tiempo por muchas otras Administraciones tributarias, tanto de España (casos forales), como de otros países de la Unión Europea (Francia, Italia, Portugal, Alemania…) y del resto del mundo.

En el caso que nos ocupa, tras estudiar numerosos sistemas ya implantados y sus respectivos tipos de requisitos, se ha optado por un enfoque en línea con las recomendaciones más recientes al respecto de la Organización para la Cooperación y el Desarrollo Económicos (OCDE). Además, se ha intentado no condicionar la forma de implementarlos, lo cual permite mayor libertad y flexibilidad a la hora de llevarlos a la práctica, favoreciendo la competencia de soluciones, bien sean basadas en software, en hardware o mixtas. Así se reducen costes y se permite elegir el SIF que mejor se adapte a las circunstancias y necesidades de cada empresario o profesional, facilitando, en definitiva, su adopción.

**Normativa/Doctrina**:

- Artículo 2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria.
- Real Decreto 1007/2023, de 5 de diciembre (RRSIF).

## ¿Qué ventajas aporta el reglamento que establece los requisitos de los sistemas informáticos de facturación y para quiénes?

En primer lugar, con la utilización de sistemas informáticos de facturación adaptados al reglamento se evitará –o dificultará y detectará– que se puedan llevar a cabo prácticas fraudulentas en ese proceso, tales como la omisión de facturas o la alteración de las facturas de venta una vez expedidas. Esto tiene dos grandes consecuencias:

- Por un lado, incidirá directamente en una reducción del fraude cometido, lo que traerá consigo una mayor justicia fiscal que redundará en el bien de toda la ciudadanía.
- Por otro lado, impedirá o reducirá significativamente la competencia desleal de la que se aprovechan quienes defraudan frente a quienes cumplen con sus obligaciones tributarias.

Adicionalmente, la adopción de este tipo de requisitos y formatos contribuirá a estandarizar y modernizar los sistemas informáticos empresariales, avanzando en la digitalización de los empresarios y profesionales. Como resultado de esto se consiguen dos efectos:

- Se facilitan y fomentan las relaciones entre los propios empresarios y profesionales, y de estos con sus representantes fiscales, al utilizar unos formatos de información de facturación comunes, favoreciendo su intercambio y reduciendo costes, cuestiones que tienen un impacto beneficioso en la actividad comercial.
- Se concreta y simplifica la comunicación de información a la Administración tributaria, facilitándose el cumplimiento tributario.

Asimismo, este reglamento pretende ofrecer a quienes reciban facturas (incluyendo facturas simplificadas) una forma fácil e inmediata de remitir ciertos datos de las mismas a la Agencia Tributaria, para su posible comprobación. Esto contribuye a una mayor transparencia en los negocios, así como a desarrollar la conciencia fiscal y la cultura del cumplimiento tributario.

**Normativa/Doctrina**:

- Artículo 2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria.
- Apartado I del preámbulo del Real Decreto 1007/2023, de 5 de diciembre (RRSIF).

## ¿Qué obligaciones establece la «ley tributaria» en relación con cierto tipo de sistemas y programas informáticos o electrónicos utilizados por empresarios y profesionales en el desempeño de sus actividades económicas?

El artículo 29.2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria (LGT), obliga a los productores, comercializadores y usuarios de sistemas y programas informáticos o electrónicos que soporten los procesos contables, de facturación o de gestión de quienes desarrollen actividades económicas a que dichos sistemas informáticos garanticen la integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros, sin interpolaciones, omisiones o alteraciones de las que no quede la debida anotación en los sistemas mismos. Para ello, permite que se establezcan ciertas especificaciones técnicas a cumplir, así como su certificación y que usen formatos estándar de manera que sus registros sean legibles.

**Normativa/Doctrina**:

- Artículo 2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria.

## ¿Qué sanciones contempla la «ley tributaria» en relación con ciertos sistemas y programas informáticos o electrónicos que no cumplan con los requisitos exigidos?

El artículo 201 bis de la Ley 58/2003, de 17 de diciembre, General Tributaria (LGT), prevé dos tipos de sanciones, ambas graves:

- A la fabricación, producción y comercialización de sistemas informáticos que no cumplan con lo dispuesto en el artículo 29.2.j) de la LGT y normativa de desarrollo (reglamento, orden ministerial y documentación relacionada de la sede electrónica de la Agencia Tributaria).

  La cuantía estipulada es de 150.000 euros fijos por cada ejercicio económico en el que se hayan producido ventas de este tipo de sistemas informáticos y por cada tipo distinto de estos que sea objeto de la infracción.

  Por otro lado, cuando no se certifiquen dichos sistemas informáticos estando obligados a ello, se sancionará con 1.000 euros por sistema informático comercializado sin dicha certificación.

- A la tenencia de sistemas informáticos que no se ajusten a lo establecido en el artículo 29.2.j) de la LGT, cuando los mismos no estén debidamente certificados teniendo que estarlo por disposición reglamentaria o cuando se hayan alterado o modificado los dispositivos certificados. El importe es de 50.000 euros por cada ejercicio.

**Normativa/Doctrina**:

- Artículo 201 bis de la Ley 58/2003, de 17 de diciembre, General Tributaria.

## ¿A qué sistemas informáticos se aplica el reglamento que establece los requisitos de los sistemas informáticos de facturación?

Solo a aquellos que se utilicen para expedir facturas (incluyendo las facturas simplificadas), es decir, a los sistemas informáticos de facturación (SIF), siempre y cuando sean utilizados por obligados a expedir facturas (completas o simplificadas, tanto a otros empresarios como a consumidores finales) a quienes les aplique el reglamento aprobado por el Real Decreto 1007/2023, de 5 de diciembre: ver el apartado 2 de la pregunta frecuente "¿A quién afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?" y su "regla de los 4 «NO»" de *Cuestiones generales: ámbitos de aplicación*.

Por el contrario, no se aplicará a otros sistemas informáticos que se utilicen para emitir otro tipo de documentos justificativos de entrega de bienes o prestación de servicios.

**Normativa/Doctrina**:

- Artículo 2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria.
- Artículos 1.1 y 1.2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## (Novedad) A partir de 2027 cambiaré de programa de facturación para cumplir con los nuevos requisitos ¿tengo que eliminar el programa de facturación utilizado hasta 2026 que contiene el histórico, si no cumple con los requisitos de VERI\*FACTU, aunque en 2027 ya no lo utilice? ¿o es sancionable su mera tenencia?

No necesariamente.

Según el apartado segundo del artículo 201 bis de la LGT se establece en el apartado 2 anterior, se sancionará con multa pecuniaria fija de 50.000 euros por cada ejercicio, cuando se trate de la **infracción por la tenencia de sistemas o programas informáticos o electrónicos que no estén debidamente certificados**, teniendo que estarlo por disposición reglamentaria, o se hayan alterado o modificado los dispositivos certificados.

La "tenencia" de sistemas informáticos de facturación (SIF) no adaptados al RRSIF -y, por tanto, no certificados al respecto- debe considerarse relacionada con una tenencia en orden a la funcionalidad de facturación. Si se usa la base de datos del programa no adaptado al RRSIF *exclusivamente* para guardar (y, en su caso, consultar) las facturas históricas, **pero NO se puede facturar con dicho programa**, podría no vulnerarse la normativa, con las siguientes consideraciones:

- Tener un SIF antiguo no adaptado al RRSIF *estaría permitido, si y solo si se puede acreditar que con él YA NO se pueden expedir facturas*. Normalmente ello se consigue con su *desinstalación*, pero también se podría *modificar el programa* para que fuera imposible emitir nuevas facturas a partir de una fecha. De esta forma, ya no constituiría un SIF.
- Si llegara a detectarse, después del 1/1/2027 (o 1/7/2027, según corresponda al obligado), *la tenencia de un SIF no adaptado al RRSIF con capacidad de emitir facturas*, con su mera tenencia se estaría cometiendo la infracción y sí sería objeto de la imposición de la sanción contemplada en el artículo 201 bis.2 de la LGT. En todo caso, previa valoración del comportamiento del obligado y su responsabilidad.
- Prácticamente todos los programas de facturación tienen entre sus utilidades la *exportación* de los registros generados con ellos, sin que sea necesario, por tanto, conservar el SIF mismo. Esta posibilidad es la más *aconsejable* de cara a asegurar no incurrir en modo alguno en el presupuesto de hecho de la infracción.
- Se debe recomendar *consultar con el fabricante* de su SIF no adaptado por si dispone de una versión adaptada al RRSIF con la que poder actualizarlo, ya que esta posibilidad suele ser muy habitual. De lo contrario, se debe recomendar valorar la utilización de algún SIF adaptado de otro fabricante o de la aplicación de facturación gratuita de la AEAT –si fuera suficiente para dar respuesta a sus necesidades– o bien el desarrollo de un SIF propio adaptado.

## (Novedad) Una sociedad que opte por utilizar el sistema informático VERI\*FACTU dentro del periodo de pruebas ¿es obligatoria la permanencia en dicho sistema hasta que finalice el año natural?

No.

La Disposición final cuarta del RRSIF (Reglamento que establece los requisitos de los sistemas informáticos de facturación), modificada por el Real Decreto-ley 15/2025, de 2 de diciembre, establece que entrará en vigor de forma obligatoria el 1 de enero de 2027 para contribuyentes del Impuesto sobre Sociedades y el 1 de julio de 2027 para el resto de obligados tributarios mencionados en el artículo 3.1 del RRSIF, entre ellos, los contribuyentes del Impuesto sobre la Renta de las Personas Físicas que desarrollen actividades económicas. **El periodo anterior a la entrada en vigor del RRSIF es un periodo de pruebas.**

Se podrá dejar de expedir facturas y remitir registros en prueba con un SIF modalidad VERI\*FACTU y utilizar para facturar otros SIF (sistema informático de facturación), que podrían ser adaptados y funcionar en modo NO VERI\*FACTU (si así lo permiten) o incluso sistemas antiguos no adaptados, mientras no tengan obligación: hasta el 31/12/2026 o 30/06/2027, según aplique.

Una vez se tenga obligación de adaptación al RRSIF, es decir, a partir del 1/1/2027 o 1/7/2027, según aplique, si los obligados optan por comenzar a expedir facturas y remitir registros de facturación (RF) con un SIF VERI\*FACTU, debe permanecer, al menos, hasta la finalización del año natural en el que se haya producido, de forma efectiva, el primer envío de los registros de facturación.

---

# Cuestiones generales: conceptos y definiciones

## ¿A qué documentos mercantiles afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación, y de qué manera?

Dado que el reglamento que establece los requisitos de los sistemas informáticos de facturación se aplica a los sistemas informáticos de facturación (SIF), entendiéndose por SIF los utilizados para expedir facturas, los únicos documentos afectados por este reglamento son las FACTURAS, tanto las «completas u ordinarias» como las simplificadas, no afectando a ningún otro tipo de documentos justificativos de entrega de bienes o prestación de servicios.

Las facturas expedidas con estos SIF deberán incluir una representación de cierta información de las mismas mediante un código «QR» tributario. Además, estos SIF deberán generar –y firmar y guardar o, en su caso, remitir– los correspondientes registros de facturación de las facturas expedidas.

**Normativa/Doctrina**:

- Artículos 1.1 y 1.2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículos 6.5 y 7.5 del reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre, introducidos por la disposición final primera uno y dos del Real Decreto 1007/2023, de 5 de diciembre.

## (Novedad) Realizo compras a particulares para una actividad económica generando documentos justificativos de la operación (por ejemplo, chatarrería o desguace, conserveras de setas o frutas, etc….) ¿estoy obligado a aplicar el RRSIF por la emisión de estos documentos?

No.

Salvo que se trate de una adquisición a particulares realizada por sujetos pasivos en REBU, en cuyo caso existe obligación de expedir una factura (art. 16.2 ROF), estas adquisiciones a particulares pueden documentarse por cualquier otro medio válido en derecho distinto de una factura. Al no ser facturas, el sistema informático que genere estos justificantes no es un SIF. Su emisión, por sí sola y sin otras operaciones por las que exista obligación de expedir factura, no obliga al RRSIF.

Ello sin perjuicio del cumplimiento de las exigencias genéricas a los sistemas informáticos del art. 29.2.j) de la LGT, por lo que se ha de recomendar que estos justificantes se custodien inalterados y que sean lo más completos posibles, incluyendo la identidad (con NIF / NIE) de la persona que entrega los bienes.

## (Novedad) Soy un agricultor acogido al REAGP y vendo a una Cooperativa agrícola que expide un recibo acreditativo del pago de la compensación ¿estoy obligado a aplicar el RRSIF por la emisión de estos documentos?

No.

Los recibos emitidos por empresarios o profesionales que efectúan el reintegro de las compensaciones del artículo 131.2 de la LIVA no tienen la consideración de factura. Su emisión, por sí sola y sin otras operaciones por las que exista obligación de expedir factura, no obliga al RRSIF.

## ¿Qué características añade a la factura y a la factura simplificada el Real Decreto 1007/2023 que aprueba el reglamento que establece los requisitos de los sistemas informáticos de facturación?

Además de las menciones que deben tener actualmente las facturas, sean ordinarias o simplificadas, aquellas que sean expedidas con sistemas informáticos de facturación (SIF) a los que se refiere el Real Decreto 1007/2023, de 5 de diciembre, deberán incorporar un código «QR» tributario que facilite la comunicación a la Agencia Tributaria de ciertos datos de la misma. Y si el SIF que las ha expedido está funcionando en la modalidad VERI\*FACTU, deberá incluirse también la frase «Factura verificable en la sede electrónica de la AEAT» o VERI\*FACTU.

**Normativa/Doctrina:**

- Artículos 6.5 y 7.5 del reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre, introducidos por los apartados uno y dos de la disposición final primera del Real Decreto 1007/2023, de 5 de diciembre.

## (Novedad) ¿Si una factura no tiene código «QR» tributario, puedo deducirme el IVA soportado?

Sí.

La falta de código «QR» tributario no impide la deducción del IVA soportado, siempre que se cumplan los requisitos sustantivos previstos por la normativa del IVA y por la jurisprudencia del TJUE. Este requisito solo aplica a facturas emitidas mediante sistemas informáticos de facturación regulados por el Real Decreto 1007/2023.

No todas las facturas deben incorporar el código «QR» impreso (por ejemplo, no es obligatorio incluir el código «QR» en facturas emitidas por los contribuyentes adscritos al SII, ni las expedidas por sujetos que no utilizan un sistema informático de facturación para ello, o sujetos a normas forales).

El código QR es una obligación formal del emisor que, por sí solo, no determina la deducibilidad de la factura.

**Normativa aplicable:**

- Ley 37/1992, del Impuesto sobre el Valor Añadido (art. 97).
- Real Decreto 1619/2012, por el que se aprueba el Reglamento por el que se regulan las obligaciones de facturación.
- Real Decreto 1007/2023, de 5 de diciembre.

## ¿Se puede implementar un sistema de «Pre-Facturación» («facturas proforma») o Borrador antes de expedir –y registrar– una factura?

La introducción y edición temporal de datos, visualización previa, etc. de facturas no está prohibida ni por el reglamento que establece los requisitos de los sistemas informáticos de facturación ni por el reglamento de obligaciones de facturación, si bien hasta no estar terminada la factura, esta no podrá ser expedida con su correspondiente código «QR» tributario. Por ello tanto los borradores de factura como las facturas proforma no llevan ningún código «QR» tributario. La emisión de facturas – o facturas simplificadas– proforma o sin validez fiscal, está permitida siempre y cuando se sustituyan finalmente por la factura o factura simplificada oficial expedida y esta se entregue al cliente.

Cuando una factura sea definitivamente emitida (es decir, en general, cuando se haya incorporado a ella el QR y generado el correspondiente registro de facturación de alta, firmado o remitido a la Sede electrónica de la Agencia Tributaria), ya no podrá ser considerada un borrador y su alteración, en los elementos informativos que integran el "registro de facturación de alta", no estará permitida a menos que se realice por medio de nuevos registros de facturación, como indica el tercer párrafo del artículo 8.2.a) del reglamento aprobado por el RD 1007/2023.

A efectos informáticos, el sistema de generación de facturas pro-forma o sin validez fiscal, debe estar vinculado indefectiblemente al sistema de emisión de facturas formando una unidad. Conviene, a efectos de control interno, que se conserve registro de las prefacturas o facturas proforma elaboradas.

Por ello, no sería legal y sería susceptible de sanción, el uso de sistemas que generen documentos preparatorios de facturas o de facturas simplificadas, sin que el sistema informático mismo disponga de elementos de control para la conservación de tales documentos preparatorios de forma debidamente vinculada a las facturas o a los registros de facturación que finalmente se emitan o, en defecto de factura, de forma que queden registrados y conservados en el sistema.

**Normativa/Doctrina**:

- Artículos 1.1 y 1.2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículos 6.5 y 7.5 del reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre, introducidos por la disposición final primera uno y dos del Real Decreto 1007/2023, de 5 de diciembre.

## ¿Qué se considera sistema informático de facturación?

Resumidamente, se considera sistema informático de facturación (SIF) al conjunto de hardware y software utilizado para expedir facturas que admita la entrada de información de facturación por cualquier vía, conserve esta información y la procese para generar otros productos derivados, con independencia de dónde se realice este proceso.

De forma más extensa, un sistema informático de facturación (SIF) es el conjunto de hardware y software utilizado para expedir facturas mediante la realización de las siguientes acciones:

a. **Admitir la entrada de información de facturación** por cualquier método. Como ejemplos típicos:
   - Introducir en el SIF los datos de las facturas directamente de forma manual.
   - Importar en el SIF los datos necesarios para expedir las facturas, cuando estos han sido capturados en otros sistemas.
   - Recibir en el SIF (en línea o por lotes) mediante procesos automatizados los datos necesarios para expedir las facturas, cuando estos han sido capturados en otros sistemas.

b. **Conservar la información de facturación**, dentro o fuera del SIF.

   Con ello se quiere decir que el producto obtenido, una vez expedida –y, típicamente, impresa– la factura (a partir de la información del apartado anterior), no se descarta o elimina, sino que se almacena y guarda, manteniéndose en el tiempo.

c. **Procesar la información de facturación** mediante cualquier procedimiento para producir otros resultados derivados, independientemente de dónde se realice dicho procesamiento (en el propio SIF o en otro sistema informático que tenga acceso a dicha información).

   Es decir, implica que la información capturada y guardada electrónicamente de las facturas expedidas sea procesada con otras finalidades, obteniendo nuevos resultados derivados de ella, como puede ser la confección de los libros registros de IVA, los libros registros de IRPF, la contabilidad o cualquier otro resultado que se utilice para el cumplimiento de obligaciones tributarias.

**Normativa/Doctrina:**

- Artículo 1.2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

---

# Cuestiones generales: ámbitos de aplicación

## ¿A quién afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?

Hay 2 tipos de colectivos afectados:

1. Los **productores y comercializadores** de sistemas informáticos de facturación (SIF) en las cuestiones relativas a sus respectivas actividades de producción y comercialización de los sistemas informáticos destinados a ser utilizados por el colectivo que se menciona a continuación en el siguiente apartado.

2. Aquellos empresarios y profesionales –personas físicas o jurídicas– que, estando establecidos en territorio español, expidan **facturas** (ver NOTA 1 aclaratoria al final de esta respuesta), siempre y cuando cumplan las **4** condiciones siguientes (lo que podría denominarse la "regla de los 4 «NO»"):

   a. Que **NO** facturen exclusivamente de forma manual (sin ayuda de SIF). Dicho de otro modo, que utilicen algún SIF para expedir facturas.
   b. Que **NO** estén adscritos, de forma obligatoria o voluntaria, a las exigencias del conocido como Suministro Inmediato de Información o SII. Ver NOTA 2 aclaratoria al final de esta respuesta.
   c. Que **NO** tengan su domicilio fiscal en los Territorios Históricos de la Comunidad Autónoma del País Vasco o de la Comunidad Foral de Navarra. Ver más aclaraciones en la NOTA 3 al final de esta respuesta.
   d. Que **NO** dispongan de alguna resolución en vigor de no aplicación que les exima de cumplir con el RRSIF, aprobado por el Real Decreto 1007/2023, de 5 de diciembre. Ver NOTA 4 aclaratoria al final de esta respuesta.

**NOTA 1 al apartado 2 de esta respuesta**:

Como se puede observar, en este segundo apartado se habla en todo momento de quienes expidan **FACTURAS** –incluidas las facturas simplificadas– cualquiera que sea el motivo para ello (normalmente por estar obligados según el Real Decreto 1619/2012, de 30 de noviembre, que aprueba el Reglamento por el que se regulan las obligaciones de facturación, ROF). Así pues, a ese respecto, se excluyen todas aquellas operaciones que no se documenten con factura porque no haya obligación de expedir factura según dichos RD 1619/2012 y ROF (incluyendo las autorizaciones "especiales" concedidas que pudiera haber en este sentido).

Por lo tanto, el hecho de expedir (o no) factura es clave porque, por definición (artículo 1.2 del RRSIF) el RRSIF no cambia las obligaciones sustanciales de facturación. Un SIF –cuyo funcionamiento es lo que el reglamento regula– es, en esencia, un sistema informático utilizado para expedir FACTURAS. Así que el RRSIF no aplica a sistemas informáticos que no expidan facturas.

**NOTA 2 a la letra b) del apartado 2 de esta respuesta**:

El SII se refiere a la llevanza en la sede electrónica de la Agencia Tributaria de los libros registros de IVA en los términos establecidos en el apartado 6 del artículo 62 del Reglamento del Impuesto sobre el Valor Añadido, aprobado por el Real Decreto 1624/1992, de 29 de diciembre.

Si un obligado tributario está acogido al SII deberá usar un Sistema que le permita cumplir con las exigencias informativas del SII.

**NOTA 3 a la letra c) del apartado 2 de esta respuesta**:

La letra c) del apartado 2 se refiere a que la competencia de exacción tributaria según el domicilio de quien expide la factura NO sea propia de los Territorios Históricos de la Comunidad Autónoma del País Vasco o de la Comunidad Foral de Navarra, de acuerdo con las normas del Concierto y Convenio Económicos. O sea, que NO sean obligados tributarios que realicen actividades económicas (ya sean personas físicas o jurídicas) que se encuentren sujetas por dichas actividades a la normativa foral en la Imposición Directa, tanto en el caso de los 3 territorios históricos de la Comunidad Autónoma del País Vasco (Ley 12/2002, de 23 de mayo, por la que se aprueba el Concierto Económico con la Comunidad Autónoma del País Vasco, y, en concreto, lo establecido en los artículos 6 y 14 de dicho texto, respectivamente, para IRPF e Impuesto de Sociedades), como en el de la Comunidad Foral de Navarra (Ley 28/1990, de 26 de diciembre, por la que se aprueba el Convenio Económico entre el Estado y la Comunidad Foral de Navarra, y, en concreto, según lo establecido en los artículos 9 y 18 de dicho texto, respectivamente para IRPF e Impuesto de Sociedades). De acuerdo con la mencionada normativa existente al respecto y según las condiciones de aplicación que se dan en el RRSIF, esa circunstancia se determina con base en el domicilio fiscal de los mismos.

Por último, para que no haya dudas en lo referente a este aspecto, se confirma que quedan sujetos a la aplicación del reglamento (al menos por lo que se refiere a este criterio) los obligados a expedir facturas radicados en Canarias, Ceuta o Melilla, entendiendo que las referencias al Impuesto sobre el Valor Añadido (IVA) deben considerarse hechas al Impuesto General Indirecto Canario (IGIC) e Impuesto sobre la Producción, los Servicios y la Importación (IPSI), respectivamente.

**NOTA 4 a la letra d) del apartado 2 de esta respuesta**:

Se refiere a la posibilidad prevista específicamente en el artículo 5 del RRSIF.

**Normativa/Doctrina:**

- Artículo 29.2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria (LGT).
- Artículos 1, 3, 4 y 5 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Real Decreto 1619/2012, de 30 de noviembre, que aprueba el reglamento por el que se regulan las obligaciones de facturación (ROF).
- Artículo 62.6 del Reglamento del Impuesto sobre el Valor Añadido, aprobado por el Real Decreto 1624/1992, de 29 de diciembre.

## (Revisada) Entrada en vigor y efectos. ¿Cuál es la fecha límite para tener adaptados los sistemas informáticos de facturación al RRSIF?

Esto varía según el colectivo afectado de que se trate:

- Los contribuyentes sujetos al Impuesto sobre Sociedades deberán tener adaptados los sistemas informáticos a las características y requisitos que se establecen en el reglamento de los requisitos que deben adoptar los sistemas y programas informáticos o electrónicos que soporten los procesos de facturación de empresarios y profesionales y en su normativa de desarrollo antes del 1 de enero de 2027.
- El resto de obligados tributarios mencionados en el artículo 3.1., deberán tener operativos los sistemas informáticos adaptados a las características y requisitos que se establecen en el citado reglamento y en su normativa de desarrollo antes del 1 de julio de 2027.
- Los productores y comercializadores de aquellos SIF a los que les sea de aplicación el reglamento, en relación con sus actividades de producción y comercialización de dichos SIF, deberán ofrecer sus productos adaptados totalmente al reglamento en el plazo máximo de nueve meses desde la entrada en vigor de la orden ministerial (29 de julio de 2025) que desarrolle las especificaciones técnicas de los requisitos impuestos a los SIF. No obstante, en relación con SIF incluidos en los contratos de mantenimiento de carácter plurianual contratados antes de este último plazo, deberán estar adaptados al contenido del reglamento con anterioridad a las fechas indicadas en los párrafos anteriores.

**Normativa/Doctrina:**

- Disposición final cuarta del Real Decreto 1007/2023, de 5 de diciembre, por el que se aprueba el reglamento (RRSIF), modificada por el Real Decreto-ley 15/2025, de 2 de diciembre.

## Pertenezco a un colectivo que, en principio, no está obligado a expedir facturas: ¿me afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?

No, siempre y cuando no se expidan facturas o estas se expidan TODAS a mano, es decir, sin utilizar para ello un sistema informático de facturación (SIF).

Por el contrario, si en algún momento se expidiera alguna factura –por el motivo que sea– y para ello se utilizara un SIF, entonces sí que sería de aplicación el RRSIF (siempre que se cumpla también con el resto de condiciones indicadas en el apartado 2 de la pregunta frecuente "¿A quién afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?" (regla de los 4 «NO») de *Cuestiones generales: ámbitos de aplicación*.

Es importante recordar que el RRSIF solo aplica a los SIF y estos, por definición (artículo 1.2 del RRSIF), solo se consideran tales si son utilizados para expedir lo que –según el ROF– tenga la consideración de FACTURA, incluida la factura simplificada (artículo 1.2 del RRSIF) pero no otros documentos similares o "equivalentes" también justificativos de operaciones.

**Normativa/Doctrina:**

- Artículo 2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria (LGT).
- Artículos 1, 3, 4 y 5 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Real Decreto 1619/2012, de 30 de noviembre, que aprueba el reglamento por el que se regulan las obligaciones de facturación (ROF).

## Un empresario que tributa a las Haciendas Forales Vascas, ¿qué normativa debe cumplir en relación con sus sistemas informáticos de facturación?

No se incluyen dentro del ámbito subjetivo del Reglamento SIF aprobado por el RD 1007/2023 aquellas personas que realicen actividades económicas (ya sean personas físicas o jurídicas) que se encuentren sujetas por dichas actividades a la normativa foral en la imposición directa.

Para determinar qué empresarios y profesionales, se sujetan a normativa foral se seguirán las normas de la Ley 12/2002, de 23 de mayo, por la que se aprueba el Concierto Económico con la Comunidad Autónoma del País Vasco, y, en concreto, lo establecido en los artículos 6 y 14 de dicho texto, respectivamente, para IRPF e Impuesto de Sociedades.

En los territorios históricos de Guipúzcoa, Vizcaya y Álava se está aplicando un sistema, conocido como "TicketBAI", en sus distintas modalidades de contenido similar a la modalidad VERI\*FACTU del Reglamento de Sistemas Informáticos de Facturación.

Por ejemplo, en el caso de que se relacionen comercialmente una empresa con domicilio foral y otra con domicilio en territorio común (resto de España), los SIF utilizados por la primera para expedir sus facturas estarán sometidos a las obligaciones que establece su correspondiente Hacienda Foral, mientras que los SIF de la segunda estarían sujetos al RRSIF.

**Normativa/Doctrina:**

- Artículo 1.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Es aplicable el reglamento que establece los requisitos de los sistemas informáticos de facturación en la Comunidad Foral de Navarra?

Con carácter general, en la Comunidad Foral de Navarra no será aplicable el RD 1007/2023, de 5 de diciembre, que aprueba el Reglamento regulador de los sistemas informáticos de facturación, cuando los empresarios y profesionales, se sujeten a normativa foral de acuerdo con las normas de la Ley 28/1990, de 26 de diciembre, por la que se aprueba el Convenio Económico entre el Estado y la Comunidad Foral de Navarra, y, en concreto, de acuerdo con lo establecido en los artículos 9 y 18 de dicho texto, respectivamente para IRPF e Impuesto de Sociedades.

## (Novedad) Una empresa domiciliada en territorio foral y adscrita a las obligaciones del SII foral, si es la emisora material de las facturas como destinatario (auto-facturación) de operaciones con un proveedor residente en territorio común ¿debe cumplir respecto de dichas operaciones con la normativa RRSIF?

No.

Las empresas adscritas a las obligaciones forales de suministro inmediato de información (SII foral), cuando emitan materialmente las facturas como destinatarias (auto-factura), en nombre y por cuenta de proveedores residentes en territorio común, no deberán cumplir con el RRSIF por dichas operaciones (ni enviando registros de facturación a VERI\*FACTU, ni conservando a disposición los registros de facturación generados).

La exclusión del art. 4.3 RRSIF (facturas emitidas materialmente por un destinatario con residencia en territorio común y adscrito al SII) resulta aplicable cuando el destinatario de la operación tiene su domicilio fiscal en los Territorios Históricos de la Comunidad Autónoma del País Vasco o de la Comunidad Foral de Navarra y se encuentra adscrito al SII de dicho territorio foral.

**Normativa aplicable:**

- Artículo 4.3 del RRSIF, en la redacción dada por el Real Decreto 254/2025, de 1 de abril.

## (Novedad) Una empresa domiciliada en territorio foral y NO adscrita a las obligaciones del SII foral, si es la emisora material de las facturas como destinatario (auto-facturación) de operaciones con un proveedor residente en territorio común ¿debe cumplir respecto de dichas operaciones con la normativa RRSIF?

Sí.

Las empresas **no** adscritas a las obligaciones forales de suministro inmediato de información (SII foral), cuando emitan materialmente las facturas como destinatarias (auto-factura), en nombre y por cuenta de proveedores residentes en territorio común, sí deberán cumplir con el RRSIF por dichas operaciones (enviando registros de facturación a VERI\*FACTU o conservando a disposición los registros de facturación generados).

## Si tengo mi domicilio fiscal en Canarias, Ceuta o Melilla, ¿debo seguir las disposiciones del Real Decreto 1007/2023 y su desarrollo por OM?

Sí, los contribuyentes con domicilio fiscal en Canarias, Ceuta y Melilla, se encuentran comprendidos dentro del ámbito subjetivo de aplicación del Reglamento SIF aprobado por el Real Decreto 1007/2023 y, consiguientemente, les son de aplicación dichas normas y las de su desarrollo por medio de Orden Ministerial.

De acuerdo con el artículo 1.3, las referencias que realiza el Reglamento SIF a la normativa del Impuesto sobre el Valor Añadido, se considerarán también efectuadas a la normativa del Impuesto General Indirecto Canario y a la del Impuesto sobre la Producción, los Servicios e Importación en Ceuta y Melilla.

## Desarrollo mi actividad en territorio común y en Canarias: ¿debo adaptarme al reglamento que establece los requisitos de los sistemas informáticos de facturación?

Sí, siempre que cumpla también con el resto de condiciones indicadas en el apartado 2 de la pregunta frecuente "¿A quién afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?" (regla de los 4 «NO») de *Cuestiones generales: ámbitos de aplicación*.

El Real Decreto 1007/2023, de 5 de diciembre, y el reglamento de requisitos de los sistemas informáticos de facturación (RRSIF) que aprueba son aplicables en todo el territorio español no foral, teniendo en cuenta las especialidades previstas en su normativa específica para Canarias, Ceuta y Melilla, entendiendo que las referencias realizadas a la normativa del Impuesto sobre el Valor Añadido (IVA) deben considerarse también efectuadas a la normativa del Impuesto General Indirecto Canario (IGIC) y a la del Impuesto sobre la Producción, los Servicios y la Importación (IPSI), respectivamente.

**Normativa/Doctrina:**

- Artículo 1.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## (Novedad) Una misma persona jurídica que realiza operaciones que se incluyen en el SII - IVA pero dispone de establecimiento en territorio canario por las que no está adscrito al SII - IGIC ¿debe cumplir para estas últimas la normativa de RRSIF?

Sí.

En el mismo obligado tributario existen dos contribuyentes (en su consideración de persona jurídica en el territorio de aplicación del impuesto IVA y de establecimiento permanente en el territorio de aplicación del impuesto IGIC) a efectos de la aplicación de la exclusión de sujetos adscritos al suministro de información inmediata (SII) del art.3.3 RRSIF. La exclusión debe analizarse de forma separada para cada uno de los dos impuestos indirectos y, por tanto, en relación a su respectivo SII (IVA o IGIC), sin que la exclusión del RRSIF por SII en IVA implique la exclusión del RSIF para la facturación por SII IGIC.

El artículo 3.3 RRSIF se refiere a contribuyentes poniéndolo en relación con un artículo del RIVA, el art.62.6 (registros SII), por lo que el concepto relevante a efectos de la exclusión es el contribuyente que aparece respecto de cada uno de estos impuestos.

En consecuencia, si la exclusión de la aplicación del RRSIF deriva de la adscripción al SII en relación con el IVA, por las operaciones realizadas por el establecimiento canario, que no está adscrito al SII - IVA ni al SII - IGIC no concurre la citada exclusión **y dichas operaciones deben sujetarse a la normativa derivada de RRSIF.**

## (Novedad) Una misma persona jurídica que realiza operaciones que se incluyen en el SII - IVA y dispone de establecimiento en territorio canario por las que también está adscrito al SII - IGIC ¿debe cumplir para estas últimas la normativa de RRSIF?

No.

En el mismo obligado tributario existen dos contribuyentes (en su consideración de persona jurídica en el territorio de aplicación del impuesto IVA y de establecimiento permanente en el territorio de aplicación del impuesto IGIC) a efectos de la aplicación de la exclusión de sujetos adscritos al suministro de información inmediata (SII) del art.3.3 RRSIF. La exclusión debe analizarse de forma separada para cada uno de los dos impuestos indirectos y, por tanto, en relación a su respectivo SII (IVA o IGIC), sin que la exclusión del RRSIF por SII en IVA implique la exclusión del RSIF para la facturación por SII IGIC.

El artículo 3.3 RRSIF se refiere a contribuyentes poniéndolo en relación con un artículo del RIVA, el art.62.6 (registros SII), por lo que el concepto relevante a efectos de la exclusión es el contribuyente que aparece respecto de cada uno de estos impuestos.

Por su parte, el artículo 1 del RRSIF dispone que el Reglamento es aplicable en todo el territorio español, teniendo en cuenta las especialidades previstas en su normativa específica para Canarias, Ceuta y Melilla; y que las referencias que realiza el Reglamento a la normativa del IVA se considerarán también efectuadas a la normativa del IGIC y a la del IPSI en Ceuta y Melilla.

En consecuencia, en el caso de un contribuyente adscrito al SII - IVA, pero con establecimiento permanente en Canarias, cuando las operaciones del establecimiento en Canarias sean declaradas al SII - IGIC (por adscripción obligatorio o voluntaria), **la exclusión de la aplicación del Reglamento RRSIF concurrirá respecto de las operaciones realizadas en territorio de aplicación del impuesto IVA, como las realizadas en Canarias.**

## Soy una persona física que me dedico a alquilar viviendas y locales de negocio: ¿debo adaptar mi sistema informático de facturación al reglamento que establece los requisitos de los sistemas informáticos de facturación?

Por lo que se refiere a IRPF, es preciso determinar si el arrendamiento realizado supone la realización de actividad económica o por el contrario es fuente de rendimientos del capital inmobiliario. Para la consideración como actividad económica se exige que se utilice, al menos una persona empleada con contrato laboral y a jornada completa.

Por lo tanto, si la actividad no tiene consideración empresarial, no será actividad económica en el sentido del artículo 3.1.b) RRSIF, y en ese caso el arrendador no deberá adaptarse porque no se está desarrollando actividad económica.

No obstante, si se trata de un alquiler de un apartamento turístico y se ofrecen servicios complementarios, propios de la industria hotelera, los rendimientos que obtiene por el alquiler son rendimientos de actividades económicas, y, por lo tanto, las facturas que se emitan en este contexto deben entenderse incluidas en el ámbito objetivo del Real Decreto 1007/2023, que aprueba el Reglamento que regula los Sistemas Informáticos de Facturación (RRSIF).

**Normativa/Doctrina:**

- Artículo 3.1 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## (Novedad) Soy un empresario persona física que realiza una actividad económica y utiliza un SIF adaptado al RRSIF para emitir las facturas. Además, tengo alquilado un local sin contratar personas para ello ¿afecta el RRSIF a las facturas emitidas por el arrendamiento?

No.

Los contribuyentes del IRPF que desarrollen actividades económicas y utilicen sistemas informáticos de facturación (SIF), aunque sólo sea en parte de su actividad, deberán utilizar un SIF adaptado al RRSIF (Reglamento que establece los requisitos de los sistemas informáticos de facturación), para todas las actividades económicas respecto de las cuales deban emitir factura.

Sin embargo, si realiza la actividad de alquiler sin tener a ninguna persona contratada a jornada completa y con contrato laboral, no se considera que la misma es una actividad económica a efectos del IRPF, por lo que no le resulta de aplicación el RRSIF a las facturas que debe emitir por el alquiler. Sin perjuicio de que, por comodidad, pueda emitir voluntariamente estas facturas utilizando el SIF.

## (Novedad) Una sociedad patrimonial ¿está obligada a aplicar el RRSIF?

Sí.

El artículo 3 del RRSIF regula específicamente el ámbito subjetivo de la norma e incluye a la totalidad de los contribuyentes del Impuesto sobre Sociedades, sin hacer distinción en función del tipo de actividad que realizan.

## ¿Qué diferencia hay entre el SII (Suministro Inmediato de Información) y el reglamento que establece los requisitos de los sistemas informáticos de facturación? ¿El sistema informático de una empresa incluida en el SII debe cumplir los requisitos del reglamento que establece los requisitos de los sistemas informáticos de facturación?

Se trata de normativas diferentes con obligaciones diferenciadas. El SII consiste en la llevanza de los libros registro de IVA (facturas emitidas, facturas recibidas, bienes de inversión…) a través de la sede electrónica de la Agencia Tributaria, lo que implica obligaciones de comunicación electrónica a la Agencia Tributaria de una amplia información relacionada con el IVA de las facturas emitidas y recibidas en un determinado plazo de tiempo. Por su parte, el reglamento que establece los requisitos de los sistemas informáticos de facturación obliga a que los SIF registren, con determinadas medidas de seguridad y control, cierta información solo de las facturas expedidas, pudiendo remitirse opcionalmente a la Agencia Tributaria.

El ámbito subjetivo de ambos proyectos es excluyente, es decir, quienes cumplan con el SII no han de cumplir con el reglamento que establece los requisitos de los sistemas informáticos de facturación y viceversa.

Por lo tanto, conforme al artículo 3.3 del Reglamento aprobado por RD 1007/2023, este Reglamento NO obliga a los obligados tributarios sometidos al Suministro Inmediato de Información (SII) en relación con sus propias facturas.

**Normativa/Doctrina:**

- Artículo 3.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Orden HFP/417/2017, de 12 de mayo, por la que se regulan las especificaciones normativas y técnicas que desarrollan la llevanza de los Libros registro del Impuesto sobre el Valor Añadido a través de la Sede electrónica de la Agencia Estatal de Administración Tributaria establecida en el artículo 62.6 del Reglamento del Impuesto sobre el Valor Añadido, aprobado por el Real Decreto 1624/1992, de 29 de diciembre, y se modifica otra normativa tributaria.

## ¿Puede un obligado tributario optar voluntariamente al SII y no aplicar las obligaciones del reglamento que establece los requisitos de los sistemas informáticos de facturación?

Sí, mediante la opción prevista en la declaración censal modelo 036, un contribuyente que se haya inscrito en REDEME o que directamente haya optado voluntariamente al SII no estaría obligado a cumplir las especificaciones del RD 1007/2023, sin perjuicio de asumir desde el periodo de liquidación inmediato siguiente el conjunto de las obligaciones que se desprenden del artículo 62.6 del RIVA sobre su facturación emitida y recibida.

**Normativa/Doctrina:**

- Artículo 3.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## (Novedad) Un contribuyente acogido al Suministro Inmediato de Información (SII) y excluido del RRSIF ¿puede acogerse o mantenerse voluntariamente en la modalidad Veri\*factu e incluir QR en sus facturas? (cesar adscripción)

No.

El ámbito subjetivo de ambos proyectos es **excluyente**, es decir, quienes cumplan con el SII no han de cumplir con el RRSIF (Reglamento que establece los requisitos de los sistemas informáticos de facturación) y viceversa. Son normas y obligaciones diferentes.

Si una empresa resultara obligada a su adscripción al SII por su volumen de operaciones, **debe dejar de remitir** registros de facturación a Veri\*factu y dejar de **incluir el QR** tributario en las facturas desde que empiece a cumplir con el SII de forma efectiva, sin que para ello deba esperar al final del año natural en curso.

Conforme al artículo 3.3 del RRSIF, este Reglamento no obliga a los obligados tributarios sometidos al SII al que hace referencia el artículo 62.6 del Real Decreto 1624/1992, de 29 de diciembre, por el que se aprueba el Reglamento de IVA, en relación con sus propias facturas.

## (Novedad) Un contribuyente acogido al Suministro Inmediato de Información (SII) y excluido del RRSIF ¿puede acogerse o mantenerse voluntariamente en la modalidad Veri\*factu e incluir QR en sus facturas? (mantenerse voluntariamente)

No.

El ámbito subjetivo de ambos proyectos es **excluyente**, es decir, quienes cumplan con el SII no han de cumplir con el RRSIF (Reglamento que establece los requisitos de los sistemas informáticos de facturación) y viceversa. Son normas y obligaciones diferentes.

Si una empresa resultara obligada a su adscripción al SII por su volumen de operaciones, **debe dejar de incluir el QR** tributario en las facturas desde que empiece a cumplir con el SII de forma efectiva, sin que para ello deba esperar al final del año natural en curso. En este caso, no habiendo remisión de registros y no imprimiéndose QR tributario, nada impediría utilizar **voluntariamente** un SIF adaptado al SII que también cumpla el resto de requisitos del RRSIF, es decir, genere un registro de facturación, empleando el hash encadenado, firmando las facturas y conservándolas.

Conforme al artículo 3.3 del RRSIF, este Reglamento no obliga a los obligados tributarios sometidos al SII al que hace referencia el artículo 62.6 del Real Decreto 1624/1992, de 29 de diciembre, por el que se aprueba el Reglamento de IVA, en relación con sus propias facturas.

## Estoy acogido al régimen de agricultura, ganadería y pesca de IVA: ¿me afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?

No con carácter general, ya que los obligados a este régimen, no están obligados a expedir factura salvo determinadas excepciones.

Sin embargo, la respuesta es la contraria, siempre que utilicen un sistema informático de facturación, cuando emitan otras facturas de obligada expedición por las entregas de inmuebles a que se refiere el segundo párrafo del apartado uno del artículo 129 de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, según indica el último párrafo del artículo 3.3 del ROF, y siempre que cumplan también con el resto de condiciones indicadas en el apartado 2 de la pregunta frecuente "¿A quién afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?" (regla de los 4 «NO») de *Cuestiones generales: ámbitos de aplicación*. Para estas operaciones excepcionales podrán utilizar el sistema facilitado para ello por la AEAT en su sede electrónica, de acuerdo con el artículo 7.b) del RRSIF.

De igual manera también estará obligado a cumplir el RRSIF cuando utilice un sistema informático de facturación para la expedición voluntaria de facturas en relación a las operaciones exceptuadas de la obligación de expedir facturar.

**Normativa/Doctrina:**

- Artículos 3.3 y 16.1 del reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre.
- Artículo 129.1 de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido.

## Solo realizo operaciones en régimen de recargo de equivalencia de IVA: ¿me afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?

No con carácter general, ya que los obligados a este régimen no están obligados a expedir factura, salvo determinadas excepciones.

No obstante, estará obligado a cumplir el RRSIF cuando utilice un sistema informático de facturación para la expedición voluntaria de facturas en relación a las operaciones exceptuadas de la obligación de expedir facturar.

También, deberá cumplir las obligaciones del reglamento que establece los requisitos de los sistemas informáticos de facturación en el caso de que expida facturas, siempre que cumpla también con el resto de condiciones indicadas ("regla de los 4 «NO»"). Según la normativa de facturación, en el régimen de recargo de equivalencia se deben expedir facturas por realizar determinadas operaciones:

- Cuando efectúe entregas de inmuebles sujetas y no exentas al IVA.
- Cuando tribute en IROF en estimación directa.
- Cuando el cliente sea un empresario o profesional o una Administración Pública.
- Cuando el destinatario lo exija para el ejercicio de cualquier derecho de naturaleza tributaria.
- Cuando se le exija para determinadas operaciones de comercio exterior.

Para estas operaciones excepcionales podrán utilizar el sistema facilitado para ello por la AEAT en su sede electrónica, de acuerdo con el artículo 7.b) del RRSIF.

**Normativa/Doctrina:**

- Artículo 3.1.b) del reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre.

## Solo realizo operaciones en régimen simplificado de IVA: ¿me afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?

No con carácter general, ya que los obligados a este régimen no están obligados a expedir factura, salvo determinadas excepciones.

No obstante, estará obligado a cumplir el RRSIF cuando utilice un sistema informático de facturación para la expedición voluntaria de facturas en relación a las operaciones exceptuadas de la obligación de expedir facturar.

También, deberá cumplir las obligaciones del RRSIF en el caso de que expida facturas, siempre que cumpla también con el resto de condiciones indicadas ("regla de los 4 «NO»"). Según la normativa de facturación, en el régimen simplificado de IVA se deben expedir facturas por realizar determinadas operaciones:

- Cuando la determinación de las cuotas devengadas se efectúe en atención al volumen de ingresos,
- Cuando efectúe la venta de activos fijos,
- Cuando el cliente sea un empresario o profesional o una Administración Pública.
- Cuando el destinatario lo exija para el ejercicio de cualquier derecho de naturaleza tributaria.
- Cuando se le exija para determinadas operaciones de comercio exterior.

Para estas operaciones excepcionales podrán utilizar el sistema facilitado para ello por la AEAT en su sede electrónica, de acuerdo con el artículo 7.b) del RRSIF.

**Normativa/Doctrina:**

- Artículo 3.1.c) del reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre.
- Artículo 123.Uno.B).3.º de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido.

## Si estoy acogido a los regímenes especiales de la agricultura, ganadería y pesca, simplificado o recargo de equivalencia, por los documentos que expida que no cumplan los requisitos de la factura simplificada, emitidos a través de cajas registradoras y similares no considerados como SIF ¿me afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?

Los contribuyentes acogidos a los regímenes de la agricultura, ganadería y pesca, simplificado y de recargo de equivalencia, están, en general, excluidos de la obligación de emitir factura o factura simplificada. Si bien, esa regla tiene excepciones recogidas en los artículos 3.1 y 26 del Reglamento de Obligaciones de Facturación (RD 1619/2012). La mencionada normativa en relación a la obligatoriedad de emitir factura o factura simplificada es presupuesto de la normativa contenida en el Reglamento que regula los Sistemas Informáticos de Facturación (RRSIF), aprobado por RD 1007/2023, de 5 de diciembre.

No obstante, la práctica empresarial, a menudo exige la emisión de justificantes de venta que pueden, o no, revestir la forma de facturas simplificadas y que, estrictamente hablando, no están prohibidas por la norma y pueden emitirse voluntariamente, ya que la normativa se limita a no exigir la obligación de facturar en determinados supuestos. Tales documentos justificativos, en la medida que no sean facturas completas o simplificadas, que sean emitidos en el contexto de las operaciones que quedan excluidas de la obligación de facturación, no estarán sometidas al RRSIF.

Por consiguiente, debe entenderse que cualquiera que sea la razón por la que un empresario emita facturas o facturas simplificadas mediante un Sistema Informático de Facturación (SIF), deberá adoptar sus sistemas a la normativa derivada del RD 1007/23 y su OM de desarrollo.

Por el contrario, si en aplicación de la normativa de facturación (que incluye también el artículo 26 ROF), no se emiten facturas en sentido propio, no será de aplicación el RRSIF.

## Soy titular de una oficina de farmacia que tributo en el régimen especial del recargo de equivalencia, ¿me afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?

Sí, porque con independencia de su tributación en el IVA, a efectos del IRPF determina su rendimiento de actividad económica mediante la aplicación del método de estimación directa.

El artículo 26 ROF establece que los contribuyentes del IRPF que obtengan rendimientos de actividades económicas estarán obligados a expedir factura, cuando dichos rendimientos se determinen por el método de estimación directa, con independencia del régimen a que estén acogidos en el IVA.

En consecuencia, el RRSIF se aplicará a los sistemas informáticos de facturación empleados por los titulares de oficina de farmacia o a cualquier otro contribuyente del IRPF que determine su rendimiento de actividad económica mediante estimación directa, con independencia del régimen de IVA.

## Una tienda emite facturas simplificadas y al final del día saca una "factura recapitulativa" de todas las ventas. ¿Qué se hace con estas facturas simplificadas?

Las facturas simplificadas están sometidas al RRSIF y, en el caso de sistemas VERI\*FACTU deben comunicarse a la AEAT. Lo anterior es independiente de que al final del día se genere una factura o extracto recapitulativo como resumen, con el propósito de asentar en un solo apunte contable las ventas del día o de gestionar el negocio.

En el caso de que se trate de operaciones que correspondan a regímenes especiales de IVA, simplificado, de recargo de equivalencia o de agricultura, nos remitimos a las preguntas específicamente dedicadas a estos.

**Normativa/Doctrina:**

- Artículo 2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Están afectadas las tiendas online?

Sí, la forma convencional o virtual por medio de la cual se oferten o entreguen los bienes o se presten los servicios es indiferente para la obligatoriedad de la aplicación de la normativa incluida en el reglamento de requisitos de los sistemas informáticos de facturación (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre, y su normativa de desarrollo.

La venta online, en algunos casos tiene normativa específica cuando se utilicen regímenes europeos de ventanilla única, que pueden dar lugar a codificaciones específicas en el registro de alta de facturación, pero tales especialidades no excluyen del cumplimiento de las obligaciones del RRSIF.

**Normativa/Doctrina:**

- Artículos 2 y 3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## Expido TODAS mis facturas de forma manual: ¿me afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?

En el caso de que la facturación se produzca de forma manual, por talonarios o escribiendo sobre los mismos a mano o a máquina, no le afectaría el RRSIF porque **no utiliza NINGÚN sistema informático** de facturación (SIF) para expedir sus facturas.

Una alternativa sencilla y adecuada que puede servirle para sustituir los sistemas manuales es utilizar la aplicación básica de facturación que ofrecerá gratuitamente la Agencia Tributaria en su sede electrónica, siempre y cuando sus funcionalidades y condiciones de uso se ajusten a las necesidades de quien la vaya a utilizar.

**Normativa/Doctrina:**

- Artículo 29.2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria.
- Artículo 1 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## (Novedad) Un sujeto que NO utiliza ningún SIF para hacer sus facturas, pero realiza alguna operación con una administración pública y emite facturas a través de la Plataforma "FACe / MiFacturae" ¿quedaría obligado al RRSIF en relación con todas sus facturas?

No.

Con carácter general, **no es posible que conviva la emisión de parte de las facturas con un SIF y parte de forma manual**. De acuerdo con el RRSIF (Reglamento que establece los requisitos de los sistemas informáticos de facturación) la utilización de cualquier SIF que produzca facturas obliga a que toda la facturación debe ser informática.

Con carácter **excepcional**, cuando los obligados a emitir factura NO utilicen ningún SIF (sistema informático de facturación) para emitir sus facturas, pero estén obligados por la normativa legal específica (la Ley 25/2013), a emitir facturas electrónicas a una Administración y para ello usen el **programa informático gratuito MiFacturae**, esta circunstancia constituye una excepción a la unicidad de facturación.

La excepción **no aplica** a las facturas generadas por un SIF en formato Facturae integrado con FACe.

**Notas aclaratorias:**

- Ley 25/2013, de 27 de diciembre, de impulso de la factura electrónica y creación del registro contable de facturas en el Sector Público.
- El Punto General de Entrada de Facturas Electrónicas (FACe) es un registro administrativo de presentación de las facturas a administraciones públicas. Este sistema está conectado con la aplicación MiFacturae y con otros sistemas información del sector privado, lo que permite un envío cómodo y sencillo de sus facturas electrónicas a FACe.
- MiFacturae es el programa informático gratuito que ofrece el Ministerio de Transformación Digital para la generación de la factura electrónica en formato Facturae que generará un archivo informático con datos organizados y se remite a través FACe.
- La principal diferencia entre FACe y Facturae es que FACe es el sistema de entrada de facturas electrónicas a la Administración, mientras que Facturae es el formato estructurado que deben seguir las facturas para ser aceptadas por FACe.
- Para crear una factura electrónica para una Administración puede utilizarse un programa informático (privado o público) que cree facturas electrónicas o bien se puede efectuar mediante la intermediación de un prestador de servicios de facturación electrónica (expedición por un tercero). Una pequeña o mediana empresa, o autónomo, pueden utilizar el programa informático gratuito que ofrece el Ministerio de Transformación Digital (Mifacturae).

## Si uso hojas de cálculo (Excel, Numbers, etc.) o procesadores de texto (Word, Apple Pages, etc.): ¿me afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?

El reglamento **no le afectará** si los procesadores de texto o las hojas de cálculo se utilizan exclusivamente para:

- **Introducir los datos de las facturas.**
- **Expedir e imprimir las facturas.**
- **Conservar la información de facturación.**

Por el contrario, **sí estará sujeto al reglamento y se considerará un sistema informático de facturación** si, además de las funciones anteriores, se utiliza para **procesar la información de facturación contenida en el programa para generar directamente los libros registros de IVA, los libros registro de IRPF, la contabilidad, o cualquier otro resultado que se utilice para el cumplimiento voluntario de obligaciones tributarias.**

Por ejemplo, si un usuario utiliza una hoja de cálculo **Excel** para generar **simples listados de facturas** emitidas, incluyendo sumatorios o el uso de otras reglas de cálculo, no le afectará el Reglamento. **Pero** si la utiliza **programando una Macro, para generar el libro registro de facturas expedidas**, su hoja de cálculo sí se considerará un sistema informático de facturación y, por lo tanto, deberá cumplir con los requisitos del Reglamento.

**Comprobación por parte de la AEAT**

La Agencia Tributaria podrá verificar si los procesadores de texto o las hojas de cálculo utilizadas para la emisión de facturas cumplen los criterios de un sistema informático de facturación en función de las capacidades y herramientas que utilicen.

**Alternativa gratuita para pequeños empresarios y profesionales**

Le recordamos que la AEAT ofrecerá gratuitamente una aplicación básica de facturación, que podrá utilizar siempre y cuando sus funcionalidades y condiciones de uso se ajusten a sus necesidades.

## (Novedad) Un empresario emite materialmente sus facturas sin utilizar un SIF, entregando posteriormente las facturas a su asesor/gestor, quien le presta los servicios de llevanza de libros de contabilidad y libros registros de IVA o IRPF, así como el cumplimiento de sus obligaciones fiscales ¿le afecta el Reglamento que establece los requisitos de los sistemas informáticos de facturación (RRSIF)?

En el caso de que la facturación se produzca **materialmente** por el propio empresario de forma manual, por talonarios o escribiendo sobre los mismos a mano o a máquina (Word/Excel no SIF), **no** le afectaría el RRSIF porque no utiliza ningún sistema informático de facturación (SIF) para expedir sus facturas.

Por el contrario, **sí** estará sujeto al Reglamento cuando el empresario entregue al asesor/gestor la información para que sea éste quien emita **materialmente** las facturas y utiliza un SIF. En este contexto, si el empresario ha delegado la expedición material de la factura en un tercero (como puede ser el asesor/gestor), es el tercero quien, si utiliza un SIF, además de expedir materialmente dicha factura, deberá generar y, si está en la modalidad «VERI\*FACTU», remitir el registro de facturación de alta que exige el RRSIF.

En cualquier caso, esta posibilidad (la delegación) no exime al obligado a expedir facturas (empresario) de la responsabilidad sobre dicho cumplimiento.

## Si, de acuerdo con las disposiciones del Reglamento de Obligaciones de Facturación (ROF), aprobado por Real Decreto 1619/2012, o bien por una autorización de facturación emitida por el Departamento de Gestión Tributaria emitida al amparo del artículo 3.1.d) de dicho Reglamento, un empresario (persona física o jurídica) está exonerado de la obligación de expedir factura, ¿le afecta el reglamento que establece los requisitos de los sistemas informáticos de facturación?

No, si de acuerdo con el Reglamento por el que se regulan las obligaciones de facturación, aprobado Real Decreto 1619/2012, de 30 de noviembre, o bien por una autorización de facturación del artículo 3.1.d) de ese mismo Reglamento no concurriera obligación de facturación, tampoco será aplicable la normativa del Reglamento de Sistemas Informáticos de Facturación.

## En cuanto a los nuevos requisitos en la emisión de facturas completas y simplificadas cuando se utilicen sistemas informáticos de facturación (nuevo apartado 5 del artículo 6 y nuevo apartado 5 del artículo 7 del Reglamento por el que se regulan las obligaciones de facturación) (código "QR" y mención "VERI\*FACTU") ¿afecta sólo a los obligados tributarios del artículo 3.1 del RRSIF o bien, a todos los obligados a emitir factura (incluyendo a los estén en el SII) que utilicen sistemas informáticos?

La inclusión del código QR y la mención VERI\*FACTU es de aplicación a los sistemas informáticos a que se refiere el artículo 7 del Reglamento aprobado por el Real Decreto 1007/2023. Como quiera que de dicho ámbito subjetivo se excluye a los obligados al SII, dichos requisitos SOLO se aplican a las operaciones y los obligados del artículo 3. Los obligados al SII, a todos los efectos, no quedan afectados por el RD 1007/2023.

**Normativa/Doctrina:**

- Artículo 3.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Apartado 5 del artículo 6 y apartado 5 del artículo 7 del Reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre.

## (Revisada) En cuanto a los nuevos requisitos en la emisión de facturas completas y simplificadas cuando se utilicen sistemas informáticos de facturación, en el caso que sólo afecte a los obligados del artículo 3.1 del RRSIF, ¿esta obligación entra en vigor en las fechas previstas en la disposición final cuarta del RD 1007/2023?

Sí, de hecho, todas las obligaciones del Real Decreto 1007/2023, por lo que se refiere a los usuarios, serán de aplicación en las fechas propuestas en la disposición final cuarta del RD 1007/2023, redacción dada por el Real Decreto-ley 15/2025, de 2 de diciembre, ya que la normativa modificada del Reglamento de obligaciones de facturación (ROF) RD 1619/2012, depende de la que se regula en el reglamento que establece los requisitos que deben adoptar los sistemas y programas informáticos o electrónicos que soporten los procesos de facturación de empresarios y profesionales, y la estandarización de formatos de los registros de facturación (RRSIF).

Las obligaciones que corresponden a los productores y comercializadores (producir y vender programas de software adaptados) entrarán en vigor a los 9 meses de la publicación de la OM técnica.

**Normativa/Doctrina:**

- Disposición final cuarta del Real Decreto 1007/2023, de 5 de diciembre (RRSIF), modificada por el Real Decreto-ley 15/2025, de 2 de diciembre.

## En el caso de operaciones exentas del IVA, incluidas en la letra a) del artículo 3.1. del Reglamento de obligaciones de facturación y en el apartado 2 de ese mismo artículo 3, en el supuesto de que conforme a dicho Reglamento no se deba expedir factura ¿el reglamento que establece los requisitos de los sistemas informáticos de facturación se aplicará a estas operaciones?

No, dichas exclusiones implican que no será de aplicación para tales operaciones el RRSIF.

No obstante, debe considerarse que incluso en los supuestos excluidos de facturación por el artículo 3.1.a) ROF, existen excepciones señaladas en el artículo 2.2 del ROF que exigen la emisión de factura. En tales casos, el obligado tributario deberá cumplir las obligaciones del reglamento que establece los requisitos de los sistemas informáticos de facturación en el caso de que expida facturas, siempre que cumpla también con el resto de condiciones indicadas ("regla de los 4 «NO»").

**Normativa/Doctrina:**

- Artículo 1.2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículos 3.1.a), 3.2 y 2.2 del Reglamento por el que se regulan las obligaciones de facturación, aprobado Real Decreto 1619/2012, de 30 de noviembre.

## Un grupo de empresas con el mismo SIF, donde una está en SII y otra no, ¿La empresa que está acogida al SII debe cumplir el reglamento que establece los requisitos de los sistemas informáticos de facturación?

La normativa contempla a los obligados tributarios de forma individualizada (no por grupos) en los que se refiere a sus obligaciones de facturación, por lo que, aunque pertenezcan al mismo grupo de empresas, deberán cumplir con sus obligaciones de facturación con arreglo a su condición. Por lo tanto, el SIF de cada sociedad debe cumplir con las obligaciones de facturación que le correspondan a la misma. Debe señalarse no obstante que voluntariamente las entidades de un grupo pueden darse de alta en el SII a fin de mantener una homogeneidad de gestión con el grupo al que pertenezcan.

Por otro lado, existen productos de mercado capaces de aplicar los requisitos de ambas normativas.

**Normativa/Doctrina:**

- Artículo 3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## Un pequeño comerciante de venta al por menor, dispone de una o varias balanzas para el peso y una máquina registradora donde teclea manualmente las ventas que previamente se han pesado en la balanza, finalmente expide un justificante acumulado (que no es factura simplificada) donde se ven las pesadas y los precios por producto. ¿Este pequeño comerciante está sujeto al RRSIF?

En el supuesto de que el empresario individual estuviera obligado a expedir factura (ordinaria o simplificada), desde el momento que utiliza un sistema informático de facturación consistente en una caja para registrar las ventas realizadas e imprimir para cada una de ellas lo que debería ser una factura simplificada para entregar al cliente está sujeto al RD 1007/2023, de 5 de diciembre, y al reglamento por él aprobado, por lo que deberá cumplirlo, bien adaptando las cajas registradoras (si esto fuera posible), bien adquiriendo algún sistema informático de facturación (SIF) adaptado.

En cuanto a la balanza electrónica, si el empresario o profesional la utiliza solo para pesar el producto y obtener el importe que luego introduce manualmente en la caja registradora para expedir la factura simplificada final, no se consideraría SIF, sino un elemento -independiente- auxiliar de medida (y, en su caso, de cálculo del importe asociado al producto, según su precio por kilogramo). En este caso, el SIF sería la caja registradora, por lo que la balanza electrónica no tendría por qué adaptarse al RD 1007/2023.

Sin embargo, hay balanzas electrónicas con funcionalidades más potentes que permiten acumular los importes de los diferentes productos pesados y expedir en unidad de acto una factura simplificada de la compra total realizada (entre otras posibles funcionalidades), por lo que entonces sí serían consideradas SIF al ser utilizadas también como cajas registradoras. Dicho de otro modo, serían SIF con otros elementos electrónicos auxiliares (en este caso, para el pesaje) añadidos. Si es así, entonces deberían adaptarse al RD 1007/2023 y al reglamento por él aprobado. Las conexiones a internet pueden gestionarse a través de líneas telefónicas y, por otra parte, los sistemas de emisión de facturas no verificables permiten la custodia de los ficheros en la sede local.

**Normativa/Doctrina:**

- Artículo 3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## Las facturas expedidas por empresarios o profesionales residentes en España a empresarios o particulares en el extranjero ¿Se encuentran sometidas a las obligaciones que establece el reglamento que establece los requisitos de los sistemas informáticos de facturación (RRSIF), aprobado por Real Decreto 1007/2023?

Sí, TODAS las operaciones respecto de las cuales empresarios y profesionales (personas físicas o jurídicas) deban emitir factura con arreglo a la normativa vigente (especialmente de acuerdo con el Reglamento de Obligaciones de Facturación aprobado por RD 1619/2012) se someten al RRSIF. Lo anterior incluye tanto las exportaciones como las entregas intracomunitarias de bienes y las prestaciones internacionales o intracomunitarias de servicios.

**Normativa/Doctrina:**

- Artículos 1, 3 y 4 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## Las facturas expedidas por empresarios o profesionales NO residentes en España ¿Se encuentran sometidas a las obligaciones que establece el reglamento que establece los requisitos de los sistemas informáticos de facturación (RRSIF), aprobado por Real Decreto 1007/2023, si se emiten en España?

Sí, cuando el empresario no residente disponga de un establecimiento permanente a los efectos de la normativa del Impuestos sobre la Renta de no Residentes (Real Decreto Legislativo 5/2004, de 5 de marzo).

**Normativa/Doctrina:**

- Artículo 1 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

---

# Cuestiones generales: cumplimiento y delegación

## ¿Se puede solicitar la no aplicación total o parcial del reglamento que establece los requisitos de los sistemas informáticos de facturación?

Sí. El reglamento que establece los requisitos que deben adoptar los sistemas y programas informáticos o electrónicos que soporten los procesos de facturación de empresarios y profesionales, y la estandarización de formatos de los registros de facturación (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre, prevé en su artículo 5 la posibilidad de que se solicite la no aplicación del o de algún aspecto del mismo cuando concurran determinadas circunstancias, que se entienden extraordinarias, relacionadas con la actividad económica o de índole técnica.

La solicitud se podrá presentar a través de la sede electrónica de la Agencia Tributaria.

**Normativa/Doctrina:**

- Artículo 5 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Se puede delegar en un tercero el cumplimiento de los requisitos del reglamento que establece requisitos de los sistemas informáticos de facturación?

Sí. Se puede delegar en el destinatario de la operación o en un tercero el cumplimiento material de las obligaciones del reglamento que establece los requisitos de los sistemas informáticos de facturación siempre que se den las condiciones establecidas en el artículo 5 del reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre, a los efectos de la obligación de expedir de la factura, con facultades otorgadas para ello.

En cualquier caso, esta posibilidad no exime al obligado a expedir facturas de la responsabilidad sobre dicho cumplimiento.

**Normativa/Doctrina:**

- Artículo 6 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 5 del reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre.

## Cuando la factura la expide materialmente el destinatario de la operación («autofactura»), ¿quién genera el registro de facturación de alta para cumplir con el reglamento que establece los requisitos de los sistemas informáticos de facturación? ¿Cómo incluyen la factura en sus respectivos libros registros de IVA?

Antes de nada, debe tenerse en cuenta que el objeto regulado en el reglamento que establece los requisitos que deben adoptar los sistemas y programas informáticos o electrónicos que soporten los procesos de facturación de empresarios y profesionales, y la estandarización de formatos de los registros de facturación (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre, son precisamente los sistemas informáticos de facturación (SIF), que es diferente de la obligación de la llevanza de libros registros de IVA (LRI). Son por tanto obligaciones diferentes que pueden afectar a obligados tributarios distintos.

En el caso planteado, y por lo que se refiere a las obligaciones impuestas por el RRSIF, si el proveedor ha delegado la expedición material de la factura en su cliente, es el cliente quien, además de expedir materialmente dicha factura, deberá generar –y, en la modalidad «VERI\*FACTU», remitir– el registro de facturación de alta que exige el RRSIF. No obstante, si el cliente lleva los libros registros de facturación en los términos establecidos en el artículo 62.6 del Reglamento del Impuesto sobre el Valor Añadido, aprobado por el Real Decreto 1624/1992, de 29 de diciembre, (mediante el suministro inmediato de información, o SII) queda excepcionado del cumplimiento de las obligaciones previstas en el RRSIF para dichas operaciones.

Por otro lado, en relación con la llevanza de los LRI, es independiente de quién expida materialmente las facturas, y se encuentra regulada en los artículos 62 y 63 del Reglamento del Impuesto sobre el Valor Añadido, aprobado por el Real Decreto 1624/1992, de 29 de diciembre. Por lo tanto, cada empresa deberá incluir las facturas expedidas por todos los bienes vendidos y servicios prestados (independientemente de quién haya expedido materialmente la factura, pudiendo ser la propia empresa vendedora, un tercero o el destinatario/comprador) en el LRI de facturas expedidas, y las facturas recibidas de los bienes comprados o servicios recibidos (independientemente de quién haya expedido materialmente la factura, pudiendo ser la empresa vendedora, un tercero o el destinatario/comprador) en el LRI de facturas recibidas.

**Normativa/Doctrina:**

- Artículos 5 y 6 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre, modificado por el Real Decreto 254/2025, de 1 de abril.
- Artículo 5 del reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre.
- Artículos 62 y 63 del reglamento del Impuesto sobre el Valor Añadido (RIVA), aprobado por el Real Decreto 1624/1992, de 29 de diciembre.

## (Novedad) ¿En los supuestos en los que el destinatario de la operación emite materialmente la factura (auto facturas) por cuenta del obligado a emitirla ¿debe el obligado a emitirla, sujeto al RRSIF, comunicar esta circunstancia en el modelo 036?

No.

La comunicación censal del obligado a emitir (proveedor) a través de las casillas 739 y 740 del Modelo 036 atienden únicamente al ámbito de los sujetos adscritos al SII (Suministro Inmediato de Información).

Artículo 5 del ROF (Reglamento que establece las obligaciones de facturación) y artículo 6 del RRSIF (Reglamento que establece los requisitos de los sistemas informáticos de facturación).

## (Novedad) ¿Es necesario apoderar al tercero o destinatario de la operación cuando expiden materialmente la factura en lugar del obligado a emitir la misma?

Para que un tercero/destinatario autorizados de acuerdo con el artículo 5 del Reglamento que establece las obligaciones de facturación (ROF) a emitir facturas, pueda enviar los registros de facturación de acuerdo con el Reglamento que establece los requisitos de los sistemas informáticos de facturación (RRSIF) en nombre y por cuenta del obligado a su emisión, debe estar apoderado, y dicho apoderamiento debe estar inscrito en el registro de apoderamientos: ya bien sea con un poder general o un poder específico para enviar los registros de VERI\*FACTU.

Para dar de alta el apoderamiento existen 3 vías:

- Poder otorgado mediante comparecencia personal en las Delegaciones y Administraciones de la Agencia y en el caso de personas jurídicas o entidades carentes de personalidad jurídica a que se refiere el artículo 35.4 LGT, mediante comparecencia del representante legal de la entidad o de quien ostente poder suficiente para otorgar los apoderamientos.
- Poder otorgado mediante documento público o documento privado con firma notarialmente legitimada presentado ante la Agencia Tributaria.
- Poder otorgado por internet mediante el uso de alguno de los sistemas de identificación y autenticación previstos en la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas.

Esta última es la vía más fácil y preferible para otorgar el citado apoderamiento. Para ello, el poderdante puede entrar en el siguiente trámite: *Agencia Tributaria: Registro de apoderamientos*.

Y posteriormente, entrar en la gestión *Alta de poder para trámites tributarios específicos (agenciatributaria.gob.es)*.

En este enlace, pueden accederse a los trámites específicos relativos a los "Sistemas Informáticos de Facturación y VERI\*FACTU". Trámites disponibles:

- IZ860 - Remisión y consulta de registros de facturación por servicio web
- IZ861 - Consulta de registros de facturación
- IZ862 - Emisión de facturas mediante aplicación de facturación de la AEAT
- IZ863 - Consulta de facturas emitidas por la aplicación de facturación de la AEAT
- IZ864 - Aportar autorización

## (Novedad) ¿Cómo se otorga la representación a un profesional tributario para que remitan, en el ámbito de la colaboración social en la aplicación de los tributos, los registros de facturación generados por sistemas informáticos de facturación?

A diferencia de los apoderamientos, en la colaboración social el contribuyente autoriza a su representante mediante un modelo de representación (no confundir con un documento de apoderamiento) para que realice determinados trámites por internet ante la AEAT. **Dicha autorización debe quedar en poder del colaborador social y no debe aportarse a la AEAT, salvo requerimiento.**

Para otorgar la representación al colaborador social serán válidos los modelos aprobados por la Resolución de 18 de diciembre de 2024, de la Dirección General de la Agencia Estatal de Administración Tributaria, por la que se aprueban los documentos normalizados para acreditar la representación de terceros en el procedimiento para el envío de los ficheros que contienen registros de facturación generados por sistemas de emisión de facturas, a través de la Sede electrónica de la Agencia Tributaria, y que son los que figuran como anexos en dicha resolución:

- Anexo II, para el otorgamiento de la representación de los obligados tributarios a los profesionales tributarios.

## (Novedad) ¿Cómo se otorga la representación a las empresas suministradoras de software para que remitan, en el ámbito de la colaboración social en la aplicación de los tributos, los registros de facturación generados por sistemas informáticos de facturación?

A diferencia de los apoderamientos, en la colaboración social el contribuyente autoriza a su representante mediante un modelo de representación (no confundir con un documento de apoderamiento) para que realice determinados trámites por internet ante la AEAT. **Dicha autorización debe quedar en poder del colaborador social y no debe aportarse a la AEAT, salvo requerimiento.**

Para otorgar la representación al colaborador social serán válidos los modelos aprobados por la Resolución de 18 de diciembre de 2024, de la Dirección General de la Agencia Estatal de Administración Tributaria, por la que se aprueban los documentos normalizados para acreditar la representación de terceros en el procedimiento para el envío de los ficheros que contienen registros de facturación generados por sistemas de emisión de facturas, a través de la Sede electrónica de la Agencia Tributaria, y que son los que figuran como anexos en dicha resolución:

- Anexo I, para el otorgamiento de la representación directa de los obligados tributarios a las empresas suministradoras de software, que prestarán servicios desde sus plataformas.
- Anexo III, para el otorgamiento de la representación de los profesionales tributarios a las empresas suministradoras de software, para profesionales tributarios que prestan sus servicios a los obligados tributarios bajo licencia de las aplicaciones y programas suministrados por empresas suministradoras de software.

---

# Características y requisitos de los sistemas informáticos de facturación (SIF): recursos necesarios, uso múltiple

## ¿Qué alternativas existen para que quien expida facturas y esté afectado por el reglamento que establece los requisitos de los sistemas informáticos de facturación cumpla con él?

Esta pregunta se refiere a los recursos informáticos necesarios para llevar a cabo dicho cumplimiento y la respuesta se encuentra en el artículo 7 del reglamento que establece los requisitos que deben adoptar los sistemas y programas informáticos o electrónicos que soporten los procesos de facturación de empresarios y profesionales, y la estandarización de formatos de los registros de facturación (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

Se puede resumir en que debería utilizar un sistema informático de facturación (SIF) adaptado al RRSIF, que podría ser:

- SIF existente en el mercado, gratuito o de pago: artículo 7.a). Podría estar instalado en las dependencias de quien expida las facturas (*on-premise*), en remoto, o bien en la nube (*cloud*).
- SIF desarrollado internamente por quien expida las facturas: artículo 7.a).
- La aplicación básica de facturación que ofrecerá gratuitamente la Agencia Tributaria en su sede electrónica, siempre y cuando sus funcionalidades y condiciones de uso se ajusten a las necesidades de quien la vaya a utilizar: artículo 7.b)

Por último, se recuerda que existe la posibilidad de delegar en un tercero o en el destinatario de la operación la expedición material de las facturas, que deberá realizarse cumpliendo el RRSIF. Existen otras preguntas frecuentes que tratan sobre este aspecto.

## Para un pequeño empresario o microempresa, ¿qué soluciones prevé el reglamento que establece los requisitos de los sistemas informáticos de facturación aprobado por RD 1007/2023, de 5 de diciembre?

Aunque no está mencionado en el RRSIF, debe señalarse que se ha ampliado el plazo de presentación de solicitudes del SEGMENTO III (entre 0 y de 3 empleados) del KIT DIGITAL, hasta el 31/10/2025. Este Programa está financiado con fondos del Plan de Recuperación Transformación y Resiliencia y tiene como objetivo el impulso al «Plan de Digitalización de las PYMEs 2021-2025». El importe máximo de ayuda por beneficiario será de dos mil euros (2.000 €). Y entre las soluciones financiables se encuentra la de Gestión de Procesos en la que se encuadran los Sistemas Informáticos de Facturación.

Por otro lado, el Reglamento SIF (aprobado por RD 1007/23) prevé en su artículo 7.b) la creación de una aplicación informática que será desarrollada por la Administración tributaria y que servirá para cumplir con el Reglamento SIF en su modalidad VERI\*FACTU. Esta aplicación podría servir también más adelante para facilitar la emisión de facturas electrónicas B2B.

## ¿Qué requisitos debe cumplir un sistema informático de facturación (SIF) para considerarse que está adaptado al reglamento que establece los requisitos de los sistemas informáticos de facturación?

Resumidamente, debe:

- Garantizar la integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros de facturación que está obligado a generar por cada factura expedida, en los términos del RRSIF y de su OM, generando un fichero de alta de factura por cada una de las expedidas. Además, debe imprimirse un código QR en las condiciones específicamente reguladas.
- Tener la capacidad de comunicación con la AEAT para la remisión de los mismos.
- Además, si se tratan datos personales, debe cumplir con las medidas previstas en la legislación en materia de protección de datos para lo cual debe disociar o separar el acceso a la información tributaria de otro tipo de información confidencial, de manera que la Agencia Tributaria pueda acceder a la primera.
- Por último, el SIF deber registrar ciertos eventos que sucedan en el mismo (a menos de que se trate de un SIF funcionando en modo VERI\*FACTU).

Los detalles concretos sobre cómo han de implementarse estos requisitos se aclaran en otras preguntas frecuentes.

**Normativa/Doctrina:**

- Artículo 29.2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria.
- Artículos 7 y 8 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Puede ser utilizado un mismo sistema informático de facturación (SIF) para llevar la facturación de varios obligados a expedir facturas (OEF)?

Sí, pero con ciertas condiciones. En el artículo 7.a) del reglamento que establece los requisitos que deben adoptar los sistemas y programas informáticos o electrónicos que soporten los procesos de facturación de empresarios y profesionales, y la estandarización de formatos de los registros de facturación (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre, se prevé tal posibilidad siempre que los registros de facturación de cada obligado tributario se encuentren diferenciados y se cumplan los requisitos exigidos en el RRSIF por separado para cada uno de los obligados tributarios. Es decir, el sistema deberá comportarse como si fuera un SIF «propio» e independiente para cada OEF.

Esto se traduce en que debe gestionar separadamente los registros de facturación y, en su caso, de evento de cada OEF incluido en el SIF, cumpliendo con los requisitos exigidos en los artículos 7.a) y 8 del RRSIF, con encadenamiento independiente para dichos registros de cada OEF. Asimismo, deberá poder permitir el funcionamiento del SIF en la modalidad «VERI\*FACTU» de forma independiente para cada OEF. Adicionalmente, deberá visualizar, claramente y en todo momento, la información identificativa del OEF al que corresponde la operativa que se está realizando en cada instante. Además, en el caso de que efectivamente esté soportando la facturación de más de un OEF, independientemente del estado operativo en que se encuentren, bien sea de alta, de baja o cualquier otro, deberá indicarlo con algún mensaje explicativo que pueda ser consultado de forma rápida, fácil e intuitiva.

**Normativa/Doctrina:**

- Artículos 7 y 8 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 2 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## Cuando un sistema informático de facturación (SIF) tiene la posibilidad de borrar registros de facturación ya generados, es decir, de eliminarlos. ¿Cumple con el reglamento que establece los requisitos de los sistemas informáticos de facturación?

No. Cualquier funcionalidad o mecanismo del SIF que permita alterar los registros de facturación una vez generada la factura o el rastro de las operaciones supone un incumplimiento de los requisitos exigidos por el reglamento.

A estos efectos, se entiende por alteración de los registros de facturación, la ocultación o eliminación de cualquier registro de facturación originalmente generado y registrado por el sistema informático, o la ocultación o modificación, total o parcial, de los datos de cualquier registro de facturación originalmente generado y registrado por el sistema informático, o la adición de registros de facturación, simulados o falsos, distintos a los originalmente generados y registrados por el sistema informático.

Cualquier necesidad de corrección o anulación de los datos obligatorios registrados deberá ser realizada mediante los procedimientos regulados en el reglamento y su orden ministerial, generando al menos un registro de facturación adicional posterior, de forma que se conserven inalterables los datos originalmente registrados y los corregidos.

**Normativa/Doctrina:**

- Artículos 8.2.a) y 8.2.b) del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Cuántas facturas está previsto que se puedan enviar por cada obligado y por año o por mes, con la aplicación de la AEAT?

La limitación viene dada por la operativa de digitación de la información contenida en el formulario. Lo lógico es que dicha aplicación de uso subsidiario se utilice por microempresarios o profesionales con un número limitado de facturas emitidas al año.

---

# Características y requisitos de los SIF: capacidad de remisión, certificados, etc.

## Si una empresa NO se acoge al sistema VERI\*FACTU (sistema de emisión de facturas verificables) ¿debe igualmente mantener un sistema que permita la conexión con la AEAT?

Sí, la potencial conexión de todos los sistemas informáticos de facturación con la Agencia Tributaria viene obligada por el artículo 8.1 del RRSIF que establece:

*(…) El sistema informático deberá tener capacidad de remitir por medios electrónicos a la Administración tributaria, de forma continuada, segura, correcta, íntegra, automática, consecutiva, instantánea y fehaciente, todos los registros de facturación generados a que se refieren los artículos 9, 10 y 11 de este Reglamento.*

Por lo tanto, la normativa obliga a que todos los sistemas informáticos de facturación tengan la capacidad de comunicar con la AEAT y, por ejemplo, ante un requerimiento de la Agencia Tributaria puedan comunicar directamente los registros que le son requeridos, o bien, adoptar en cualquier momento la modalidad VERI\*FACTU, con remisión inmediata en línea a la AEAT.

**Normativa/Doctrina:**

- Artículo 8.1 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Para la generación de firma se usarán certificados como TicketBAI?

El tipo de firma electrónica a utilizar por parte de los desarrolladores de software para cumplimentación de la obligación de firmar los ficheros de alta o anulación de facturas puede ser distinto de los utilizados por la AEAT, siempre que sea firma cualificada y sirva a la finalidad de autenticar y hacer inmutable el contenido del registro de facturación de alta.

## Una empresa tiene dos centros de facturación, uno central y otro en una sede distinta que no están conectados entre sí. ¿Cómo hacer que se siga entre ambos centros la secuencia correlativa de facturación?

Si todos los sistemas informáticos mencionados (tanto el central como el de la sede "desconectada") expiden independientemente facturas, cada una con su QR incluido, serán ambos sistemas considerados sistemas informáticos de facturación (SIF) independientes, según el artículo 1.2 del reglamento aprobado por el RD 1007/2023, de 5 de diciembre (RRSIF) y, por lo tanto, cada uno de ellos debe cumplir separadamente dicho RRSIF.

Así, cada uno de ambos SIF, al mismo tiempo que expiden cada factura deben generar su correspondiente registro de facturación (RF) de alta. Estos Registros de Facturación deberán estar encadenados (con el hash correspondiente) de forma independiente dentro de cada SIF, respetando la secuencia de generación de los mismos, es decir, de acuerdo al orden en el que fueron generados en cada uno de ellos. Por lo tanto, para expedir sus propias facturas (y generar los correspondiente Registros de Facturación asociados, de forma encadenada) no tienen por qué -ni necesitan- saber qué facturas están expidiendo otros SIF de la misma sociedad o empresa, ya que son independientes a estos efectos y no necesitan para ello estar "conectados o comunicados" entre sí.

## Una empresa tiene dos centros de facturación, uno central y otro en una sede distinta que no están conectados entre sí. ¿Es posible que uno de los sistemas sea un sistema VERI\*FACTU y el otro no?

Sí, ya que ambos SIF pueden cumplir con la norma en distintas modalidades. No obstante, se significa que no es esta la opción preferible ya que generará en los registros disponibles en sede electrónica de la AEAT listados incompletos de facturas emitidas, que harán preciso completar mediante requerimientos.

## Una empresa tiene dos centros de facturación, uno central y otro en una sede distinta que no están conectados entre sí. ¿Puede plantearse la posibilidad de que el sistema informático vuelque, al final del día los registros de facturación en un sistema conectado para su remisión a la AEAT?

No, ese volcado ulterior no es en sentido propio una facturación, puesto que los clientes ya se habrán llevado las facturas impresas y, por lo tanto no cabe esa remisión "en diferido".

## ¿Qué pasa si el SIF sufre un incidente que pueda provocar pérdida de datos?

Un SIF cumplidor del reglamento y la orden debería garantizar que no se den ese tipo de circunstancias o que es capaz de recuperarse adecuadamente ante las mismas y seguir cumpliendo el reglamento y la orden, estableciendo las medidas y procedimientos necesarios para ello.

## ¿Qué quiere decir que el sistema informático de facturación (SIF) debe permitir una disociación de acceso a los datos según el carácter de estos?

Significa que el SIF deberá tener una forma diferenciada de acceder a las funcionalidades y a los datos con trascendencia tributaria exigidos en el reglamento, de manera que quede preservada la confidencialidad de otros datos distintos y no se pueda acceder indebidamente a ellos por esa vía. Esto se prevé sobre todo en el caso de que se produzca una personación de algún miembro de la Agencia Tributaria para inspeccionar in situ el SIF, siempre cumpliendo con los procedimientos establecidos al respecto.

---

# Características y requisitos de los SIF: integridad e inalterabilidad

## ¿Cómo pueden los desarrolladores asegurar que alguien no pueda eliminar o modificar un archivo correspondiente a esos registros de facturación?

El SIF deberá garantizar la integridad e inalterabilidad, la trazabilidad, y conservación de los registros de facturación, en los términos establecidos en el artículo 8 del RRSIF y su normativa de desarrollo. Además, deberá contar con un registro de eventos en el que se recojan determinadas interacciones con el sistema determinadas por orden ministerial (entre otras, la detección de anomalías en la integridad, inalterabilidad y trazabilidad de registros de facturación o en el propio registro de eventos).

Por lo que se refiere a los desarrolladores y su responsabilidad, deberán afrontar las exigencias reglamentarias para hacer posible asegurar que, durante el periodo de conservación de los registros, no se han producido interacciones indebidas sobre los mismos que los hayan alterado, modificado, interpolado, suprimido o regenerado. Igualmente deberán certificar a sus clientes que cumplen con esas exigencias. Naturalmente el régimen sancionador al que se refiere el artículo 201.bis de la LGT debe tener en cuenta a la hora de sancionar los comportamientos de los fabricantes de sistemas y de los usuarios si ha concurrido en sus comportamientos culpabilidad, incluso a título de mera negligencia, o se ha producido la destrucción o hackeo de los códigos del programa.

## Si la modificación del registro de facturación se debe a un error informático (por ejemplo una corrupción de datos, un fallo en la migración…) ¿puede el fabricante del software corregir dicho registro de facturación sin generar un registro adicional?

No, un registro de facturación, una vez generado (y firmado / remitido a la AEAT según la modalidad empleada) no debe ser modificado nunca por nadie (si se hiciera, se podría detectar: gracias a la huella, firma, encadenamiento...). Cualquier "cambio" que se desee hacer constar sobre el mismo, deberá realizarse a través de la generación de uno o más -según se necesite- registros de facturación nuevos, del tipo que corresponda a cada caso (normalmente -y de forma preferente- utilizando los procedimientos establecidos por el reglamento de obligaciones de facturación). Si por corregir se refiere a "recuperar" de algún modo lo que ya estaba generado, pero se había "perdido" o "corrompido", la respuesta debe ser la contraria.

En cuanto a la corrupción de datos, se recuerda que se debe cumplir con todos los requisitos que exige el reglamento y la orden, siendo en este caso de especial importancia la conservación (y también la legibilidad, accesibilidad e integridad inalterabilidad), por lo que deberán ponerse los medios necesarios para impedir la corrupción y garantizar la conservación.

Finalmente, sobre la cuestión de la migración, el reglamento y la orden no entran en lo que se haga posteriormente con los registros de facturación generados (como su posible envío a otros sistemas con idea de utilizarlos para otros fines), más allá de exigir su conservación, legibilidad y accesibilidad a futuro durante el plazo de conservación.

## ¿Cómo se debe corregir una factura (registro de facturación) con errores generada en un sistema informático de facturación?

Un registro de facturación con errores se debe subsanar mediante la generación de un nuevo registro de facturación y, en su caso, su remisión en los sistemas VERI\*FACTU (ya que no se puede alterar el registro erróneo si ya se emitió).

De acuerdo con el diseño de registro que se publicará en la Orden Ministerial (ya disponible en la Sede electrónica de la AEAT), esta nueva generación de un registro de facturación deberá llevar 'Tipo de registro'="Sustitutivo" e indicador SubsanaError a "S". Con ello la trazabilidad no se ve afectada, ya que esta va ligada a los registros de facturación según el orden temporal de su generación, no a las facturas a las que estos referencian.

## ¿Está permitido tener un sistema de pre-facturación (o borrador) antes de generar los registros de facturación?

El reglamento que aprueba el RD 1007/2023, de 5 de diciembre, y la Orden Ministerial que lo desarrolla solo aplican a los sistemas informáticos de facturación (SIF), es decir, aquellos sistemas que son utilizados para expedir facturas o facturas simplificadas. Cualquier otro sistema informático que no sea de facturación, en principio no se ve afectado por la normativa.

Los requisitos generales de trazabilidad que emanan del literal del artículo 29.2.j) determinan que, a efectos informáticos, el sistema de generación de pre-facturación, borradores o proformas sin validez fiscal, debe estar vinculado indefectiblemente al Sistema de emisión de facturas, formando una unidad. Por ello y por razones de control interno, conviene que se conserven registros de las prefacturas o facturas proforma elaboradas.

Por ello, no sería legal y sería susceptible de sanción, el uso de sistemas que generen documentos preparatorios de facturas o de facturas simplificadas, sin que el sistema informático mismo disponga de elementos de control para la conservación de tales documentos preparatorios de forma debidamente vinculada a las facturas o a los registros de facturación que finalmente se emitan o, en defecto de factura, de forma que queden registrados y conservados en el sistema.

## ¿A partir de qué momento se considera que debe haber integridad o inalterabilidad en un registro de facturación?

Como el registro de facturación se genera inmediatamente antes de expedir la factura, se debe entender que en el momento de generar dicho registro que, además, o bien será remitido a la AEAT, o bien será firmado.

## ¿Qué datos de un registro de facturación podrían ser modificados sin que afecte a la integridad e inalterabilidad? ¿Podrían modificarse los datos que no formen parte de la huella?

Se puede subsanar (tipo registro Sustitutivo) cualquier dato al que el reglamento de facturación no imponga la emisión de una factura rectificativa. En cualquier caso, si el dato modificado de la factura no está en el registro de facturación generado y firmado / remitido (ni afecta a ninguno de los campos de este), propiamente no habría que subsanar nada del registro de facturación generado y firmado / remitido. Pudiéndose cambiar sin que ello afecte a la integridad del fichero.

## ¿Cómo se debe actuar en el caso de pérdida total de registros por un virus o incidente similar?

Si la pérdida solo afecta a registros de facturación, en un sistema VERI\*FACTU esta situación sería menos problemática pues los registros los tendría la AEAT y el obligado podría recuperarlos en su integridad. En un sistema de emisión de facturas no verificables, es el empresario el que debe velar por la conservación de los registros de facturación, tal y como se fija en la norma, sin que quepa negar la posible existencia de casos de fuerza mayor que excluirían la culpabilidad y podrían dar lugar a determinar las bases imponibles por el método de estimación indirecta.

---

# Características y requisitos de los SIF: trazabilidad

## ¿En qué consiste la trazabilidad exigida a los sistemas informáticos de facturación (SIF) en el reglamento y la orden «de requisitos de los SIF»?

La trazabilidad se refiere a que se pueda garantizar (y, en su caso, detectar) que no hay "huecos" o "saltos" en la secuencia de generación de los registros de facturación (RF) correspondientes a las facturas expedidas utilizando un determinado SIF de un obligado tributario (OT), así como que dicha secuencia se corresponde con la de la fecha y hora de generación empleadas.

Esto se consigue "encadenando" los RF generados por cada SIF del OT, es decir, formando virtualmente una "cadena" debido a que dentro de los datos de cada RF generado figuran ciertos datos (ver abajo, al pie de esta respuesta, la **NOTA 1**) del RF generado inmediatamente antes (y que, por tanto, permiten identificarlo), actuando a modo de "puntero" hacia él. Si esta cadena se viese alterada de algún modo (ruptura de la secuencia de punteros, fechas y horas no coherentes…), este hecho podría ser detectado.

En definitiva, con la implementación de la trazabilidad se puede saber si se cuenta con todos los RF generados por un SIF de un OT y si estos están en el mismo orden secuencial en que fueron generados.

Por último, mencionar que los sistemas de emisión de facturas no verificables también deben garantizar la trazabilidad de los registros de evento que generen, de una forma equivalente a como lo realizan para los RF.

**NOTA 1**: los datos que intervienen en el encadenamiento se pueden ver en los correspondientes diseños de registros del anexo de la orden, pero básicamente son la identificación de la factura (emisor, nº de serie y nº de factura, fecha de expedición) a la que hace referencia el RF anterior y "parte" de la huella del RF anterior (actualmente se trata de toda la huella).

**Normativa/Doctrina:**

- Artículos 8.2.b) del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 7 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## ¿A qué nivel se debe realizar la trazabilidad exigida en el reglamento y la orden «de requisitos de los sistemas informáticos de facturación (SIF)»: obligado tributario (OT), tienda, terminal punto de venta (TPV)…?

Los registros de facturación (RF) se deben encadenar de forma independiente dentro de cada SIF, y para cada OT (en el caso de que el SIF gestione la facturación de varios OT). Es decir, debe existir una única cadena de RF por cada par de valores distintos de (SIF; OT).

Por lo tanto, la respuesta a esta pregunta dependerá de cómo tenga organizado cada OT su forma de facturar y del número de OT cuya facturación se gestione en cada SIF empleado.

En relación con lo 1º (la organización de la forma de facturar por parte del OT), por ejemplo, si un OT dispone de varios TPV (en uno o diversos centros de venta, o tiendas) que **expiden o gestionan la expedición de sus propias facturas de forma independiente** a las del resto de TPV, cada TPV se considera que es un SIF, de acuerdo a la definición dada en el reglamento, así que deberá poseer su propia cadena de RF. De esta manera, el OT tendrá tantas cadenas de RF como TPV tenga.

En relación con lo 2º (número de OT gestionados por el SIF), si un SIF permite la gestión de la facturación de varios OT (como puede ser el caso de un SIF utilizado por una gestoría para llevar en él la facturación de varios OT que son clientes de esa gestoría), dicho SIF deberá tener una cadena independiente por cada OT cuya facturación gestione.

## ¿Qué ámbito o alcance tiene la trazabilidad exigida en el reglamento y la orden «de requisitos de los sistemas informáticos de facturación (SIF)»? Por ejemplo, ¿debe mi SIF garantizar la trazabilidad de los registros de facturación (RF) cuando estos salen del propio SIF?

La respuesta a esta pregunta se deriva de la definición y explicación dada (ver otras preguntas frecuentes de este apartado) sobre el concepto de trazabilidad, y es que se limita al ámbito del propio SIF (para cada OT, si permite gestionar la facturación de varios OT). Es decir, una vez que el SIF implementa la trazabilidad mediante el completo y correcto encadenamiento –y fechado– de los RF generados (sin olvidar su firma y guardado –por los sistemas de emisión de facturas no verificables– o remisión –por los SIF VERI\*FACTU– a la Agencia Tributaria), ya está cumplida y los RF son rastreables.

A partir de ese momento, el reglamento y la orden no entran en lo que se haga posteriormente con los RF generados por el SIF (ver abajo, al pie de esta respuesta, la **NOTA 1**), más allá de exigir su conservación, legibilidad y accesibilidad a futuro en el caso de sistemas de emisión de facturas no verificables.

Por lo tanto, la trazabilidad no se refiere al intercambio de los RF generados por un SIF con otros sistemas informáticos, ni a que esto sea rastreable.

**NOTA 1**: un ejemplo de esta posibilidad, en la práctica muy frecuente, sería el posible envío posterior de los RF generados por el SIF a otros sistemas informáticos distintos con idea de utilizarlos para fines diversos: contabilidad, gestión de *stocks*… Tampoco se exigirían requisitos al respecto a estos sistemas informáticos destinatarios (diferentes al SIF) a los que les lleguen los RF generados en otro SIF.

## Dentro de un mismo sistema informático de facturación (SIF), ¿hay que encadenar entre sí de forma separada (en 2 cadenas diferentes) los registros de facturación (RF) de alta, por un lado, y los RF de anulación, por otro?

No. Un SIF tiene una única cadena de RF (por cada obligado tributario que gestione, en el caso de que gestione varios dentro de él) en la que se encadenan ambos tipos de RF (alta y anulación) indistintamente, en el mismo orden secuencial en el que hayan sido generados.

## ¿Forman parte de la trazabilidad la fecha y la hora de generación de los registros de facturación (RF) correspondientes a las facturas expedidas?

Efectivamente, forman parte del mecanismo de trazabilidad de los RF, ya que dichos campos deberían ser coherentes con el orden temporal de generación de los RF que conforman la cadena de RF del sistema informático de facturación (SIF). Por lo tanto, esta es una de las cuestiones que el SIF debería garantizar que se hace correctamente.

Además, en el caso de tratarse de sistemas de emisión de facturas no verificables, el SIF también debería ser capaz de detectar e informar de incongruencias encontradas al respecto en los RF generados que se encuentren a su alcance.

## ¿Afecta en algo a la trazabilidad el cambio de año (o ejercicio fiscal) y, asociado a él, el posible cambio en la numeración de las facturas expedidas con el sistema informático de facturación (SIF)?

No. Es práctica habitual por parte de los obligados a expedir facturas (OEF) "cambiar" la numeración de sus facturas con el cambio de año, ya que suelen incluir dicho año dentro de la propia numeración de las facturas. Sin embargo, esto no afecta en nada a la trazabilidad. Son dos cuestiones completamente independientes. La trazabilidad solo exigiría que el RF de la primera factura expedida en el nuevo año fiscal se encadene correctamente con el RF de la última factura expedida en el año anterior, independientemente del número de factura (o de serie) que tengan.

## ¿Influyen en algo en la trazabilidad el que se realicen anulaciones o subsanaciones de registros de facturación (RF) correspondientes a facturas expedidas?

No. Cuando en un sistema informático de facturación (SIF), de manera justificada, haya que generar un RF de anulación de una factura expedida indebidamente (en ese SIF o en otro) o un RF de alta de subsanación de ciertos errores detectados en alguna factura expedida (en ese SIF o en otro), estos irán encadenados con el anterior registro de facturación generado por el SIF en el que se está haciendo la operación de anulación o subsanación. Es decir, en cuanto a trazabilidad, a la hora de encadenar estos RF se tratan como un RF más del SIF en el que se realiza la operativa.

## ¿Qué debe realizar el sistema informático de facturación (SIF) si, por cualquier circunstancia, en un momento dado detecta algún error en el encadenamiento de los registros de facturación (RF)?

Deberá actuar de igual forma que cuando detecta un error en la integridad e inalterabilidad de algún RF (ver en el apartado correspondiente la pregunta frecuente equivalente).

Por último, recordar que solo los sistemas de emisión de facturas no verificables están obligados a poder detectar estos errores en la trazabilidad de los RF y registros de evento generados que estén a su alcance. Ver al respecto, dentro de este mismo apartado, la contestación a una pregunta frecuente con más detalles.

## ¿Tienen las mismas obligaciones en cuanto a trazabilidad los sistemas «VERI\*FACTU» y los sistemas de emisión de facturas no verificables?

No, los sistemas de emisión de facturas no verificables tienen más obligaciones, al no remitir los registros de facturación (RF) generados a la Agencia Tributaria, por lo que es necesario que refuercen los mecanismos de control al respecto.

Hay que decir que ambos tipos de SIF, sistemas VERI\*FACTU y sistemas de emisión de facturas no verificables, tienen las mismas obligaciones en cuanto a implementar y garantizar la trazabilidad mediante el correcto encadenamiento de los RF (y también, por su parte, de los registros de evento generados en el caso de los sistemas de emisión de facturas no verificables). Sin embargo, a partir de este momento, los SIF VERI\*FACTU ya no tienen más obligaciones relacionadas con este requisito.

Por el contrario, los sistemas de emisión de facturas no verificables están también obligados a detectar fallos (y a ofrecer funcionalidades que lo permitan hacer) en el encadenamiento de los RF y de los registros de evento generados que estén a su alcance, avisando cuando se produzca esta circunstancia, además de generar el correspondiente registro de evento.

Por otro lado, los obligados tributarios (OT) usuarios de los sistemas de emisión de facturas no verificables también son responsables de garantizar la precisión de la hora de fechado con un margen máximo de error de un minuto, cosa que no aplica a los OT de los SIF VERI\*FACTU.

---

# Características y requisitos de los SIF: conservación, accesibilidad y legibilidad

## ¿Dónde se han de conservar los registros de facturación (RF) generados por el sistema informático de facturación (SIF)? Es decir, ¿es obligatorio mantenerlos en él o, por el contrario, hay que descargarlos siempre?

El lugar donde se conserven los RF será, en última instancia, una decisión del obligado a expedir factura (OEF) que utiliza el SIF (puede que en función de las circunstancias y de las características que tenga dicho SIF).

En este punto, se debe recordar que los SIF VERI\*FACTU (y los OEF que los utilicen) no están obligados a conservar los RF generados, ya que se han remitido a la Agencia Tributaria y, por tanto, obran en poder de esta.

Aclarado este matiz, en principio, el SIF almacenará bajo su control (ver abajo, al pie de esta respuesta, la **NOTA 1**) los RF que genere (puede que, por limitaciones de almacenamiento, necesite en algún momento que los RF sean exportados y eliminados de él para dejar espacio libre). En cualquier caso, el SIF debe ofrecer un procedimiento de descarga, volcado y archivo seguro de los registros de facturación generados por él, que deberán poder ser exportados a un almacenamiento externo en formato electrónico legible.

**Normativa/Doctrina:**

- Artículos 8.2.c) del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 8 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

**NOTA 1**: Los RF generados pueden almacenarse remotamente, incluso "en la nube", con tal de cumplir con toda la normativa que les sea de aplicación, y, en particular, con lo exigido en el reglamento y en la orden de requisitos de los SIF, especialmente en lo referido a su accesibilidad.

## ¿Es a través de la funcionalidad de exportación de registros de facturación (RF) la única forma que tiene un sistema informático de facturación (SIF) para dejar de conservar dentro de él los RF que ha generado y guardado?

Efectivamente, para que el SIF pueda dejar de conservar "dentro de él" los RF que ha generado, esto solo puede realizarse mediante una operación de exportación ejecutada correctamente y que admita la posibilidad de dejar de conservarlos en él.

Antes de continuar con la respuesta, ha de recordarse que este asunto relacionado con la exportación de los RF generados solo aplica a los sistemas de emisión de facturas no verificables, ya que los SIF VERI\*FACTU no están obligados a guardar los RF que generan ni a ofrecer su exportación (aunque podrían hacer voluntariamente ambas cosas), ya que los remiten a la Agencia Tributaria y, por tanto, obran en poder de esta.

Aclarado lo anterior, ha de decirse que, aunque para el SIF es obligatoria la existencia de la funcionalidad de exportación de los RF generados por dicho SIF, no es obligatorio ofrecer la posibilidad de que dicha funcionalidad permita la eliminación de los mismos del SIF, es decir, dejar de conservarlos "dentro" del SIF (bajo su gestión y control). Por lo tanto, este es un aspecto que dependerá de las características del SIF: si no tiene esta opción, estará obligado a conservar dentro de él –bajo su gestión y control– y para siempre todos los RF generados. Por otro lado, aunque tenga disponible dicha opción, dependerá del obligado a expedir factura (OEF) usuario del SIF si la utiliza o no (aunque, en la práctica, podría verse "forzado" a ello por diversas causas, como limitaciones en el rendimiento o en la capacidad del almacenamiento del SIF).

Por lo tanto, lo más probable es que, en general, los sistemas de emisión de facturas no verificables ofrezcan esta posibilidad de exportación de RF generados que suponga dejar de conservarlos en el SIF.

Los requisitos para el uso de esta opción serán los siguientes:

- Que forme parte del proceso de exportación y solo sea accesible desde dicha funcionalidad.
- Que antes de que sea llevada a cabo se avise claramente al usuario del SIF de lo que implica ejecutar esa opción (dejar de conservar los RF en el SIF, estando ya solo disponibles fuera de él, bajo la responsabilidad del OEF usuario del SIF), dándole la oportunidad de continuar o cancelar el proceso.
- En el caso de que el OEF usuario del SIF acepte continuar, el SIF solo podrá dejar de conservar los RF generados y exportados en dicho proceso cuando este acabe correctamente.
- Además, solo podrá dejar de conservar los RF exportados cuando ello no suponga el incumplimiento por parte del SIF de ningún requisito del reglamento y la orden «de requisitos de los SIF». Por ejemplo, si el método empleado por el SIF para llevar a cabo la obligación de verificar la correcta trazabilidad del último RF generado (antes de poder generar el siguiente RF) es consultar expresamente dicho último registro y el anterior, no podrá dejar de conservar estos dos registros.
- Por último, para evitar la aparición de huecos entre los registros de facturación conservados en el SIF, esta posibilidad de dejar de conservar los RF exportados solo podrá aplicarse a RF consecutivos, empezando siempre por los más antiguos que aún se conserven en el SIF. Es decir, no se podrá ofrecer al OEF usuario del SIF la posibilidad de que "exporte y deje de conservar en el SIF" RF generados si estos no empiezan desde el principio de la cadena de RF que obra en poder del SIF (debiendo ir además seguidos, como si formaran un bloque).

## ¿Se puede considerar que las copias de seguridad, tanto si se realizan o se gestiona su realización a través del sistema informático de facturación (SIF) o directamente desde la base de datos, son procesos de exportación a los efectos del reglamento y la orden «requisitos de los SIF»?

No. El proceso de exportación que permita la descarga, volcado y archivo seguro de los registros de facturación generados por él debe ser una funcionalidad adicional específica (con sus propias características) del SIF, diferente a los procedimientos de copia de seguridad de los que disponga el SIF o la instalación informática en la que este resida.

Se recuerda que la funcionalidad de exportación solo es exigible a los sistemas de emisión de facturas no verificables, es decir, que los SIF VERI\*FACTU no están obligados a disponer de ella.

## ¿De quién es la responsabilidad de la conservación de los registros de facturación (RF): del sistema informático de facturación (SIF) y su fabricante, o bien del obligado a expedir facturas (OEF) usuario del SIF?

Cada uno tiene su parte de responsabilidad:

- El productor (fabricante) del SIF es responsable de que el SIF genere y guarde o remita los RF en el tiempo y forma exigidos, así como que proporcione acceso rápido, fácil e intuitivo a los mismos mientras se encuentren en dicho SIF, junto con un procedimiento de descarga (exportación) seguro. Por lo tanto, el productor (fabricante) del SIF, que ha firmado una declaración responsable sobre dicho SIF, es responsable de que este cumpla con los requisitos que exige la normativa a este respecto.
- El OEF usuario del SIF es responsable de asegurarse de que conserva durante el plazo previsto para tal fin los RF generados, incluso aunque haya dejado de usar el SIF que los generó. Es por ello muy recomendable –y se considera una buena práctica– que el OEF exporte frecuentemente los RF generados por el SIF y los conserve de forma redundante en un sitio seguro.

En todo caso, se recuerda que la conservación de los RF solo es exigible a los sistemas de emisión de facturas no verificables y a los OEF usuarios de este tipo de SIF. Por lo tanto, los SIF VERI\*FACTU y los OEF usuarios de estos no están obligados a conservar los RF generados (aunque pueden hacerlo), ya que los han remitido a la Agencia Tributaria.

## ¿Cuál es el plazo a que se refieren el reglamento y la orden «de requisitos de los sistemas informáticos de facturación (SIF)» en relación con la conservación, accesibilidad y legibilidad de los registros de facturación (RF)?

Se trata del mismo plazo exigido en el artículo 19.1 del Reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre, para la conservación de las facturas expedidas (ver abajo, al pie de esta respuesta, la **NOTA 1**).

En la LGT (Ley 58/2003, de 17 de diciembre, General Tributaria) hay diversas menciones a plazos (ver abajo, al pie de esta respuesta, la **NOTA 2**) para varios aspectos, con sus matices y excepciones. Por otro lado, la LIVA (Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido) contempla sus propios plazos (ver abajo, al pie de esta respuesta, la **NOTA 3**), según el artículo 165 de la LIVA) y el apartado 6.4 del manual de facturación de 2011 (ver abajo, al pie de esta respuesta, la **NOTA 4**). También se puede encontrar en la pregunta 4 del manual práctico IVA 2023 (ver abajo, al pie de esta respuesta, la **NOTA 5**) una referencia a plazos de conservación de más de 10 años para ciertas facturas.

Por ello, cabría concluir que el plazo depende de la operación de que se trate y las circunstancias que concurran, pudiendo oscilar entre un mínimo de 4 años a partir del plazo de presentación de la declaración o autoliquidación correspondiente al ejercicio o periodo impositivo que aplique a dicha factura hasta más de 10 años en algunos casos.

Se acompaña esta respuesta de las mencionadas notas 2 a 5 con documentación y ejemplos al respecto.

**NOTA 1**: No se debe confundir la conservación de las facturas exigida por el ROF con la conservación de los RF exigida por el reglamento y la orden «de requisitos de los SIF». Ambos (factura y RF) son productos diferentes y están regulados por distinta normativa.

**NOTA 2**: Algunos plazos mencionados en la Ley 58/2003, de 17 de diciembre, General Tributaria (LGT):

- Artículo 66: 4 años para ciertos derechos.
- Artículo 66 bis, especialmente su apartado 2, sobre el derecho a comprobar e investigar bases o cuotas compensadas o pendientes de compensación o deducciones aplicadas o pendientes de aplicación: 10 años a contar desde el día siguiente a aquel en que finalice el plazo reglamentario establecido para presentar la declaración o autoliquidación correspondiente al ejercicio o periodo impositivo en que se generó el derecho a compensar dichas bases o cuotas o a aplicar dichas deducciones.
- Artículos 70.2 y 70.3: se mencionan otros plazos, pudiendo ser superiores a 4 años (plazo previsto en la normativa mercantil; plazo de exigencia de sus propias obligaciones formales al que se refiere el apartado anterior, si este último fuese superior; obligación de justificar la procedencia de los datos que tengan su origen en operaciones realizadas en períodos impositivos prescritos se mantendrá durante el plazo de prescripción del derecho para determinar las deudas tributarias afectadas por la operación correspondiente).
- Artículo 115, en el que se recoge que las potestades y funciones de comprobación e investigación pueden exceder los 4 años previstos en el artículo 66 para investigar otros derechos que no hubieran prescrito.

**NOTA 3**: (Aunque en este caso se refiere a las facturas recibidas, aplica también a las expedidas, según el artículo 165 de la LIVA):

*Pregunta: ¿Cuál es el plazo durante el cual deben conservarse las facturas recibidas?*

*Respuesta:* Con carácter general, cualquier factura recibida debe conservarse durante el período de prescripción -cuatro años- del impuesto. No obstante, si la factura se refiere a la adquisición de un bien que tenga que ser objeto de regularización, deberá ser conservada durante su período de regularización y los cuatro años siguientes. Si se realizan operaciones que tengan por objeto de inversión, las facturas y registros correspondientes a tales operaciones deben mantenerse durante cinco años.

**Normativa/Doctrina:**

- Artículo 165 Ley 37/1992, de 28 de diciembre de 1992, del Impuesto sobre el Valor Añadido (LIVA).
- Artículo 140 Sexies Ley 37/1992, de 28 de diciembre de 1992, del Impuesto sobre el Valor Añadido (LIVA).

**NOTA 4**: Apartado 6.4 del manual de facturación de 2011:

*6.4 Plazo de conservación.* Los documentos de facturación deben conservarse durante el plazo previsto en la Ley General Tributaria.

Cuando las facturas recibidas o expedidas se refieran a adquisiciones por las cuales se hayan soportado cuotas del Impuesto sobre el Valor Añadido cuya deducción esté sometida a un período de regularización, deberán conservarse durante su correspondiente periodo de regularización y los cuatro años siguientes.

Por otra parte, los empresarios o profesionales que realicen operaciones que tengan por objeto oro de inversión, deberán conservar las copias de las facturas correspondientes a dichas operaciones durante un período de cinco años. (artículo 140 sexies LIVA).

**NOTA 5**: Pregunta 4 del manual práctico IVA 2023, conteniendo un ejemplo referido al artículo 165.Uno de la LIVA, sobre el artículo 107.Cuatro de la LIVA, que trata las regularizaciones:

*4.¿Durante cuánto tiempo debe conservarse la factura de compra de un edificio?*

Si se comienza a utilizar el mismo año de la adquisición, debe conservarse durante 14 años: el año de compra, los 9 años siguientes por ser el período de regularización y los 4 siguientes.

Si se comienza a utilizar en años posteriores a la adquisición, debe tenerse en cuenta que el período de regularización comienza el año de utilización y que deben incrementarse los años en que deben conservarse las facturas.

## ¿Qué se entiende por accesibilidad y legibilidad de los registros de facturación (RF) generados por el sistema informático de facturación (SIF) a los efectos del reglamento y la orden «de requisitos de los SIF»?

Por accesibilidad debe entenderse el proporcionar acceso rápido, fácil e intuitivo a las funcionalidades exigidas al SIF por el reglamento y la orden, así como a los RF generados por el SIF, bien para consultarlos o para descargarlos de forma segura y fidedigna, independientemente de dónde y cómo se encuentren almacenados y conservados. Todo ello deberá, además, hacerse preservando al mismo tiempo la confidencialidad de otros datos distintos a los exigidos en el reglamento y la orden.

La accesibilidad deber ser garantizada tanto por el SIF (con el matiz hecho de que lo referente a los RF solo aplica cuando los RF se encuentren en él) como por el obligado a expedir factura (OEF) usuario del SIF.

En cuanto a la legibilidad, se refiere a que los RF generados tengan la estructura, contenido y formato exigidos, de forma que, mediante procesos electrónicos automáticos, puedan ser leídos y entendidos.

**Normativa/Doctrina:**

- Artículos 8.2.c) del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 8 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

---

# Características y requisitos de los SIF: registro de eventos.

## ¿En qué consiste el registro de eventos?

En que el sistema informático de facturación (SIF) detecte y recoja automáticamente, en el momento en que se produzcan, determinadas interacciones con dicho sistema informático, operaciones realizadas con él o sucesos ocurridos durante su uso, guardando los datos correspondientes a cada uno de ellos, que deberán poder ser consultados desde el propio SIF.

Este registro de eventos solo es obligatorio en el caso de los sistemas de emisión de facturas no verificables, no siendo necesario en los casos de SIF «VERI\*FACTU».

**Normativa/Doctrina:**

- Artículo 8.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Por qué es necesario registrar ciertos eventos? ¿Qué utilidad tiene?

La normativa al respecto exige a los sistemas informáticos de facturación (SIF) que garanticen la integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros, sin interpolaciones, omisiones o alteraciones de las que no quede la debida anotación en los sistemas mismos.

La remisión inmediata a la Agencia Tributaria de los registros de facturación generados por los SIF VERI\*FACTU contribuye decisivamente a cumplir con dichos requisitos. Sin embargo, esto no ocurre en el caso de los sistemas de emisión de facturas no verificables, por lo que entonces es necesario adoptar una medida adicional de seguridad y control consistente en que los sistemas de emisión de facturas no verificables graben de forma inalterable aquellas circunstancias –y sus principales características– que puedan ayudar a conocer con posterioridad cualquier posible anomalía o alteración relacionada con alguno de los requisitos mencionados.

**Normativa/Doctrina:**

- Artículo 29.2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria.
- Artículo 8.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Qué tipos de registro de evento existen?

Existen al menos los siguientes registros de evento:

a. Inicio del funcionamiento del sistema informático como «NO VERI\*FACTU».
b. Fin del funcionamiento del sistema informático como «NO VERI\*FACTU».
c. Lanzamiento del proceso de detección de anomalías en los registros de facturación.
d. Detección de anomalías en la integridad, inalterabilidad y trazabilidad de registros de facturación.
e. Lanzamiento del proceso de detección de anomalías en los registros de evento.
f. Detección de anomalías en la integridad, inalterabilidad y trazabilidad de registros de evento.
g. Restauración de copia de seguridad, cuando esta se gestione desde el propio sistema informático de facturación.
h. Exportación de registros de facturación generados en un periodo.
i. Exportación de registros de evento generados en un periodo.

Además de los anteriores, existe un registro de evento adicional, que es el registro resumen de eventos sucedidos en un determinado periodo (desde que se generó el registro resumen de eventos anterior, o bien desde el inicio de funcionamiento del sistema informático de acuerdo al Reglamento si no se hubiera generado aún ningún registro resumen de eventos anterior). Este registro resumen de eventos se grabará cada 6 horas en las que el SIF haya estado operativo y disponible para su uso, así como antes de cerrarse o apagarse.

Por último, el productor (fabricante) del SIF podría voluntariamente registrar otros eventos que considerara de interés al respecto.

**Normativa/Doctrina:**

- Artículo 8.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículos 9.1 y 9.2 de la orden por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre.

## En el caso de un sistema informático de facturación (SIF) que gestione la facturación de varios obligados a expedir facturas (OEF), ¿debe haber un único registro común de eventos en el SIF o uno para cada OEF?

En el caso mencionado, el SIF deberá registrar los eventos independientemente para cada OEF, como si fueran SIF distintos. En definitiva, habrá tantos como OEF.

**Normativa/Doctrina:**

- Artículos 7.a) y 8.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 2.a) de la orden por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre.

## ¿Qué características deben cumplir los registros de evento?

En general, las mismas exigidas a los registros de facturación, es decir, los registros de evento deberán realizarse de tal forma que queden garantizadas sus características de integridad, inalterabilidad, trazabilidad, conservación, accesibilidad y legibilidad, tal y como se exige para los registros de facturación, cumpliendo de forma análoga las especificaciones indicadas para estos últimos.

Para más detalle sobre dichas características y requisitos, se recomienda consultar las preguntas frecuentes recogidas en sus correspondientes apartados.

**Normativa/Doctrina:**

- Artículo 8.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 9.3 de la orden por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre.

## ¿Deben firmarse los registros de evento?

Sí. El sistema informático de facturación (SIF) deberá firmar electrónicamente todos los registros de evento que genere, cumpliendo de forma análoga las especificaciones dadas al respecto para el caso de los registros de facturación.

**Normativa/Doctrina:**

- Artículo 8.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 9.3 de la orden por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre.

## ¿Por cuánto tiempo debo guardar los registros de evento y quién es el responsable de su conservación?

El plazo de tiempo durante el que se deben guardar los registros de evento generados coincide con el que aplica a los registros de facturación generados en el mismo periodo temporal (ver en el apartado correspondiente la pregunta frecuente equivalente).

En cuanto a la responsabilidad de su conservación es también la misma que en el caso de los registros de facturación (ver en el apartado correspondiente la pregunta frecuente equivalente).

**Normativa/Doctrina:**

- Artículo 8.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 9.3 de la orden por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre.

## ¿Debo remitir a la Agencia Tributaria los registros de evento?

No, salvo que la Agencia Tributaria le requiera el envío de los mismos.

**Normativa/Doctrina:**

- Artículo 8.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

---

# Registros de facturación: alta

## El registro de alta de facturación al expedir cada factura ¿puede ser un registro de formato .xml guardado en la base de datos con la estructura que aparece en el "Diseño de registro de facturación de alta" en el apartado documentación de AEAT actualmente?

La normativa de este proyecto no detalla el modo en el que puede realizarse el almacenamiento de los registros de facturación. Se admiten diversas soluciones técnicas, siempre que cumplan las funcionalidades requeridas (integridad, posibilidad de exportación, etc.). La apuntada es una posibilidad que parece adecuada ya que debe suponer menos necesidad de conversión.

## ¿Qué tipos de acciones se van a permitir sobre los registros de facturación?

Cuando sea necesario cambiar algún dato de un registro de facturación de alta ya producido, deberá generarse otro registro que complete, modifique o anule el contenido del anterior, pero no podrá alterarse o manipularse el primer registro de facturación para evitar que la secuencia de facturas se altere.

Por lo tanto, no hay acciones permitidas sobre los registros de facturación una vez producidos estos de forma definitiva.

Para modificar un "registro de facturación de alta" deberá generarse un nuevo registro de anulación. En este último caso podrá ser una anulación completa del registro inicial o una subsanación / sustitución (es decir sustitución del "registro de alta" por otro registro subsanado). En cualquier caso, la forma de proceder es elaborar nuevos registros de anulación /subsanación y nunca alterar directamente los registros de facturación de alta generados previamente.

En el caso de que se pretenda cambiar menciones de la factura que no estén contempladas en el "registro de facturación de alta", y que, por consiguiente, no determinen alteración en el registro de alta producido, la subsanación no exigirá generar un nuevo registro, pudiendo realizarse directamente.

## Para facturación emitida en régimen de ventanilla única (OSS) ¿cómo se identificarán estas ventas de ventanilla única (OSS) en el registro de facturación? ¿Cuál es la codificación del régimen a utilizar?

En las operaciones de los regímenes de ventanilla única (OSS, one stop shop), contempladas en el artículo 166.bis de la Ley del IVA, 37/1992, introducido por Real Decreto Ley 7/2021, el código de régimen a indicar de la lista L8 es el "17": Operación acogida a alguno de los regímenes previstos en el Capítulo XI del Título IX (OSS e IOSS).

En cuanto al código de factura a informar de la lista L2, será el que le corresponda a la naturaleza de la factura, según se trate de factura ordinaria/completa ("F1"), simplificada ("F2").

## ¿Cómo se tratan los suplidos, el recargo financiero u otras cantidades en el esquema de la norma? ¿Cómo incluir las retenciones a cuenta de los impuestos directos practicadas en factura?

En las facturas existen menciones voluntarias perfectamente válidas, que derivan de prácticas mercantiles o incluso de otra naturaleza, y que, por una parte, no son menciones fiscales obligatorias del artículo 6.1 del Reglamento de Obligaciones de Facturación, aprobado por RD 1619/2012; y por otra, no han sido incluidas como menciones en el registro de facturación, que se regula en el artículo 10 del RRSIF, que aprueba el RD 1007/2023. Como es sabido, el mencionado registro es simplificado. Por tanto, los importes suplidos al igual que ocurre con el recargo financiero, no son importes "propios" del registro de facturación, y no tienen que incluirse entre las menciones del "registro de facturación de alta". No obstante, en el caso de que se incluyeran como mayor importe en el concepto "Importe total factura" (lo cual, no es obligatorio), deberán consignarse como importe no sujeto al IVA o cantidades a tipo cero (0%).

Por lo que se refiere a las retenciones, estas no forman parte formalmente del registro de facturación (no es uno de los elementos constitutivos de la factura de acuerdo con la Directiva UE).

No obstante lo mencionado en los párrafos anteriores sobre los registros de facturación de alta, nada impide incluir esas u otras menciones en la factura efectivamente emitida e impresa (o remitida electrónicamente) al destinatario, que contendrá toda la información logística, financiera, etc. que sea precisa o conveniente. Pero el extracto de información obligatoria que integra el "registro de facturación de alta" (y que se detalla en el artículo 10 del RRSIF) no contemplará tales datos.

## ¿Cómo se tratan las cantidades correspondientes a descuentos por pronto pago en el esquema de la norma?

Respecto de los descuentos por pronto pago, la doctrina administrativa puede resumirse así:

- El otorgamiento de descuentos y bonificaciones constituye una práctica frecuente dentro del ámbito empresarial como un método para incentivar las ventas. La consecuencia de los mismos, con independencia del tratamiento contable que proceda, es una minoración del precio de adquisición de los correspondientes bienes o servicios.
- Estos descuentos y bonificaciones pueden concederse en metálico o en especie. Generalmente, se trata de descuentos por **pronto pago**, descuentos promocionales (de temporada o estacionales, inicio de una nueva actividad, liquidación, introducción de un nuevo producto, por la condición del adquirente, etc.), descuentos por cantidad relativos a una operación y otros de análogas características.
- Los descuentos o bonificaciones **no forman parte de la base imponible cuando concurran los requisitos siguientes:**

  a. Que se justifiquen por cualquier medio de prueba admisible en Derecho. Generalmente, el documento que justifica su práctica es la propia factura que documente la operación, sin que sea preciso que tales descuentos y bonificaciones figuren separadamente, si bien debe probarse su existencia, circunstancia particularmente relevante en operaciones vinculadas. Sin embargo, **sí que se exige que en la factura consten todos los datos necesarios para la determinación de la base imponible**, haciendo mención expresa, en su caso, de cualquier descuento o rebaja que no esté incluido en el precio unitario, **concepto que debe figurar siempre en la factura.**
  b. Que se concedan previa o simultáneamente al momento de realización de la operación -el de devengo del impuesto-. Esta es la práctica comercial en este tipo de descuentos, predominando aquellos que se conceden en el momento de realizarse la operación. Cuando los descuentos o bonificaciones se concedan con posterioridad al momento de realizarse la operación también afectan a la base imponible, modificándose a la baja su importe.
  c. Que se otorguen en función de tal operación.
  d. Que no sean remuneración de otras operaciones efectuadas por el destinatario de la operación o por un tercero en su nombre, en favor del sujeto pasivo que realiza la operación a la que se pretenda afectar el otorgamiento de los descuentos o bonificaciones.

De acuerdo con lo anterior, en la factura debe figurar el descuento por pronto pago cuando se conceda de forma previa o simultánea a la operación.

Siendo el registro de alta previo a la factura y a partir del cual se generará la factura, si se desea que quede constancia de dicho descuento, este debe aparecer en el "registro de facturación de alta". La forma de incluirlo es en una de las líneas del bloque de desglose, sin perjuicio de hacer mención al descuento en el campo "descripción de la operación".

---

# Registros de facturación: anulación

## Si se emite una factura por error (y se genera y graba o envía (sistema VERI\*FACTU) el fichero de alta) es preciso generar un registro de signo contrario para la anulación, y generar posteriormente un nuevo registro de alta con la factura correcta. En estos casos ¿debe informarse en el registro de anulación cuál es la factura anulada?

Se pueden dar varios casos de error, existiendo diferentes posibles soluciones (anulación, facturas rectificativas, etc.), para las cuales el Reglamento prevé registros de facturación de anulación y también, en el registro de facturación de alta, un campo de "tipo factura", en el cual se encontrarían incorporadas diferentes tipos de facturas rectificativas.

En concreto por lo que se refiere al "Registro de facturación de anulación", el artículo 11.2.c) y ss del RRSIF exige determinadas menciones que identifican el registro de facturación de alta que se anule.

El detalle sobre el modo de codificar este tipo de errores aparecerá regulado en la OM que desarrolla el RRSIF.

## ¿Debe mantenerse el número de la factura que se anule en la serie de facturas emitidas?

Sí. Desde el punto de vista sustantivo, si las facturas se han emitido, aunque sean erróneas deben mantenerse, con su correspondiente numeración, y sin perjuicio de que se anulen posteriormente y se sustituyan por nuevas facturas correctas.

Por lo que se refiere a los sistemas de facturación (RRSIF), deberán mantenerse en el sistema los "Registros de facturación de alta", aunque sean erróneos, y deberá generarse un "registro de facturación de anulación" vinculado al registro de alta anulado. Ambos deberán aparecer en los listados de facturación, a fin de preservar la integridad de la cadena de registros.

---

# Huella o «hash»

## ¿Qué es la huella o «hash» de un registro?

Es el resultado de aplicar una función o algoritmo de cálculo de huella a una determinada información (en este caso, a unos datos del registro). Se trata de un dato (habitualmente de mucha menor longitud que la información sobre la que se ha calculado) con la propiedad de que es único para la información origen y a partir de la cual sería "virtualmente imposible" encontrar u obtener otra información alternativa (y menos aún que fuera significativa) cuya huella fuera la misma que la calculada para la información original. Es decir, si se cambiara –por poco que fuera– la información original, la huella de la nueva información modificada también cambiaría y no coincidiría con la huella obtenida para la información original.

De ahí su nombre, porque es como si fuera una huella dactilar ("pequeña") que "identifica" al contenido original ("grande") sobre el que se obtuvo.

## ¿A qué registros hay que calcular su huella o «hash»?

A todos los registros de facturación, de alta y de anulación, generados por el sistema informático de facturación (SIF).

Adicionalmente, los sistemas de emisión de facturas no verificables, como están obligados a generar registros de evento, también deberán calcular la huella o «hash» de estos.

## La huella o «hash», ¿ha de calcularse sobre todo el registro completo o, si no, qué datos del registro han de tenerse en cuenta para calcularla (y dónde se almacena)?

La huella o «hash» se calcula solo sobre unos pocos datos relevantes de los registros. Dichos datos son distintos en función del tipo de registro generado (de facturación de alta, de facturación de anulación o de evento) sobre el que se va a calcular la huella o «hash». Se puede consultar cuáles son en el documento "Detalle de las especificaciones técnicas para la generación de la huella o hash de los registros" que se puede encontrar en la web de desarrolladores y en la sede electrónica de la Agencia Tributaria.

Finalmente, el resultado de aplicar el algoritmo de cálculo de la huella sobre dichos datos del registro se almacenará en el propio registro como un campo más. Además, dicha huella también deberá incluirse dentro del contenido del registro inmediatamente siguiente que se pueda generar con posterioridad, formando así parte del mecanismo de encadenamiento de registros con el que se implementa el requisito de trazabilidad de los registros.

## ¿Qué algoritmo de cálculo de huella o «hash» hay que emplear? ¿Hay disponible algún ejemplo?

El algoritmo de cálculo de huella o «hash» a emplear es, por el momento, SHA-256 en todos los casos, es decir, para todos los tipos de registro. Tanto este como otros detalles y ejemplos del procedimiento de cálculo de la huella se pueden consultar en el documento "Detalle de las especificaciones técnicas para la generación de la huella o hash de los registros" que se puede encontrar en la web de desarrolladores y en la sede electrónica de la Agencia Tributaria.

## ¿Qué papel tiene la huella o «hash» en la seguridad y control de los registros?

La huella o «hash» de un registro juega un papel fundamental para saber si se ha mantenido la integridad e inalterabilidad de ciertos datos relevantes del registro. Por otro lado, como la huella de un registro ha de incluirse a su vez dentro del contenido del registro inmediatamente siguiente que se pueda generar con posterioridad, también forma parte del mecanismo de encadenamiento de registros con el que se implementa el requisito de trazabilidad de los registros.

## ¿Debe comprobar un sistema informático de facturación (SIF) las huellas generadas (y cuándo)? ¿Hay diferencias a este respecto entre sistemas VERI\*FACTU y sistemas de emisión de facturas no verificables?

Todos los SIF están obligados a calcular y colocar la huella correctamente, encadenando los registros según se exige en las correspondientes especificaciones.

Dicho esto, los SIF VERI\*FACTU no están obligados a realizar comprobaciones de huellas ni a ofrecer funcionalidades que permitan comprobarlas, ya que remiten todos sus registros de facturación (RF) a la Agencia Tributaria y es esta quien lo puede hacer (y, por este mismo motivo, no están obligados a generar registros de evento).

Sin embargo, en el caso de un sistema de emisión de facturas no verificables, este también debe ofrecer como funcionalidad la posibilidad de comprobar las huellas de los registros generados que estén a su alcance. Asimismo, al generar un nuevo registro, debe efectuar obligatoriamente la comprobación del correcto encadenamiento del anterior registro generado, lo que incluye la verificación de que la huella del anterior registro generado es correcta y que la huella encadenada en él (del registro previo al anterior) también es correcta. Esto debe hacerlo tanto para los registros de facturación, de alta y de anulación, como para los registros de evento que genere (se recuerda que los sistemas de emisión de facturas no verificables sí están obligados a generar registros de evento).

## ¿Hay que incluir la huella del registro de facturación (RF), o parte de ella, entre los datos que forman parte del código «QR» tributario de la factura, como en TicketBAI?

No. La huella del RF no forma parte de los datos que se incluyen en el código «QR» tributario añadido a las facturas expedidas por los sistemas informáticos de facturación (SIF) utilizados por los obligados a expedir facturas a los que aplica el reglamento aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

---

# Firma

## ¿En qué consiste la firma electrónica de los registros que se exige a ciertos sistemas informáticos de facturación (SIF)?

Se trata de un determinado proceso que, aplicado a cierta información (en este caso, un registro), genera un resultado con el que es posible comprobar a posteriori que el contenido de lo firmado se corresponde con la firma realizada sobre el mismo, así como la autoría de lo firmado, garantizando que ningún otro autor puede haber generado dicha firma, es decir, asegura que el autor de la firma no puede repudiar lo firmado.

## ¿Están todos los sistemas informáticos de facturación (SIF) obligados a firmar electrónicamente los registros generados por ellos?

No. Los SIF VERI\*FACTU no están obligados a firmar electrónicamente los registros generados. Solamente los sistemas de emisión de facturas no verificables están obligados a firmar electrónicamente tanto los registros de facturación, de alta y de anulación, como los registros de evento generados por ellos, de acuerdo a las especificaciones dadas al respecto.

## ¿Por qué los sistemas informáticos de facturación (SIF) VERI\*FACTU no están obligados a firmar electrónicamente los registros generados por ellos?

Porque remiten inmediatamente a la Agencia Tributaria los registros de facturación (RF) generados y este proceso de remisión incluye autenticación mediante certificado electrónico cualificado, así como medios de transmisión seguros, por lo que, al remitir de esta manera, se considera que se realiza una firma básica del RF y, por tanto, no es necesario realizar la firma electrónica explícita del RF.

## ¿Pueden los sistemas informáticos de facturación (SIF) VERI\*FACTU firmar electrónicamente los registros de facturación (RF) generados por ellos y remitirlos así firmados a la Agencia Tributaria?

Aunque los SIF VERI\*FACTU no están obligados a firmar electrónicamente los RF que generan y remiten a la Agencia Tributaria, si quieren pueden hacerlo y remitirlos firmados electrónicamente. Se recuerda que, en el caso de SIF VERI\*FACTU, tampoco están obligados a generar registros de evento (ni, por tanto, a firmarlos).

## ¿Qué registros deben firmar los sistemas de emisión de facturas no verificables?

Los sistemas de emisión de facturas no verificables deben firmar electrónicamente todos los tipos de registros que generen, es decir, tanto los registros de facturación (RF), de alta y de anulación, como los registros de evento.

## ¿Qué tipo de firma electrónica hay que implementar? ¿Hay disponible algún ejemplo?

El tipo de firma electrónica a utilizar en todos los casos (registros de facturación, de alta y de anulación, y registros de evento) será *XAdES Enveloped Signature*. Tanto este como otros detalles y ejemplos del procedimiento de cálculo de la firma electrónica se pueden consultar en el documento "Especificaciones técnicas para generación de la firma electrónica de los registros de facturación" y en el archivo comprimido "ZIP: Anexos ejemplos firma registros de facturación" que se pueden encontrar en la web de desarrolladores y en la sede electrónica de la Agencia Tributaria.

## ¿Qué papel tiene la firma electrónica en la seguridad y control de los registros?

Junto con la huella y el resto de datos firmados, la firma electrónica permite saber si se ha mantenido la integridad e inalterabilidad del registro firmado, garantizando la autoría de la firma sobre lo firmado (es decir, el no repudio de lo firmado). Por este motivo también contribuye a garantizar la integridad e inalterabilidad del encadenamiento de registros, que es la forma de implementar el requisito de trazabilidad.

## ¿Debe comprobar un sistema informático de facturación (SIF) las firmas generadas (y cuándo)?

Los sistemas de emisión de facturas no verificables deben ofrecer la posibilidad de comprobar de forma rápida, fácil e intuitiva la firma electrónica de los registros de facturación, de alta y de anulación, y de los registros de evento generados que estén a su alcance. La comprobación se hace, en principio, a petición del usuario del sistema de emisión de facturas no verificables (no es obligatorio que sea automática ni que se deba hacer periódicamente).

Se recuerda que, como se ha indicado en otras preguntas frecuentes, los SIF VERI\*FACTU no están obligados a firmar los registros ni, por tanto, a comprobar firmas.

---

# Certificación de los sistemas informáticos: declaración responsable

## ¿Cómo se certifica que un Sistema Informático de Facturación cumple con la normativa que regula estos sistemas?

En el art. 29.2.j) de la LGT (introducido por la Ley 11/2021, de 9 de julio, conocida coloquialmente como "Ley Antifraude") se menciona la posibilidad de que *los sistemas y programas informáticos que soporten los procesos de contables, de facturación o de gestión de los empresarios* deban estar certificados en la forma que se determine reglamentariamente.

Acogiéndose a esta posibilidad, y por lo que se refiere a los sistemas de facturación, en el artículo 13.1 del Reglamento de Requisitos de Sistemas de Facturación (RRSIF), aprobado por R. D. 1007/2023, de 5 de diciembre, que integra la Sección 3ª denominada "Certificación de los sistemas informáticos", se indica que corresponderá a la persona o entidad productora del sistema informático certificar, mediante una declaración responsable, que el sistema informático cumple con lo dispuesto en el artículo 29.2.j) de la Ley 58/2003, General Tributaria, así como con lo dispuesto en el citado Reglamento (RRSIF) y en las especificaciones que, en su desarrollo, se aprueben mediante orden ministerial.

Por lo que se refiere a su formato y sin perjuicio del mayor detalle que aparece en la OM de desarrollo, el artículo 13.2 del RRSIF establece que deberá constar por escrito y de modo visible en el propio sistema informático en cada una de sus versiones, así como para el cliente y el comercializador en el momento de la adquisición del producto.

**Normativa/Doctrina:**

- Artículo 29.2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria.
- Artículo 13.1 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Debe un producto SIF obtener alguna certificación externa? ¿Debe registrarse el SIF previamente a su comercialización?

No. Para certificar un producto no se requiere de procesos de certificación realizados por otras personas, entidades u organismos independientes –y, por tanto, ajenos al productor– que se dediquen a este tipo de tareas, sino que se trata de una "auto-certificación" del propio productor del producto SIF realizada como Declaración Responsable e incorporada al producto.

En cuanto a su previo registro no está previsto en la norma. Para cumplir con la normativa a este respecto no se prevé ningún registro previo del producto SIF por parte de nadie (ni productor, ni comercializador, ni usuario).

**Normativa/Doctrina:**

- Artículo 13.1 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Quién debe realizar la Certificación de un producto SIF, el productor o el comercializador del mismo?

La Certificación mediante Declaración Responsable le corresponde, según lo establecido en el RRSIF al productor (fabricante o desarrollador) de dicho SIF.

Por lo que se refiere a los comercializadores (que no sean los fabricantes o productores de los SIF), para no incurrir en la responsabilidad a que se refiere el artículo 201.bis de la LGT, deberán asegurarse de que los productos SIF que comercialicen estén debidamente certificados por sus fabricantes.

**Normativa/Doctrina:**

- Artículo 13.1 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Es obligatorio que todo producto SIF tenga su correspondiente Certificación?

Sí. La Certificación de un producto SIF es obligatoria y es la forma en que su productor certifica que dicho producto SIF cumple con los requisitos exigidos en la normativa al respecto. De esta forma el usuario puede utilizar ese producto con total tranquilidad.

**Normativa/Doctrina:**

- Artículo 13.1 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Debe el productor del SIF certificar cada versión de producto que ponga a disposición de los usuarios?

Sí. Cada versión, por pequeña variación que introduzca, es un producto distinto de los anteriores, con un funcionamiento particular, por lo que es necesario que el productor de dicha versión del SIF certifique expresamente que dicha versión cumple con los requisitos exigidos, emitiendo e incorporando en el producto la correspondiente Declaración Responsable.

**Normativa/Doctrina:**

- Artículo 13.2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 15.4 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## ¿Cómo y dónde debe proporcionarse la Certificación del productor?

La Certificación por medio de Declaración responsable del SIF deberá ser proporcionada por el productor del mismo en formato legible y estar accesible dentro del propio SIF que se ponga a disposición de los usuarios, es decir, formando parte del propio producto. Además, deberá estar a disposición del cliente y del comercializador en el momento de la adquisición del producto.

Por lo tanto, la Certificación deberá estar accesible en dos ubicaciones distintas:

1. Interna al propio SIF que se ponga a disposición de los usuarios, es decir, dentro del mismo producto, formando parte de él. Por lo tanto, un SIF deberá contener la Certificación correspondiente a su versión actual, que será accesible de forma rápida, fácil e intuitiva desde cualquier punto de acceso o terminal conectado a dicho SIF a través del cual se pueda facturar o administrar el SIF. A este respecto, se recomienda que, a ser posible, se ubique en una opción específica dentro de algún menú, como por ejemplo "Ayuda" (en el caso de que exista), al lado de otras opciones similares que suelen existir habitualmente, como "Acerca de".
2. Externa al propio SIF, de manera que pueda ser accedida de forma directa e independiente del producto para que el comercializador, y el usuario o potencial usuario del SIF puedan ver la misma en cualquier momento (por ejemplo, antes o en el momento de su adquisición) y así asegurarse de que éste cumple la normativa vigente sin necesidad de tener que instalar y poner en funcionamiento el producto para acceder a ella desde dentro del mismo.

   En este último caso de ubicación externa al SIF, la certificación concreta que corresponde al producto se podrá proporcionar en formato papel o electrónico, bien en soporte físico, como por ejemplo un CD, o siendo accesible a través de Internet, pero siempre en un formato de uso ampliamente extendido y gratuito, como el texto puro, PDF o similar. Ver en otra FAQ las recomendaciones que se dan sobre la gestión de las Declaraciones Responsables en cuanto a su guardado y almacenamiento, ubicación y acceso "externos".

**Normativa/Doctrina:**

- Artículo 13.2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 15.3 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## ¿Debe guardar el productor la certificación de todas las versiones de sus productos SIF que haya puesto a disposición de los usuarios a lo largo del tiempo? ¿Y el comercializador?

Sí, tanto fabricante como comercializador deben guardar esas certificaciones hechas mediante Declaración Responsable. El productor, para todas las versiones que haya producido y puesto a disposición de los usuarios desde el momento en el que así lo exija la normativa. El comercializador, para todas las que haya comercializado, es decir, para todas las que se hayan producido y puesto a disposición de los usuarios durante el tiempo en el que las ha comercializado, siempre a partir del momento en el que así lo exija la normativa. Tanto el cliente usuario como la Administración tributaria les podrán solicitar las mismas.

A este respecto se recomienda que, adicionalmente, todas las certificaciones sean accesibles públicamente y localizables fácilmente a través de Internet, aunque la versión del producto que certifiquen ya no esté disponible para su adquisición, descarga o uso (típicamente por obsolescencia, falta de soporte o similar). Esto, además de cumplir con los requisitos exigidos al respecto, facilitaría tanto su gestión por parte de los productores y comercializadores, como su consulta por parte de los usuarios y de la Administración tributaria, haciendo el proceso más sencillo, ágil y transparente para todos.

**Normativa/Doctrina:**

- Artículos 13.2 y 13.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículos 15.2.b) y 15.3 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## ¿Es obligatorio que estén disponibles en el propio SIF las Certificaciones de TODAS las versiones por las que haya pasado el producto?

No. La Certificación que obligatoriamente deberá constar en el propio SIF será la correspondiente a la versión actualmente utilizada, no siendo necesario mantener en el propio SIF las certificaciones de versiones anteriores. Sin embargo, como ya se explica en otra pregunta frecuente, los productores y comercializadores de dichos productos deberán guardar todas las Certificaciones de todas las versiones de sus SIF puestas a disposición de los usuarios desde el momento en el que así lo exija la normativa. De la misma forma, los usuarios de estos Sistemas cuando los sustituyan o actualicen las versiones, deben conservar los certificados de los sistemas que se sustituyan o actualicen a partir de la entrada en aplicación de las obligaciones de la normativa de SIF. Esta conservación puede ser en formato papel o electrónico, bien en soporte físico, como por ejemplo un CD, o siendo accesible a través de Internet.

**Normativa/Doctrina:**

- Artículos 13.2 y 13.3 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 15.3 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## ¿Qué datos ha de incluir el productor del SIF obligatoriamente en las Certificaciones?

Los productores de sistemas y programas informáticos de facturación (SIF), además de certificar que el sistema informático cumple con el artículo 29.2.j) de la LGT con el contenido del RRSIF, aprobado por R. D. 1007/2023, y con las especificaciones dictadas por medio de OM del Ministerio de Hacienda en desarrollo de los anteriores, deberán incluir:

a. los datos referentes al sistema informático, que permitan identificarlo y saber su tipología, composición y funcionalidades, así como conocer las características de la instalación del mismo.
b. los datos identificativos y de localización del productor del mencionado sistema informático, y la fecha y lugar en que firma la correspondiente certificación mediante declaración responsable.

El detalle de estos datos obligatorios se puede ver en el artículo 15 de la OM. Adicionalmente, y para ayudar en la confección de dicha Certificación, en la Sede-e de la AEAT se proporcionarán diversos ejemplos, de manera que puedan servir de modelo a seguir a la hora de elaborarla.

**Normativa/Doctrina:**

- Artículo 13.4 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 15.1 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## ¿Se puede completar la Certificación añadiendo datos y explicaciones adicionales a los exigidos?

Sí. De hecho, cuanta más información precisa se aporte sobre el producto, mejor para todos, ya que el productor será más transparente, lo que podrá generar mayor confianza en los usuarios (clientes del productor), y la Administración tributaria podrá disponer de un conocimiento más completo, lo que puede contribuir a evitar o reducir los requerimientos de información al respecto. En este sentido, en el artículo 15.2 de la OM se recomienda añadir algunos de forma voluntaria.

**Normativa/Doctrina:**

- Artículo 13.4 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 15 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## ¿Ha de ir firmada electrónicamente la Certificación realizada mediante Declaración Responsable del Productor?

Para la Certificación realizada mediante Declaración Responsable no se exige una firma electrónica del Productor del programa o sistema. Cuando en el artículo 13.4 se habla de incluir en ella la fecha y lugar en que la firma el productor, no se refiere específicamente a una firma electrónica, sino a la fecha y lugar en que es elaborada y suscrita la Certificación por parte del productor. Dicho de otra forma, es la fecha y el lugar en que se certifica ese producto mediante la Declaración Responsable que va incorporada en él.

**Normativa/Doctrina:**

- Artículo 13.4 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 15.1.m) de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## En el caso de que, por parte de otros productores distintos al que ha producido el SIF utilizado, se realicen ampliaciones a dicho SIF utilizado (por ejemplo, con desarrollos a medida para personalizar el producto y adaptarlo más y mejor al usuario), ¿se debe realizar y proporcionar adicionalmente la correspondiente Certificación de esas ampliaciones? y, en ese caso, ¿quién debe proporcionarla?

Cualquier actuación de un productor de software sobre los programas y sistemas SIF producidos por otro, suponen una alteración o modificación del programa original. Por ejemplo, la realización de desarrollos a medida para personalizar el producto y adaptarlo más y mejor al usuario, lo son. Por lo tanto, las modificaciones, adaptaciones o ampliaciones –hardware, software o combinación de ambas– de un sistema informático de facturación producidas por un tercer productor distinto al productor del SIF original no están cubiertas por la certificación del productor del SIF original, por lo que, adicionalmente, es necesario que incorporen su propia certificación realizada por dicho tercer productor.

A este respecto, por ejemplo, si la ampliación es realizada por el usuario del SIF con sus propios medios (personal propio y/o personal especializado contratado o subcontratado al efecto dependiente del usuario), el responsable de la ampliación será el usuario del SIF, que como productor de la misma deberá certificarla suscribiendo su correspondiente Declaración Responsable y cumpliendo con todos los requisitos exigidos para la misma. Sin embargo, si el usuario del SIF contrata esa ampliación, como un producto, a una tercera persona o entidad productora, que se encargará de realizarla y entregarla al usuario, será dicho tercer productor quien la deba certificar cumpliendo con todos los requisitos exigidos para la misma. Es decir, en éste último caso el usuario está adquiriendo un nuevo producto (o componente) de facturación a un tercer productor.

**Normativa/Doctrina:**

- Artículos 13.1 y 13.2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 15.4 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## Si el Sistema Informático de Facturación utilizado ha experimentado varias ampliaciones distintas, por parte del mismo productor o de productores distintos al que fabricó el SIF utilizado, ¿cuántos Certificados deben existir?

Se deberá suscribir y proporcionar un Certificado por cada productor y producto distinto, considerando como producto tanto a un SIF como a una ampliación de un SIF, en ambos casos para cada una de sus versiones. Es decir, habrá tantos certificados como productores distintos, tal y como sucedería si todos ellos solo aportaran un producto, cada uno con una única versión.

No obstante, en el caso de que las certificaciones (mediante Declaración Responsable) de las ampliaciones posteriores contengan todos los datos a incluir, referidos en el RSSIF, y abarquen los datos referentes al sistema informático, tipología, composición y funcionalidades, así como conocer las características de la instalación última del mismo, incluyendo el sistema previo y las sucesivas ampliaciones, bastará con disponer de la Certificación de la última instalación que contenga dichas referencias.

**Normativa/Doctrina:**

- Artículos 13.1 y 13.2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 15.4 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## ¿Qué hay que poner en la Certificación respecto de los datos de nombre y código identificador del producto SIF a que se refieren los artículos 15.1.a) y 15.1.b) del Proyecto de OM?

La letra a) se refiere al nombre que el productor ha dado a su propio producto y típicamente será la denominación genérica como se da a conocer de cara a su distribución o comercialización. En los diseños de registro que figuran en el Anexo I de la OM se le denomina "NombreSistemaInformatico" y se incluye una breve descripción, junto con su formato.

Por su parte, la letra b) se refiere a un código que ha de establecer también el productor del SIF para identificar de forma única y abreviada a dicho producto de cara a la AEAT, y que también habrá de rellenarse en los registros de facturación, siempre cumpliendo el formato dado en los correspondientes diseños de registro que figuran en el Anexo I de la OM. En dicho anexo se le denomina "IdSistemaInformatico" y se incluye una breve descripción.

Este código no se podrá repetir en otro SIF distinto del mismo productor (aunque sí podría darse la coincidencia de que dos productores distintos utilizarán el mismo código para referirse a sus respectivos SIF: por ejemplo, un productor con NIF A9999999A, podría establecer el código "S1" para uno de sus SIF, y un productor con NIF B8888888B, podría también establecer el código "S1" para uno de sus SIF).

Ver en la Sede-e de la AEAT los ejemplos dados al respecto.

**Normativa/Doctrina:**

- Artículos 15.1.a), 15.1.b) y anexo I de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## Soy un productor de SIF y tengo tres productos disponibles a la venta, cuyos nombres son: Factura x Basic, Factu X Standard y Factu X Enterprise. ¿Qué código debe ponerse en la Certificación y cuál en el registro de facturación para cumplir con los artículos 15.1.b) y Anexo I de la OM?

Con tal de respetar el formato que se especifica en el Anexo I de la OM (para el que solo se admiten dos posiciones, cada una de las cuales deberá ser una letra mayúscula –excepto la Ñ– o un dígito numérico), el fabricante o productor puede poner lo que le parezca oportuno, pero una vez establecidos han de mantenerse en adelante y no deben repetirse entre los distintos SIF que produzca.

Por ejemplo, para los 3 nombres del ejemplo, que deberían consignarse expresa y completamente en los correspondientes Certificados, podría establecer en los registros de facturación, respectivamente, los 3 códigos: XB, XS y XE. O cualesquiera otros: X1, X2 y X3; F1, F2 y F3…

Ver en la Sede-e de la AEAT los ejemplos dados al respecto.

**Normativa/Doctrina:**

- Artículos 15.1.b) y anexo I de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## Como productor de SIF, ofrezco un producto SIF que, además de software, también incluye hardware propio, con su correspondiente versión de firmware. En este caso, ¿qué debo poner en la Certificación en cuanto a la versión completa a que se refiere el artículo 15.c) de la OM?

Se deben indicar todas las versiones de los componentes que conforman el SIF, con la denominación exacta (números, letras, caracteres especiales…) que les dé el productor, en el formato indicado en el Anexo I de la OM. Se puede empezar por el software y continuar con el hardware.

Ver en la Sede-e de la AEAT los ejemplos dados al respecto.

**Normativa/Doctrina:**

- Artículos 15.1.c) y anexo I de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## Soy un productor de un SIF que ha sido diseñado y producido de manera que solo puede funcionar, siempre y exclusivamente, como sistema VERI\*FACTU. ¿Qué debo poner en la Certificación en relación con el artículo 15.1.e) de la OM?

En ese caso, dado que dicho SIF solo puede funcionar, siempre y exclusivamente, como sistema VERI\*FACTU (es decir, no permite la posibilidad de no remitir automáticamente todos los registros de facturación a la AEAT), deberá indicar una "S" tanto en la Certificación (letra e) como en el campo correspondiente ("TipoUsoPosibleSolo VERI\*FACTU") dentro de los registros de facturación generados.

**Normativa/Doctrina:**

- Artículos 15.1.e) y anexo I de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## Soy un productor de un SIF que tiene la capacidad de remitir por medios electrónicos a la Administración tributaria, de forma continuada, segura, correcta, íntegra, automática, consecutiva, instantánea y fehaciente, todos los registros de facturación generados, tal y como obliga el Reglamento. Sin embargo, dicho SIF puede ser utilizado sin que esa capacidad se lleve a efecto, es decir, puede usarse sin que se remitan a la AEAT los registros de facturación generados, ya que dicha remisión en principio no es obligatoria y el SIF así lo permite. ¿Qué debo poner en la Certificación en relación con el art. 15.1.e) de la OM?

Todo aquel SIF que no esté diseñado y producido para funcionar, **siempre y exclusivamente**, como sistema VERI\*FACTU, independientemente de si luego el usuario lo llegara a utilizar como sistema VERI\*FACTU o no, deberá indicar una "N" tanto en la Certificación (letra e) como en el campo correspondiente ("TipoUsoPosibleSolo VERI\*FACTU") dentro de los registros de facturación generados.

**Normativa/Doctrina:**

- Artículos 15.1.e) y anexo I de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## Soy el productor de una ampliación de un SIF producido por otra empresa, que consiste en la realización de nuevas pantallas con cuadros estadísticos personalizados de la facturación. ¿Qué debo poner en la Certificación en relación con el artículo 15.1.e) de la OM?

Al tratarse de una ampliación de utilidades del SIF, pero que no afectan ni alteran los requisitos obligatorios regulados en el Reglamento y la Orden Ministerial, ese segundo fabricante no estaría obligado a certificar el producto, por lo que no procede completar lo establecido en el artículo citado del Reglamento.

Por el contrario, si la ampliación/modificación es alguna funcionalidad que implementa requisitos obligatorios de seguridad y control exigidos por el reglamento a los SIF, sobre todo los referidos a la generación y firma/grabación o remisión de los registros de facturación (RF), lo que incluiría -por contenerlos como datos que forman parte del RF- el cálculo de la huella y la trazabilidad, la certificación será obligatoria. En este último caso, si la ampliación no afecta a la remisión de registros de facturación, deberá indicar una "N" en la Certificación (letra 1.e), en otro caso deberá indicar una "S" en la misma.

**Normativa/Doctrina:**

- Artículos 15.1.e) de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## Soy el productor de una ampliación de un SIF producido por otra empresa, que consiste en la realización de nuevas pantallas con cuadros estadísticos personalizados de la facturación. ¿Qué debo poner en la Certificación en relación con el artículo 15.1.f) de la OM?

Dado que se trata de una ampliación de un SIF hecha por un tercer productor distinto del original que produjo el SIF y que el objeto de dicha ampliación es limitado y no afecta a las capacidades originales de uso del SIF exclusivamente por un solo obligado tributario o por varios obligados tributarios para la llevanza de sus respectivas facturaciones, deberá indicar una "N" en la DR (letra 1.f).

**Normativa/Doctrina:**

- Artículo 7.a) del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículos 15.1.f) de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## Como fabricante de software de facturación en la que los datos están gestionados por un sistema gestor de base de datos comercial, ¿debo bloquear el acceso a la base de datos para evitar que el cliente modifique las facturas? Y si se restringe, ¿Cómo podrá gestionar el cliente y hacer copia de la base de datos?

El Reglamento RSSIF y la Orden Ministerial de desarrollo no dicen nada sobre ese tipo de medidas concretas relacionadas con las posibles BBDD empleadas, que pueden tener muy diferentes características y formas de gestionar su seguridad, sino que se centran en las medidas mínimas que debe cumplir el SIF para implementar los requisitos exigidos. Con ellas, debe ser posible asegurar que no se pueda alterar la realidad facturada, se considera que el sistema debe detectar el intento de efectuar cambios e impedirlos. En cualquier caso, nada impide al fabricante y a su SIF tomar más medidas y, de hecho, toda medida adicional que el fabricante y el SIF adopten, tendente a garantizar o robustecer esos requisitos exigidos, siempre es bienvenida. En cualquier caso, las restricciones no deben suponer una merma de utilidades para el usuario en la realización de cualquier tipo de tareas lícitas como las copias mencionadas.

## ¿Hay algún modelo de ejemplo de Certificación mediante declaración responsable publicado?

Será uno de los de modelos que se publicarán en Sede Electrónica.

## ¿Cómo se compondría la Certificación mediante declaración responsable si se usa un sistema de facturación con varios componentes cada uno desarrollado e implementado por una empresa diferente?

En un caso como el descrito en la pregunta, hay que definir qué implica cada componente y cuál es su funcionalidad dentro del conjunto. Si tiene impacto en el cumplimiento del Reglamento por parte del Sistema Informático de Facturación, lo lógico es que haya tantos Certificaciones como componentes afectan al cumplimiento del Reglamento RSIF. Todas ellas deberán hallarse disponibles para el usuario del sistema.

## Como empresa fabricante de sistemas informáticos de facturación, ¿quién es responsable del cumplimiento del reglamento en el caso de que un cliente no quiera actualizar el sistema de facturación que fue adquirido a nuestra empresa para que cumpla los requisitos del reglamento?

Pasados los periodos transitorios contenidos en la Disposición Adicional Cuarta del R. D. 1007/2023, los productores o fabricantes deberán proveer a sus clientes de programas SIF adaptados a la norma. No obstante, si un cliente no quiere adaptar sus sistemas adquiridos con anterioridad, el fabricante o productor queda exento de toda responsabilidad, respondiendo el cliente en los términos del artículo 201.bis LGT en su redacción por Ley 11/2021, de 9 de julio.

Un fabricante, con carácter general, deberá dar soporte *solo* a sistemas de facturación adaptados a la norma, ya que desde el fin de los periodos transitorios, el resto de sistemas dejarán de ser lícitos. Lo anterior se entiende sin perjuicio del soporte necesario para adaptar dichos sistemas.

## ¿Quién es responsable en el caso de que un cliente rompa las medidas de seguridad de un sistema de facturación cuya certificación ha firmado un fabricante, desarrollador o implementador?

La diligencia con la que todo productor, fabricante, desarrollador o implementador debe cumplir con la normativa vigente, a la cual se ha comprometido emitiendo la correspondiente Certificación (mediante su declaración responsable), le obliga a adoptar cuantas medidas estén técnicamente disponibles para que la seguridad del SIF (preservando los registros de facturación) no se rompa.

Conviene recalcar que si el software opera en modo VERI\*FACTU (con remisión voluntaria inmediata de los registros), es más improbable que el usuario pueda llevar a cabo ninguna alteración de los registros u otra acción irregular (ya sea voluntaria o involuntariamente) "a posteriori", pues los registros de facturación constarán en la AEAT, lo que impide realizar cambios sobre ellos.

## ¿El productor de un SIF que solo funciona en modalidad VERI\*FACTU está obligado a aportar la Certificación del software?

Sí, la obligación de certificación se aplica a todos los SIF.

## Sobre la certificación por declaración responsable de los sistemas informáticos, ¿se requiere la declaración a todos los fabricantes de software o únicamente a los que fabriquen software de facturación?

La Ley 11/2021, de 9 de julio, ha introducido el nuevo artículo 29.2.j) de la Ley General Tributaria en el que se establece que cualquier programa de contabilidad, facturación o gestión de los empresarios debe respetar los requisitos de garanticen la integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros, sin interpolaciones, omisiones o alteraciones de las que no quede la debida anotación en los sistemas mismos. Esa genérica obligación, para el caso de los Sistemas de Facturación, en función de su importancia desde el punto de vista del cumplimiento tributario, se ha materializado en ciertas obligaciones reguladas por Real Decreto 1007/2023, de 5 de diciembre que aprueba el RRSIF. Este Reglamento de requisitos de los sistemas informáticos de facturación es el que obliga, desde la entrada en vigor de sus disposiciones, a que todos los programas y sistemas informáticos de facturación (SIF) correspondientes a los empresarios y operaciones del ámbito subjetivo y objetivo de la norma, deban estar Certificados.

Por lo tanto, la obligación de certificación a la que se refiere el artículo 13 del RRSIF, no abarca a todos los fabricantes de software, ni a todos los programas, sino exclusivamente a los fabricantes de Sistemas Informáticos de Facturación y en relación con dichos sistemas.

## El contenido de la Certificación en la OM menciona que hay que incluir en la misma los componentes hardware y software de que conste el sistema informático. ¿Hay que certificar el hardware? ¿Cuándo deben incluirse componentes hardware?

No, el hardware genérico –ordenador– sobre el que se instala un software informático de facturación no hay que certificarlo. Lo más frecuente será que se deba certificar el programa o sistema mismo, es decir el código instalado en el hardware.

Evidentemente, todo software ha de ejecutarse en un hardware. Pero la mención al hardware contenida en el artículo solo se refiere a aquellos supuestos en los que el hardware del sistema SIF forme parte de un "todo" que se ofrece (comercializa) como producto completo (software y hardware) para dar soporte a la facturación, o bien cuando se trate de algún hardware específico que realiza o interviene de forma relevante en el cumplimiento de algún requisito exigidos al SIF.

## Si se usa software de facturación de código abierto ¿quién hace la declaración responsable?

La empresa que efectúe la programación del código o integre partes de otro software, ya sea o no de código abierto, debe realizar la declaración responsable, incorporar los datos obligatorios e indicar qué componentes utiliza. En el caso de que utilice código abierto, se hará responsable del funcionamiento del mismo, incluyendo los sistemas de seguridad exigidos para preservar la integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros.

## ¿Si una empresa tiene software de facturación basado en un desarrollo propio y sólo para uso propio (no se comercializa) ¿debe disponer también de Certificación?

Cada sistema en operación debe disponer de una Certificación emitida mediante declaración responsable de su productor (artículo 13.1 RRSIF). Si el software hubiera sido desarrollado por la propia empresa, será esta la que deba certificarlo, cumpliendo para ello lo que establece el mencionado artículo 13 y su normativa de desarrollo.

## Si un software de facturación es del tipo "on-premise" en la cual el cliente es dueño de los datos ya que los tiene en sus servidores. ¿Debemos limitar el acceso a través de la base de datos al cliente para evitar su modificación? En caso afirmativo, ¿en cualquier caso? ¿Seamos o no VERI\*FACTU?

Cualquier operación sobre los registros de facturación, sea VERI\*FACTU o no, debe ser registrada a través de un registro de facturación, por lo que el acceso desde el SIF a modificaciones directamente sobre la base de datos de registros ya emitidos no debe ser una operativa permitida.

Si el SIF opera en modalidad VERI\*FACTU (con remisión voluntaria inmediata de los registros), es más improbable que el usuario pueda llevar a cabo ningún acceso u otras actuaciones indebidas "a posteriori", pues los registros originales de facturación ya constarán en la AEAT, lo que impide realizar cambios sobre ellos. En este sentido, el acceso a las bases de datos de registros de facturación ya remitidos a la Sede Electrónica carece de los mismos riesgos que si el sistema fuera de conservación en local de los registros y los sistemas de seguridad no tienen por qué ser igual de rigurosos.

Conviene recalcar que si el software opera en modo VERI\*FACTU (con remisión voluntaria inmediata de los registros), es más improbable que el usuario pueda llevar a cabo ninguna alteración de registros u otra acción irregular "a posteriori" (ya sea de forma voluntaria o por error), pues los registros de facturación constarán en la AEAT, lo que impide realizar cambios sobre ellos.

## Si una empresa utiliza un programa informático no adaptado y del que ya no se ofrece mantenimiento y por tanto no tiene actualizada la versión del programa ¿qué responsabilidad tiene el fabricante de ese programa?

En un caso como el descrito la responsabilidad no recae en el fabricante, sino que recaería en su integridad en el usuario, en la medida que no haya adaptado sus sistemas a la normativa vigente.

## ¿Hasta dónde llega la responsabilidad del fabricante de software si se opta por ofrecer también el sistema de emisión de facturas no verificables? Ya que si solo se implanta el sistema VERI\*FACTU los sistemas fabricados están obligados a remitir los registros de facturación a la AEAT de forma inmediata.

Los SIF comercializados pueden ser "SOLO VERI\*FACTU" (es decir que solo permiten su uso como VERI\*FACTU) o "duales" (que permiten ser usados, a elección, como VERI\*FACTU y como sistema de emisión de facturas no verificables) y es el cliente (usuario del SIF) quien elige el modo de funcionamiento. No puede existir un SIF que únicamente funcione como sistema de emisión de facturas no verificables, porque el Reglamento obliga a que todos los SIF tenga la capacidad de ser VERI\*FACTU (aunque luego el usuario no elija esa modalidad de funcionamiento).

La responsabilidad en este aspecto del productor de sistemas "duales" es asegurarse del cumplimiento de la normativa (Ley, Reglamento y OM), de modo que se garanticen la integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros.

## Los sistemas y programas informáticos de facturación que usan los contribuyentes acogidos al SII, ¿tienen que estar certificados conforme a lo dispuesto en el artículo 29.2.j) de la Ley 58/2003, General Tributaria?

El artículo 29.2.j) de la Ley General Tributaria, establece la obligación, por parte de los productores, comercializadores y usuarios, de que los sistemas y programas informáticos o electrónicos que soporten los procesos contables, de facturación o de gestión de quienes desarrollen actividades económicas, garanticen la integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros, sin interpolaciones, omisiones o alteraciones de las que no quede la debida anotación en los sistemas mismos. Reglamentariamente se podrán establecer especificaciones técnicas que deban reunir dichos sistemas y programas, así como la obligación de que los mismos estén debidamente certificados y utilicen formatos estándar para su legibilidad.

Los contribuyentes incluidos en el SII aparecen expresamente excluidos del desarrollo reglamentario aprobado por RD 1007/2023, de 5 de diciembre, que aprueba el Reglamento que regula los Sistemas Informáticos de Facturación (RRSIF). Así consta expresamente en el artículo 3.3 del citado Reglamento que establece:

*El presente Reglamento no se aplicará a los contribuyentes que lleven los libros registros en los términos establecidos en el apartado 6 del artículo 62 del Reglamento del Impuesto sobre el Valor Añadido, aprobado por el Real Decreto 1624/1992, de 29 de diciembre.*

Por lo tanto, no existiendo, en relación con los obligados adscritos al SII, el desarrollo reglamentario al que se alude en el artículo 29.2.j) de la LGT, debe entenderse que no le es de aplicación la obligación de certificar sus sistemas. Todo ello sin perjuicio de que queden genéricamente obligados a garantizar la integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros que generen.

---

# Sistemas VERI\*FACTU (Sistemas de emisión de facturas verificables)

## ¿Qué posibilidades plantea el RRSIF sobre cómo debe ser un Sistema Informático de Facturación?

Para el cumplimiento de las obligaciones previstas en el Reglamento que regula los requisitos de los sistemas de facturación (RRSIF), aprobado por RD 1007/2023, de 5 de diciembre, se admiten dos modalidades: VERI\*FACTU (sistemas de emisión de facturas verificables) y sistemas de emisión de facturas no verificables.

Adicionalmente, de acuerdo con el artículo 7.b) del RRSIF aprobado por RD 1007/2023, de 5 de diciembre. También, la Administración Tributaria, diseñará un aplicativo web de último recurso, que tendrá la condición de VERI\*FACTU y lo pondrá a disposición de los empresarios que carezcan de SIF, en cuyo caso también se cumplirán los requisitos del RRSIF.

**Normativa/Doctrina:**

- Artículos 7 y 15 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Qué es un sistema VERI\*FACTU y en qué se diferencia de un sistema de emisión de facturas no verificables?

La respuesta a esta pregunta se encuentra en los artículos 15 y 16 del Reglamento, donde se mencionan a su vez los artículos 7, 8.2 y 14.2.

De forma resumida, la diferencia clave está en que los SIF «VERI\*FACTU» remiten en línea –a través de una conexión a Internet, de forma continuada, segura, correcta, íntegra, automática, consecutiva, instantánea y fehaciente– a la Agencia Tributaria todos los registros de facturación correspondientes a las facturas expedidas por el SIF, mientras que un sistema de emisión de facturas no verificables no los remite, sino que los almacena obligándose a garantizar la integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros, sin interpolaciones, omisiones o alteraciones de las que no quede la debida anotación en los sistemas mismos durante todo el periodo de prescripción fiscal.

La remisión en línea por parte de los SIF «VERI\*FACTU» es una forma de cumplir con el Reglamento que hace innecesaria la implementación –más complicada y costosa– de otras características de seguridad, a la vez que exime de responsabilidades de conservación y custodia de los registros a los usuarios de los mismos. Por su parte, para cumplir con los requisitos del Reglamento, los sistemas de emisión de facturas no verificables deben incorporar adicionalmente otras medidas de control, entre las que destacan el registro de eventos, la firma electrónica de los registros de facturación y de evento, permitir la posibilidad de exportación de los registros de facturación y de evento, ofrecer la comprobación de varios requisitos (huella, firma, encadenamiento…) de los registros de facturación y de evento, gestionar alarmas, etc.

**Normativa/Doctrina:**

- Artículos 7.b), 8.2, 14.2, 15 y 16 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Cuándo y cómo puede optarse por el sistema VERI\*FACTU?

La opción se entenderá realizada de forma tácita por el hecho de iniciar sistemáticamente la remisión de registros de facturación a la sede electrónica de la AEAT. Esta opción se prolongará, al menos, hasta el fin del año natural en el que se haya producido, de forma efectiva, el primer envío voluntario de los registros de facturación.

**Normativa/Doctrina:**

- Artículo 16.5 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 17 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## (Novedad) ¿Es necesario comunicar en el modelo 036 que se van a remitir los registros de facturación mediante un SIF modalidad VERI\*FACTU?

No.

Una vez se tenga obligación de adaptación al RRSIF, la opción se prolongará, al menos, hasta la finalización del año natural en el que se haya producido, de forma efectiva, el primer envío de los registros de facturación.

**Normativa aplicable:**

- Artículo 16 del RRSIF (Reglamento que establece los requisitos de los sistemas informáticos de facturación).

## ¿Es posible el cambio de la modalidad VERI\*FACTU (sistema de emisión de facturas verificables) a la modalidad sistema de emisión de facturas no verificables, y viceversa? ¿O, por el contrario, hay limitaciones en estos cambios?

Una empresa se puede adherir a VERI\*FACTU cuando desee. Una vez adherida a esta modalidad, deberá permanecer al menos hasta finalizar el año natural.

Si se inicia el año como sistema de emisión de facturas no verificables, en cualquier momento podrá cambiar a VERI\*FACTU debiendo permanecer en esta modalidad, como mínimo, hasta el fin del año natural.

**Normativa/Doctrina:**

- Artículos 15 y 16.5 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículo 17 de la Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## ¿La llevanza y conservación de los registros de facturación de alta y de los registros de facturación de anulación excluye la obligación de confeccionar el Libro Registro de Facturas emitidas? ¿Y de la presentación de modelos informativos 347 / 349?

No, la obligación de confeccionar los Libros Registro de Facturas Emitidas (regulada en el artículo 63 del Reglamento del Impuesto sobre el Valor Añadido, aprobado por el RD 1624/1992, de 29 de diciembre) se mantiene, al tratarse de una obligación diferente y autónoma de la establecida por el Reglamento SIF, que regula la forma en que deben funcionar los sistemas informáticos de facturación en la emisión y conservación de los registros de facturación de alta o anulación de facturas.

Tampoco se exonera de la presentación de modelos informativos como los mencionados, sin perjuicio de la agilización que pueda derivarse de la asistencia para la confección de las mismas.

## ¿Un SIF puede funcionar únicamente como sistema de emisión de facturas verificables? ¿Se pueden fabricar sistemas informáticos que puedan cumplir los requisitos del RRSIF y del SII?

Sí, los fabricantes de Sistemas Informáticos de Facturación pueden ofrecer aplicaciones solo VERI\*FACTU (sistemas de emisión de facturas verificables), aplicaciones "duales" que permitan al usuario optar por VERI\*FACTU y por sistemas de emisión de facturas no verificables, o incluso aplicaciones "triples" que permitan lo anterior y, en su caso, utilizarlo en la modalidad de SII.

Por el contrario, no se admite la producción de sistemas que únicamente emiten facturas no verificables ya que el RRSIF aprobado por RD 1007/2023, en su artículo 8.1 párrafo segundo, exige a los sistemas tener la capacidad de remisión.

En cualquier caso, la decisión de fabricar y comercializar unos u otros sistemas corresponde a los mismos fabricantes en función de necesidades comerciales, ya que la norma no obliga a fabricar sistemas con opción.

**Normativa/Doctrina:**

- Artículos 8.1, 15 y 16 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## En el caso de sistemas VERI\*FACTU, si se produce un corte de energía o un fallo informático, un problema de conexión de internet, o el servicio de la Sede Electrónica de la AEAT estuviera transitoriamente inoperativo ¿cómo se debe producir el envío de información a la AEAT? ¿Debe interrumpirse la facturación?

En casos excepcionales como los mencionados, u otros análogos, se ampliarían los plazos de remisión hasta la restauración de la caída o el restablecimiento de servicio. En la Orden Ministerial que desarrolla el Reglamento aprobado por el RD 1007/2023 se dan más detalles de cómo proceder al respecto (reenvíos periódicos, marca de "Incidencia" en la cabecera del envío de Registros, etc).

En estos casos de incidencias, no hay establecido un plazo máximo fijo para el envío que deberá reintentarse periódicamente hasta que se subsane le incidencia incorporando en el envío la "S" en el campo "Incidencia".

Incidencias como las mencionada, que afectan a la remisión a la AEAT, NO suponen en ningún caso que deba interrumpirse la facturación de la empresa. Esta deberá continuar con normalidad y los sistemas podrán enviar los registros "a posteriori" (reintentando la remisión periódicamente tal como se expone en los párrafos anteriores). Evidentemente si el corte es de energía eléctrica y los sistemas no pueden operar, la decisión de seguir operando/facturando corresponderá al empresario, pero en tal caso la información e facturación deberá recuperarse y remitirse cuanto antes.

## Comercios con múltiples terminales que cada uno es un SIF, ¿pueden comportarse de forma distinta? Por ejemplo, es posible tener 2 terminales de pago, uno con sistema VERI\*FACTU y luego otro con sistema de emisión de facturas no verificables.

Cada usuario debe tener sus Sistemas Informáticos de Facturación adaptados a la normativa que los regula. Pero ello no significa que deba tener solo un único SIF. Es lícito disponer de varios SIF, especialmente cuando las necesidades empresariales así lo justifiquen (varios centros de negocio no interconectados, varias líneas de producto diferenciadas, etc.). En este caso, los SIF deberán cumplir con la normativa, pero la opción por una u otra modalidad no es conjunta para el obligado a facturar, que podrá tener un SIF en la modalidad VERI\*FACTU y otro en modalidad sistema de emisión de facturas no verificables. Debe entenderse que cada uno de esos sistemas NO podrá intercalar operaciones en la otra modalidad, es decir, el sistema VERI\*FACTU siempre actuará como tal (siempre con envío) y el sistema de emisión de facturas no verificables siempre actuará como tal (siempre con conservación segura de los registros).

Debe tenerse en cuenta a este respecto que parte de los beneficios que derivan del uso de soluciones de tipo VERI\*FACTU no se puede producir para aquellos obligados tributarios que no tengan TODAS sus operaciones en esta modalidad (por ejemplo, servicios de asistencia como la descarga de registros, precursor del libro registro, menores requerimientos…).

**Normativa/Doctrina:**

- Artículos 7, 15 y 16 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## Aunque el reglamento especifica que no es necesario en VERI\*FACTU, ¿se pueden enviar los registros de facturación firmados electrónicamente?

La modalidad VERI\*FACTU no contempla como requisito la firma electrónica de los registros de facturación a remitir, ni dicha firma constituye campo obligatorio de la estructura del registro de alta de facturación. Precisamente, una de las ventajas de utilizar VERI\*FACTU es la ausencia de esta obligación.

Por el contrario, sí será obligatorio en el caso de que el envío de los tiques haya sido a raíz de un requerimiento y/o en el caso de almacenarlas en el propio SIF (sistema de facturación) al no hacer uso de VERI\*FACTU.

**Normativa/Doctrina:**

- Artículo 16 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## En el SIF instalado en un ERP hay "n" módulos diferentes (cada uno con una serie de facturación diferente) que emiten facturas: ¿es necesario encadenar todas las facturas mediante un único encadenamiento para toda la empresa? ¿e podría crear una cadena de registros de facturación por cada módulo?

La pertenencia de todos los módulos señalados al mismo ERP, hacen suponer la interconexión de dichos módulos en un sistema de facturación centralizado (o al menos consolidado y controlado de forma central). En ese caso, todos los registros deberán ser encadenados en el único SIF con un único encadenamiento, independientemente de la serie o número que tengan las facturas a las que correspondan.

No obstante, si se tratase de módulos inconexos o parcialmente inconexos, por ejemplo, porque generen la lógica obligatoria (registros de facturación de alta, códigos QR, etc.) de forma descentralizada y sin enlazar en tiempo real o ser controlados por el único ERP (al que le remiten los registros una vez al mes), puede entenderse que son SIF diferentes unos de otros. En este caso, el encadenamiento (y en su caso, el envío) se produce por cada SIF que tiene un funcionamiento aislado de los demás y, por lo tanto, no conoce lo que realiza otro módulo. En este caso cada uno de los SIF deberá cumplir individualmente los requisitos del RRSIF aprobado por RD 1007/2023, de 5 de diciembre.

## ¿Qué ventajas tiene utilizar un SIF «VERI\*FACTU» en lugar de un sistema de emisión de facturas no verificables?

De entrada, hay que decir que para los productores de SIF, los SIF «VERI\*FACTU» resultan más sencillos de producir que los sistemas de emisión de facturas no verificables, ya que tienen bastantes menos requisitos técnicos y de seguridad que implementar.

En cuanto a su utilización por parte del obligado a expedir facturas, las principales ventajas de emplear SIF «VERI\*FACTU» en lugar de sistemas de emisión de facturas no verificables son las siguientes:

1. Se les exime de la responsabilidad –y, en su caso, de realizar las propias tareas– de almacenar y/o exportar y conservar accesibles y legibles durante años los registros de facturación y los registros de evento. Por lo tanto, su uso puede resultar más sencillo, a la vez que aporta mayor tranquilidad en cuanto al cumplimiento.
2. Derivado del punto anterior, no deberán preocuparse de que lleguen requerimientos de la Agencia Tributaria para que entreguen posteriormente registros de facturación de sus facturas expedidas con SIF «VERI\*FACTU», con el consiguiente ahorro en tiempo y costes de todo tipo (de personal especializado, económico…) vinculados a la tramitación necesaria para el cumplimiento de este tipo de gestiones. Indirectamente ello puede acelerar la tramitación de devoluciones fiscales que se soliciten.
3. No estarán obligados a asegurar que, en todo momento, el reloj empleado por el SIF para datar los registros de facturación y de evento tiene la hora exacta (con un margen de error de un minuto).
4. Mediante los códigos «QR» que se incorporan a las facturas (incluyendo las facturas simplificadas), en las que además también aparecerá la frase "Factura verificable en la sede electrónica de la AEAT" o "VERI\*FACTU"), sus clientes podrán comprobar que esas facturas han quedado registradas en la Agencia Tributaria, lo que supone una garantía de transparencia y calidad en el grado de cumplimiento tributario. Este aspecto podría ser publicitado y argumentado como un elemento distintivo de "calidad y cumplimiento fiscal".
5. Dispondrán de servicios electrónicos proporcionados por la Agencia Tributaria que les faciliten la presentación de los libros registros de facturas expedidas, completándolos a partir de la información que ya se suministró al remitir los registros de facturación, así como ayudas en la confección de las autoliquidaciones.

**Normativa/Doctrina:**

- Diversos artículos del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## Respecto a la inmediatez de la remisión de los registros de facturación en VERI\*FACTU, ¿la fecha de emisión [creación] del registro de facturación debe coincidir con la fecha de comunicación?

La fecha de expedición de la factura debe coincidir con la de generación del registro de facturación. Ambas fechas, generalmente deben corresponderse con la fecha en que se remite el Registro de facturación. No obstante, se pueden dar situaciones puntuales de no coincidencia, de la fecha de generación del registro con la de envío (por ejemplo, incidencia al remitir que obliga a reintentar más adelante, cambio de horario de verano/invierno...).

Un mayor detalle puede encontrarse en las reglas de validación que afecten a los campos del registro de facturación y del mensaje de remisión a la AEAT.

## ¿Cómo se debe actuar si se remite un conjunto de registros de facturación, pero por alguna razón técnica no se recibe la respuesta de correcta recepción?

Si no se obtiene una respuesta tras un envío, se deben remitir de nuevo los registros de facturación hasta obtenerla.

Debe recalcarse que estos "envíos" y "respuestas" corresponden a comunicaciones de máquina a máquina, que son gestionados por los SIF y por la sede electrónica de la AEAT, por lo tanto, en general, son transparentes para los usuarios.

**Normativa/Doctrina:**

- Orden Ministerial por la que se desarrollan las especificaciones técnicas, funcionales y de contenido referidas en el reglamento (RRSIF), aprobado por el real decreto 1007/2023, de 5 de diciembre, y en el artículo 6.5 del reglamento por el que se regulan las obligaciones de facturación, aprobado por el real decreto 1619/2012, de 30 de noviembre.

## ¿Es posible usar un certificado electrónico de un tercero en la identificación [autenticación] para la remisión de los registros o es obligatorio que se use el certificado electrónico del obligado tributario de las facturas emitidas?

Para el envío de los Registros de facturación se puede utilizar cualquiera de las vías actuales de identificación admitidas por la AEAT, incluyendo la representación, el apoderamiento y la colaboración social, haciendo uso de un certificado cualificado por parte del tercero que ostente la condición de representante, apoderado o colaborador social.

## ¿Va a proporcionar la AEAT el servicio de descarga de todas las facturas presentadas por un obligado tributario si usa un sistema VERI\*FACTU?

Sí, la AEAT tiene previsto poner operativo un servicio que permita la descarga de la totalidad de los registros de facturación emitidos por un obligado tributario y comunicados por medio del sistema VERI\*FACTU. Igualmente se prevé la descarga de los registros emitidos por los proveedores de ese mismo obligado tributario en la medida que también sean VERI\*FACTU.

## En un sistema VERI\*FACTU, en los lotes de registros de facturación de envío ¿se pueden incluir registros de facturación de diferentes empresas usuarias del SIF, o cada lote solo debe incluir facturas de la misma empresa usuaria?

Todos los registros de facturación que se envíen en un mismo lote deben corresponder al mismo obligado tributario. En el caso de que el mismo SIF dé servicio a múltiples empresas, el sistema deberá realizar envíos separados.

## ¿Cómo será el proceso de recibo o recepción de las facturas?

La forma en que el cliente recibe la factura emitida por un SIF, no tiene ninguna diferencia respecto a las emitidas por otros sistemas; esto es, se regula por el Reglamento por el que se regulan las obligaciones de facturación, aprobado por Real Decreto 1619/2012. Así, quien la recibe de otros empresarios o profesionales por las operaciones de las que sean destinatarios y que se efectúen en desarrollo de la citada actividad, así como otras personas y entidades que no tengan la condición de empresarios o profesionales están obligadas a conservarlas (Artículos 1, y 19 a 23). La forma en que se puede expedir y recibir la factura dependerá de que sea facturación en papel o electrónica, y en este caso si es estructurada o no estructurada. El RRSIF no limita las anteriores posibilidades en modo alguno.

Por otro lado, si la pregunta se refiere a los registros de facturación (de las facturas):

- La AEAT ofrecerá servicios que permitan descargar los registros de facturación a quien los remitió.
- Asimismo, la AEAT ofrecerá servicios que permitan descargarlos al destinatario (obviamente, solo aquellos registros de facturación que sus proveedores hayan remitido a la AEAT mediante SIF VERI\*FACTU).
- Por último, el receptor de la factura podrá cotejar con el QR la constancia del registro de facturación en la sede electrónica de la AEAT y, en su caso, la coincidencia de la información remitida por el SIF del proveedor.

## Los aplicativos informáticos que contabilizan las facturas importadas de un sistema VERI\*FACTU ¿están sujetas a las mismas obligaciones del real decreto?

El artículo 29.2.j) de la Ley General Tributaria aplica a los sistemas informáticos utilizados para dar soporte a los procesos contables, de facturación y de gestión, por lo que todos ellos están obligados a garantizar los 6 requisitos exigidos sobre los registros empleados (es decir, sobre la información y datos que maneja cada uno) y, por tanto, no permitir interpolaciones, omisiones o alteraciones de las que no quede la debida anotación en los sistemas mismos.

Sin embargo, dicho mandato es genérico para todos los aplicativos salvo en el caso de los Sistemas de Facturación. Para ellos se concreta cómo cumplir con este mandato, lo cual se hace mediante el Reglamento que regula los Requisitos de los Sistemas de Facturación (RRSIF) aprobado por el RD 1007/2023, de 5 de diciembre, que desarrolla los requisitos que se deben implementar en los sistemas informáticos de facturación para cumplir con el artículo 29.2.j) de la LGT.

**Normativa/Doctrina:**

- Artículo 29.2.j) de la Ley General Tributaria Ley 58/2003, de 17 de diciembre, introducido por Ley 11/2021, de 9 de julio.

## Un sistema que tiene varias tiendas distribuidas por toda España y está realizando ventas, por medio de facturas simplificadas, ¿tiene que mandar la información VERI\*FACTU inmediatamente, o es posible realizar el envío, por ejemplo, al cerrar las tiendas?

La inmediatez del envío a VERI\*FACTU es parte del sistema de seguridad de los registros de facturación, por lo que se aplica en todos los casos. Por otro lado, el contraste de la operación por el cliente utilizando el código QR, característico de los sistemas VERI\*FACTU, solo puede realizarse si el envío se produce con inmediatez. Por lo tanto, el envío de las facturas simplificadas debe producirse en un caso como el mencionado de forma inmediata, respetando los tiempos técnicos exigidos por el control de flujo de información que la Sede Electrónica establezca.

**Normativa/Doctrina:**

- Artículos 15 y 16 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

---

# Posibilidad de remisión de información de la factura por parte de su receptor. Representación gráfica a incluir en la factura. Código QR. Frase «VERI\*FACTU».

## ¿A quiénes afectan los nuevos requisitos en la emisión de facturas completas y simplificadas (artículos 6.5 y 7.5 del Reglamento de Obligaciones de Facturación aprobado por R. D. 1619/2012), cuando se utilicen sistemas informáticos de facturación, consistentes en incorporar un código "QR" y, en su caso, las expresiones "VERI\*FACTU" o "Factura verificable en la sede electrónica de la AEAT" en las facturas impresas emitidas?

Los citados artículos del Reglamento de Obligaciones de Facturación se refieren a los sistemas informáticos del artículo 7 del Reglamento aprobado por R. D. 1007/23 (esto es, el Reglamento RSSIF). A su vez, el artículo 3.3 del Reglamento SIF, excluye del ámbito subjetivo de este a los obligados al SII (Suministro Inmediato de Información). Por lo tanto, dichos nuevos requisitos incorporados a los artículos 6.5 y 7.5 del Reglamento de Obligaciones de Facturación (ROF) aprobado por RD 1619/2012, solo son obligatorios para aquellos empresarios y profesionales obligados NO sujetos al SII, cuando deban expedir facturas. En particular las expresiones "VERI\*FACTU" o "Factura verificable en la sede electrónica de la AEAT" incluidas en las facturas impresas emitidas solo serán obligatorias para los SIF de los citados empresarios que opten por funcionar de acuerdo a esta modalidad.

Los obligados al SII, a todos los efectos relativos a su facturación propia, no quedan afectados por el R. D. 1007/2023.

## ¿Debe imprimirse el código QR en todas las facturas, tanto en la modalidad VERI\*FACTU (sistemas de emisión de facturas verificables), como en los sistemas de emisión de facturas no verificables? ¿Cuál es su finalidad?

Efectivamente, todas las facturas producidas con un SIF, cualquiera que sea la modalidad empleada, deberán llevar obligatoriamente el código «QR» impreso. Esa obligatoriedad deriva de la redacción de la Disposición final primera del Real Decreto 1007/2023, en relación con el artículo 17 del Reglamento SIF aprobado por dicho Real Decreto.

En cuanto a la finalidad del código «QR», a través de este no se envía la factura a la AEAT por su emisor, sino que sirve:

1. Para que el cliente destinatario de la factura pueda cotejar o comprobar si el correspondiente registro de facturación se encuentra en poder de la AEAT o no. Este cotejo tendrá lugar cuando se utiliza un sistema de emisión de facturas verificables (sistema VERI\*FACTU).
2. Por el contrario, cuando el sistema informático de facturación empleado es un sistema de emisión de facturas no verificables, la remisión de la información a la Administración Tributaria por el cliente destinatario de la factura, por medio del código QR, sirve para dejar constancia de la existencia de la factura misma y su contenido esencial, lo cual podría servir para un posible contraste futuro por parte de la AEAT.

En general el «QR» contribuye a permitir un mejor control del cumplimiento tributario del emisor de la factura, es decir, es una forma de mostrar una mayor "fiabilidad" fiscal (si la factura está registrada en la AEAT, el cliente puede esperar que su proveedor no está realizando ningún tipo de fraude fiscal, ni le está repercutiendo un IVA que luego no declara).

**Normativa/Doctrina:**

- Artículo 17 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Cuál es el mensaje de respuesta que recibe el receptor de una factura que remite los datos contenidos en el código «QR» a la AEAT?

La respuesta que recibirá el empresario o consumidor final, receptor de la factura, dependerá de si se han utilizado o no sistemas «VERI\*FACTU» para expedir la factura.

Si la factura ha sido generada a través de un sistema «VERI\*FACTU», la AEAT procederá a cotejar la información recibida con los registros de facturación remitidos por el expedidor de la factura. Las respuestas dadas a peticiones realizadas a través del código «QR» por un sistema «VERI\*FACTU» serán las siguientes:

1. Factura encontrada. En la Agencia Tributaria consta una factura con idénticas características a la remitida.
2. Factura no encontrada. En la Agencia Tributaria no consta ninguna factura con las características remitidas.

Si la factura ha sido generada a través de un sistema de emisión de facturas no verificables, la AEAT no puede realizar un cotejo con los registros de facturación porque estos no han sido enviados previamente por el expedidor de la factura. En este caso, el mensaje de respuesta es "Factura no verificable". Esta factura ha sido expedida por un sistema informático de facturación que NO es «VERI\*FACTU», (es decir, que no envía información de la factura a la Agencia Tributaria), por lo que no se puede verificar, si bien esa información puede servir de ayuda a la Agencia Tributaria en el desempeño de sus tareas de control del cumplimiento tributario.

## ¿Qué sucede con el Código «QR» si se utiliza factura electrónica?

Para el caso de que se utilice facturación electrónica estructurada, al no existir impresión en papel, el código QR no podrá incorporarse como tal a la factura. No obstante, la obligación de incorporar la información del QR, para el caso de facturación electrónica, ya sea la factura completa o simplificada, se sustituye por la incorporación a las e-Facturas del contenido del QR, incluyendo la url de cotejo en sede de la factura. Así lo establece el artículo 6.5.a) del Reglamento de Obligaciones de Facturación al disponer que *En el caso de que la factura sea electrónica, la representación gráfica podrá ser sustituida por el contenido que representa el código "QR".*

Por ello los clientes que reciban facturas electrónicas estructuradas podrán utilizar la información contenida en la factura electrónica para, a través de la URL recibida (la misma que codificaría el QR), acceder al servicio de verificación de factura igual que si escanearan el código QR.

Si la factura electrónica no es estructurada, sino que simplemente se transmite en formato electrónico visible (PDF, TIF, etc) e imprimible, la incorporación del QR no tendrá especialidades respecto de la que corresponde a la emisión en papel.

**Normativa/Doctrina:**

- Artículo 6.5.a) del Reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre, en la redacción que le da el RD 1007/2023, de 5 de diciembre.
- Artículo 17 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre y su desarrollo por Orden Ministerial.

## ¿Tengo que incluir el código «QR» tributario en los albaranes (o notas de entrega)?

No. El código «QR» tributario solo se añade a las facturas –sean «completas u ordinarias» o simplificadas, sean en papel o electrónicas– expedidas por los sistemas informáticos de facturación afectados por el RRSIF.

**Normativa/Doctrina:**

- Artículos 1.1 y 1.2 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.
- Artículos 6.5 y 7.5 del reglamento por el que se regulan las obligaciones de facturación (ROF), aprobado por el Real Decreto 1619/2012, de 30 de noviembre, introducidos por la disposición final primera uno y dos del Real Decreto 1007/2023, de 5 de diciembre.

## (Novedad) Un arrendador excluido del ámbito subjetivo del RRSIF (no AA.EE.), en el caso de emitir factura, si utiliza un SIF ¿está obligado a incluir en factura el código QR tributario? ¿podría utilizar un SIF adaptado al RRSIF que emitiera facturas sin el QR tributario?

No se encuentra **obligado** a utilizar un SIF (sistema informático de facturación) adaptado al RRSIF (Reglamento que establece los requisitos de los sistemas informáticos de facturación) que incluya el código «QR» tributario en la factura.

Sin embargo, si utiliza **voluntariamente** un SIF adaptado al RRSIF, dicho SIF no puede dejar de cumplir con los requisitos previstos en el mismo por lo que la factura necesariamente llevará el QR tributario.

## Tanto para transacciones B2B como B2C, ¿es necesario que impriman en papel la factura y en ellas impreso el QR, firma electrónica etc.?, ¿o con la comunicación por parte de la empresa a la AEAT será suficiente?

NO es obligatorio imprimir en papel la factura, siempre que se utilicen sistemas de facturación electrónica (ya sea estructurada o no estructurada).

Por otro lado, cualquier impresión de una factura (ordinaria o simplificada), o imagen de la misma en soporte digital (factura electrónica no estructurada), debe llevar impreso o visible el QR y la demás información requerida. Por el contrario, si la factura es electrónica estructurada no se requiere la imagen del QR, pero sí su contenido (en forma de URL de la sede electrónica habilitada para este efecto).

La remisión del registro de facturación (con todo el contenido al que se refieren los artículos 10 y 11 del RRSIF aprobado por RD 1007/2023) por parte de la empresa a la AEAT es una obligación adicional (en la modalidad VERI\*FACTU), pero responde a otra finalidad y en nada contradice la obligación de incorporar el código «QR» o la url a las facturas emitidas.

**Normativa/Doctrina:**

- Artículo 17 del reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Cómo debe remitir el receptor de la factura la información del «QR» a la AEAT?

El servicio de cotejo de «QR» se va a poder realizar desde cualquier dispositivo que disponga de una cámara y tenga acceso al reconocimiento del QR para obtener la URL y conexión a la web.

Para realizar el anterior proceso el uso de la APP de la AEAT es aconsejado, aunque no imprescindible. La APP de la AEAT es una garantía a la hora de asegurar que el «QR» incorporado a la factura y leído no sea irregular.

## ¿Dónde debe figurar el Código «QR» dentro de la factura?

Con carácter general, los códigos «QR» en las facturas impresas (o visualizables) deberán figurar en al principio de la factura, antes de que empiece el contenido de esta. Por lo tanto, será siempre el primer código «QR» que aparecerá en la factura. Si se utiliza un formato de orientación vertical para organizar y disponer el contenido de la factura, el código «QR» se situará arriba de esta, próximo al margen superior, preferiblemente centrado o, si no, próximo al margen superior izquierdo. En el caso de utilizar un formato de orientación horizontal (apaisado) para la factura, el código «QR» se situará a la izquierda de esta, preferiblemente cercana al margen superior izquierdo (o, si no, centrada respecto a los márgenes superior e inferior de la factura). Se trata de homogeneizar su ubicación para que sea previsible su ubicación. No obstante, está previsto que, si existen obstáculos que hagan inconveniente esta ubicación, pueda adoptarse otra ubicación, siempre que sea claramente visible y se distinga de cualquier otro código o QR empleado. Si hay algún elemento preimpreso en el papel que se va a utilizar para imprimir la factura y que, por tanto, no es generado desde el SIF (como podría ser el logotipo de la empresa, suponiéndose que el resto de información la genera el SIF), la parte preimpresa, al no haber sido generada por el SIF podría mantenerse en su lugar, quedando el QR ubicado como primer elemento del "resto" de la factura que sí genera el SIF.

El QR tributario solo debe aparecer una vez, al principio de la factura y antes del contenido de esta. Por lo tanto, si la factura ocupara más de una página, deberá figurar en la primera página y no en las siguientes.

El planteamiento de ubicación al principio de la factura pretende alinearse con el espíritu del artículo 29.2.j) de la Ley 58/2003, de 17 de diciembre, General Tributaria, introducido por el artículo de la Ley 11/2021, de 9 de julio, de medidas de prevención y lucha contra el fraude fiscal, dado que así se logra dar máxima visibilidad al QR tributario, siendo un pilar fundamental del modelo. De esta forma se garantiza que sea visible, se normaliza y hace previsible su ubicación favoreciendo su uso y contribuyendo a la concienciación y colaboración ciudadana y a la transparencia en el cumplimiento fiscal de quien expide las facturas, lo que además contribuye a favorecer su buena imagen.

**Normativa/Doctrina:**

- Orden Ministerial que desarrolla el reglamento (RRSIF), aprobado por el Real Decreto 1007/2023, de 5 de diciembre.

## ¿Cuál es el tamaño del QR que debe incorporarse a todas las facturas y facturas simplificadas?

En cuanto al tamaño del código QR, en orden a una mayor normalización del mismo en todas las facturas, y a asegurar una legibilidad estándar, ha de estar comprendido dentro del rango exigido de dimensiones (que coincide con el adoptado en las especificaciones por las Haciendas Forales en el Proyecto TicketBAI), no pudiendo ser ni inferior ni superior.

Ese tamaño debe situarse en la siguiente horquilla:

- no puede ser menor de 30x30 mm
- no puede ser mayor de 40x40 mm.

Se considera que dicho rango es el más adecuado, para permitir albergar el contenido que debe incluirse en el código QR, y para facilitar su lectura por los dispositivos con capacidad para ello.

---

# Procedimientos de facturación

## Tipo de facturas

El contenido del campo Tipo de Factura podrá tener uno de los siguientes valores:

### "F1": Factura (artículos 6, 7.2 y 7.3 del RD 1619/2012).

Se registran con la clave F1:

- Las facturas completas, excepto las facturas completas en las que no sea obligatoria la consignación del Número de Identificación Fiscal del destinatario en virtud de lo previsto en la letra d) del artículo 6.1 del Reglamento por el que se regulan las obligaciones de facturación, caracterizadas porque no se identifica al destinatario de las mismas (estas facturas se anotarán con la clave F2).
- Las facturas simplificadas cualificadas reguladas en los artículos 7.2 y 7.3 del Reglamento por el que se regulan las obligaciones de facturación, caracterizadas porque se identifica al destinatario de las mismas.

### "F2": Factura Simplificada y Facturas sin identificación del destinatario artículo 6.1.d) RD 1619/2012.

Se registran con la clave F2:

- Las facturas simplificadas, excepto las facturas simplificadas cualificadas reguladas en los artículos 7.2 y 7.3 del Reglamento por el que se regulan las obligaciones de facturación, que se registrarán con la clave F1.
- Las facturas completas para las que no sea obligatoria la consignación del Número de Identificación Fiscal del destinatario en virtud de lo previsto en la letra d) del artículo 6.1 del citado Reglamento por el que se regulan las obligaciones de facturación, caracterizadas porque no se identifica al destinatario de las mismas.

### "F3": Factura emitida en sustitución de facturas simplificadas facturadas y declaradas.

Sólo utilizarán este tipo de factura aquellos obligados que registren facturas en sustitución de facturas simplificadas.

### "R1": Factura Rectificativa (Error fundado en derecho y Art. 80 Uno Dos y Seis LIVA).

Cuando se haya producido un error fundado de derecho o alguna de las causas del art. 80.Uno, Dos y Seis LIVA (devoluciones de mercancías, descuentos o alteraciones en el precio posteriores a la realización de la operación, resolución de operaciones, importe de la contraprestación provisional) deberá emitirse una factura rectificativa con serie específica cuya información se registrará con el tipo de factura R1.

En el caso de la devolución de mercancías o de envases y embalajes que se realicen con ocasión de un posterior suministro al mismo destinatario y tipo impositivo no será necesario la expedición de una factura rectificativa, sino que se restará el importe de las mercancías o de los envases y embalajes devueltos del importe de dicha operación posterior, pudiendo ser el resultado positivo o negativo.

Se incluirá como fecha de operación la fecha en que se realizó la entrega o prestó el servicio, indicada en la factura inicial. En el caso de rectificar varias facturas con una única factura rectificativa se indicará la fecha más reciente.

### "R2": Factura Rectificativa (Art. 80.Tres, por concurso de acreedores).

Cuando se haya producido una modificación de la base imponible del IVA por encontrarse el cliente en concurso de acreedores (art. 80.Tres LIVA) deberá emitirse una factura rectificativa con serie específica cuya información se registrará con el tipo de factura R2.

Asimismo, se deberá identificar el tipo de factura rectificativa con las claves "S- por sustitución" o "I- por diferencias" según la forma en que el empresario desee llevar a cabo la rectificación.

Se incluirá como fecha de operación la fecha en que se realizó la entrega o presto el servicio, indicada en la factura inicial. En el caso de rectificar varias facturas con una única factura rectificativa se indicará la fecha más reciente.

La identificación de las facturas rectificadas será opcional. En el caso de que se identifiquen se deberá informar el número y la fecha de expedición.

### "R3": Factura Rectificativa (Art. 80.Cuatro, por crédito incobrable).

Cuando se haya producido una modificación de la base imponible del IVA por incobro del cliente (art. 80.Cuatro LIVA) deberá emitirse una factura rectificativa con serie específica cuya información se registrará con el tipo de factura R3.

Asimismo, se deberá identificar el tipo de factura rectificativa con las claves "S- por sustitución" o "I- por diferencias" según la forma en que el empresario desee llevar a cabo la rectificación.

Se incluirá como fecha de operación la fecha en que se realizó la entrega o presto el servicio, indicada en la factura inicial. En el caso de rectificar varias facturas con una única factura rectificativa se indicará la fecha más reciente.

La identificación de las facturas rectificadas será opcional. En el caso de que se identifiquen se deberá informar el número y la fecha de expedición.

### "R4": Factura Rectificativa (Resto).

Se indicará tipo de factura R4 en estas situaciones:

- Cuando se haya producido una modificación de la base imponible del IVA por causas distintas a las previstas en el artículo 80 LIVA y no se deba a un error fundado de derecho deberá emitirse una factura rectificativa con serie específica cuya información se registrará con el tipo de factura R4.
- Cuando se haya consignado erróneamente algún dato no monetario de la factura.

### "R5": Factura Rectificativa en facturas simplificadas.

La rectificación de una factura simplificada se registrará con la clave R5 cualquiera que sea el motivo de la misma.

## ¿Cómo registra el emisor una factura emitida en sustitución de facturas simplificadas (art. 7.2 RD 1619/2012)?

Se deberá informar en el bloque "Tipo Factura" con la clave "F3: factura emitida en sustitución de facturas simplificadas facturadas y declaradas" y en el bloque de "Datos sustituidas" se identificarán las facturas simplificadas sustituidas con el número, serie y fecha de expedición. La identificación es opcional.

IMPORTANTE: En el caso de que se realice un abono de la factura simplificada (mediante el envío de un registro negativo con clave "F2"), la factura emitida en sustitución de esta tendrá que informarse con la clave "F1".

## ¿Cómo registra el emisor una factura rectificativa?

Cuando se haya producido un error material en la factura (cuando no se cumpla en la factura alguno de los requisitos exigidos conforme al artículo 6 o 7 del Reglamento de Facturación), un error fundado de derecho, una incorrecta determinación de la cuota repercutida o alguna de las circunstancias que dan lugar a la modificación de la base imponible (art. 80 LIVA) deberá emitirse una factura rectificativa cuya información se remitirá identificando el tipo de factura con las claves "R1", "R2", "R3" y "R4" según cuál sea el motivo de la rectificación (errores fundados de derecho y causas del artículo 80.Uno, Dos y Seis LIVA, concurso de acreedores, deudas incobrables y resto de causas).

Asimismo, se deberá identificar el tipo de factura rectificativa con las claves "S- sustitución" o "I-por diferencias".

Cuando la rectificación se realice sobre una factura simplificada, la información a remitir implicará indicar el tipo de factura con la clave "R5" (factura Rectificativa en facturas simplificadas).

## ¿Cómo registra el emisor una factura rectificativa por sustitución "S"?

La información de la factura se remitirá indicando tipo de factura con las claves "R1", "R2", "R3" y "R4". En el caso de que se rectifique una factura simplificada la clave será "R5". Cuando la rectificación se haga por "sustitución" se deberá informar de la rectificación efectuada señalando igualmente el importe de dicha rectificación.

Esta información se podrá realizar:

- Opción 1: Informando de un nuevo registro en el que se indiquen los importes correctos tras la rectificación en los campos "base imponible", "cuota" y en su caso "recargo" y a su vez de los importes rectificados respecto de la factura original en los campos "base rectificada", "cuota rectificada" y en su caso "cuota recargo rectificado".
- Opción 2: Informando de un nuevo registro en el que se indiquen los importes correctos tras la rectificación en los campos "base imponible", "cuota repercutida" y en su caso "cuota recargo equivalencia" y de otro registro en el que se informe de los importes rectificados.

La identificación de la relación de facturas rectificadas será opcional.

### Ejemplo 1. Disminución de la base imponible

La factura nº1 de base imponible 1.000 € y cuota 210 € con fecha de operación 01/05/2024 y fecha de expedición 7/05/2024.

Esta factura va a ser objeto de rectificación, consistiendo dicha rectificación en una disminución de la base imponible de 200 euros.

**Opción 1:** La modificación por sustitución supondría emitir una factura rectificativa con base imponible de 800 € y cuota 168, en la que se indicará que la rectificación realizada es de 1000 € por la base imponible rectificada y 210 € por la cuota rectificada.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: Rx
- Tipo Rectificativa: S
- Fecha Operación: 01/05/2024
- Fecha expedición: 18/10/2024
- Importe Rectificación: se informará de dos campos adicionales con la "base rectificada" (1.000) y la "cuota rectificada" (210).
- Importe total: se indicará el importe final válido 968.
- Desglose IVA: base imponible: 800, cuota repercutida 168

**Opción 2:** La modificación por sustitución supondría emitir una factura con base imponible de -1000 € y una factura rectificativa en la que se indicará que la base imponible es de 800 €.

En la primera factura los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: F1
- Fecha Operación: dejar en blanco
- Fecha expedición: 18/10/2024
- Desglose IVA: se indicará el importe que se rectifica con signo contrario (base imponible: (-1.000), cuota repercutida (-210).

En la segunda de las facturas rectificativas los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: Rx
- Tipo Rectificativa: S
- Fecha Operación: 01/05/2024
- Fecha expedición: 18/10/2024
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" 0 y la "cuota rectificada" 0.
- Importe total: se indicará el importe final válido 968.
- Desglose IVA: base imponible: 800, cuota repercutida 168.

### Ejemplo 2: Aumento de base imponible

La factura nº2 de base imponible 1.000 € y cuota 210 € va a ser objeto de rectificación. La rectificación consiste en un aumento de la base imponible de 200 euros.

**Opción 1:** La modificación por sustitución supondría emitir una factura rectificativa con base imponible de 1.200 € y cuota 252, en la que se indicará que la rectificación realizada es de 1000 € por la base imponible rectificada y 210 € por la cuota rectificada.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: Rx
- Tipo Rectificativa: S
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" (1.000) y la "cuota rectificada" (210).
- Importe total: se indicará el importe final válido 1.452.
- Desglose IVA: base imponible: 1.200, cuota repercutida 252.

**Opción 2:** La modificación por sustitución supondría emitir una factura con base imponible de -1000 € y una factura rectificativa en la que se indicará que la base imponible es de 1.200 €.

En la primera factura los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: F1
- Desglose IVA: se indicará el importe que se rectifica con signo contrario (base imponible: (-1.000), cuota repercutida (-210).

En la segunda de las facturas rectificativas los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: Rx
- Tipo Rectificativa: S
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" 0 y la "cuota rectificada" 0.
- Importe total: se indicará el importe final válido 1.452
- Desglose IVA: base imponible: 1.200, cuota repercutida 252.

### Ejemplo 3: Disminución de base imponible por impago

La factura nº3 de base imponible 1.000 € y cuota 210 € va a ser objeto de rectificación por impago, eliminando la totalidad de la cuota repercutida.

**Opción 1:** La modificación por sustitución supondría emitir una factura rectificativa con base imponible de 1.000 € y cuota 0, en la que se indicará que la rectificación realizada es de 1000 € por la base imponible rectificada y 210 € por la cuota rectificada.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R2 / R3
- Tipo Rectificativa: S
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" 1.000 y la "cuota rectificada" 210.
- Importe total: se indicará el importe final válido 1.000.
- Desglose IVA: base imponible: 1.000, cuota repercutida 0.

**Opción 2:** La modificación por sustitución supondría emitir una factura con base imponible de -1000 €, cuota de -210 y una factura rectificativa en la que se indicará que la base imponible es de 1.000 € y la cuota 0€.

En la primera factura los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: F1
- Desglose IVA: se indicará el importe que se rectifica con signo contrario (base imponible: (-1.000) y cuota repercutida (-210).

En la segunda de las facturas rectificativas los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R2 / R3
- Tipo Rectificativa: S
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" 0 y la "cuota rectificada" 0.
- Importe total: se indicará el importe final válido 1.000
- Desglose IVA: base imponible: 1.000, cuota repercutida 0

### Ejemplo 4: Rectificación de factura rectificativa previa: aumento de base imponible.

La factura rectificativa nº1 bis de base imponible -1.000 € y cuota -210 € va a ser objeto de rectificación. La rectificación consiste en un aumento de la base imponible de 200 euros pues la factura rectificativa nº1 bis debía haberse emitido por un importe de base imponible -800 € y cuota -168 €

**Opción 1:** La modificación por sustitución supondría emitir una nueva factura rectificativa con base imponible de -800 € y cuota -168 €, en la que se indicará que la rectificación realizada es de -1000 € por la base imponible rectificada y -210 € por la cuota rectificada.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R4
- Tipo Rectificativa: S
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" (-1.000) y la "cuota rectificada" (-210).
- Importe total: se indicará el importe final válido (-968).
- Desglose IVA: base imponible: -800, cuota repercutida (-168).

**Opción 2:** La modificación por sustitución supondría emitir una factura con base imponible de 1.000 € y una factura rectificativa en la que se indicará que la base imponible es de -800 €.

En la primera factura los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: F1
- Desglose IVA: se indicará el importe que se rectifica con signo contrario (base imponible: 1.000, cuota repercutida 210).

En la segunda de las facturas rectificativas los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R4
- Tipo Rectificativa: S
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" 0 y la "cuota rectificada" 0.
- Importe total: se indicará el importe final válido (-968)
- Desglose IVA: base imponible:( -800), cuota repercutida (-168).

### Ejemplo 5: Rectificación de factura rectificativa previa: disminución de base imponible.

La factura rectificativa nº2 bis de base imponible -1.000 € y cuota -210 € va a ser objeto de rectificación. La rectificación consiste en una disminución de la base imponible de 200 euros pues la factura rectificativa nº2 bis debía haberse emitido por un importe de base imponible -1.200 € y cuota -252 €

**Opción 1:** La modificación por sustitución supondría emitir una nueva factura rectificativa con base imponible de -1.200 € y cuota -252 €, en la que se indicará que la rectificación realizada es de -1000 € por la base imponible rectificada y -210 € por la cuota rectificada.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R4
- Tipo Rectificativa: S
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" (-1.000) y la "cuota rectificada" (-210).
- Importe total: se indicará el importe final válido (-1.452).
- Desglose IVA: base imponible: (-1.200), cuota repercutida (-252).

**Opción 2:** La modificación por sustitución supondría emitir una factura con base imponible de 1.000 € y una factura rectificativa en la que se indicará que la base imponible es de -1.200 €.

En la primera factura los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: F1
- Desglose IVA: se indicará el importe que se rectifica con signo contrario (base imponible: 1.000, cuota repercutida 210.

En la segunda de las facturas rectificativas los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R4
- Tipo Rectificativa: S
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" 0 y la "cuota rectificada" 0.
- Importe total: se indicará el importe final válido (-1.452)
- Desglose IVA: base imponible: (-1.200), cuota repercutida (-252).

### Ejemplo 6: Rectificación de factura rectificativa previa de importe negativo: aumento de base imponible hasta importe positivo.

La factura rectificativa nº3 bis de base imponible -1.000 € y cuota -210 € va a ser objeto de rectificación. La rectificación consiste en un aumento de la base imponible de 1.500 euros pues la factura rectificativa nº2 bis debía haberse emitido por un importe de base imponible 500 € y cuota 105 €

**Opción 1:** La modificación por sustitución supondría emitir una nueva factura rectificativa con base imponible de 500 € y cuota 105 €, en la que se indicará que la rectificación realizada es de -1.000 € por la base imponible rectificada y -210 € por la cuota rectificada.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R4
- Tipo Rectificativa: S
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" (-1.000) y la "cuota rectificada" (-210).
- Importe total: se indicará el importe final válido 605.
- Desglose IVA: base imponible: 500, cuota repercutida 105.

**Opción 2:** La modificación por sustitución supondría emitir una factura con base imponible de 1.000 € y una factura rectificativa en la que se indicará que la base imponible es de 500 €.

En la primera factura los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: F1
- Desglose IVA: se indicará el importe que se rectifica con signo contrario (base imponible: 1.000, cuota repercutida 210.

En la segunda de las facturas rectificativas los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R4
- Tipo Rectificativa: S
- Importe Rectificación: se informará de dos campos adicionales con "la base rectificada" 0 y la "cuota rectificada" 0.
- Importe total: se indicará el importe final válido 605.

## ¿Cómo registra el emisor una factura rectificativa por diferencias "I"?

La información de la factura se remitirá indicando tipo de factura con las claves "R1", "R2", "R3" y "R4". En el caso de que se rectifique una factura simplificada la clave será "R5".

Cuando la rectificación se haga por "diferencias" se deberá informar directamente del importe de la rectificación.

Para ello se deberá informar en un solo registro de la factura rectificativa con la clave "I". En este caso no se deben rellenar los campos adicionales "Base rectificada" y "Cuota rectificada". La identificación de la relación de facturas rectificadas será opcional.

### Ejemplo 1. Disminución de la base imponible

La factura nº1 de base imponible 1.000 € y cuota 210 € va a ser objeto de rectificación. La rectificación consiste en una disminución de la base imponible de 200 euros.

La modificación por diferencias supondría emitir una factura con base imponible de -200 €.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: Rx
- Tipo Rectificativa: I
- Importe total: se indicará el importe total de la rectificación -242.
- Desglose IVA: base imponible: -200, cuota repercutida – 42.

### Ejemplo 2: Aumento de base imponible

La factura nº2 de base imponible 1.000 € y cuota 210 € va a ser objeto de rectificación. La rectificación consiste en un aumento de la base imponible de 200 euros. La modificación por diferencias supondría emitir una factura con base imponible de 200 €.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: Rx
- Tipo Rectificativa: I
- Importe total: se indicará el importe total de la rectificación 242.
- Desglose IVA: base imponible: 200, cuota repercutida 42.

### Ejemplo 3: Disminución de base imponible por impago

La factura nº3 de base imponible 1.000 € y cuota 210 € va a ser objeto de rectificación por impago, eliminando la totalidad de la cuota repercutida.

La modificación por diferencias supondría emitir una factura con base imponible de 0 € y cuota de -210 €.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R2 / R3
- Tipo Rectificativa: I
- Importe total: se indicará el importe total de la rectificación (-210).
- Desglose IVA: base imponible: 0, cuota repercutida (-210).

### Ejemplo 4: Rectificación de factura rectificativa previa: aumento de base imponible.

La factura rectificativa nº1 bis de base imponible -1.000 € y cuota -210 € va a ser objeto de rectificación. La rectificación consiste en un aumento de la base imponible de 200 euros pues la factura rectificativa nº1 bis debía haberse emitido por un importe de base imponible -800 € y cuota -168 €

La modificación por diferencias supondría emitir una nueva factura rectificativa con base imponible de 200 €.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R4
- Tipo Rectificativa: I
- Importe total: se indicará el importe total de la rectificación 242.
- Desglose IVA: base imponible: 200, cuota repercutida 42.

### Ejemplo 5: Rectificación de factura rectificativa previa: disminución de base imponible.

La factura rectificativa nº2 bis de base imponible -1.000 € y cuota -210 € va a ser objeto de rectificación. La rectificación consiste en una disminución de la base imponible de 200 euros pues la factura rectificativa nº2 bis debía haberse emitido por un importe de base imponible -1.200 € y cuota -252 €

La modificación por diferencias supondría emitir una nueva factura rectificativa con base imponible de -200 €.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R4
- Tipo Rectificativa: I
- Importe total: se indicará el importe total de la rectificación (-242).
- Desglose IVA: base imponible: -200, cuota repercutida (-42).

### Ejemplo 6: Rectificación de factura rectificativa previa de importe negativo: aumento de base imponible hasta importe positivo.

La factura rectificativa nº3 bis de base imponible -1.000 € y cuota -210 € va a ser objeto de rectificación. La rectificación consiste en un aumento de la base imponible de 1.500 euros pues la factura rectificativa nº2 bis debía haberse emitido por un importe de base imponible 500 € y cuota 105 €.

La modificación por diferencias supondría emitir una nueva factura rectificativa con base imponible de 1.500 €.

Los campos y claves a consignar en el registro de facturación de alta son:

- Tipo Factura: R4
- Tipo Rectificativa: I
- Importe total: se indicará el importe total de la rectificación 1.815.
- Desglose IVA: base imponible 1.500, cuota repercutida 315.

## ¿Cómo se modifica o anula una factura emitida por error o con errores en los datos de identificación (ej. operación inexistente)?

El registro de alta enviado previamente y que no procede se dará de baja mediante un registro de facturación de anulación identificando el número de la factura original.

En el caso de que proceda emitir una nueva factura correcta se deberá registrar con un alta y con un número de factura o fecha de expedición diferente.

## ¿Qué fecha de operación debe hacerse constar en una factura rectificativa?

La fecha de realización de la operación correspondiente a la factura original que se está rectificando.

## ¿Qué fecha de operación debe constar en una factura rectificativa si se rectifican varias facturas mediante un único documento de rectificación?

Se consignará el último día en el que se haya efectuado la operación que documenta la última factura rectificada (la de fecha más reciente).

---

# Colaboración social

## ¿Cómo pueden las empresas desarrolladoras de software remitir los registros de facturación de los obligados tributarios en el marco de lo dispuesto en el Reglamento que establece los requisitos que deben adoptar los sistemas y programas informáticos o electrónicos que soporten los procesos de facturación de empresarios y profesionales, y la estandarización de formatos de los registros de facturación, aprobado por Real Decreto 1007/2023, de 5 de diciembre?

Para remitir los registros de facturación a la Sede electrónica de la Agencia Estatal de Administración Tributaria, el envío podrá ser efectuado por el propio obligado tributario o por un tercero que actúe en su representación, de acuerdo con lo establecido en los artículos 79 a 81, ambos inclusive, del Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, aprobado por el Real Decreto 1065/2007, de 27 de julio, y en la Orden HAC/1398/2003, de 27 de mayo, por la que se establecen los supuestos y condiciones en que podrá hacerse efectiva la colaboración social en la gestión de los tributos, y se extiende ésta expresamente a la presentación telemática de determinados modelos de declaración y otros documentos tributarios.

Como terceros que actúen en representación del obligado tributario, las empresas desarrolladoras de software pueden suscribir el acuerdo de colaboración social en la aplicación de los tributos Tipo 017 para la prestación de servicios de suministro electrónico de registros de facturación en el ámbito del Suministro Inmediato de Información (SII), de suministro electrónico de los asientos contables de los establecimientos afectados por la normativa de los Impuestos Especiales (SILICIE), y de remisión de ficheros que contienen los registros de facturación generados por sistemas de emisión de facturas, a través de la Sede Electrónica de la Agencia Estatal de Administración Tributaria.

Para la firma del acuerdo de colaboración social en la aplicación de los tributos las empresas desarrolladoras de software deberán ponerse en contacto con la Agencia Tributaria a través de la dirección comunicacion.sepri@correo.aeat.es

## ¿Cómo se otorga la representación a las empresas suministradoras de software para que remitan, en el ámbito de la colaboración social en la aplicación de los tributos, los registros de facturación generados por sistemas informáticos de facturación?

Para otorgar la representación al colaborador social serán válidos los modelos aprobados por la Resolución de 18 de diciembre de 2024, de la Dirección General de la Agencia Estatal de Administración Tributaria, por la que se aprueban los documentos normalizados para acreditar la representación de terceros en el procedimiento para el envío de los ficheros que contienen registros de facturación generados por sistemas de emisión de facturas, a través de la Sede electrónica de la Agencia Tributaria.

Los modelos de representación podrán ser firmados por el titular de los registros de facturación (otorgante) de forma manuscrita, aportando en este caso copia de su DNI si fuera persona física o copia de DNI del representante, con estampado del sello de la empresa si el otorgante fuera persona jurídica, o mediante suscripción electrónica, bien sea utilizando una firma electrónica reconocida realizada con un certificado electrónico cualificado de persona física o de representación de persona jurídica, en vigor, no revocado y emitido por una autoridad de certificación incluida en la Lista de confianza de prestadores de servicios de certificación del Ministerio de Industria y Turismo, o una firma electrónica avanzada que cumpla con los requisitos previstos en el artículo 26 del Reglamento eIDAS, (Reglamento (UE) nº 910/2014 del Parlamento Europeo y del Consejo, de 23 de julio de 2014, relativo a la identificación electrónica y los servicios de confianza para las transacciones electrónicas en el mercado interior y por el que se deroga la Directiva 1999/93/CE).

Para otorgar la representación en colaboración social no se admitirán modalidades de aceptación de condiciones del servicio u otras alternativas que no permitan acreditar el otorgamiento para la remisión de los ficheros que contienen los registros de facturación en la Sede electrónica de la Agencia Tributaria.

---

# Glosario de abreviaturas

1. **AEAT**: Agencia Estatal de Administración Tributaria
2. **DR**: Declaración responsable
3. **FAQ**: (Frequently Asked Question/s): Pregunta/s frecuentes
4. **IGIC**: Impuesto General Indirecto Canario
5. **IOSS**: Ventanilla única para las importaciones (por sus siglas en inglés)
6. **IPSI**: Impuesto sobre la Producción, los Servicios y la Importación
7. **IRPF**: Impuesto sobre la Renta de las Personas Físicas
8. **IVA**: Impuesto sobre el Valor Añadido
9. **LGT**: Ley General Tributaria
10. **LIVA**: Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido
11. **LRI**: Libros registros de IVA
12. **NIF**: Número de Identificación Fiscal
13. **OEF**: Obligado a expedir factura
14. **OM**: Orden Ministerial
15. **OSS**: Ventanilla única (por sus siglas en inglés)
16. **OT**: Obligado tributario
17. **R. D.**: Real Decreto
18. **RF**: Registros de facturación
19. **RIVA**: Reglamento del Impuesto sobre el Valor Añadido
20. **ROF**: Reglamento por el que se regulan las obligaciones de facturación
21. **RRSIF**: Reglamento que establece los requisitos de los sistemas informáticos de facturación
22. **RSIF**: Reglamento que establece los requisitos de los sistemas informáticos de facturación
23. **RSSIF**: Reglamento de los Requisitos de los Sistemas Informáticos de Facturación
24. **SIF**: Sistemas informáticos de facturación
25. **SII**: Suministro Inmediato de Información del IVA
26. **VERI\*FACTU**: Sistema/s de emisión de facturas verificables

---

*Documento generado con fecha 17/Junio/2026 en la dirección web https://sede.agenciatributaria.gob.es en la ruta: Inicio / IVA / Sistemas Informáticos de Facturación (SIF) y VERI\*FACTU*

:- dynamic accion/5.
:- dynamic imagen_accion/5.
:- dynamic respuesta/5.

:- discontiguous imagen_accion/5.
:- discontiguous accion/5.
:- discontiguous respuesta/5.


tipo(insultos_burlas).
tipo(exclusion_grupal).
tipo(agresion_fisica).

lugar(escuela).
lugar(trabajo).
lugar(hogar).
lugar(calle_transporte).

gravedad(me_molesta).
gravedad(me_afecta).
gravedad(me_pone_en_riesgo).

causa(forma_de_ser).
causa(origen).
causa(economia).

% Casos espec�ficos con mensajes detallados
accion(exclusion_grupal, trabajo, me_pone_en_riesgo, forma_de_ser,
"Ser excluido/a en el trabajo por tu forma de ser puede afectar seriamente tu salud emocional y f�sica. No es algo que debas aguantar ni justificar. Existen protocolos y pol�ticas que protegen tu derecho a un ambiente laboral seguro. Hablar con alguien dentro o fuera del entorno laboral puede ayudarte a activar esos mecanismos y a encontrar formas de apoyo efectivas.").
respuesta(exclusion_grupal, trabajo, me_pone_en_riesgo, forma_de_ser,
"Te Recomiendo Que Documentes Lo Que est�s viviendo y busques el �rea de recursos humanos o alg�n canal confidencial dentro de tu lugar de trabajo para expresar tu situaci�n. Tambi�n puedes acercarte a una persona de confianza dentro de la organizaci�n que pueda ayudarte a mediar. No enfrentes esto solo/a; busca apoyo psicol�gico para cuidar tu bienestar emocional.").


accion(agresion_fisica, calle_transporte, me_pone_en_riesgo, origen,
"Agresiones F�sicas en la calle o
transporte, estado grave, por origen de
la persona:
Se recomienda activar protocolos de
protecci�n urgente, acompa�ar a la
v�ctima a presentar denuncia formal con
asesor�a legal especializada en cr�menes
de odio, ofrecer apoyo psicol�gico
inmediato y coordinar con
organizaciones civiles o defensor�as de
derechos humanos para garantizar
seguimiento y medidas de seguridad.").
respuesta(agresion_fisica, calle_transporte, me_pone_en_riesgo, origen,
"Te recomiendo que acudas de
inmediato a una instituci�n de apoyo legal o
de derechos humanos, y que te acerques a
alguien de confianza que pueda
acompa�arte en este proceso. Tambi�n es
importante que busques atenci�n
psicol�gica especializada para procesar lo
ocurrido y proteger tu bienestar emocional.").

% Asociaci�n de im�genes con los casos
imagen_accion(exclusion_grupal, trabajo, me_pone_en_riesgo, forma_de_ser, "imagen1.jpg").
imagen_accion(agresion_fisica, calle_transporte, me_pone_en_riesgo, origen, "imagen2.jpg").




accion(insultos_burlas, hogar, me_afecta, economia, "dfg").
imagen_accion(insultos_burlas, hogar, me_afecta, economia, "descarga.png").
respuesta(insultos_burlas, hogar, me_afecta, economia, "dfg").

accion(insultos_burlas, escuela, me_molesta, origen, "asdasdqweqwe").
imagen_accion(insultos_burlas, escuela, me_molesta, origen, "descarga.png").
respuesta(insultos_burlas, escuela, me_molesta, origen, "qweqweqweasdfqwrqwewqeqwe").

accion(insultos_burlas, escuela, me_molesta, forma_de_ser, "asd").
imagen_accion(insultos_burlas, escuela, me_molesta, forma_de_ser, "descarga.png").
respuesta(insultos_burlas, escuela, me_molesta, forma_de_ser, "asd").

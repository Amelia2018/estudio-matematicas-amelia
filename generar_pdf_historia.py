import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def draw_header(c, page_num, total_pages=8, section_title=""):
    """Encabezado oficial institucional para 3° básico"""
    # Barra superior
    c.setFillColor(colors.HexColor("#C2410C")) # Terracotta
    c.rect(36, 756, 540, 22, fill=1, stroke=0)
    
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(44, 763, "COLEGIO - EVALUACIÓN FORMATIVA OFICIAL | HISTORIA, GEOGRAFÍA Y CIENCIAS SOCIALES")
    c.drawRightString(568, 763, f"Pág. {page_num} de {total_pages}")

    # Datos estudiante
    c.setStrokeColor(colors.HexColor("#E2E8F0"))
    c.setLineWidth(1)
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.roundRect(36, 714, 540, 36, 4, fill=1, stroke=1)

    c.setFillColor(colors.HexColor("#1E293B"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(44, 735, "Estudiante: Amelia Bustos")
    c.drawString(220, 735, "Curso: 3° Básico A")
    c.drawString(340, 735, "Fecha: Octubre 2026")
    c.drawString(450, 735, "Puntaje: ___ / 45 pts")

    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.HexColor("#64748B"))
    c.drawString(44, 721, f"Unidad 2: La Civilización Griega (Texto MINEDUC / Santillana) • {section_title}")

def draw_footer(c, page_num, total_pages=8):
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.setLineWidth(0.8)
    c.line(36, 32, 576, 32)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(colors.HexColor("#64748B"))
    c.drawString(36, 22, "Guía Oficial de Preparación para Prueba de Historia • 3° Básico A • Amelia Bustos")
    c.drawRightString(576, 22, f"Página {page_num} de {total_pages}")

def draw_section_banner(c, y, num_str, title_str):
    c.setFillColor(colors.HexColor("#9A3412"))
    c.roundRect(36, y, 540, 20, 3, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(44, y + 6, f"{num_str}. {title_str.upper()}")

def draw_q_box(c, x, y, w, h, q_num, text_lines, choices=None):
    """Caja para ejercicio con opciones de selección o líneas para escribir."""
    c.setStrokeColor(colors.HexColor("#E2E8F0"))
    c.setLineWidth(1)
    c.setFillColor(colors.HexColor("#FAFAF9"))
    c.roundRect(x, y, w, h, 4, fill=1, stroke=1)

    # Número
    c.setFillColor(colors.HexColor("#C2410C"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(x + 8, y + h - 13, f"{q_num})")

    # Texto enunciado
    c.setFillColor(colors.HexColor("#1C1917"))
    c.setFont("Helvetica-Bold", 8)
    cur_y = y + h - 13
    for line in text_lines:
        c.drawString(x + 28, cur_y, line)
        cur_y -= 10.5

    # Opciones de alternativas
    if choices:
        c.setFont("Helvetica", 7.8)
        c.setFillColor(colors.HexColor("#334155"))
        cur_y -= 2
        for ch in choices:
            c.rect(x + 30, cur_y - 1.5, 7, 7, stroke=1, fill=0) # Casilla
            c.drawString(x + 42, cur_y, ch)
            cur_y -= 11.5


# =============================================================================
# PÁGINA 1: UBICACIÓN GEOGRÁFICA DE LOS GRIEGOS
# =============================================================================
def draw_page_1(c):
    draw_header(c, 1, 8, "Módulo 1: Ubicación Geográfica")
    draw_section_banner(c, 686, "I", "Ubicación Geográfica de los Griegos (5 ejercicios)")

    # Gráfico esquemático del mapa de Grecia
    c.setStrokeColor(colors.HexColor("#BAE6FD"))
    c.setLineWidth(1)
    c.setFillColor(colors.HexColor("#E0F2FE"))
    c.roundRect(36, 535, 540, 142, 6, fill=1, stroke=1)

    # Dibujo simplificado de la geografía
    # Península Balcánica
    c.setFillColor(colors.HexColor("#BBF7D0"))
    c.setStrokeColor(colors.HexColor("#16A34A"))
    c.setLineWidth(1.5)
    p = c.beginPath()
    p.moveTo(130, 665); p.lineTo(210, 665); p.lineTo(240, 620); p.lineTo(270, 595)
    p.lineTo(240, 560); p.lineTo(200, 570); p.lineTo(170, 610); p.close()
    c.drawPath(p, fill=1, stroke=1)

    # Peloponeso
    p2 = c.beginPath()
    p2.moveTo(210, 560); p2.lineTo(245, 555); p2.lineTo(255, 538); p2.lineTo(215, 538); p2.close()
    c.drawPath(p2, fill=1, stroke=1)

    # Creta
    c.rect(260, 542, 90, 8, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 6.8); c.setFillColor(colors.HexColor("#1E3A8A"))
    c.drawString(285, 544, "Isla de Creta")

    # Mares
    c.setFont("Helvetica-Bold", 8); c.setFillColor(colors.HexColor("#0284C7"))
    c.drawString(290, 625, "MAR EGEO")
    c.drawString(60, 610, "MAR JÓNICO")
    c.drawString(270, 555, "MAR MEDITERRÁNEO")

    # Etiquetas de tierra
    c.setFont("Helvetica-Bold", 8); c.setFillColor(colors.HexColor("#166534"))
    c.drawString(145, 645, "Península de los Balcanes")
    c.setFont("Helvetica-Bold", 7); c.setFillColor(colors.HexColor("#991B1B"))
    c.circle(245, 595, 2.5, fill=1, stroke=0); c.drawString(252, 593, "Atenas")
    c.circle(225, 550, 2.5, fill=1, stroke=0); c.drawString(185, 550, "Esparta")

    # Rótulo del mapa
    c.setFont("Helvetica-Oblique", 7.5); c.setFillColor(colors.HexColor("#475569"))
    c.drawString(45, 542, "Esquema: Península Balcánica, Mar Egeo, Mar Jónico, Isla de Creta y relieve montañoso.")

    # Ejercicios 1.1 al 1.5
    draw_q_box(c, 36, 435, 540, 92, "1.1", 
               ["¿En qué península del sur de Europa se ubicó principalmente la civilización griega?"],
               ["a) Península de los Balcanes.", 
                "b) Península Ibérica.", 
                "c) Península Itálica."])

    draw_q_box(c, 36, 335, 540, 92, "1.2", 
               ["Los griegos estaban rodeados por tres mares. Si navegaban hacia el este (oriente),",
                "¿qué mar surcaban entre la península griega y Asia Menor?"],
               ["a) Mar Egeo.", 
                "b) Mar Jónico.", 
                "c) Océano Atlántico."])

    draw_q_box(c, 36, 235, 540, 92, "1.3", 
               ["El relieve griego era sumamente montañoso, con valles estrechos e islas separadas.",
                "¿Qué gran consecuencia histórica tuvo esta geografía en su forma de organizarse?"],
               ["a) Dificultó la comunicación terrestre e impulsó que cada ciudad fuera independiente (polis).", 
                "b) Facilitó que existiera un solo rey para toda Grecia con un ejército unificado.", 
                "c) Provocó que los griegos no pudieran navegar en barcos."])

    draw_q_box(c, 36, 135, 540, 92, "1.4", 
               ["Al tener tantas costas recortadas, islas y valles cerrados por montañas,",
                "¿cuál fue la principal vía de comunicación, comercio y transporte de los griegos?"],
               ["a) El mar y la navegación en embarcaciones a vela y remos.", 
                "b) Grandes caminos de tierra planos para carretas tiradas por caballos.", 
                "c) Trenes y ferrocarriles de vapor entre valles."])

    draw_q_box(c, 36, 38, 540, 88, "1.5", 
               ["Al sur del Mar Egeo se encuentra la isla griega más grande, cuna de la civilización cretense o minoica.",
                "¿Cómo se llama esta importante isla?"],
               ["a) Isla de Creta.", 
                "b) Isla de Sicilia.", 
                "c) Isla de Pascua."])

    draw_footer(c, 1)


# =============================================================================
# PÁGINA 2: PARTES IMPORTANTES DE LA POLIS
# =============================================================================
def draw_page_2(c):
    draw_header(c, 2, 8, "Módulo 5: Partes de la Polis")
    draw_section_banner(c, 686, "V", "Partes Importantes de la Polis Griega (5 ejercicios)")

    # Esquema ilustrado de la Polis
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.setLineWidth(1)
    c.setFillColor(colors.HexColor("#F0FDF4"))
    c.roundRect(36, 535, 540, 142, 6, fill=1, stroke=1)

    # Colina de la Acrópolis
    c.setFillColor(colors.HexColor("#E2E8F0"))
    c.setStrokeColor(colors.HexColor("#64748B"))
    p = c.beginPath()
    p.moveTo(50, 545); p.lineTo(160, 655); p.lineTo(280, 655); p.lineTo(350, 545); p.close()
    c.drawPath(p, fill=1, stroke=1)

    # Templo en la cumbre
    c.setFillColor(colors.HexColor("#FFFBEB"))
    c.rect(190, 655, 60, 14, fill=1, stroke=1)
    p_roof = c.beginPath()
    p_roof.moveTo(185, 669)
    p_roof.lineTo(220, 680)
    p_roof.lineTo(255, 669)
    p_roof.close()
    c.drawPath(p_roof, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(colors.HexColor("#9A3412"))
    c.drawString(193, 658, "ACRÓPOLIS")

    # Ágora (plaza baja)
    c.setFillColor(colors.HexColor("#FEF3C7"))
    c.setStrokeColor(colors.HexColor("#D97706"))
    c.roundRect(350, 565, 90, 45, 4, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 8); c.setFillColor(colors.HexColor("#B45309"))
    c.drawString(372, 592, "ÁGORA")
    c.setFont("Helvetica", 6.8)
    c.drawString(358, 576, "(Plaza y Mercado)")

    # Teatro semicircular
    c.setStrokeColor(colors.HexColor("#475569"))
    c.arc(80, 560, 140, 620, 30, 90)
    c.arc(70, 550, 150, 630, 30, 90)
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(colors.HexColor("#334155"))
    c.drawString(100, 580, "TEATRO")

    # Puerto y mar
    c.setFillColor(colors.HexColor("#BAE6FD"))
    c.rect(460, 545, 105, 50, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 8); c.setFillColor(colors.HexColor("#0284C7"))
    c.drawString(485, 568, "PUERTO Y MAR")

    # Muralla
    c.setStrokeColor(colors.HexColor("#334155")); c.setLineWidth(2)
    c.line(45, 545, 45, 600); c.line(460, 545, 460, 600)
    c.setFont("Helvetica-Bold", 6.5); c.drawString(38, 605, "Muralla")

    # Preguntas 5.1 a 5.5
    draw_q_box(c, 36, 435, 540, 92, "5.1", 
               ["¿Qué era exactamente una **polis** en la antigua Grecia?"],
               ["a) Una ciudad-Estado independiente, con su propio gobierno, leyes, moneda y ejército.", 
                "b) Un templo sagrado construido con mármol en honor al dios del mar Poseidón.", 
                "c) Una fiesta olímpica donde los griegos competían en carreras y lanzamiento de disco."])

    draw_q_box(c, 36, 335, 540, 92, "5.2", 
               ["La zona más alta y fortificada de la colina, donde estaban los templos de los dioses",
                "y servía de refugio seguro en caso de ataques guerreros, se llamaba:"],
               ["a) Acrópolis.", 
                "b) Ágora.", 
                "c) Gineceo."])

    draw_q_box(c, 36, 235, 540, 92, "5.3", 
               ["La plaza pública en la parte baja, donde los ciudadanos comerciaban en el mercado,",
                "conversaban y discutían las leyes de la ciudad, se llamaba:"],
               ["a) Ágora.", 
                "b) Acrópolis.", 
                "c) Estadio olímpico."])

    draw_q_box(c, 36, 135, 540, 92, "5.4", 
               ["El recinto al aire libre edificado en la pendiente de un cerro con gradas semicirculares,",
                "diseñado con acústica perfecta para ver tragedias y comedias, era el:"],
               ["a) Teatro griego.", 
                "b) Puerto marítimo.", 
                "c) Andrón."])

    draw_q_box(c, 36, 38, 540, 88, "5.5", 
               ["¿Cuál era la función de las **murallas** y el **puerto** en una polis como Atenas?"],
               ["a) Las murallas protegían de invasiones y el puerto conectaba a la ciudad con el comercio marítimo.", 
                "b) Las murallas servían para hacer ejercicio y el puerto para criar peces en peceras.", 
                "c) Ambos lugares se usaban únicamente para realizar juicios a los extranjeros."])

    draw_footer(c, 2)


# =============================================================================
# PÁGINA 3: ORGANIZACIÓN SOCIAL Y LA FAMILIA GRIEGA
# =============================================================================
def draw_page_3(c):
    draw_header(c, 3, 8, "Módulos 2 y 7: Sociedad y Familia")
    
    # Sección 1: Sociedad (5 ejercicios)
    draw_section_banner(c, 686, "II", "Organización Social de los Griegos")

    draw_q_box(c, 36, 615, 540, 64, "2.1", 
               ["En una polis como Atenas, ¿quiénes eran considerados **ciudadanos** con plenos derechos políticos?"],
               ["a) Solo los hombres libres mayores de edad, nacidos de padre y madre atenienses.", 
                "b) Todas las personas que vivieran dentro de las murallas de la ciudad (hombres, mujeres y niños)."])

    draw_q_box(c, 36, 545, 540, 64, "2.2", 
               ["¿Qué grupo social carecía de libertad, era propiedad de otras personas y hacía los trabajos pesados?"],
               ["a) Los esclavos.", 
                "b) Los metecos (extranjeros libres)."])

    draw_q_box(c, 36, 475, 540, 64, "2.3", 
               ["Los extranjeros libres que vivían en Atenas, trabajaban en el comercio o artesanía y pagaban impuestos pero NO votaban eran:"],
               ["a) Los metecos.", 
                "b) Los ciudadanos atenienses."])

    draw_q_box(c, 36, 405, 540, 64, "2.4", 
               ["Las mujeres en la antigua Grecia: ¿Podían votar en la asamblea o ejercer cargos de gobierno?"],
               ["a) No, no tenían derechos políticos y estaban dedicadas al cuidado del hogar y la familia.", 
                "b) Sí, votaban junto a sus esposos en igualdad de condiciones."])

    draw_q_box(c, 36, 342, 540, 58, "2.5", 
               ["Aproximadamente, ¿qué parte de la población real tenía la condición de ciudadano con derecho a voto?"],
               ["a) Una minoría (menos del 20% de la población total).", 
                "b) La gran mayoría de todos los habitantes (más del 80%)."])

    # Sección 2: Familia (5 ejercicios)
    draw_section_banner(c, 314, "VII", "La Familia Griega y la Vida en el Hogar")

    draw_q_box(c, 36, 252, 540, 56, "7.1", 
               ["La familia, su casa, tierras, esclavos y bienes materiales formaban una unidad básica llamada:"],
               ["a) El Oikos.", 
                "b) La Polis."])

    draw_q_box(c, 36, 192, 540, 56, "7.2", 
               ["¿Quién ejercía la máxima autoridad legal en la familia y representaba a todos ante la sociedad?"],
               ["a) El padre de familia (kyrios o cabeza de hogar).", 
                "b) El hijo mayor menor de edad."])

    draw_q_box(c, 36, 132, 540, 56, "7.3", 
               ["La habitación de la casa reservada exclusivamente para las mujeres, donde cuidaban a los niños y tejían, era el:"],
               ["a) Gineceo.", 
                "b) Andrón (sala para banquetes de hombres)."])

    draw_q_box(c, 36, 72, 540, 56, "7.4", 
               ["¿Qué aprendían principalmente las **niñas** en su casa durante su infancia?"],
               ["a) Labores del hogar (hilar lana, tejer ropa, cocinar y administrar la casa junto a su madre).", 
                "b) A pelear con lanzas y navegar barcos de guerra."])

    draw_q_box(c, 36, 36, 540, 32, "7.5", 
               ["En Atenas, el esclavo de confianza que acompañaba al niño a la escuela y cuidaba su conducta se llamaba:"],
               ["a) Pedagogo.       b) Hoplita.       c) Sacerdote."])

    draw_footer(c, 3)


# =============================================================================
# PÁGINA 4: ALIMENTACIÓN GRIEGA Y LA TRÍADA MEDITERRÁNEA
# =============================================================================
def draw_page_4(c):
    draw_header(c, 4, 8, "Módulo 6: Alimentación Griega")
    draw_section_banner(c, 686, "VI", "Alimentación Griega y la Tríada Mediterránea (5 ejercicios)")

    # Ilustración vectorial de la tríada
    c.setStrokeColor(colors.HexColor("#FED7AA"))
    c.setFillColor(colors.HexColor("#FFF7ED"))
    c.roundRect(36, 555, 540, 122, 6, fill=1, stroke=1)

    # 1. Trigo
    c.setFont("Helvetica-Bold", 8.5); c.setFillColor(colors.HexColor("#9A3412"))
    c.drawString(60, 655, "1. EL TRIGO")
    c.setFillColor(colors.HexColor("#FBBF24"))
    c.circle(85, 615, 14, fill=1, stroke=1)
    c.setFont("Helvetica", 7.5); c.setFillColor(colors.HexColor("#451A03"))
    c.drawString(55, 592, "Base del pan, gachas")
    c.drawString(60, 582, "y harinas diarias.")

    # 2. Olivo
    c.setFont("Helvetica-Bold", 8.5); c.setFillColor(colors.HexColor("#3F6212"))
    c.drawString(245, 655, "2. EL OLIVO")
    c.setFillColor(colors.HexColor("#65A30D"))
    c.circle(270, 615, 14, fill=1, stroke=1)
    c.setFont("Helvetica", 7.5); c.setFillColor(colors.HexColor("#1A2E05"))
    c.drawString(235, 592, "Aceitunas y aceite para")
    c.drawString(240, 582, "cocinar e iluminar.")

    # 3. Vid
    c.setFont("Helvetica-Bold", 8.5); c.setFillColor(colors.HexColor("#581C87"))
    c.drawString(435, 655, "3. LA VID")
    c.setFillColor(colors.HexColor("#9333EA"))
    c.circle(460, 615, 14, fill=1, stroke=1)
    c.setFont("Helvetica", 7.5); c.setFillColor(colors.HexColor("#3B0764"))
    c.drawString(428, 592, "Uvas frescas, pasas")
    c.drawString(432, 582, "y vino con agua.")

    # Preguntas 6.1 al 6.5
    draw_q_box(c, 36, 450, 540, 92, "6.1", 
               ["La base fundamental de la alimentación en la antigua Grecia fue la **Tríada Mediterránea**.",
                "¿Cuáles eran los tres cultivos que la componían?"],
               ["a) El Trigo (para hacer pan), el Olivo (para aceite y aceitunas) y la Vid (para uvas y vino).", 
                "b) El Maíz, las papas y los porotos negros.", 
                "c) El Arroz blanco, la carne de vacuno y la leche de vaca pasteurizada."])

    draw_q_box(c, 36, 345, 540, 95, "6.2", 
               ["Debido a que Grecia tenía muchísimas costas y terrenos montañosos ideales para cabras,",
                "¿qué otros alimentos complementaban a diario la dieta griega?"],
               ["a) Pescados frescos y secos, mariscos, queso de cabra y queso de oveja.", 
                "b) Hamburguesas de carne de res y bebidas con gas.", 
                "c) Salmón de río gigante y mantequilla dulce importada."])

    draw_q_box(c, 36, 245, 540, 92, "6.3", 
               ["¿Con qué frecuencia consumía **carne roja** una familia griega común y corriente?"],
               ["a) Rara vez; era un alimento muy costoso que se comía casi solo en sacrificios y fiestas religiosas.", 
                "b) Todos los días en el almuerzo y en la cena.", 
                "c) Nunca, porque en Grecia estaba prohibido por ley criar animales."])

    draw_q_box(c, 36, 145, 540, 92, "6.4", 
               ["Como los griegos no conocían el azúcar refinada moderna,",
                "¿qué productos naturales utilizaban para endulzar sus preparaciones y postres?"],
               ["a) La miel de abejas y frutas deshidratadas como los higos secos.", 
                "b) Endulzantes químicos en tabletas.", 
                "c) Azúcar blanca traída del supermercado."])

    draw_q_box(c, 36, 45, 540, 92, "6.5", 
               ["En la zona central de Chile tenemos un clima templado mediterráneo muy parecido al de Grecia.",
                "¿Qué productos de la tríada mediterránea griega cultivamos y consumimos con gran éxito hoy en Chile?"],
               ["a) Uvas (para vino y mesa), aceitunas (para aceite de oliva) y trigo (para harina y pan).", 
                "b) Plátanos tropicales, piñas y café en grano.", 
                "c) Cacao para hacer chocolate y té negro."])

    draw_footer(c, 4)


# =============================================================================
# PÁGINA 5: DIFERENCIAS ENTRE ESPARTA Y ATENAS
# =============================================================================
def draw_page_5(c):
    draw_header(c, 5, 8, "Módulo 4: Atenas vs Esparta")
    draw_section_banner(c, 686, "IV", "Diferencias entre Esparta y Atenas (5 ejercicios)")

    # Cuadro comparativo gráfico
    c.setStrokeColor(colors.HexColor("#BFDBFE"))
    c.setFillColor(colors.HexColor("#EFF6FF"))
    c.roundRect(36, 560, 260, 118, 6, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 9); c.setFillColor(colors.HexColor("#1E3A8A"))
    c.drawString(48, 660, "🏛️ ATENAS: LA CIUDAD DE LAS ARTES")
    c.setFont("Helvetica", 7.5); c.setFillColor(colors.HexColor("#1E293B"))
    c.drawString(48, 642, "• Cuna de la democracia y asamblea ciudadana.")
    c.drawString(48, 628, "• Foco en la educación: leer, escribir, filosofía y música.")
    c.drawString(48, 614, "• Gran potencia marítima y comercial por el mar Egeo.")
    c.drawString(48, 600, "• Las mujeres administraban el hogar sin salir solas.")

    c.setStrokeColor(colors.HexColor("#FECACA"))
    c.setFillColor(colors.HexColor("#FEF2F2"))
    c.roundRect(316, 560, 260, 118, 6, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 9); c.setFillColor(colors.HexColor("#991B1B"))
    c.drawString(328, 660, "⚔️ ESPARTA: LA CIUDAD GUERRERA")
    c.setFont("Helvetica", 7.5); c.setFillColor(colors.HexColor("#1E293B"))
    c.drawString(328, 642, "• Gobierno de pocos ancianos y dos reyes (oligarquía).")
    c.drawString(328, 628, "• Foco en el ejército, disciplina de hierro y valentía.")
    c.drawString(328, 614, "• Niños al Estado desde los 7 años para entrenamiento.")
    c.drawString(328, 600, "• Mujeres con libertad física y gimnasia para tener hijos fuertes.")

    # Preguntas 4.1 a 4.5
    draw_q_box(c, 36, 455, 540, 95, "4.1", 
               ["¿Cuál era el valor central y el propósito de la vida en la polis de **Esparta**?"],
               ["a) La preparación militar, la valentía en el combate y la obediencia estricta a las leyes.", 
                "b) La creación de grandes poesías, cuadros de pintura y viajes comerciales en barco.", 
                "c) El cultivo de jardines botánicos y el descanso familiar."])

    draw_q_box(c, 36, 350, 540, 95, "4.2", 
               ["¿Cuál fue el gran orgullo y legado político que distinguió a la polis de **Atenas** en el mundo?"],
               ["a) La invención de la Democracia, permitiendo que los ciudadanos debatieran y votaran las leyes.", 
                "b) Tener un emperador con corona dorada que tomaba todas las decisiones sin consultar.", 
                "c) La prohibición total de aprender a leer y escribir."])

    draw_q_box(c, 36, 245, 540, 95, "4.3", 
               ["Al cumplir 7 años, la vida de un niño espartano cambiaba por completo. ¿Qué ocurría con él?"],
               ["a) Dejaba su hogar familiar y pasaba a manos del Estado para recibir un duro entrenamiento militar.", 
                "b) Entraba a estudiar medicina y astronomía a la universidad.", 
                "c) Se convertía de inmediato en comerciante de trigo en el mercado."])

    draw_q_box(c, 36, 140, 540, 95, "4.4", 
               ["¿Cómo era la educación de los niños atenienses de familias libres?"],
               ["a) Iban a la escuela acompañados de un pedagogo para aprender a leer, escribir, música y gimnasia.", 
                "b) Solo se les enseñaba a luchar con espadas y lanzas, prohibiendo los libros y el canto.", 
                "c) No tenían maestros y se educaban únicamente en la navegación marina."])

    draw_q_box(c, 36, 40, 540, 90, "4.5", 
               ["¿Qué diferencia tenían las **mujeres espartanas** en comparación con las mujeres atenienses?"],
               ["a) Las espartanas tenían mayor libertad física, practicaban deportes al aire libre y administraban bienes.", 
                "b) Las mujeres espartanas eran las únicas que votaban en la asamblea de Grecia.", 
                "c) Las mujeres espartanas eran vendidas como esclavas al cumplir 15 años."])

    draw_footer(c, 5)


# =============================================================================
# PÁGINA 6: CONCEPTO DE DEMOCRACIA
# =============================================================================
def draw_page_6(c):
    draw_header(c, 6, 8, "Módulo 8: Concepto de Democracia")
    draw_section_banner(c, 686, "VIII", "Concepto de Democracia y Comparación con Chile (5 ejercicios)")

    # Esquema etimológico
    c.setStrokeColor(colors.HexColor("#FED7AA"))
    c.setFillColor(colors.HexColor("#FFFBEB"))
    c.roundRect(36, 565, 540, 112, 6, fill=1, stroke=1)

    c.setFont("Helvetica-Bold", 10.5); c.setFillColor(colors.HexColor("#9A3412"))
    c.drawCentredString(306, 655, "ORIGEN DE LA PALABRA: DEMOCRACIA")

    c.setFillColor(colors.HexColor("#C2410C"))
    c.roundRect(80, 595, 180, 42, 4, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 9.5)
    c.drawCentredString(170, 620, "DEMOS = PUEBLO")
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(170, 605, "(La comunidad de ciudadanos)")

    c.setFont("Helvetica-Bold", 14); c.setFillColor(colors.HexColor("#78350F"))
    c.drawString(285, 615, "+")

    c.setFillColor(colors.HexColor("#B45309"))
    c.roundRect(320, 595, 180, 42, 4, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 9.5)
    c.drawCentredString(410, 620, "KRATOS = PODER O GOBIERNO")
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(410, 605, "(La capacidad de tomar decisiones)")

    c.setFont("Helvetica-Bold", 8.5); c.setFillColor(colors.HexColor("#166534"))
    c.drawCentredString(306, 575, "= \"EL GOBIERNO DEL PUEBLO\" (Nacido en Atenas, siglo V a.C.)")

    # Preguntas 8.1 a 8.5
    draw_q_box(c, 36, 455, 540, 95, "8.1", 
               ["A partir de las raíces griegas *Demos* y *Kratos*, ¿cuál es el significado etimológico de **Democracia**?"],
               ["a) El gobierno o poder que ejerce el pueblo de forma colectiva.", 
                "b) La fuerza militar de los reyes y emperadores.", 
                "c) El poder que tienen los comerciantes con más dinero."])

    draw_q_box(c, 36, 350, 540, 95, "8.2", 
               ["En Atenas, los ciudadanos se reunían en una gran asamblea llamada la **Ecclesia**.",
                "¿Cómo votaban habitualmente las leyes y decisiones que afectaban a la polis?"],
               ["a) A mano alzada (levantando la mano al aire libre en la colina Pnyx).", 
                "b) Mediante votaciones secretas por computadores.", 
                "c) El rey decidía por su cuenta y los demás solo obedecían."])

    draw_q_box(c, 36, 245, 540, 95, "8.3", 
               ["¿Por qué decimos que la democracia ateniense era una **democracia directa**?"],
               ["a) Porque los propios ciudadanos votaban directamente las leyes, sin necesidad de diputados intermediarios.", 
                "b) Porque se votaba caminando en línea recta hacia el mar.", 
                "c) Porque solo se podía votar una vez en toda la vida."])

    draw_q_box(c, 36, 140, 540, 95, "8.4", 
               ["¿Por qué la democracia ateniense era **limitada y excluyente** según nuestros criterios actuales?"],
               ["a) Porque excluía de la política a las mujeres, a los esclavos y a los extranjeros (metecos).", 
                "b) Porque los niños recién nacidos estaban obligados a votar.", 
                "c) Porque solo se permitía votar a quienes tuvieran más de 90 años."])

    draw_q_box(c, 36, 40, 540, 90, "8.5", 
               ["Comparación con Chile: ¿Cuál es la gran diferencia entre la democracia ateniense y la **democracia chilena actual**?"],
               ["a) En Chile hoy el voto es universal (votan hombres y mujeres mayores de 18 años) y elegimos representantes.", 
                "b) En Chile hoy solo votan los hombres ricos dueños de tierras.", 
                "c) Son exactamente iguales y no ha cambiado ninguna regla en 2.500 años."])

    draw_footer(c, 6)


# =============================================================================
# PÁGINA 7: RELIGIÓN Y LEGADO CULTURAL GRIEGO
# =============================================================================
def draw_page_7(c):
    draw_header(c, 7, 8, "Módulos 3 y 9: Religión y Legado")

    # Módulo 3: Religión (5 ejercicios)
    draw_section_banner(c, 686, "III", "Religión y Dioses del Olimpo")

    draw_q_box(c, 36, 615, 540, 64, "3.1", 
               ["Los griegos creían en la existencia de muchos dioses diferentes. ¿Cómo se llama esta creencia religiosa?"],
               ["a) Politeísmo (creencia en muchos dioses).", 
                "b) Monoteísmo (creencia en un solo Dios)."])

    draw_q_box(c, 36, 545, 540, 64, "3.2", 
               ["¿Dónde creían los griegos que vivían los 12 dioses principales de su panteón?"],
               ["a) En la cumbre más alta de Grecia: el Monte Olimpo.", 
                "b) En el fondo del mar Egeo dentro de una concha marina."])

    draw_q_box(c, 36, 475, 540, 64, "3.3", 
               ["¿Quién era el rey supremo de todos los dioses griegos, señor del cielo y lanzador del rayo?"],
               ["a) Zeus.", 
                "b) Poseidón."])

    draw_q_box(c, 36, 405, 540, 64, "3.4", 
               ["Diosa de la sabiduría, de la justicia y de la estrategia, protectora de la ciudad de Atenas:"],
               ["a) Atenea.", 
                "b) Afrodita (diosa de la belleza)."])

    draw_q_box(c, 36, 342, 540, 58, "3.5", 
               ["¿Qué dios gobernaba los mares y provocaba tempestades y terremotos con su tridente de tres puntas?"],
               ["a) Poseidón.", 
                "b) Ares (dios de la guerra sangrienta)."])

    # Módulo 9: Legado Cultural (5 ejercicios)
    draw_section_banner(c, 314, "IX", "El Gran Legado Cultural Griego")

    draw_q_box(c, 36, 252, 540, 56, "9.1", 
               ["Los actores griegos usaban máscaras para representar los dos grandes géneros del teatro antiguo:"],
               ["a) La Tragedia (historias tristes) y la Comedia (historias alegres y divertidas).", 
                "b) La Telenovela y el Cine de acción moderno."])

    draw_q_box(c, 36, 192, 540, 56, "9.2", 
               ["Cada 4 años, deportistas de todas las polis se reunían en Olimpia para competir en paz. Esto dio origen a:"],
               ["a) Los Juegos Olímpicos modernos.", 
                "b) La Copa Mundial de Fútbol."])

    draw_q_box(c, 36, 132, 540, 56, "9.3", 
               ["En la arquitectura griega, ¿cuál de los tres órdenes de columnas tiene volutas en espiral (como cuernos de carnero)?"],
               ["a) El Orden Jónico.", 
                "b) El Orden Dórico (capitel liso y sobrio)."])

    draw_q_box(c, 36, 72, 540, 56, "9.4", 
               ["¿Cuál de estas parejas de palabras que usamos habitualmente en español proviene del idioma griego?"],
               ["a) Geografía (descripción de la Tierra) y Democracia (gobierno del pueblo).", 
                "b) Jeans y Smartphone."])

    draw_q_box(c, 36, 36, 540, 32, "9.5", 
               ["La Filosofía (\"amor a la sabiduría\") nació en Grecia. ¿Qué buscaban pensadores como Sócrates y Platón?"],
               ["a) Explicar el mundo mediante la razón, la lógica y las preguntas.       b) Hacer trucos de magia."])

    draw_footer(c, 7)


# =============================================================================
# PÁGINA 8: SOLUCIONARIO PEDAGÓGICO COMPLETO
# =============================================================================
def draw_page_8(c):
    draw_header(c, 8, 8, "Solucionario Pedagógico")
    draw_section_banner(c, 686, "★", "Solucionario Oficial y Pauta de Corrección (45 ejercicios)")

    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.roundRect(36, 40, 540, 636, 6, fill=1, stroke=1)

    soluciones = [
        ("I. Ubicación Geográfica", [
            "1.1) a - Península de los Balcanes.",
            "1.2) a - Mar Egeo (al oriente/este).",
            "1.3) a - Dificultó la comunicación terrestre y facilitó ciudades independientes (polis).",
            "1.4) a - El mar y la navegación en barcos a vela y remos.",
            "1.5) a - Isla de Creta (al sur del Mar Egeo)."
        ]),
        ("V. Partes de la Polis", [
            "5.1) a - Ciudad-Estado independiente con sus propias leyes, gobierno y ejército.",
            "5.2) a - Acrópolis (zona alta sagrada con templos y refugio seguro).",
            "5.3) a - Ágora (plaza pública, centro comercial, social y político).",
            "5.4) a - Teatro griego (construido al aire libre en la ladera de la colina).",
            "5.5) a - Murallas protegían la ciudad y el puerto la conectaba al mar."
        ]),
        ("II. Organización Social", [
            "2.1) a - Solo hombres libres mayores de edad nacidos de padres atenienses.",
            "2.2) a - Los esclavos (sin libertad, propiedad de amos o del Estado).",
            "2.3) a - Los metecos (extranjeros libres comerciantes sin derecho a voto).",
            "2.4) a - No; las mujeres no tenían derechos políticos.",
            "2.5) a - Una minoría (menos del 20% de la población total)."
        ]),
        ("VII. La Familia Griega", [
            "7.1) a - El Oikos (hogar, familia y todos sus bienes).",
            "7.2) a - El padre de familia (cabeza del hogar / kyrios).",
            "7.3) a - Gineceo (habitación exclusiva de las mujeres).",
            "7.4) a - Labores del hogar (hilar, tejer, cocinar y administrar la casa).",
            "7.5) a - Pedagogo (esclavo educado que acompañaba y cuidaba al niño)."
        ]),
        ("VI. Alimentación Griega", [
            "6.1) a - Trigo (pan), Olivo (aceite) y Vid (uvas y vino) = Tríada Mediterránea.",
            "6.2) a - Pescados, mariscos, queso de cabra y de oveja.",
            "6.3) a - Rara vez; alimento costoso reservado para fiestas religiosas.",
            "6.4) a - La miel de abejas y frutas secas como los higos.",
            "6.5) a - Uvas, aceitunas y trigo (clima mediterráneo chileno)."
        ]),
        ("IV. Diferencia Esparta y Atenas", [
            "4.1) a - Formar soldados disciplinados, valientes y obedientes al ejército.",
            "4.2) a - La invención de la Democracia y el debate ciudadano.",
            "4.3) a - Pasaba al Estado para recibir un riguroso entrenamiento militar.",
            "4.4) a - Leer, escribir, poesía, música con flauta/lira y gimnasia.",
            "4.5) a - Mayor libertad física, deportes al aire libre y administración."
        ]),
        ("VIII. Concepto de Democracia", [
            "8.1) a - Demos (pueblo) + Kratos (poder/gobierno) = El gobierno del pueblo.",
            "8.2) a - A mano alzada (levantando la mano en la colina Pnyx).",
            "8.3) a - Los propios ciudadanos votaban directamente las leyes.",
            "8.4) a - Excluía a mujeres, esclavos y extranjeros.",
            "8.5) a - En Chile hoy el voto es universal (mujeres y hombres) y representativo."
        ]),
        ("III. Religión y IX. Legado Cultural", [
            "3.1) a - Politeísmo (muchos dioses) | 3.2) a - Monte Olimpo | 3.3) a - Zeus.",
            "3.4) a - Atenea (sabiduría y justicia) | 3.5) a - Poseidón (dios del mar).",
            "9.1) a - Tragedia y Comedia con uso de máscaras teatrales.",
            "9.2) a - Los Juegos Olímpicos modernos (celebrados en Olimpia cada 4 años).",
            "9.3) a - Orden Jónico (con volutas en espiral). Dórico (liso), Corintio (hojas).",
            "9.4) a - Geografía y Democracia (origen griego directo).",
            "9.5) a - Explicar el mundo mediante la razón, la lógica y las preguntas."
        ])
    ]

    cur_y = 660
    for titulo, items in soluciones:
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(colors.HexColor("#C2410C"))
        c.drawString(48, cur_y, f"• {titulo.upper()}")
        cur_y -= 11.5

        c.setFont("Helvetica", 7.2)
        c.setFillColor(colors.HexColor("#1E293B"))
        for it in items:
            c.drawString(56, cur_y, it)
            cur_y -= 9.5
        cur_y -= 4

    draw_footer(c, 8)


def main():
    pdf_path = "/Users/familia_bustos_estrada/Maxi/guia_estudio_historia.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    
    print("Generando Página 1: Ubicación Geográfica...")
    draw_page_1(c); c.showPage()

    print("Generando Página 2: Partes de la Polis...")
    draw_page_2(c); c.showPage()

    print("Generando Página 3: Organización Social y Familia...")
    draw_page_3(c); c.showPage()

    print("Generando Página 4: Alimentación Griega...")
    draw_page_4(c); c.showPage()

    print("Generando Página 5: Atenas vs Esparta...")
    draw_page_5(c); c.showPage()

    print("Generando Página 6: Concepto de Democracia...")
    draw_page_6(c); c.showPage()

    print("Generando Página 7: Religión y Legado Cultural...")
    draw_page_7(c); c.showPage()

    print("Generando Página 8: Solucionario Pedagógico...")
    draw_page_8(c); c.showPage()

    c.save()
    print(f"PDF generado con éxito en: {pdf_path}")

if __name__ == "__main__":
    main()

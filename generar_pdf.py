import math
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def draw_clock(c, center_x, center_y, radius, hour, minute):
    """Reloj analógico vectorial exacto sin números de pista."""
    c.setStrokeColor(colors.HexColor("#2563EB"))
    c.setLineWidth(2)
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.circle(center_x, center_y, radius, stroke=1, fill=1)
    
    c.setStrokeColor(colors.HexColor("#DBEAFE"))
    c.setLineWidth(0.7)
    c.circle(center_x, center_y, radius - 3.5, stroke=1, fill=0)

    c.setFillColor(colors.HexColor("#1E293B"))
    c.setFont("Helvetica-Bold", 6.8)
    for num in range(1, 13):
        angle = math.radians(90 - num * 30)
        num_r = radius - 8
        nx = center_x + num_r * math.cos(angle)
        ny = center_y + num_r * math.sin(angle) - 2.5
        c.drawCentredString(nx, ny, str(num))

    c.setFillColor(colors.HexColor("#0F172A"))
    c.circle(center_x, center_y, 2.5, stroke=0, fill=1)

    # Minutos (azul)
    min_angle = math.radians(90 - minute * 6)
    mx = center_x + (radius - 6) * math.cos(min_angle)
    my = center_y + (radius - 6) * math.sin(min_angle)
    c.setStrokeColor(colors.HexColor("#0284C7"))
    c.setLineWidth(1.8)
    c.line(center_x, center_y, mx, my)

    # Horas (rojo)
    hour_angle = math.radians(90 - ((hour % 12) + minute / 60.0) * 30)
    hx = center_x + (radius * 0.54) * math.cos(hour_angle)
    hy = center_y + (radius * 0.54) * math.sin(hour_angle)
    c.setStrokeColor(colors.HexColor("#DC2626"))
    c.setLineWidth(2.5)
    c.line(center_x, center_y, hx, hy)


def draw_header(c, title, subtitle, page_num, total_pages=8):
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.setLineWidth(1)
    c.roundRect(36, 720, 540, 56, 7, fill=1, stroke=1)

    c.setFillColor(colors.HexColor("#1E3A8A"))
    c.setFont("Helvetica-Bold", 11.5)
    c.drawString(48, 756, title)

    c.setFillColor(colors.HexColor("#475569"))
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(48, 742, subtitle)

    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor("#334155"))
    c.drawString(48, 727, "Alumna: Amelia Bustos")
    c.drawString(200, 727, "Curso: 3° Básico A")
    c.drawString(320, 727, "Fecha: ___ / ___ / 2026")
    c.drawString(450, 727, "Puntaje: ____ / 80 pts")

    c.setFont("Helvetica", 7.5)
    c.setFillColor(colors.HexColor("#94A3B8"))
    c.drawRightString(576, 14, f"Página {page_num} de {total_pages} • Guía Oficial de Estudio Matemáticas 3° Básico")


def draw_section_banner(c, y, text, color_hex="#3B82F6"):
    c.setFillColor(colors.HexColor(color_hex))
    c.roundRect(36, y, 540, 18, 4, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(44, y + 5, text)


def draw_cdu_box(c, x, y, width, height, op_type, num1, num2, has_reserva=False):
    c.setFillColor(colors.HexColor("#FFFFFF"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.setLineWidth(1)
    c.roundRect(x, y, width, height, 5, fill=1, stroke=1)

    cell_w = 17
    cell_h = 14
    start_x = x + width - 3 * cell_w - 8
    top_y = y + height - 18

    headers = ["C", "D", "U"]
    for i, h in enumerate(headers):
        c.setFillColor(colors.HexColor("#F1F5F9"))
        c.setStrokeColor(colors.HexColor("#94A3B8"))
        c.setLineWidth(0.6)
        c.rect(start_x + i * cell_w, top_y, cell_w, cell_h, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#334155"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(start_x + i * cell_w + cell_w/2, top_y + 3.5, h)

    curr_y = top_y - cell_h
    if has_reserva:
        for i in range(3):
            c.setFillColor(colors.HexColor("#FFFBEB"))
            c.setStrokeColor(colors.HexColor("#F59E0B"))
            c.setLineWidth(0.6)
            c.rect(start_x + i * cell_w, curr_y, cell_w, cell_h - 2, fill=1, stroke=1)
        curr_y -= (cell_h - 2)

    s_num1 = str(num1).rjust(3)
    for i, digit in enumerate(s_num1):
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.rect(start_x + i * cell_w, curr_y, cell_w, cell_h, fill=1, stroke=1)
        if digit != ' ':
            c.setFillColor(colors.HexColor("#0F172A"))
            c.setFont("Courier-Bold", 10)
            c.drawCentredString(start_x + i * cell_w + cell_w/2, curr_y + 3, digit)
    curr_y -= cell_h

    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(colors.HexColor("#DC2626") if op_type == "-" else colors.HexColor("#2563EB"))
    c.drawCentredString(start_x - 8, curr_y + 2.5, op_type)

    s_num2 = str(num2).rjust(3)
    for i, digit in enumerate(s_num2):
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.rect(start_x + i * cell_w, curr_y, cell_w, cell_h, fill=1, stroke=1)
        if digit != ' ':
            c.setFillColor(colors.HexColor("#0F172A"))
            c.setFont("Courier-Bold", 10)
            c.drawCentredString(start_x + i * cell_w + cell_w/2, curr_y + 3, digit)
    curr_y -= 3

    c.setStrokeColor(colors.HexColor("#0F172A"))
    c.setLineWidth(1.4)
    c.line(start_x - 9, curr_y, start_x + 3 * cell_w, curr_y)
    curr_y -= cell_h + 2

    for i in range(3):
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.setLineWidth(0.8)
        c.rect(start_x + i * cell_w, curr_y, cell_w, cell_h + 2, fill=1, stroke=1)


def generate_mega_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # =========================================================================
    # PÁGINA 1: OPERATORIA Y NUMERACIÓN (PARTE A: ANTECESOR, PALABRAS, SUMAS)
    # =========================================================================
    draw_header(c, "✏️ GUÍA OFICIAL DE MATEMÁTICAS — 3° BÁSICO", "Módulo 1: Numeración y Operatoria Vertical (Parte 1)", 1, 8)

    # I. Antecesor y Sucesor (5 ejercicios)
    draw_section_banner(c, 692, "🔢 I. ANTECESOR Y SUCESOR (5 EJERCICIOS)", "#2563EB")
    nums_ant = [600, 499, 820, 700, 350]
    y_ant = 638
    b_w = 100
    for idx, n in enumerate(nums_ant):
        bx = 36 + idx * 109
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.roundRect(bx, y_ant, b_w, 48, 5, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#1D4ED8"))
        c.setFont("Helvetica-Bold", 7)
        c.drawString(bx + 6, y_ant + 36, f"1.{idx+1}")
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(colors.HexColor("#0F172A"))
        c.drawCentredString(bx + b_w/2, y_ant + 18, f"___ < {n} < ___")

    # II. Escritura en Palabras (5 ejercicios)
    draw_section_banner(c, 610, "✍️ II. ESCRITURA DE NÚMEROS EN PALABRAS (5 EJERCICIOS)", "#4F46E5")
    nums_words = [753, 608, 942, 516, 870]
    y_w = 582
    for idx, nw in enumerate(nums_words):
        yw_curr = y_w - idx * 24
        c.setFillColor(colors.HexColor("#1E3A8A"))
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(42, yw_curr, f"2.{idx+1}) Número {nw}:")
        c.setStrokeColor(colors.HexColor("#94A3B8"))
        c.setLineWidth(0.8)
        c.line(130, yw_curr, 560, yw_curr)

    # III. Sumas Verticales (5 ejercicios: 2 sin reserva, 3 con reserva)
    draw_section_banner(c, 452, "➕ III. SUMAS VERTICALES CON Y SIN RESERVA (5 EJERCICIOS)", "#059669")
    sumas = [
        (342, 154, False, "3.1 Directa"),
        (523, 261, False, "3.2 Directa"),
        (586, 247, True, "3.3 Con reserva"),
        (479, 385, True, "3.4 Con reserva"),
        (658, 196, True, "3.5 Con reserva")
    ]
    y_sum = 352
    for idx, (n1, n2, res, lbl) in enumerate(sumas):
        bx = 36 + idx * 109
        draw_cdu_box(c, bx, y_sum, 102, 92, "+", n1, n2, has_reserva=res)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.setFont("Helvetica-Bold", 7)
        c.drawString(bx + 4, y_sum + 80, lbl)

    # IV. Restas Verticales (5 ejercicios: 2 sin canje, 3 con canje)
    draw_section_banner(c, 324, "➖ IV. RESTAS VERTICALES CON Y SIN CANJE (5 EJERCICIOS)", "#DC2626")
    restas = [
        (785, 341, False, "4.1 Directa"),
        (964, 523, False, "4.2 Directa"),
        (600, 238, True, "4.3 Con canje"),
        (800, 456, True, "4.4 Con canje"),
        (742, 385, True, "4.5 Con canje")
    ]
    y_res = 224
    for idx, (n1, n2, can, lbl) in enumerate(restas):
        bx = 36 + idx * 109
        draw_cdu_box(c, bx, y_res, 102, 92, "-", n1, n2, has_reserva=can)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.setFont("Helvetica-Bold", 7)
        c.drawString(bx + 4, y_res + 80, lbl)

    # V. Multiplicaciones Verticales (5 ejercicios)
    draw_section_banner(c, 196, "✖️ V. MULTIPLICACIONES (5 EJERCICIOS)", "#D97706")
    mults = [(32, 3), (41, 2), (24, 2), (13, 3), (23, 3)]
    y_m = 136
    for idx, (m1, m2) in enumerate(mults):
        bx = 36 + idx * 109
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.roundRect(bx, y_m, 102, 52, 5, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#B45309"))
        c.setFont("Helvetica-Bold", 7)
        c.drawString(bx + 6, y_m + 38, f"5.{idx+1}")
        c.setFont("Courier-Bold", 10.5)
        c.setFillColor(colors.HexColor("#0F172A"))
        c.drawCentredString(bx + 51, y_m + 18, f"{m1} x {m2} = [___]")

    c.showPage()

    # =========================================================================
    # PÁGINA 2: PROBLEMAS DE APLICACIÓN (5 PROBLEMAS FORMATO CUADERNO)
    # =========================================================================
    draw_header(c, "📖 PROBLEMAS DE APLICACIÓN (FORMATO CUADERNO)", "Módulo 1: Razonamiento, Datos, Operación y Respuesta Completa", 2, 8)

    draw_section_banner(c, 692, "📝 RESUELVE EN FORMATO CUADERNO (5 PROBLEMAS)", "#059669")

    problemas = [
        ("6.1", "“Martina compró 4 cajas con 5 lápices cada una. ¿Cuántos lápices tiene en total?”"),
        ("6.2", "“Joaquín tiene 3 paquetes con 6 galletas cada uno. ¿Cuántas galletas tiene en total?”"),
        ("6.3", "“En una biblioteca hay 450 libros y llegan 235 libros nuevos. ¿Cuántos libros hay en total?”"),
        ("6.4", "“Matías tenía $800 pesos y compró un helado de $350 pesos. ¿Cuánto dinero le sobró?”"),
        ("6.5", "“En un jardín infantil hay 5 mesas y en cada mesa se sientan 4 niños. ¿Cuántos niños hay sentados?”")
    ]

    y_pb = 604
    for num, enunc in problemas:
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.roundRect(36, y_pb, 540, 80, 5, fill=1, stroke=1)

        c.setFillColor(colors.HexColor("#FDF2F8"))
        c.roundRect(42, y_pb + 56, 528, 18, 3, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#9D174D"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(48, y_pb + 62, f"{num})")
        c.setFont("Helvetica", 7.5)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawString(72, y_pb + 62, enunc)

        # 3 columnas
        col_w = 170
        # Datos
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.roundRect(42, y_pb + 8, col_w, 44, 3, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#475569"))
        c.setFont("Helvetica-Bold", 7)
        c.drawString(48, y_pb + 40, "DATOS:")
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.line(48, y_pb + 26, 42 + col_w - 6, y_pb + 26)
        c.line(48, y_pb + 14, 42 + col_w - 6, y_pb + 14)

        # Operación
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.roundRect(218, y_pb + 8, col_w, 44, 3, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#475569"))
        c.setFont("Helvetica-Bold", 7)
        c.drawString(224, y_pb + 40, "OPERACIÓN:")
        c.line(224, y_pb + 26, 218 + col_w - 6, y_pb + 26)
        c.line(224, y_pb + 14, 218 + col_w - 6, y_pb + 14)

        # Respuesta
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.roundRect(394, y_pb + 8, col_w + 6, 44, 3, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#475569"))
        c.setFont("Helvetica-Bold", 7)
        c.drawString(400, y_pb + 40, "RESPUESTA COMPLETA:")
        c.line(400, y_pb + 26, 394 + col_w, y_pb + 26)
        c.line(400, y_pb + 14, 394 + col_w, y_pb + 14)

        y_pb -= 88

    c.showPage()

    # =========================================================================
    # PÁGINA 3: EL TIEMPO Y LOS RELOJES (5 RELOJES + 5 CONVERSIONES + 5 INTERVALOS)
    # =========================================================================
    draw_header(c, "⏰ EVALUACIÓN: EL TIEMPO Y LOS RELOJES", "Módulo 2: Relojes Análogos, Conversión 24h e Intervalos de Tiempo", 3, 8)

    draw_section_banner(c, 692, "🕒 I. LECTURA DE RELOJES ANÁLOGOS (5 RELOJES ILUSTRADOS)", "#7C3AED")

    relojes = [
        (7, 0, "1.1 En punto"),
        (2, 30, "1.2 Y media"),
        (9, 15, "1.3 Y cuarto"),
        (4, 45, "1.4 Un cuarto para..."),
        (11, 10, "1.5 Con 10 min")
    ]
    y_rel = 586
    for idx, (h, m, lbl) in enumerate(relojes):
        bx = 36 + idx * 109
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.roundRect(bx, y_rel, 102, 98, 5, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#6D28D9"))
        c.setFont("Helvetica-Bold", 7)
        c.drawString(bx + 4, y_rel + 86, lbl)
        draw_clock(c, bx + 51, y_rel + 48, 30, hour=h, minute=m)
        c.setFont("Helvetica", 7.5)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawCentredString(bx + 51, y_rel + 8, "Son: _________")

    draw_section_banner(c, 558, "🔄 II. CONVERSIÓN DE HORAS (5 EJERCICIOS)", "#059669")
    convs = [
        ("2.1", "2:00 PM a formato 24 horas:", "R: _________ hrs."),
        ("2.2", "5:30 PM a formato 24 horas:", "R: _________ hrs."),
        ("2.3", "8:00 PM a formato 24 horas:", "R: _________ hrs."),
        ("2.4", "10:15 PM a formato 24 horas:", "R: _________ hrs."),
        ("2.5", "¿Qué hora es las 17:00 hrs en formato 12h de la tarde?", "R: _________ PM")
    ]
    y_cnv = 512
    for num, preg, resp in convs:
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.roundRect(36, y_cnv, 540, 22, 4, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#047857"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(44, y_cnv + 7, f"{num})")
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawString(68, y_cnv + 7, preg)
        c.setFont("Helvetica-Bold", 8)
        c.drawRightString(564, y_cnv + 7, resp)
        y_cnv -= 26

    draw_section_banner(c, 372, "⏳ III. INTERVALOS DE TIEMPO / MINUTOS FALTANTES (5 PROBLEMAS)", "#D97706")
    intervs = [
        ("3.1", "Son las 09:00 hrs y el recreo comienza a las 09:30 hrs. ¿Cuántos minutos faltan?", "Faltan: ________ min."),
        ("3.2", "Son las 10:45 hrs y la clase termina a las 11:15 hrs. ¿Cuántos minutos faltan?", "Faltan: ________ min."),
        ("3.3", "Son las 12:35 hrs y el almuerzo es a las 12:50 hrs. ¿Cuántos minutos faltan?", "Faltan: ________ min."),
        ("3.4", "La película empezó a las 15:10 hrs y ahora son las 15:40 hrs. ¿Cuántos minutos han pasado?", "Han pasado: ________ min."),
        ("3.5", "Son las 08:20 hrs y la prueba empieza a las 08:45 hrs. ¿Cuántos minutos faltan?", "Faltan: ________ min.")
    ]
    y_int = 324
    for num, preg, resp in intervs:
        c.setFillColor(colors.HexColor("#FFFBEB"))
        c.setStrokeColor(colors.HexColor("#FDE68A"))
        c.roundRect(36, y_int, 540, 24, 4, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#B45309"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(44, y_int + 7.5, f"{num})")
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawString(68, y_int + 7.5, f"“{preg}”")
        c.setFont("Helvetica-Bold", 8)
        c.drawRightString(564, y_int + 7.5, resp)
        y_int -= 28

    c.showPage()

    # =========================================================================
    # PÁGINA 4: GEOMETRÍA (ÁNGULOS, TRIÁNGULOS Y CUERPOS 3D - 5 DE CADA UNO)
    # =========================================================================
    draw_header(c, "📐 EVALUACIÓN DE MATEMÁTICAS: GEOMETRÍA", "Módulo 3: Ángulos, Clasificación de Triángulos y Cuerpos 3D", 4, 8)

    # I. Ángulos (5 ejercicios)
    draw_section_banner(c, 692, "📐 I. CLASIFICACIÓN Y PROPIEDADES DE ÁNGULOS (5 EJERCICIOS)", "#7C3AED")
    y_ang = 604
    # 3 gráficos de ángulos
    angulos_graf = [
        ("1.1 Ángulo A", 90),
        ("1.2 Ángulo B", 45),
        ("1.3 Ángulo C", 135)
    ]
    for idx, (lbl, val) in enumerate(angulos_graf):
        bx = 36 + idx * 180
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.roundRect(bx, y_ang, 172, 80, 5, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#6D28D9"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(bx + 6, y_ang + 68, lbl)

        # Dibujo
        c.setStrokeColor(colors.HexColor("#1E3A8A"))
        c.setLineWidth(2)
        if val == 90:
            c.line(bx + 30, y_ang + 18, bx + 30, y_ang + 58)
            c.line(bx + 30, y_ang + 18, bx + 70, y_ang + 18)
            c.setStrokeColor(colors.HexColor("#DC2626"))
            c.rect(bx + 30, y_ang + 18, 10, 10, fill=0, stroke=1)
        elif val == 45:
            c.line(bx + 20, y_ang + 18, bx + 55, y_ang + 52)
            c.line(bx + 20, y_ang + 18, bx + 65, y_ang + 18)
            c.setStrokeColor(colors.HexColor("#2563EB"))
            c.arc(bx + 10, y_ang + 8, bx + 30, y_ang + 28, 0, 50)
        else:
            c.line(bx + 45, y_ang + 18, bx + 18, y_ang + 50)
            c.line(bx + 45, y_ang + 18, bx + 80, y_ang + 18)
            c.setStrokeColor(colors.HexColor("#059669"))
            c.arc(bx + 35, y_ang + 8, bx + 55, y_ang + 28, 0, 135)

        c.setFont("Helvetica", 7.5)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawString(bx + 85, y_ang + 42, "Clasificación:")
        c.drawString(bx + 85, y_ang + 26, "______________")

    # 1.4 y 1.5 preguntas teóricas de ángulos
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.setStrokeColor(colors.HexColor("#E2E8F0"))
    c.roundRect(36, 560, 540, 36, 4, fill=1, stroke=1)
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor("#1E293B"))
    c.drawString(44, 580, "1.4) ¿Cuántos ángulos rectos (90°) tiene una ventana o puerta rectangular?: R: ________ ángulos rectos.")
    c.drawString(44, 566, "1.5) Si las manecillas de un reloj marcan exactamente las 3:00 en punto, ¿qué ángulo forman?: R: _________________")

    # II. Triángulos (5 ejercicios)
    draw_section_banner(c, 532, "🔺 II. CLASIFICACIÓN DE TRIÁNGULOS (5 EJERCICIOS)", "#2563EB")
    triangulos_items = [
        ("2.1", "Tiene sus 3 lados de igual medida:", "R: Triángulo _______________________"),
        ("2.2", "Tiene 2 lados iguales y 1 lado diferente:", "R: Triángulo _______________________"),
        ("2.3", "Tiene sus 3 lados de diferente medida:", "R: Triángulo _______________________"),
        ("2.4", "Tiene 1 ángulo recto exacto de 90°:", "R: Triángulo _______________________"),
        ("2.5", "¿Cuántos lados, vértices y ángulos interiores tiene cualquier triángulo?:", "R: _____ lados, _____ vértices y _____ ángulos.")
    ]
    y_tri = 484
    for num, enunc, resp in triangulos_items:
        c.setFillColor(colors.HexColor("#EFF6FF"))
        c.setStrokeColor(colors.HexColor("#BFDBFE"))
        c.roundRect(36, y_tri, 540, 22, 4, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#1E40AF"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(44, y_tri + 7, f"{num})")
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawString(68, y_tri + 7, enunc)
        c.setFont("Helvetica-Bold", 8)
        c.drawRightString(564, y_tri + 7, resp)
        y_tri -= 26

    # III. Cuerpos Geométricos 3D (5 ejercicios)
    draw_section_banner(c, 344, "📦 III. CUERPOS GEOMÉTRICOS 3D (5 EJERCICIOS)", "#059669")
    c3d_items = [
        ("3.1 EL CUBO", "Caras cuadradas: _____   Vértices: _____   Aristas: _____"),
        ("3.2 EL PRISMA RECTANGULAR", "Caras rectangulares: _____   Vértices: _____   Aristas: _____"),
        ("3.3 LA PIRÁMIDE (Base cuadrada)", "Caras totales: _____   Vértices: _____   Aristas: _____"),
        ("3.4 EL CILINDRO", "¿Cuántas caras planas circulares tiene?: _____   ¿Rueda?: _________"),
        ("3.5 LA ESFERA", "¿Cuántas caras planas tiene?: _____   ¿Tiene vértices o aristas?: _________")
    ]
    y_c3d = 296
    for tit, detalle in c3d_items:
        c.setFillColor(colors.HexColor("#F0FDF4"))
        c.setStrokeColor(colors.HexColor("#BBF7D0"))
        c.roundRect(36, y_c3d, 540, 24, 4, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#065F46"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(44, y_c3d + 7.5, f"• {tit}:")
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawRightString(564, y_c3d + 7.5, detalle)
        y_c3d -= 28

    c.showPage()

    # =========================================================================
    # PÁGINA 5: DATOS Y GRÁFICOS (PARTE 1: PICTOGRAMAS 1 Y 2 CON 5 PREGUNTAS C/U)
    # =========================================================================
    draw_header(c, "📊 EVALUACIÓN: DATOS Y PICTOGRAMAS", "Módulo 4: Análisis de Pictogramas con Clave de Escala", 5, 8)

    # Pictograma 1: Libros (Clave = 4)
    draw_section_banner(c, 692, "📖 PICTOGRAMA 1: LIBROS LEÍDOS EN LA BIBLIOTECA (5 PREGUNTAS)", "#0284C7")
    y_p1 = 548
    c.setFillColor(colors.HexColor("#FFFFFF"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.roundRect(36, y_p1, 540, 136, 6, fill=1, stroke=1)

    c.setFillColor(colors.HexColor("#EFF6FF"))
    c.setStrokeColor(colors.HexColor("#38BDF8"))
    c.roundRect(370, y_p1 + 114, 196, 16, 4, fill=1, stroke=1)
    c.setFillColor(colors.HexColor("#0C4A6E"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(380, y_p1 + 119, "🔑 CLAVE: Cada 📘 = 4 libros leídos")

    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.rect(46, y_p1 + 54, 520, 54, fill=1, stroke=1)
    c.setFillColor(colors.HexColor("#1E293B"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(56, y_p1 + 94, "Marzo:")
    c.drawString(56, y_p1 + 80, "Abril:")
    c.drawString(56, y_p1 + 66, "Mayo:")
    c.drawString(56, y_p1 + 52, "Junio:")

    c.setFont("Helvetica", 7.5)
    c.drawString(110, y_p1 + 94, "📘  📘  📘  📘")
    c.drawString(110, y_p1 + 80, "📘  📘  📘  📘  📘  📘")
    c.drawString(110, y_p1 + 66, "📘  📘")
    c.drawString(110, y_p1 + 52, "📘  📘  📘  📘  📘")

    # 5 preguntas limpias
    c.setFont("Helvetica", 7.5)
    c.drawString(46, y_p1 + 38, "1.1) ¿Cuántos libros se leyeron en Marzo?: ________ libros.")
    c.drawString(46, y_p1 + 25, "1.2) ¿En qué mes se leyó la MENOR cantidad de libros?: __________________.")
    c.drawString(46, y_p1 + 12, "1.3) ¿Cuántos libros MÁS se leyeron en Abril que en Mayo?: ________ libros.")
    c.drawString(300, y_p1 + 38, "1.4) ¿Cuántos libros se leyeron en Junio?: ________ libros.")
    c.drawString(300, y_p1 + 25, "1.5) ¿Cuántos libros se leyeron en TOTAL durante los 4 meses?: ________ libros.")

    # Pictograma 2: Manzanas (Clave = 5)
    draw_section_banner(c, 514, "🍎 PICTOGRAMA 2: COSECHA DE MANZANAS (5 PREGUNTAS)", "#059669")
    y_p2 = 370
    c.setFillColor(colors.HexColor("#FFFFFF"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.roundRect(36, y_p2, 540, 136, 6, fill=1, stroke=1)

    c.setFillColor(colors.HexColor("#F0FDF4"))
    c.setStrokeColor(colors.HexColor("#86EFAC"))
    c.roundRect(370, y_p2 + 114, 196, 16, 4, fill=1, stroke=1)
    c.setFillColor(colors.HexColor("#166534"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(380, y_p2 + 119, "🔑 CLAVE: Cada 🍎 = 5 manzanas")

    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.rect(46, y_p2 + 54, 520, 54, fill=1, stroke=1)
    c.setFillColor(colors.HexColor("#1E293B"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(56, y_p2 + 94, "Lunes:")
    c.drawString(56, y_p2 + 80, "Martes:")
    c.drawString(56, y_p2 + 66, "Miércoles:")
    c.drawString(56, y_p2 + 52, "Jueves:")

    c.setFont("Helvetica", 7.5)
    c.drawString(110, y_p2 + 94, "🍎  🍎  🍎")
    c.drawString(110, y_p2 + 80, "🍎  🍎  🍎  🍎")
    c.drawString(110, y_p2 + 66, "🍎  🍎")
    c.drawString(110, y_p2 + 52, "🍎  🍎  🍎  🍎  🍎")

    # 5 preguntas limpias
    c.setFont("Helvetica", 7.5)
    c.drawString(46, y_p2 + 38, "2.1) ¿Cuántas manzanas se cosecharon el Martes?: ________ manzanas.")
    c.drawString(46, y_p2 + 25, "2.2) ¿Qué día se cosecharon exactamente 10 manzanas?: __________________.")
    c.drawString(46, y_p2 + 12, "2.3) ¿Cuántas manzanas MÁS se cosecharon el Jueves que el Lunes?: ________ manzanas.")
    c.drawString(300, y_p2 + 38, "2.4) ¿Qué día se produjo la MAYOR cosecha?: __________________.")
    c.drawString(300, y_p2 + 25, "2.5) ¿Cuántas manzanas se cosecharon en TOTAL en los 4 días?: ________ manzanas.")

    c.showPage()

    # =========================================================================
    # PÁGINA 6: DATOS Y GRÁFICOS (PARTE 2: GRÁFICOS DE BARRAS 1 Y 2 CON 5 PREGUNTAS C/U)
    # =========================================================================
    draw_header(c, "📊 EVALUACIÓN: GRÁFICOS DE BARRAS", "Módulo 4: Análisis de Gráficos de Barras con Escalas Graduadas", 6, 8)

    # Gráfico de Barras 1: Deportes (Escala de 5 en 5)
    draw_section_banner(c, 692, "⚽ GRÁFICO DE BARRAS 1: DEPORTE FAVORITO (ESCALA DE 5 EN 5)", "#4F46E5")
    y_b1 = 502
    c.setFillColor(colors.HexColor("#FFFFFF"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.roundRect(36, y_b1, 540, 182, 6, fill=1, stroke=1)

    # Ejes
    bx1 = 76
    by1 = y_b1 + 30
    c.setStrokeColor(colors.HexColor("#475569"))
    c.setLineWidth(1.2)
    c.line(bx1, by1, bx1, by1 + 115)
    c.line(bx1, by1, bx1 + 200, by1)

    c.setFont("Helvetica", 7)
    c.setFillColor(colors.HexColor("#475569"))
    for v in range(0, 26, 5):
        py = by1 + (v / 25.0) * 110
        c.drawRightString(bx1 - 5, py - 2.5, str(v))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.setLineWidth(0.6)
        c.line(bx1, py, bx1 + 200, py)

    deportes = [("Fútbol", 25, "#3B82F6"), ("Básquet", 15, "#F59E0B"), ("Natación", 20, "#06B6D4"), ("Atletismo", 10, "#8B5CF6")]
    for idx, (dname, dval, dcol) in enumerate(deportes):
        bar_x = bx1 + 14 + idx * 46
        bar_h = (dval / 25.0) * 110
        c.setFillColor(colors.HexColor(dcol))
        c.rect(bar_x, by1, 30, bar_h, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(bar_x + 15, by1 - 12, dname)

    # 5 preguntas
    c.setFont("Helvetica", 7.5)
    c.drawString(290, y_b1 + 152, "3.1) ¿Cuál es el deporte con MAYOR preferencia?:")
    c.drawString(306, y_b1 + 138, "R: ___________________________________")

    c.drawString(290, y_b1 + 120, "3.2) ¿Cuántos votos obtuvo la Natación?:")
    c.drawString(306, y_b1 + 106, "R: ________ votos.")

    c.drawString(290, y_b1 + 88, "3.3) ¿Cuántos niños MÁS prefieren Fútbol que Atletismo?:")
    c.drawString(306, y_b1 + 74, "R: ________ niños.")

    c.drawString(290, y_b1 + 56, "3.4) ¿Cuál es el deporte MENOS votado?:")
    c.drawString(306, y_b1 + 42, "R: ___________________________________")

    c.drawString(290, y_b1 + 24, "3.5) ¿Cuántos estudiantes fueron encuestados en TOTAL?:")
    c.drawString(306, y_b1 + 10, "R: ________ estudiantes.")

    # Gráfico de Barras 2: Mascotas (Escala de 2 en 2)
    draw_section_banner(c, 468, "🐶 GRÁFICO DE BARRAS 2: MASCOTAS DEL CURSO (ESCALA DE 2 EN 2)", "#0284C7")
    y_b2 = 280
    c.setFillColor(colors.HexColor("#FFFFFF"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.roundRect(36, y_b2, 540, 180, 6, fill=1, stroke=1)

    # Ejes
    bx2 = 76
    by2 = y_b2 + 28
    c.setStrokeColor(colors.HexColor("#475569"))
    c.setLineWidth(1.2)
    c.line(bx2, by2, bx2, by2 + 115)
    c.line(bx2, by2, bx2 + 200, by2)

    c.setFont("Helvetica", 7)
    c.setFillColor(colors.HexColor("#475569"))
    for v in range(0, 13, 2):
        py = by2 + (v / 12.0) * 110
        c.drawRightString(bx2 - 5, py - 2.5, str(v))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.setLineWidth(0.6)
        c.line(bx2, py, bx2 + 200, py)

    mascotas = [("Perro", 12, "#10B981"), ("Gato", 10, "#EC4899"), ("Hámster", 6, "#EAB308"), ("Canario", 4, "#6366F1")]
    for idx, (mname, mval, mcol) in enumerate(mascotas):
        bar_x = bx2 + 14 + idx * 46
        bar_h = (mval / 12.0) * 110
        c.setFillColor(colors.HexColor(mcol))
        c.rect(bar_x, by2, 30, bar_h, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(bar_x + 15, by2 - 12, mname)

    # 5 preguntas
    c.setFont("Helvetica", 7.5)
    c.drawString(290, y_b2 + 152, "4.1) ¿Cuántos votos obtuvo el Gato?:")
    c.drawString(306, y_b2 + 138, "R: ________ votos.")

    c.drawString(290, y_b2 + 120, "4.2) ¿Cuál es la mascota con MAYOR cantidad de votos?:")
    c.drawString(306, y_b2 + 106, "R: ___________________________________")

    c.drawString(290, y_b2 + 88, "4.3) ¿Cuántos votos MÁS tiene el Perro que el Canario?:")
    c.drawString(306, y_b2 + 74, "R: ________ votos.")

    c.drawString(290, y_b2 + 56, "4.4) ¿Cuál es la mascota MENOS votada?:")
    c.drawString(306, y_b2 + 42, "R: ___________________________________")

    c.drawString(290, y_b2 + 24, "4.5) ¿Cuántas mascotas fueron registradas en TOTAL?:")
    c.drawString(306, y_b2 + 10, "R: ________ mascotas.")

    c.showPage()

    # =========================================================================
    # PÁGINA 7: SOLUCIONARIO OFICIAL (PARTE 1: OPERATORIA Y TIEMPO)
    # =========================================================================
    draw_header(c, "🎯 SOLUCIONARIO OFICIAL Y PAUTA DE CORRECCIÓN (PARTE 1)", "Claves completas para Papá y Mamá: Módulos 1 y 2", 7, 8)

    draw_section_banner(c, 692, "✅ SOLUCIONARIO MÓDULO 1: OPERATORIA Y NUMERACIÓN", "#2563EB")
    sol_op = [
        ("1. Antecesor y sucesor", "1.1: 599 < 600 < 601 | 1.2: 498 < 499 < 500 | 1.3: 819 < 820 < 821 | 1.4: 699 < 700 < 701 | 1.5: 349 < 350 < 351"),
        ("2. Escritura en palabras", "2.1: Setecientos cincuenta y tres | 2.2: Seiscientos ocho | 2.3: Novecientos cuarenta y dos | 2.4: Quinientos dieciséis | 2.5: Ochocientos setenta"),
        ("3. Sumas verticales", "3.1: 496 | 3.2: 784 | 3.3: 833 (reserva) | 3.4: 864 (reserva) | 3.5: 854 (reserva)"),
        ("4. Restas verticales", "4.1: 444 | 4.2: 441 | 4.3: 362 (canje ceros) | 4.4: 344 (canje ceros) | 4.5: 357 (canje)"),
        ("5. Multiplicaciones", "5.1: 32x3 = 96 | 5.2: 41x2 = 82 | 5.3: 24x2 = 48 | 5.4: 13x3 = 39 | 5.5: 23x3 = 69"),
        ("6.1 Problema Martina", "Datos: 4 cajas, 5 lápices c/u | Operación: 4 x 5 = 20 | Respuesta: Martina tiene en total 20 lápices."),
        ("6.2 Problema Joaquín", "Datos: 3 paquetes, 6 galletas c/u | Operación: 3 x 6 = 18 | Respuesta: Joaquín tiene en total 18 galletas."),
        ("6.3 Problema Biblioteca", "Datos: 450 libros y 235 libros | Operación: 450 + 235 = 685 | Respuesta: Hay en total 685 libros."),
        ("6.4 Problema Matías", "Datos: $800 tenía, gastó $350 | Operación: 800 - 350 = 450 | Respuesta: A Matías le sobraron $450 pesos."),
        ("6.5 Problema Jardín", "Datos: 5 mesas, 4 niños c/u | Operación: 5 x 4 = 20 | Respuesta: Hay 20 niños sentados.")
    ]
    y_sop = 660
    for tit, texto in sol_op:
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.roundRect(36, y_sop, 540, 22, 3, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#1E3A8A"))
        c.setFont("Helvetica-Bold", 7)
        c.drawString(42, y_sop + 7, tit + ":")
        c.setFillColor(colors.HexColor("#047857"))
        c.setFont("Helvetica", 7)
        c.drawString(145, y_sop + 7, texto[:100] + ("..." if len(texto)>100 else ""))
        y_sop -= 25

    draw_section_banner(c, 396, "⏰ SOLUCIONARIO MÓDULO 2: EL TIEMPO Y LOS RELOJES", "#7C3AED")
    sol_tie = [
        ("1. Relojes análogos", "1.1: 07:00 en punto | 1.2: 02:30 (dos y media) | 1.3: 09:15 (nueve y cuarto) | 1.4: 04:45 (cuarto para las cinco) | 1.5: 11:10"),
        ("2. Conversión 24 horas", "2.1: 14:00 hrs (2+12) | 2.2: 17:30 hrs (5+12) | 2.3: 20:00 hrs (8+12) | 2.4: 22:15 hrs (10+12) | 2.5: 5:00 PM (17-12)"),
        ("3. Intervalos de tiempo", "3.1: Faltan 30 min | 3.2: Faltan 30 min (15+15) | 3.3: Faltan 15 min | 3.4: Han pasado 30 min | 3.5: Faltan 25 min")
    ]
    y_stie = 366
    for tit, texto in sol_tie:
        c.setFillColor(colors.HexColor("#FAF5FF"))
        c.setStrokeColor(colors.HexColor("#E9D5FF"))
        c.roundRect(36, y_stie, 540, 24, 3, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#6D28D9"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(42, y_stie + 8, tit + ":")
        c.setFillColor(colors.HexColor("#047857"))
        c.setFont("Helvetica", 7.5)
        c.drawString(145, y_stie + 8, texto)
        y_stie -= 28

    c.showPage()

    # =========================================================================
    # PÁGINA 8: SOLUCIONARIO OFICIAL (PARTE 2: GEOMETRÍA Y DATOS)
    # =========================================================================
    draw_header(c, "🎯 SOLUCIONARIO OFICIAL Y PAUTA DE CORRECCIÓN (PARTE 2)", "Claves completas para Papá y Mamá: Módulos 3 y 4", 8, 8)

    draw_section_banner(c, 692, "📐 SOLUCIONARIO MÓDULO 3: GEOMETRÍA", "#059669")
    sol_geo = [
        ("1. Ángulos (1.1 al 1.5)", "1.1: Recto (90°) | 1.2: Agudo (<90°) | 1.3: Obtuso (>90°) | 1.4: 4 ángulos rectos | 1.5: Ángulo Recto (90°)"),
        ("2. Triángulos (2.1 al 2.5)", "2.1: Equilátero | 2.2: Isósceles | 2.3: Escaleno | 2.4: Triángulo Rectángulo | 2.5: 3 lados, 3 vértices y 3 ángulos"),
        ("3. Cuerpos 3D (3.1 al 3.5)", "3.1 Cubo: 6C, 8V, 12A | 3.2 Prisma: 6C, 8V, 12A | 3.3 Pirámide: 5C, 5V, 8A | 3.4 Cilindro: 2 planas, sí rueda | 3.5 Esfera: 0 planas, sin vértices ni aristas")
    ]
    y_sgeo = 660
    for tit, texto in sol_geo:
        c.setFillColor(colors.HexColor("#ECFDF5"))
        c.setStrokeColor(colors.HexColor("#A7F3D0"))
        c.roundRect(36, y_sgeo, 540, 24, 3, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#065F46"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(42, y_sgeo + 8, tit + ":")
        c.setFillColor(colors.HexColor("#047857"))
        c.setFont("Helvetica", 7.5)
        c.drawString(145, y_sgeo + 8, texto)
        y_sgeo -= 28

    draw_section_banner(c, 560, "📊 SOLUCIONARIO MÓDULO 4: DATOS Y GRÁFICOS", "#0284C7")
    sol_dat = [
        ("Pictograma 1 (Libros 📘=4)", "1.1: 16 libros (4x4) | 1.2: Mayo (8) | 1.3: 16 más (24 - 8) | 1.4: 20 libros (5x4) | 1.5: 68 libros en total (16+24+8+20)"),
        ("Pictograma 2 (Manzanas 🍎=5)", "2.1: 20 manzanas (4x5) | 2.2: Miércoles (2x5=10) | 2.3: 10 más (25 - 15) | 2.4: Jueves (25) | 2.5: 70 manzanas en total (15+20+10+25)"),
        ("Gráfico 1 (Deportes esc. 5)", "3.1: Fútbol (25) | 3.2: 20 votos | 3.3: 15 más (25 - 10) | 3.4: Atletismo (10) | 3.5: 70 estudiantes en total (25+15+20+10)"),
        ("Gráfico 2 (Mascotas esc. 2)", "4.1: 10 votos | 4.2: Perro (12) | 4.3: 8 más (12 - 4) | 4.4: Canario (4) | 4.5: 32 mascotas en total (12+10+6+4)")
    ]
    y_sdat = 528
    for tit, texto in sol_dat:
        c.setFillColor(colors.HexColor("#F0F9FF"))
        c.setStrokeColor(colors.HexColor("#BAE6FD"))
        c.roundRect(36, y_sdat, 540, 24, 3, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#0369A1"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(42, y_sdat + 8, tit + ":")
        c.setFillColor(colors.HexColor("#047857"))
        c.setFont("Helvetica", 7.5)
        c.drawString(160, y_sdat + 8, texto)
        y_sdat -= 28

    c.save()
    print("PDF Mega Completo (8 páginas completas, 80 ejercicios simétricos) generado exitosamente:", filename)

if __name__ == "__main__":
    out_path = "/Users/familia_bustos_estrada/Maxi/guia_estudio_amelia.pdf"
    generate_mega_pdf(out_path)

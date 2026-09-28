import math
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# =============================================================================
# HELPER DE DIBUJO VECTORIAL: RELOJ ANALÓGICO
# =============================================================================
def draw_clock(c, center_x, center_y, radius, hour, minute):
    """Reloj analógico vectorial exacto sin números de pista ni respuestas."""
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

    # Minutero (largo, azul)
    min_angle = math.radians(90 - minute * 6)
    mx = center_x + (radius - 6) * math.cos(min_angle)
    my = center_y + (radius - 6) * math.sin(min_angle)
    c.setStrokeColor(colors.HexColor("#0284C7"))
    c.setLineWidth(1.8)
    c.line(center_x, center_y, mx, my)

    # Horario (corto, rojo)
    hour_angle = math.radians(90 - ((hour % 12) + minute / 60.0) * 30)
    hx = center_x + (radius * 0.54) * math.cos(hour_angle)
    hy = center_y + (radius * 0.54) * math.sin(hour_angle)
    c.setStrokeColor(colors.HexColor("#DC2626"))
    c.setLineWidth(2.5)
    c.line(center_x, center_y, hx, hy)


# =============================================================================
# HELPERS DE DIBUJO VECTORIAL: CUERPOS GEOMÉTRICOS 3D
# =============================================================================
def draw_cube(c, cx, cy, s=34):
    """Cubo isométrico 3D con caras diferenciadas y aristas ocultas punteadas."""
    x = cx - s * 0.5
    y = cy - s * 0.5
    d = s * 0.4
    dx = d * 0.707
    dy = d * 0.707

    # Cara frontal
    c.setFillColor(colors.HexColor("#DBEAFE"))
    c.setStrokeColor(colors.HexColor("#1E3A8A"))
    c.setLineWidth(1.2)
    c.rect(x, y, s, s, fill=1, stroke=1)

    # Cara superior
    c.setFillColor(colors.HexColor("#EFF6FF"))
    p_top = c.beginPath()
    p_top.moveTo(x, y + s)
    p_top.lineTo(x + dx, y + s + dy)
    p_top.lineTo(x + s + dx, y + s + dy)
    p_top.lineTo(x + s, y + s)
    p_top.close()
    c.drawPath(p_top, fill=1, stroke=1)

    # Cara derecha
    c.setFillColor(colors.HexColor("#BFDBFE"))
    p_right = c.beginPath()
    p_right.moveTo(x + s, y)
    p_right.lineTo(x + s + dx, y + dy)
    p_right.lineTo(x + s + dx, y + s + dy)
    p_right.lineTo(x + s, y + s)
    p_right.close()
    c.drawPath(p_right, fill=1, stroke=1)

    # Aristas ocultas punteadas
    c.setStrokeColor(colors.HexColor("#93C5FD"))
    c.setLineWidth(0.8)
    c.setDash(2, 2)
    c.line(x, y, x + dx, y + dy)
    c.line(x + dx, y + dy, x + s + dx, y + dy)
    c.line(x + dx, y + dy, x + dx, y + s + dy)
    c.setDash()


def draw_prism(c, cx, cy, w=40, h=26, d=16):
    """Prisma rectangular (paralelepípedo) 3D."""
    x = cx - w * 0.5
    y = cy - h * 0.5
    dx = d * 0.707
    dy = d * 0.707

    c.setFillColor(colors.HexColor("#EDE9FE"))
    c.setStrokeColor(colors.HexColor("#5B21B6"))
    c.setLineWidth(1.2)
    c.rect(x, y, w, h, fill=1, stroke=1)

    c.setFillColor(colors.HexColor("#F5F3FF"))
    p_top = c.beginPath()
    p_top.moveTo(x, y + h)
    p_top.lineTo(x + dx, y + h + dy)
    p_top.lineTo(x + w + dx, y + h + dy)
    p_top.lineTo(x + w, y + h)
    p_top.close()
    c.drawPath(p_top, fill=1, stroke=1)

    c.setFillColor(colors.HexColor("#DDD6FE"))
    p_right = c.beginPath()
    p_right.moveTo(x + w, y)
    p_right.lineTo(x + w + dx, y + dy)
    p_right.lineTo(x + w + dx, y + h + dy)
    p_right.lineTo(x + w, y + h)
    p_right.close()
    c.drawPath(p_right, fill=1, stroke=1)

    c.setStrokeColor(colors.HexColor("#C4B5FD"))
    c.setLineWidth(0.8)
    c.setDash(2, 2)
    c.line(x, y, x + dx, y + dy)
    c.line(x + dx, y + dy, x + w + dx, y + dy)
    c.line(x + dx, y + dy, x + dx, y + h + dy)
    c.setDash()


def draw_pyramid(c, cx, cy, w=38, h=36):
    """Pirámide de base cuadrada 3D con cúspide."""
    x = cx - w * 0.5
    y = cy - h * 0.4
    apex_x = cx
    apex_y = cy + h * 0.6
    dx = w * 0.35
    dy = h * 0.25

    p_front = c.beginPath()
    p_front.moveTo(x, y)
    p_front.lineTo(apex_x, apex_y)
    p_front.lineTo(x + w, y)
    p_front.close()
    c.setFillColor(colors.HexColor("#FEF3C7"))
    c.setStrokeColor(colors.HexColor("#B45309"))
    c.setLineWidth(1.2)
    c.drawPath(p_front, fill=1, stroke=1)

    p_right = c.beginPath()
    p_right.moveTo(x + w, y)
    p_right.lineTo(apex_x, apex_y)
    p_right.lineTo(x + w + dx, y + dy)
    p_right.close()
    c.setFillColor(colors.HexColor("#FDE68A"))
    c.drawPath(p_right, fill=1, stroke=1)

    c.setStrokeColor(colors.HexColor("#FCD34D"))
    c.setLineWidth(0.8)
    c.setDash(2, 2)
    c.line(x, y, x + dx, y + dy)
    c.line(x + dx, y + dy, x + w + dx, y + dy)
    c.line(x + dx, y + dy, apex_x, apex_y)
    c.setDash()


def draw_cylinder(c, cx, cy, r=16, h=30):
    """Cilindro 3D con bases circulares elípticas."""
    y = cy - h * 0.5
    c.setFillColor(colors.HexColor("#D1FAE5"))
    c.setStrokeColor(colors.HexColor("#065F46"))
    c.setLineWidth(1.2)
    c.rect(cx - r, y, r * 2, h, fill=1, stroke=0)
    c.line(cx - r, y, cx - r, y + h)
    c.line(cx + r, y, cx + r, y + h)

    # Base inferior
    c.ellipse(cx - r, y - r * 0.35, cx + r, y + r * 0.35, fill=1, stroke=1)
    c.setFillColor(colors.HexColor("#D1FAE5"))
    c.rect(cx - r + 0.5, y, r * 2 - 1, h, fill=1, stroke=0)

    # Tapa superior
    c.setFillColor(colors.HexColor("#A7F3D0"))
    c.ellipse(cx - r, y + h - r * 0.35, cx + r, y + h + r * 0.35, fill=1, stroke=1)


def draw_sphere(c, cx, cy, r=18):
    """Esfera 3D con iluminación y elipse ecuatorial punteada."""
    c.setFillColor(colors.HexColor("#FEE2E2"))
    c.setStrokeColor(colors.HexColor("#991B1B"))
    c.setLineWidth(1.2)
    c.circle(cx, cy, r, fill=1, stroke=1)

    c.setFillColor(colors.HexColor("#FEF2F2"))
    c.circle(cx - r * 0.3, cy + r * 0.3, r * 0.35, fill=1, stroke=0)

    c.setStrokeColor(colors.HexColor("#F87171"))
    c.setLineWidth(0.8)
    c.setDash(2, 2)
    c.ellipse(cx - r, cy - r * 0.3, cx + r, cy + r * 0.3, fill=0, stroke=1)
    c.setDash()


# =============================================================================
# HELPERS DE DIBUJO VECTORIAL: TRIÁNGULOS
# =============================================================================
def draw_triangle_equil(c, cx, cy, s=34):
    """Triángulo equilátero con marcas de igualdad en sus 3 lados."""
    h = s * math.sqrt(3) / 2
    x = cx - s * 0.5
    y = cy - h * 0.4
    p = c.beginPath()
    p.moveTo(x, y)
    p.lineTo(cx, y + h)
    p.lineTo(x + s, y)
    p.close()
    c.setFillColor(colors.HexColor("#EFF6FF"))
    c.setStrokeColor(colors.HexColor("#1D4ED8"))
    c.setLineWidth(1.3)
    c.drawPath(p, fill=1, stroke=1)

    c.setStrokeColor(colors.HexColor("#DC2626"))
    c.setLineWidth(1)
    c.line(cx, y - 3, cx, y + 3)
    c.line((x + cx) / 2 - 2, (y + y + h) / 2 + 2, (x + cx) / 2 + 2, (y + y + h) / 2 - 2)
    c.line((x + s + cx) / 2 - 2, (y + y + h) / 2 - 2, (x + s + cx) / 2 + 2, (y + y + h) / 2 + 2)


def draw_triangle_iso(c, cx, cy, w=28, h=38):
    """Triángulo isósceles con marcas dobles en los 2 lados iguales."""
    x = cx - w * 0.5
    y = cy - h * 0.4
    p = c.beginPath()
    p.moveTo(x, y)
    p.lineTo(cx, y + h)
    p.lineTo(x + w, y)
    p.close()
    c.setFillColor(colors.HexColor("#F0FDF4"))
    c.setStrokeColor(colors.HexColor("#047857"))
    c.setLineWidth(1.3)
    c.drawPath(p, fill=1, stroke=1)

    c.setStrokeColor(colors.HexColor("#DC2626"))
    c.setLineWidth(0.9)
    lx, ly = (x + cx) / 2, (y + y + h) / 2
    c.line(lx - 4, ly + 2, lx, ly - 2)
    c.line(lx - 1, ly + 4, lx + 3, ly)
    rx, ry = (x + w + cx) / 2, (y + y + h) / 2
    c.line(rx, ly - 2, rx + 4, ly + 2)
    c.line(rx - 3, ly, rx + 1, ly + 4)


def draw_triangle_scal(c, cx, cy, w=40, h=28):
    """Triángulo escaleno con 3 lados desiguales."""
    x = cx - w * 0.5
    y = cy - h * 0.4
    p = c.beginPath()
    p.moveTo(x, y)
    p.lineTo(x + w * 0.22, y + h)
    p.lineTo(x + w, y)
    p.close()
    c.setFillColor(colors.HexColor("#FFFBEB"))
    c.setStrokeColor(colors.HexColor("#B45309"))
    c.setLineWidth(1.3)
    c.drawPath(p, fill=1, stroke=1)


def draw_triangle_rect(c, cx, cy, w=34, h=32):
    """Triángulo rectángulo con ángulo de 90°."""
    x = cx - w * 0.5
    y = cy - h * 0.4
    p = c.beginPath()
    p.moveTo(x, y)
    p.lineTo(x, y + h)
    p.lineTo(x + w, y)
    p.close()
    c.setFillColor(colors.HexColor("#FAF5FF"))
    c.setStrokeColor(colors.HexColor("#6D28D9"))
    c.setLineWidth(1.3)
    c.drawPath(p, fill=1, stroke=1)

    c.setStrokeColor(colors.HexColor("#DC2626"))
    c.setLineWidth(1)
    c.rect(x, y, 6, 6, fill=0, stroke=1)


# =============================================================================
# ENCABEZADO Y BANNERS
# =============================================================================
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


# =============================================================================
# CUADRÍCULA VERTICAL CDU (CENTENA, DECENA, UNIDAD)
# =============================================================================
def draw_cdu_box(c, x, y, width, height, op_type, num1, num2):
    """
    Cuadrícula vertical escolar CDU limpia y simétrica.
    Sin pistas ni avisos de reserva/canje. Todas las operaciones lucen idénticas.
    """
    c.setFillColor(colors.HexColor("#FFFFFF"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.setLineWidth(1)
    c.roundRect(x, y, width, height, 5, fill=1, stroke=1)

    cell_w = 18
    cell_h = 14
    start_x = x + width - 3 * cell_w - 12
    top_y = y + height - 16

    headers = ["C", "D", "U"]
    col_bgs = ["#DBEAFE", "#E0E7FF", "#EDE9FE"]
    for i, (h, bg) in enumerate(zip(headers, col_bgs)):
        c.setFillColor(colors.HexColor(bg))
        c.setStrokeColor(colors.HexColor("#94A3B8"))
        c.setLineWidth(0.6)
        c.rect(start_x + i * cell_w, top_y, cell_w, cell_h - 2, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(start_x + i * cell_w + cell_w / 2, top_y + 3, h)

    curr_y = top_y - cell_h

    # Casillas de reserva/canje punteadas uniformes en todos los ejercicios
    for i in range(3):
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.setLineWidth(0.5)
        c.setDash(1.5, 1.5)
        c.rect(start_x + i * cell_w, curr_y + 2, cell_w, cell_h - 3, fill=1, stroke=1)
    c.setDash()
    curr_y -= (cell_h - 1)

    # Primer sumando / minuendo
    s1 = str(num1).rjust(3)
    for i, d in enumerate(s1):
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.setLineWidth(0.5)
        c.rect(start_x + i * cell_w, curr_y, cell_w, cell_h, fill=1, stroke=1)
        if d != ' ':
            c.setFillColor(colors.HexColor("#0F172A"))
            c.setFont("Courier-Bold", 11)
            c.drawCentredString(start_x + i * cell_w + cell_w / 2, curr_y + 3, d)
    curr_y -= cell_h

    # Signo de operación
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#2563EB") if op_type == "+" else colors.HexColor("#DC2626"))
    c.drawCentredString(start_x - 9, curr_y + 2, op_type)

    # Segundo sumando / sustraendo
    s2 = str(num2).rjust(3)
    for i, d in enumerate(s2):
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.setLineWidth(0.5)
        c.rect(start_x + i * cell_w, curr_y, cell_w, cell_h, fill=1, stroke=1)
        if d != ' ':
            c.setFillColor(colors.HexColor("#0F172A"))
            c.setFont("Courier-Bold", 11)
            c.drawCentredString(start_x + i * cell_w + cell_w / 2, curr_y + 3, d)
    curr_y -= 3

    # Línea de cálculo horizontal
    c.setStrokeColor(colors.HexColor("#0F172A"))
    c.setLineWidth(1.4)
    c.line(start_x - 10, curr_y, start_x + 3 * cell_w, curr_y)
    curr_y -= (cell_h + 3)

    # Casillas de resultado
    for i in range(3):
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#94A3B8"))
        c.setLineWidth(0.8)
        c.rect(start_x + i * cell_w, curr_y, cell_w, cell_h + 2, fill=1, stroke=1)


# =============================================================================
# GENERADOR PRINCIPAL DEL DOCUMENTO
# =============================================================================
def generate_mega_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # =========================================================================
    # PÁGINA 1: OPERATORIA Y NUMERACIÓN (PARTE A: ANTECESOR, PALABRAS, SUMAS)
    # =========================================================================
    draw_header(c, "✏️ GUÍA OFICIAL DE MATEMÁTICAS — 3° BÁSICO", "Módulo 1: Numeración y Operatoria Vertical (Parte 1)", 1, 8)

    # I. Antecesor y Sucesor (5 ejercicios) - SIN SPOILERS (-1 / +1)
    draw_section_banner(c, 692, "🔢 I. ANTECESOR Y SUCESOR (5 EJERCICIOS)", "#2563EB")
    nums_ant = [600, 499, 820, 700, 350]
    y_ant = 638
    b_w = 100
    for idx, n in enumerate(nums_ant):
        bx = 36 + idx * 109
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.roundRect(bx, y_ant, b_w, 48, 5, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#1D4ED8"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(bx + 6, y_ant + 36, f"1.{idx+1})")
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(colors.HexColor("#0F172A"))
        c.drawCentredString(bx + b_w / 2, y_ant + 18, f"___ < {n} < ___")

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

    # III. Sumas Verticales (5 ejercicios) - CERO PISTAS DE RESERVA
    draw_section_banner(c, 452, "➕ III. SUMAS VERTICALES (5 EJERCICIOS)", "#059669")
    sumas = [
        (342, 154, "3.1"),
        (523, 261, "3.2"),
        (586, 247, "3.3"),
        (479, 385, "3.4"),
        (658, 196, "3.5")
    ]
    y_sum = 352
    for idx, (n1, n2, lbl) in enumerate(sumas):
        bx = 36 + idx * 109
        c.setFillColor(colors.HexColor("#047857"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(bx + 4, y_sum + 96, lbl)
        draw_cdu_box(c, bx, y_sum, 102, 92, "+", n1, n2)

    # IV. Descomposición y Valor Posicional (5 ejercicios)
    draw_section_banner(c, 320, "🧩 IV. VALOR POSICIONAL Y DESCOMPOSICIÓN (5 EJERCICIOS)", "#D97706")
    pos_items = [
        ("4.1", "¿Qué valor tiene el dígito 7 en el número 745?", "R: ________ unidades (o ________ centenas)"),
        ("4.2", "Descompón aditivamente el número 839:", "R: ________ + ________ + ________"),
        ("4.3", "¿Qué número se forma con 6 Centenas, 0 Decenas y 4 Unidades?", "R: ________"),
        ("4.4", "En el número 528, ¿cuál es el dígito de las decenas y cuánto vale?", "R: Dígito: _____ / Valor: _____"),
        ("4.5", "Descompón según su nombre de posición el número 916:", "R: ___C + ___D + ___U")
    ]
    y_pos = 286
    for num, enunc, resp in pos_items:
        c.setFillColor(colors.HexColor("#FFFBEB"))
        c.setStrokeColor(colors.HexColor("#FDE68A"))
        c.roundRect(36, y_pos, 540, 24, 4, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#92400E"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(44, y_pos + 7.5, f"{num})")
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawString(68, y_pos + 7.5, enunc)
        c.setFont("Helvetica-Bold", 8)
        c.drawRightString(564, y_pos + 7.5, resp)
        y_pos -= 28

    c.showPage()

    # =========================================================================
    # PÁGINA 2: OPERATORIA Y PROBLEMAS (RESTAS, MULTIPLICACIÓN Y RESOLUCIÓN)
    # =========================================================================
    draw_header(c, "✏️ GUÍA OFICIAL DE MATEMÁTICAS — 3° BÁSICO", "Módulo 1: Numeración y Operatoria Vertical (Parte 2)", 2, 8)

    # I. Restas Verticales (5 ejercicios) - CERO PISTAS DE CANJE
    draw_section_banner(c, 692, "➖ I. RESTAS VERTICALES (5 EJERCICIOS)", "#DC2626")
    restas = [
        (785, 341, "1.1"),
        (964, 523, "1.2"),
        (600, 238, "1.3"),
        (800, 456, "1.4"),
        (742, 385, "1.5")
    ]
    y_res = 592
    for idx, (n1, n2, lbl) in enumerate(restas):
        bx = 36 + idx * 109
        c.setFillColor(colors.HexColor("#B91C1C"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(bx + 4, y_res + 96, lbl)
        draw_cdu_box(c, bx, y_res, 102, 92, "-", n1, n2)

    # II. Multiplicaciones (5 ejercicios)
    draw_section_banner(c, 560, "✖️ II. MULTIPLICACIONES POR 1 DÍGITO (5 EJERCICIOS)", "#7C3AED")
    mults = [
        (32, 3, "2.1"),
        (41, 2, "2.2"),
        (23, 3, "2.3"),
        (54, 2, "2.4"),
        (30, 3, "2.5")
    ]
    y_mul = 484
    for idx, (m1, m2, lbl) in enumerate(mults):
        bx = 36 + idx * 109
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.roundRect(bx, y_mul, 102, 68, 5, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#6D28D9"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(bx + 6, y_mul + 54, lbl)

        c.setFont("Courier-Bold", 12)
        c.setFillColor(colors.HexColor("#0F172A"))
        c.drawCentredString(bx + 51, y_mul + 34, f"{m1}  x  {m2}")
        c.setStrokeColor(colors.HexColor("#64748B"))
        c.setLineWidth(1.2)
        c.line(bx + 20, y_mul + 26, bx + 82, y_mul + 26)

        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#94A3B8"))
        c.rect(bx + 28, y_mul + 6, 46, 16, fill=1, stroke=1)

    # III. Problemas de Aplicación (5 problemas formativos - Formato Cuaderno)
    draw_section_banner(c, 452, "📝 III. RESOLUCIÓN DE PROBLEMAS (5 PROBLEMAS FORMATIVOS)", "#0284C7")
    problemas = [
        ("3.1", "Martina compró 4 cajas con 5 lápices de colores cada una. ¿Cuántos lápices tiene en total?"),
        ("3.2", "En una biblioteca escolar hay 458 libros de cuentos y llegan 235 libros nuevos. ¿Cuántos libros hay en total ahora?"),
        ("3.3", "Tomás tenía $750 ahorrados y gastó $320 en un jugo. ¿Cuánto dinero le queda a Tomás?"),
        ("3.4", "Un agricultor recolectó 600 manzanas rojas y vendió 238 en la feria matutina. ¿Cuántas manzanas le quedan por vender?"),
        ("3.5", "En 3° Básico hay 3 salas y cada una tiene 22 estudiantes. ¿Cuántos estudiantes hay en total en el nivel?")
    ]
    y_pb = 372
    col_w = 170
    for num, enunc in problemas:
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.roundRect(36, y_pb, 540, 74, 5, fill=1, stroke=1)

        c.setFillColor(colors.HexColor("#0284C7"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(42, y_pb + 62, f"{num})")
        c.setFont("Helvetica", 7.8)
        c.setFillColor(colors.HexColor("#0F172A"))
        c.drawString(60, y_pb + 62, enunc)

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

        y_pb -= 80

    c.showPage()

    # =========================================================================
    # PÁGINA 3: EL TIEMPO Y LOS RELOJES (5 RELOJES + 5 CONVERSIONES + 5 INTERVALOS)
    # =========================================================================
    draw_header(c, "⏰ EVALUACIÓN: EL TIEMPO Y LOS RELOJES", "Módulo 2: Relojes Análogos, Conversión 24h e Intervalos de Tiempo", 3, 8)

    # I. Relojes Análogos (5 ejercicios) - CERO PISTAS EN EL TÍTULO
    draw_section_banner(c, 692, "🕒 I. LECTURA DE RELOJES ANÁLOGOS (5 RELOJES ILUSTRADOS)", "#7C3AED")
    relojes = [
        (7, 0, "Reloj 1"),
        (2, 30, "Reloj 2"),
        (9, 15, "Reloj 3"),
        (4, 45, "Reloj 4"),
        (11, 10, "Reloj 5")
    ]
    y_rel = 586
    for idx, (h, m, lbl) in enumerate(relojes):
        bx = 36 + idx * 109
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.roundRect(bx, y_rel, 102, 98, 5, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#6D28D9"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(bx + 6, y_rel + 86, lbl)
        draw_clock(c, bx + 51, y_rel + 48, 30, hour=h, minute=m)
        c.setFont("Helvetica", 7.5)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawCentredString(bx + 51, y_rel + 8, "Hora: ____ : ____")

    # II. Conversión de Horas (5 ejercicios)
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

    # III. Intervalos de Tiempo (5 ejercicios)
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
    # PÁGINA 4: GEOMETRÍA (ÁNGULOS, TRIÁNGULOS Y CUERPOS 3D CON ILUSTRACIONES)
    # =========================================================================
    draw_header(c, "📐 EVALUACIÓN DE MATEMÁTICAS: GEOMETRÍA", "Módulo 3: Ángulos, Triángulos y Cuerpos 3D Ilustrados", 4, 8)

    # I. Ángulos (5 ejercicios)
    draw_section_banner(c, 692, "📐 I. ÁNGULOS: CLASIFICACIÓN Y MEDICIÓN (5 EJERCICIOS)", "#7C3AED")
    y_ang = 612
    angulos_graf = [
        ("1.1 Ángulo A", 90),
        ("1.2 Ángulo B", 45),
        ("1.3 Ángulo C", 135)
    ]
    for idx, (lbl, val) in enumerate(angulos_graf):
        bx = 36 + idx * 180
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.roundRect(bx, y_ang, 172, 74, 5, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#6D28D9"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(bx + 6, y_ang + 62, lbl)

        # Dibujo del ángulo
        c.setStrokeColor(colors.HexColor("#1E3A8A"))
        c.setLineWidth(2)
        if val == 90:
            c.line(bx + 26, y_ang + 14, bx + 26, y_ang + 50)
            c.line(bx + 26, y_ang + 14, bx + 64, y_ang + 14)
            c.setStrokeColor(colors.HexColor("#DC2626"))
            c.rect(bx + 26, y_ang + 14, 9, 9, fill=0, stroke=1)
        elif val == 45:
            c.line(bx + 20, y_ang + 14, bx + 52, y_ang + 46)
            c.line(bx + 20, y_ang + 14, bx + 62, y_ang + 14)
            c.setStrokeColor(colors.HexColor("#2563EB"))
            c.arc(bx + 12, y_ang + 6, bx + 28, y_ang + 22, 0, 50)
        else:
            c.line(bx + 42, y_ang + 14, bx + 16, y_ang + 44)
            c.line(bx + 42, y_ang + 14, bx + 74, y_ang + 14)
            c.setStrokeColor(colors.HexColor("#059669"))
            c.arc(bx + 32, y_ang + 4, bx + 52, y_ang + 24, 0, 135)

        c.setFont("Helvetica", 7.5)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawString(bx + 78, y_ang + 38, "Clasificación:")
        c.drawString(bx + 78, y_ang + 22, "____________")

    # 1.4 y 1.5 preguntas teóricas
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.setStrokeColor(colors.HexColor("#E2E8F0"))
    c.roundRect(36, 574, 540, 32, 4, fill=1, stroke=1)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(colors.HexColor("#1E293B"))
    c.drawString(44, 592, "1.4) ¿Cuántos ángulos rectos (90°) tiene una hoja de cuaderno o puerta rectangular?: R: ________ ángulos.")
    c.drawString(44, 580, "1.5) A las 3:00 en punto, el minutero y el horario forman un ángulo: R: ________________________")

    # II. Triángulos (5 ejercicios con 4 ilustraciones)
    draw_section_banner(c, 546, "🔺 II. CLASIFICACIÓN DE TRIÁNGULOS (5 EJERCICIOS ILUSTRADOS)", "#2563EB")
    triang_cards = [
        ("2.1 Equilátero", "draw_equil"),
        ("2.2 Isósceles", "draw_iso"),
        ("2.3 Escaleno", "draw_scal"),
        ("2.4 Rectángulo", "draw_rect")
    ]
    y_tr = 464
    for idx, (lbl, func_name) in enumerate(triang_cards):
        bx = 36 + idx * 135
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.roundRect(bx, y_tr, 128, 76, 5, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#1D4ED8"))
        c.setFont("Helvetica-Bold", 7.2)
        c.drawString(bx + 6, y_tr + 64, lbl)

        # Dibujar figura
        if func_name == "draw_equil":
            draw_triangle_equil(c, bx + 64, y_tr + 34, s=30)
        elif func_name == "draw_iso":
            draw_triangle_iso(c, bx + 64, y_tr + 34, w=24, h=32)
        elif func_name == "draw_scal":
            draw_triangle_scal(c, bx + 64, y_tr + 34, w=34, h=26)
        elif func_name == "draw_rect":
            draw_triangle_rect(c, bx + 64, y_tr + 34, w=30, h=28)

        c.setFont("Helvetica", 7)
        c.setFillColor(colors.HexColor("#1E293B"))
        c.drawCentredString(bx + 64, y_tr + 8, "Tipo: ________________")

    # 2.5 Elementos del triángulo
    c.setFillColor(colors.HexColor("#EFF6FF"))
    c.setStrokeColor(colors.HexColor("#BFDBFE"))
    c.roundRect(36, 434, 540, 24, 4, fill=1, stroke=1)
    c.setFont("Helvetica", 7.8)
    c.setFillColor(colors.HexColor("#1E40AF"))
    c.drawString(44, 442, "2.5) ¿Cuántos lados, vértices y ángulos interiores tiene cualquier triángulo?:  R: ___ lados, ___ vértices y ___ ángulos.")

    # III. Cuerpos Geométricos 3D (5 ejercicios con ILUSTRACIONES VECTORIALES ISOMÉTRICAS)
    draw_section_banner(c, 404, "📦 III. CUERPOS GEOMÉTRICOS 3D (5 EJERCICIOS CON FIGURAS 3D)", "#059669")
    c3d_list = [
        ("3.1 CUBO", "cube"),
        ("3.2 PRISMA RECT.", "prism"),
        ("3.3 PIRÁMIDE", "pyramid"),
        ("3.4 CILINDRO", "cylinder"),
        ("3.5 ESFERA", "sphere")
    ]
    y_c3 = 260
    for idx, (name, shape) in enumerate(c3d_list):
        bx = 36 + idx * 109
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.roundRect(bx, y_c3, 102, 138, 5, fill=1, stroke=1)

        c.setFillColor(colors.HexColor("#065F46"))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(bx + 51, y_c3 + 126, name)

        # Dibujo 3D
        if shape == "cube":
            draw_cube(c, bx + 51, y_c3 + 92, s=30)
            c.setFont("Helvetica", 7)
            c.setFillColor(colors.HexColor("#1E293B"))
            c.drawString(bx + 8, y_c3 + 52, "• Caras: _________")
            c.drawString(bx + 8, y_c3 + 34, "• Vértices: _______")
            c.drawString(bx + 8, y_c3 + 16, "• Aristas: _______")
        elif shape == "prism":
            draw_prism(c, bx + 51, y_c3 + 92, w=36, h=22, d=14)
            c.setFont("Helvetica", 7)
            c.setFillColor(colors.HexColor("#1E293B"))
            c.drawString(bx + 8, y_c3 + 52, "• Caras: _________")
            c.drawString(bx + 8, y_c3 + 34, "• Vértices: _______")
            c.drawString(bx + 8, y_c3 + 16, "• Aristas: _______")
        elif shape == "pyramid":
            draw_pyramid(c, bx + 51, y_c3 + 92, w=32, h=30)
            c.setFont("Helvetica", 7)
            c.setFillColor(colors.HexColor("#1E293B"))
            c.drawString(bx + 8, y_c3 + 52, "• Caras: _________")
            c.drawString(bx + 8, y_c3 + 34, "• Vértices: _______")
            c.drawString(bx + 8, y_c3 + 16, "• Aristas: _______")
        elif shape == "cylinder":
            draw_cylinder(c, bx + 51, y_c3 + 92, r=14, h=26)
            c.setFont("Helvetica", 7)
            c.setFillColor(colors.HexColor("#1E293B"))
            c.drawString(bx + 8, y_c3 + 52, "• C. Planas: _____")
            c.drawString(bx + 8, y_c3 + 34, "• C. Curvas: _____")
            c.drawString(bx + 8, y_c3 + 16, "• ¿Rueda?: ______")
        elif shape == "sphere":
            draw_sphere(c, bx + 51, y_c3 + 92, r=16)
            c.setFont("Helvetica", 7)
            c.setFillColor(colors.HexColor("#1E293B"))
            c.drawString(bx + 8, y_c3 + 52, "• C. Planas: _____")
            c.drawString(bx + 8, y_c3 + 34, "• Vértices: _______")
            c.drawString(bx + 8, y_c3 + 16, "• ¿Rueda?: ______")

    c.showPage()

    # =========================================================================
    # PÁGINA 5: DATOS Y GRÁFICOS (PARTE 1: PICTOGRAMAS 1 Y 2)
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
    c.drawString(46, y_p1 + 25, "1.2) ¿Qué mes tuvo la MENOR cantidad de lecturas?: __________________.")
    c.drawString(46, y_p1 + 12, "1.3) ¿Cuántos libros MÁS se leyeron en Abril que en Marzo?: ________ libros.")
    c.drawString(300, y_p1 + 38, "1.4) ¿Cuántos libros se leyeron en Junio?: ________ libros.")
    c.drawString(300, y_p1 + 25, "1.5) ¿Cuántos libros se leyeron en TOTAL durante los 4 meses?: ________ libros.")

    # Pictograma 2: Manzanas (Clave = 5)
    draw_section_banner(c, 520, "🍎 PICTOGRAMA 2: COSECHA DE MANZANAS EN EL HUERTO (5 PREGUNTAS)", "#059669")
    y_p2 = 376
    c.setFillColor(colors.HexColor("#FFFFFF"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.roundRect(36, y_p2, 540, 136, 6, fill=1, stroke=1)

    c.setFillColor(colors.HexColor("#F0FDF4"))
    c.setStrokeColor(colors.HexColor("#4ADE80"))
    c.roundRect(370, y_p2 + 114, 196, 16, 4, fill=1, stroke=1)
    c.setFillColor(colors.HexColor("#065F46"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(380, y_p2 + 119, "🔑 CLAVE: Cada 🍎 = 5 manzanas cosechadas")

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
    # PÁGINA 6: DATOS Y GRÁFICOS (PARTE 2: GRÁFICOS DE BARRAS 1 Y 2)
    # =========================================================================
    draw_header(c, "📊 EVALUACIÓN: GRÁFICOS DE BARRAS", "Módulo 4: Análisis de Gráficos de Barras con Escalas Graduadas", 6, 8)

    # Gráfico de Barras 1: Deportes (Escala de 5 en 5)
    draw_section_banner(c, 692, "⚽ GRÁFICO DE BARRAS 1: DEPORTE FAVORITO (ESCALA DE 5 EN 5)", "#4F46E5")
    y_b1 = 502
    c.setFillColor(colors.HexColor("#FFFFFF"))
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.roundRect(36, y_b1, 540, 182, 6, fill=1, stroke=1)

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

    c.setFont("Helvetica", 7.5)
    c.drawString(290, y_b2 + 150, "4.1) ¿Cuántas familias tienen Gato como mascota?:")
    c.drawString(306, y_b2 + 136, "R: ________ familias.")
    c.drawString(290, y_b2 + 118, "4.2) ¿Cuál es la mascota con MAYOR presencia?:")
    c.drawString(306, y_b2 + 104, "R: ___________________________________")
    c.drawString(290, y_b2 + 86, "4.3) ¿Cuántos Perros MÁS hay en comparación con los Canarios?:")
    c.drawString(306, y_b2 + 72, "R: ________ perros más.")
    c.drawString(290, y_b2 + 54, "4.4) ¿Cuál es la mascota con MENOS menciones?:")
    c.drawString(306, y_b2 + 40, "R: ___________________________________")
    c.drawString(290, y_b2 + 22, "4.5) ¿Cuántas mascotas hay registradas en TOTAL?:")
    c.drawString(306, y_b2 + 8, "R: ________ mascotas en total.")

    c.showPage()

    # =========================================================================
    # PÁGINAS 7 Y 8: SOLUCIONARIO OFICIAL PARA PADRES Y APODERADOS
    # =========================================================================
    draw_header(c, "🔑 SOLUCIONARIO COMPLETO (PARTE 1 / PÁGS 1 A 3)", "Pauta de Corrección y Respuestas Exactas para Apoderados", 7, 8)

    y_s1 = 688
    def draw_sol_block(title, lines, color_code="#1E3A8A"):
        nonlocal y_s1
        c.setFillColor(colors.HexColor(color_code))
        c.roundRect(36, y_s1, 540, 16, 3, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(42, y_s1 + 4, title)
        y_s1 -= 14

        box_h = len(lines) * 14 + 10
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.roundRect(36, y_s1 - box_h, 540, box_h, 4, fill=1, stroke=1)
        c.setFont("Helvetica", 7.5)
        c.setFillColor(colors.HexColor("#0F172A"))

        curr_ly = y_s1 - 12
        for l in lines:
            c.drawString(46, curr_ly, l)
            curr_ly -= 14
        y_s1 -= (box_h + 12)

    draw_sol_block("MÓDULO 1: OPERATORIA Y NUMERACIÓN (PÁGINA 1)", [
        "I. Antecesor y Sucesor: 1.1) 599 < 600 < 601 | 1.2) 498 < 499 < 500 | 1.3) 819 < 820 < 821 | 1.4) 699 < 700 < 701 | 1.5) 349 < 350 < 351",
        "II. Escritura: 2.1) Setecientos cincuenta y tres | 2.2) Seiscientos ocho | 2.3) Novecientos cuarenta y dos | 2.4) Quinientos dieciséis | 2.5) Ochocientos setenta",
        "III. Sumas Verticales: 3.1) 342+154 = 496 | 3.2) 523+261 = 784 | 3.3) 586+247 = 833 | 3.4) 479+385 = 864 | 3.5) 658+196 = 854",
        "IV. Valor Posicional: 4.1) 700 unidades (7 centenas) | 4.2) 800 + 30 + 9 | 4.3) 604 | 4.4) Dígito: 2 / Valor: 20 unidades | 4.5) 9C + 1D + 6U"
    ], "#2563EB")

    draw_sol_block("MÓDULO 1: OPERATORIA Y PROBLEMAS (PÁGINA 2)", [
        "I. Restas Verticales: 1.1) 785 - 341 = 444 | 1.2) 964 - 523 = 441 | 1.3) 600 - 238 = 362 | 1.4) 800 - 456 = 344 | 1.5) 742 - 385 = 357",
        "II. Multiplicaciones: 2.1) 32 x 3 = 96 | 2.2) 41 x 2 = 82 | 2.3) 23 x 3 = 69 | 2.4) 54 x 2 = 108 | 2.5) 30 x 3 = 90",
        "III. Problemas de Aplicación:",
        "  • 3.1) Datos: 4 cajas, 5 lápices c/u | Op: 4 x 5 = 20 | R: Martina tiene 20 lápices en total.",
        "  • 3.2) Datos: 458 libros, 235 libros nuevos | Op: 458 + 235 = 693 | R: Ahora hay 693 libros en total.",
        "  • 3.3) Datos: $750 ahorrados, gastó $320 | Op: 750 - 320 = 430 | R: A Tomás le quedan $430.",
        "  • 3.4) Datos: 600 recolectadas, vendió 238 | Op: 600 - 238 = 362 | R: Le quedan 362 manzanas por vender.",
        "  • 3.5) Datos: 3 salas, 22 alumnos c/u | Op: 3 x 22 = 66 | R: Hay 66 estudiantes en total."
    ], "#DC2626")

    draw_sol_block("MÓDULO 2: EL TIEMPO Y LOS RELOJES (PÁGINA 3)", [
        "I. Relojes Análogos: Reloj 1: 07:00 | Reloj 2: 02:30 | Reloj 3: 09:15 | Reloj 4: 04:45 | Reloj 5: 11:10",
        "II. Conversión Horas: 2.1) 14:00 hrs | 2.2) 17:30 hrs | 2.3) 20:00 hrs | 2.4) 22:15 hrs | 2.5) 5:00 PM",
        "III. Intervalos de Tiempo: 3.1) Faltan 30 min | 3.2) Faltan 30 min | 3.3) Faltan 15 min | 3.4) Han pasado 30 min | 3.5) Faltan 25 min"
    ], "#7C3AED")

    c.showPage()

    # PÁGINA 8: SOLUCIONARIO (PARTE 2 / PÁGS 4 A 6)
    draw_header(c, "🔑 SOLUCIONARIO COMPLETO (PARTE 2 / PÁGS 4 A 6)", "Pauta de Corrección: Geometría y Datos/Gráficos", 8, 8)

    y_s1 = 688
    draw_sol_block("MÓDULO 3: GEOMETRÍA (PÁGINA 4)", [
        "I. Ángulos: 1.1) Recto (90°) | 1.2) Agudo (<90°) | 1.3) Obtuso (>90°) | 1.4) 4 ángulos rectos | 1.5) Ángulo Recto (90°)",
        "II. Triángulos: 2.1) Equilátero | 2.2) Isósceles | 2.3) Escaleno | 2.4) Triángulo Rectángulo | 2.5) 3 lados, 3 vértices y 3 ángulos.",
        "III. Cuerpos Geométricos 3D:",
        "  • 3.1 Cubo: 6 caras cuadradas, 8 vértices, 12 aristas.",
        "  • 3.2 Prisma Rectangular: 6 caras rectangulares, 8 vértices, 12 aristas.",
        "  • 3.3 Pirámide (Base cuadrada): 5 caras (1 base + 4 laterales), 5 vértices, 8 aristas.",
        "  • 3.4 Cilindro: 2 caras planas circulares, 1 superficie curva, SÍ rueda.",
        "  • 3.5 Esfera: 0 caras planas, 0 vértices, 0 aristas, SÍ rueda."
    ], "#059669")

    draw_sol_block("MÓDULO 4: DATOS Y GRÁFICOS (PÁGINAS 5 Y 6)", [
        "I. Pictograma 1 (Libros, Clave = 4):",
        "   1.1) Marzo: 4 x 4 = 16 libros | 1.2) Mayo (2 libros x 4 = 8) | 1.3) 24 - 16 = 8 libros más | 1.4) Junio: 5 x 4 = 20 libros | 1.5) Total: 16+24+8+20 = 68 libros.",
        "II. Pictograma 2 (Manzanas, Clave = 5):",
        "   2.1) Martes: 4 x 5 = 20 manzanas | 2.2) Miércoles (2 x 5 = 10) | 2.3) Jueves (25) - Lunes (15) = 10 manzanas más | 2.4) Jueves (25) | 2.5) Total: 15+20+10+25 = 70 manzanas.",
        "III. Gráfico 1 (Deportes, Escala 5):",
        "   3.1) Fútbol (25 votos) | 3.2) 20 votos | 3.3) 25 - 10 = 15 niños más | 3.4) Atletismo (10 votos) | 3.5) Total: 25+15+20+10 = 70 estudiantes.",
        "IV. Gráfico 2 (Mascotas, Escala 2):",
        "   4.1) Gato: 10 familias | 4.2) Perro (12 menciones) | 4.3) Perro (12) - Canario (4) = 8 perros más | 4.4) Canario (4) | 4.5) Total: 12+10+6+4 = 32 mascotas."
    ], "#0284C7")

    c.save()
    print(f"✅ PDF de 8 páginas generado con éxito: {filename}")


if __name__ == "__main__":
    generate_mega_pdf("guia_estudio_amelia.pdf")

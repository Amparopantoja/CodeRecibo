from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generar_recibo():
    pdf_path = "recibo_de_sueldo.pdf"

    # Crear el documento PDF
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Obtener dimensiones de la página
    w, h = letter
    margen = 60

    logo_path = "LogoWNS.png"
    c.drawInlineImage(logo_path, 55, h-84, width=95, height=35)
    
    estilo_texto = ParagraphStyle(
        'CustomStyle',
        fontSize=6,
        leading=8,  # Ajusta el valor según tu preferencia
        alignment=1,  # Alineación centrada horizontal
        spaceBefore=0,  # Espacio antes del párrafo
        spaceAfter=0,
        parent=getSampleStyleSheet()['BodyText']
    )
        
    # Datos para la tabla
    datos_tabla = [
        ["CUIT: 30-71575322-3"],
        ["Legajo", "", "", "", "", "", "Apellido y Nombre", "", "", "", "", "", "CUIL", "", "","", "", ""],
        ["78", "", "", "", "", "", "Lesnichevsky Jonathan", "", "", "", "", "", "20363995722", "", "", "", "", ""],
        ["Sector", "", "", "", "", "", "", "", "Sueldo base", "", "", "Ingreso", "", "", "", "", "", ""],
        ["R. Impositivo-contable", "", "", "", "", "", "", "", "$ -", "", "", "16/11/2023", "", "", "", "", "", ""],
        ["Categoría", "", "", "", "", "", "", "", "Período de Pago", "", "", "16/11/2023", "", "", "", "", "", ""],
        ["0", "", "", "", "", "", "", "", "ene-24", "", "", "16/11/2023", "", "", "", "", "", ""],
        ["Concepto", "", "", "", "", "", "", "Unidad", "", "Remunerativo", "", "", "No remunerativo", "", "", "Total", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["Lugar y fecha de pago:", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["Capital Federal, 29/01/2024", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["Forma de Pago", "", "", "", "", "", "", "", "", "", "", "", "Efectivo", "", "", "Total", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["Fecha", "", "", "", "", "", "", "", "", Paragraph("RECIBÍ EL IMPORTE NETO DE ESTA LIQUIDACIÓN <br /> EN PAGO DE MI REMUNERACIÓN", estilo_texto), "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["Período", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    ]
    
    
    # Calcular el ancho total de la página con margen
    ancho_tabla = w - 2 * margen
    alto_primera_fila = 45
    alto_filas_normales = 15

    # Crear la tabla y aplicar estilos
    tabla = Table(datos_tabla, colWidths=[ancho_tabla/18]*18, rowHeights=[alto_primera_fila] + [alto_filas_normales]*(datos_tabla.__len__()-1))

    estilo_tabla = TableStyle([('SPAN',(0,0),(17,0)),
                               ('SPAN',(8,5),(17,5)),
                               ('SPAN',(8,6),(17,6)),
                               ('SPAN',(0,7),(6,7)),
                               ('SPAN',(7,7),(8,7)),
                               ('SPAN',(9,7),(11,7)),
                               ('SPAN',(12,7),(14,7)),
                               ('SPAN',(15,7),(17,7)),
                               ('SPAN',(0,24),(8,24)),
                               ('SPAN',(9,24),(11,25)),
                               ('SPAN',(12,24),(14,25)),
                               ('SPAN',(15,24),(17,25)),
                               ('SPAN',(0,25),(8,25)),
                               ('SPAN',(0,28),(4,29)),     
                               ('SPAN',(5,28),(8,29)),
                               ('SPAN',(9,28),(17,31)),
                               ('SPAN',(5,29),(8,29)),
                               ('SPAN',(9,29),(17,29)),
                               ('SPAN',(0,30),(4,31)),
                               ('SPAN',(5,30),(8,31)), 
                               ('SPAN',(9,30),(17,30)),
                               ('BACKGROUND', (0, 24), (8, 24), (0.8, 0.8, 0.8)),
                               ('BACKGROUND', (0, 26), (-1, 26), (0.8, 0.8, 0.8)),
                               ('BACKGROUND', (0, 27), (4, 31), (0.8, 0.8, 0.8)),
                               ('ALIGN', (0, 0), (-1, 0), 'RIGHT'),
                               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                               ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('FONTSIZE', (8, 28), (17, 30), 6),
                               ('VALIGN', (8, 28), (17, 30), 'TOP'),
                               ('GRID', (0, 0), (-1, 7), 0.5, colors.black),
                               ('BOX', (7, 0), (8, -1), 1, colors.black),
                               ('BOX', (0, 0), (7, -1), 1, colors.black),
                               ('BOX', (9, 0), (11, -1), 1, colors.black),
                               ('BOX', (12, 0), (14, -1), 1, colors.black),
                               ('BOX', (15, 0), (17, -1), 1, colors.black),
                               ('GRID', (0, 24), (-1, -1), 0.5, colors.black)
                            ])

    for i in range(8, 24):
        estilo_tabla.add('SPAN', (0, i), (6, i))
        estilo_tabla.add('SPAN', (7, i), (8, i))
        estilo_tabla.add('SPAN', (9, i), (11, i))
        estilo_tabla.add('SPAN', (12, i), (14, i))
        estilo_tabla.add('SPAN', (15, i), (17, i))
    
    #Dividir la linea en tres partes iguales
    for i in range(1, 3):
        estilo_tabla.add('SPAN',(0,i),(5,i))
        estilo_tabla.add('SPAN',(6,i),(11,i))
        estilo_tabla.add('SPAN',(12,i),(17,i))
        
    for i in range(3, 7):    
        estilo_tabla.add('SPAN',(0,i),(7,i)),
        
    for i in range(26, 28):
        estilo_tabla.add('SPAN',(0,i),(4,i)),
        estilo_tabla.add('SPAN',(5,i),(6,i)),
        estilo_tabla.add('SPAN',(7,i),(8,i)),
        estilo_tabla.add('SPAN',(9,i),(11,i)),
        estilo_tabla.add('SPAN',(12,i),(14,i)),
        estilo_tabla.add('SPAN',(15,i),(17,i))
    
    for i in range(3, 5):
        estilo_tabla.add('SPAN',(8,i),(10,i)),
        estilo_tabla.add('SPAN',(11,i),(13,i)),
        estilo_tabla.add('SPAN',(14,i),(17,i))
        
    for i in range(1, 8, 2):
        estilo_tabla.add('BACKGROUND', (0, i), (-1, i), (0.8, 0.8, 0.8))
    
    tabla.setStyle(estilo_tabla)

    c.line(w-130, h-550, w-250, h-550)
    # Dibujar la tabla en el PDF
    tabla.wrapOn(c, 0, 0)
    tabla.drawOn(c, 50, h-90-((datos_tabla.__len__()-1)*15))

    # Guardar el PDF
    c.save()

generar_recibo()

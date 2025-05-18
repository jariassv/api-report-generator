from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generar_pdf(dataframe):
    dataframe['Ingreso'] = dataframe['Cantidad'] * dataframe['PrecioUnitario']

    total_ventas = dataframe['Cantidad'].sum()
    total_ingresos = dataframe['Ingreso'].sum()
    producto_mas_vendido = dataframe.groupby('Producto')['Cantidad'].sum().idxmax()
    producto_mayor_ingreso = dataframe.groupby('Producto')['Ingreso'].sum().idxmax()
    promedio_por_producto = dataframe.groupby('Producto')['Cantidad'].mean().mean()

    top_cantidad = dataframe.groupby('Producto')['Cantidad'].sum().nlargest(3)
    top_ingreso = dataframe.groupby('Producto')['Ingreso'].sum().nlargest(3)

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750

    c.drawString(50, y, "Resumen de Ventas")
    y -= 30
    c.drawString(50, y, f"Total de unidades vendidas: {total_ventas}")
    y -= 20
    c.drawString(50, y, f"Ingreso total: ${total_ingresos:.2f}")
    y -= 20
    c.drawString(50, y, f"Producto más vendido: {producto_mas_vendido}")
    y -= 20
    c.drawString(50, y, f"Producto con mayor ingreso: {producto_mayor_ingreso}")
    y -= 20
    c.drawString(50, y, f"Promedio de unidades por producto: {promedio_por_producto:.2f}")
    y -= 40

    c.drawString(50, y, "Top 3 productos por cantidad:")
    y -= 20
    for prod, val in top_cantidad.items():
        c.drawString(70, y, f"{prod}: {val} unidades")
        y -= 20

    y -= 10
    c.drawString(50, y, "Top 3 productos por ingreso:")
    y -= 20
    for prod, val in top_ingreso.items():
        c.drawString(70, y, f"{prod}: ${val:.2f}")
        y -= 20

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

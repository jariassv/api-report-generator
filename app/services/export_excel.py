import pandas as pd
import io

def generar_excel(dataframe):
    dataframe['Ingreso'] = dataframe['Cantidad'] * dataframe['PrecioUnitario']

    total_ventas = dataframe['Cantidad'].sum()
    total_ingresos = dataframe['Ingreso'].sum()
    producto_mas_vendido = dataframe.groupby('Producto')['Cantidad'].sum().idxmax()
    producto_mayor_ingreso = dataframe.groupby('Producto')['Ingreso'].sum().idxmax()
    promedio_por_producto = dataframe.groupby('Producto')['Cantidad'].mean().mean()

    top_productos_cantidad = dataframe.groupby('Producto')['Cantidad'].sum().nlargest(3).reset_index()
    top_productos_cantidad.columns = ['Producto', 'Cantidad Total']

    top_productos_ingreso = dataframe.groupby('Producto')['Ingreso'].sum().nlargest(3).reset_index()
    top_productos_ingreso.columns = ['Producto', 'Ingreso Total']

    ventas_por_dia = dataframe.groupby('Fecha')['Cantidad'].sum().reset_index()
    ventas_por_dia.columns = ['Fecha', 'Total Vendido']

    resumen = pd.DataFrame({
        'Total Ventas': [total_ventas],
        'Ingreso Total': [total_ingresos],
        'Producto Más Vendido': [producto_mas_vendido],
        'Producto Mayor Ingreso': [producto_mayor_ingreso],
        'Promedio por Producto': [promedio_por_producto]
    })

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        dataframe.to_excel(writer, sheet_name='Ventas', index=False)
        resumen.to_excel(writer, sheet_name='Resumen', index=False)
        top_productos_cantidad.to_excel(writer, sheet_name='Top Cantidad', index=False)
        top_productos_ingreso.to_excel(writer, sheet_name='Top Ingreso', index=False)
        ventas_por_dia.to_excel(writer, sheet_name='Ventas Diarias', index=False)

    output.seek(0)
    return output

from flask import request, jsonify, send_file
import pandas as pd
import io
from datetime import datetime
from app.services.export_excel import generar_excel
from app.services.export_pdf import generar_pdf

def register_routes(app):

    @app.route('/')
    def home():
        return "API de Generación de Reportes. Usa el endpoint /report?format=excel o /report?format=pdf con un archivo CSV."

    @app.route('/report', methods=['POST'])
    def report():
        if 'file' not in request.files:
            return jsonify({'error': 'Archivo no proporcionado'}), 400

        formato = request.args.get('format', 'excel')
        file = request.files['file']

        try:
            df = pd.read_csv(file)
            required_cols = {'Fecha', 'Producto', 'Cantidad', 'PrecioUnitario'}
            if not required_cols.issubset(df.columns):
                return jsonify({'error': 'El archivo debe contener las columnas: Fecha, Producto, Cantidad, PrecioUnitario'}), 400

            if formato == 'pdf':
                pdf_file = generar_pdf(df)
                nombre_archivo = f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
                return send_file(
                    pdf_file,
                    download_name=nombre_archivo,
                    as_attachment=True,
                    mimetype='application/pdf'
                )
            else:
                excel_file = generar_excel(df)
                nombre_archivo = f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
                return send_file(
                    excel_file,
                    download_name=nombre_archivo,
                    as_attachment=True,
                    mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )

        except Exception as e:
            return jsonify({'error': str(e)}), 500

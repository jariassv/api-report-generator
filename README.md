# 📊 API Report Generator

API REST en Python para generar reportes inteligentes a partir de archivos CSV con datos de ventas. Permite exportar reportes en formato **Excel** o **PDF**, incluyendo métricas claves como producto más vendido, ingreso total, y más.

---

## 🚀 Funcionalidades principales

✅ Procesamiento de archivos CSV  
✅ Cálculo automático de métricas de negocio  
✅ Exportación en formato Excel (`.xlsx`) o PDF (`.pdf`)  
✅ Modular y listo para integración con frontend (React, etc.)

---

## 🏗️ Estructura del Proyecto

```
api-report-generator/
├── app/
│   ├── main.py               # Inicia la app Flask
│   ├── routes.py             # Endpoints de la API
│   ├── services/
│   │   ├── export_excel.py   # Lógica para Excel
│   │   └── export_pdf.py     # Lógica para PDF
│   └── __init__.py
├── requirements.txt
├── README.md
├── sample_data/
│   └── ventas.csv
```

---

## ⚙️ Instalación

```bash
# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # en Windows

# Instalar dependencias
pip install -r requirements.txt
```

---

## ▶️ Uso

### Ejecutar la aplicación:

```bash
python -m app.main
```

La API se ejecuta por defecto en:  
`http://127.0.0.1:5000`

---

### Enviar archivo vía Postman o `curl`:

#### Formato Excel:
```bash
curl -X POST -F "file=@sample_data/ventas.csv" "http://127.0.0.1:5000/report?format=excel" --output reporte.xlsx
```

#### Formato PDF:
```bash
curl -X POST -F "file=@sample_data/ventas.csv" "http://127.0.0.1:5000/report?format=pdf" --output reporte.pdf
```

---

## 📈 Métricas generadas

- Total de unidades vendidas  
- Ingreso total  
- Producto más vendido  
- Producto con mayor ingreso  
- Promedio por producto  
- Top 3 productos por cantidad  
- Top 3 productos por ingreso  
- Ventas por día

---

## 🧱 Requisitos del CSV

Tu archivo debe tener como mínimo las siguientes columnas:

```csv
Fecha,Producto,Cantidad,PrecioUnitario
```

Ejemplo de datos:
```csv
2024-05-01,Hamburguesa,10,3.5
2024-05-02,Gaseosa,15,1.5
```

---

## 🛠️ Tecnologías usadas

- Python
- Flask
- Pandas
- OpenPyXL
- ReportLab

---

## 📌 Pendientes / Futuras mejoras

- Exportación combinada con gráficos
- Carga desde bases de datos
- Interfaz web con React o Streamlit
- Autenticación JWT para proteger endpoints

---

## 👤 Autor

**jarias**

## 📜 Licencia

MIT License

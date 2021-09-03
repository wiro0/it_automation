#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

car_list = [{
        "id": 47,
        "car": {
                "car_make": "Lamborghini",
                "car_model": "Murciélago",
                "car_year": 2002
        },
        "price": "$13724.05",
        "total_sales": 149
},
{       "id": 48,
        "car": {
                "car_make": "Lamborghini",
                "car_model": "Murciélago",
                "car_year": 2003
        },
        "price": "$13724.05",
        "total_sales": 149
}]

full_list = []
for item in car_list:
    car_data = []
    for key, value in item.items():
        if key == "car":
            full_name = ""
            for k, v in value.items():
                full_name = full_name + " " + str(v)
            value = full_name.strip()
        car_data.append([key, value])
    full_list.append(car_data)

# PDF location
report = SimpleDocTemplate("/tmp/report.pdf")
# PDF Style
styles = getSampleStyleSheet()

# PDF Title
report_title = Paragraph("A Complete Inventory of the Cars", styles["h1"])

# Table with content
table_data = []
for item in full_list:
    print("Len item:", len(item), item)
    for a, b in item:
        table_data.append([a, b])
# Tale style
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report.build([report_title, report_table])

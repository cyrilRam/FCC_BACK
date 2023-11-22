from io import BytesIO

import pandas as pd
from PyPDF2 import PdfMerger
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf_content(student, resultat):
    pdf_buffer = BytesIO()
    pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=letter)

    pdf_canvas.drawString(50, 750, f"Nom de l'élève: {student.nom}")
    pdf_canvas.drawString(50, 730, f"Prénom de l'élève: {student.prenom}")
    pdf_canvas.drawString(50, 710, f"age: {student.age}")

    pdf_canvas.drawString(50, 690, "Liste des notes:")
    y_position = 670

    for row in resultat.itertuples():
        pdf_canvas.drawString(70, y_position, f"Note: {row[6]}")
        y_position -= 20

    pdf_canvas.save()

    pdf_buffer.seek(0)
    return pdf_buffer


def merge_pdfs(students, df_resultats, df_students):
    # Générer et fusionner les PDF pour plusieurs étudiants
    merger = PdfMerger()

    merg_df = pd.merge(df_students, df_resultats, on=['nom', 'prenom'])

    for student in students:
        # resultat = pd.merge(df_students[condition], df_resultats, on=['nom', 'prenom'], how='inner')
        resultat = merg_df[merg_df['id'] == student.id]
        if not resultat.empty:
            try:
                pdf_content = generate_pdf_content(student, resultat)
                merger.append(pdf_content)
            except Exception as e:
                print(f"Une erreur s'est produite : {e}")

    # Crée un objet BytesIO pour le PDF fusionné
    merged_pdf_content = BytesIO()
    merger.write(merged_pdf_content)
    merger.close()

    merged_pdf_content.seek(0)

    return merged_pdf_content

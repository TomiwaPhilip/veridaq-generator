from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import PyPDF2
import qrcode
import io
from flask import send_file

def generateDocVerification(
        nameOfOrganization, nameOfIndividual, documentType, documentName, documentID, moreInfo,
        nameOfAdmin, adminDesignation, currentDateTime, badgeID
):
    # Load existing PDF
    existing_pdf = 'Veridaq_Badges/doc_template.pdf'  # Path to existing PDF file
    output_pdf = 'generated_badges/doc_pdf.pdf'

    # Register Montserrat font
    montserrat_font_path = 'static/Montserrat-ExtraBold.ttf'  # Path to Montserrat font file
    pdfmetrics.registerFont(TTFont("Montserrat-ExtraBold", montserrat_font_path))
    montserrat_font_path = 'static/Montserrat-Bold.ttf'  # Path to Montserrat font file
    pdfmetrics.registerFont(TTFont("Montserrat-Bold", montserrat_font_path))
    montserrat_font_path = 'static/Montserrat-Regular.ttf'  # Path to Montserrat font file
    pdfmetrics.registerFont(TTFont("Montserrat-Regular", montserrat_font_path))
    montserrat_font_path = 'static/Montserrat-Italic.ttf'  # Path to Montserrat font file
    pdfmetrics.registerFont(TTFont("Montserrat-Italic", montserrat_font_path))

    # Open the modified PDF
    with open(existing_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        # Get the first (and only) page of the PDF
        page = reader.pages[0]

        # Create a canvas to draw on the page
        packet = io.BytesIO()
        c = canvas.Canvas(packet)

        # Set font to Montserrat and font size
        c.setFont("Montserrat-ExtraBold", 12)

        # Set text color to white
        c.setFillColor("white")  # White color

        # Draw "Hello" on the page
        c.drawString(23.04, 762.08, nameOfOrganization)
        c.drawString(23.04, 690.64, nameOfIndividual)

        montserrat_font_path = 'static/Montserrat-Regular.ttf'  # Path to Montserrat font file
        pdfmetrics.registerFont(TTFont("Montserrat2", montserrat_font_path))
        c.setFont("Montserrat2", 14)
        c.setFillColor("black") 

        c.drawString(199.4, 547, documentType)
        c.drawString(199.4, 519, documentName)
        c.drawString(199.4, 491, documentID)
        c.drawString(199.4, 465, "True")
        c.drawString(199.4, 438, moreInfo)

        c.setFont("Montserrat-Bold", 14)

        c.drawString(24.48, 234, nameOfOrganization)
        c.drawString(24.48, 212, nameOfAdmin)

        c.setFont("Montserrat-Italic", 14)
        c.drawString(24.48, 192, adminDesignation)
        c.drawString(24.48, 138, currentDateTime)

        c.setFont("Montserrat-Bold", 14)        

        c.setFillColor("white")
        c.drawString(462.24, 816, badgeID)

        # Define the URL template with a placeholder for the badge ID
        url_template = 'http://individual.veridaq.com/auth/credential?id={}'

        # Replace the placeholder in the URL template with the actual badge ID
        url = url_template.format(badgeID)

        # Generate QR code and embed it into the PDF
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=3, border=4)
        qr.add_data(url)  # Replace 'http://your-link.com' with your actual link
        qr.make(fit=True)
        img = qr.make_image(fill_color="black")
        img.save('qrcode/doc_qrcode.png')
        c.drawInlineImage('qrcode/doc_qrcode.png', 410, 123)


        # Save the canvas to the PDF writer
        c.save()

        # Merge the modified page with the existing page
        overlay = PyPDF2.PdfReader(packet)
        page.merge_page(overlay.pages[0])
        writer.add_page(page)

        # Write the modified PDF to a file
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

    # Send the modified PDF as a response
    return send_file(output_pdf, as_attachment=True)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import PyPDF2
import qrcode
import io
from flask import send_file
from flask import send_file
from veridaqRequests.utils import split_text_to_lines, drawLines

def generateIndividualReference(
        individualName, issuerName, relationship, yearsOfRelationship, personalityReview,
        recommendationStatement, issuerDesignation, issuerContact, currentDateTime, badgeID
):
    # Load existing PDF
    existing_pdf = 'Veridaq_Badges/individual_template.pdf'  # Path to existing PDF file
    output_pdf = 'generated_badges/individual_pdf.pdf'

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
        c.setFont("Montserrat-ExtraBold", 20)

        # Set text color to white
        c.setFillColor("white")  # White color

        # Draw "Hello" on the page
        c.drawString(24.48, 752, individualName)
        c.drawString(24.48, 684.16, issuerName)

        c.setFont("Montserrat-Regular", 14)
        c.setFillColor("black") 

        c.drawString(249.84, 545, relationship)
        c.drawString(249.84, 517, yearsOfRelationship)
        lines_1 = split_text_to_lines(personalityReview, max_length=45)
        drawLines(lines_1, 249.84, 460, c)
        lines_2 = split_text_to_lines(recommendationStatement, max_length=45)
        drawLines(lines_2, 249.84, 411, c)  
        # c.drawString(249.84, 460, personalityReview)
        # c.drawString(249.84, 411, recommendationStatement)

        c.setFont("Montserrat-Bold", 14)
        c.drawString(23.04, 203, issuerName)

        c.setFont("Montserrat-Italic", 14)

        c.drawString(24.48, 185, issuerDesignation)
        c.drawString(24.48, 166, issuerContact)
        c.drawString(24.48, 110, currentDateTime)

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
        img.save('qrcode/individual_qrcode.png')
        c.drawInlineImage('qrcode/individual_qrcode.png', 410, 87)


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
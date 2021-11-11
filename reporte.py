from fpdf import FPDF

'''
P : portrait (vertical)
L : landscape (horizontal)
A4 : 210x297mm
'''

pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.add_page()


pdf.rect( x= 1, y= 10,
        w =60, h =30)
pdf.image('PDF\logoecopetrol.jpg',
        x= 3, y= 16,
        w = 50, h = 12 )

pdf.set_font('Arial', '', 0)

# titulo
pdf.cell(51)
pdf.cell(w =148.5, h = 10, txt = 'Reporte', border = 1, ln=1,
         align = 'C', fill =0)





pdf.output('hoja.pdf')
pdf.output('Reporte.pdf')
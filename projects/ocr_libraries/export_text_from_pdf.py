import glob
import pdftotext

# Get all PDF files in the invoices folder
files = glob.glob('invoices/*.pdf')

for i, file in enumerate(files):
    with open(file, 'rb') as f:
        # Raw=True is needed to get text grouped together
        #   which improves the accuracy
        pdf = pdftotext.PDF(f, raw=True)
        text = '\n\n'.join(pdf)
        print(text)


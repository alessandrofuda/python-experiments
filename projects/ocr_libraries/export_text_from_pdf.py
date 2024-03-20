import glob
import pdftotext
import re

data_output = [
    [
        'Invoice number',
        'Invoice date',
        'Total amount',
    ]
]

# Get all PDF files in the invoices folder
files = glob.glob('invoices/*.pdf')

for i, file in enumerate(files):
    with open(file, 'rb') as f:
        # Raw=True is needed to get text grouped together
        #   which improves the accuracy
        pdf = pdftotext.PDF(f, raw=True)
        text = '\n\n'.join(pdf)

        # print(text)

        invoice_number = re.search(r'\s[0-9]{1,3}/[0-9]{2}\n', text).group(0).strip()
        invoice_date = re.search(r'Numero\sData\n+([0-9]{2}-[0-9]{2}-20[0-9]{2})\s+', text).group(1).strip()
        total_amount = re.search(r'€\s+(.*)\n+Totale\s*\n+', text).group(1).strip()

        data_output.append([
            invoice_number,
            invoice_date,
            total_amount,
        ])

    print(data_output)


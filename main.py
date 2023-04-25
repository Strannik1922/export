import tabula


pdf_path='docs/_static/foo.pdf'

dfs = tabula.read_pdf(pdf_path, pages='1', options='--columns 10.1,20.2,30.3')

dfs[0].to_csv('first_table.csv')
tabula.convert_into(pdf_path, 'second_table.csv')


print(dfs)
print("The PDF file has been converted successfully.")

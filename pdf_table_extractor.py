import pdfplumber
import pandas as pd
import argparse

def extract_table(pdf_path, csv_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.append(table)

    dataframes = [pd.DataFrame(table[1:], columns = table[0])for table in tables]
    combined_df = pd.concat(dataframes, ignore_index = True)

    combined_df.to_csv(csv_path, index = False)


def main():
    parser = argparse.ArgumentParser(description = 'Extract table from pdf')
    parser.add_argument('pdf_path', type = str, help = 'Path to input pdf file')
    parser.add_argument('csv_path', type = str, help = 'Name of output file')

    args = parser.parse_args()

    extract_table(args.pdf_path, args.csv_path)

if __name__ == '__main__':
    main()


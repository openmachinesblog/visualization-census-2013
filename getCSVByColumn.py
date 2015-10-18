import io
import zipfile
import csv
import sys

w = csv.writer(open("output-{0}.csv".format(sys.argv[1]), "w"))
w.writerow(["STATE", "PUMA", sys.argv[1]])

# number of rows for ss13husa,ss13husb
row_counts = [756065,720248]

pumaC = 0

for fNr in range(2):
    if (fNr == 0):
        alpha = 'a'
    else:
        alpha = 'b'

    zf = zipfile.ZipFile('ss13hus{0}.csv.zip'.format(alpha))
    f = io.TextIOWrapper(zf.open("ss13hus{0}.csv".format(alpha), "rU"))
    csvf = csv.reader(f)
    header = csvf.next()

    pumaColNr = header.index('PUMA')
    stColNr = header.index('ST')

    colNr = header.index(sys.argv[1])

    for i in range(row_counts[fNr]):
        row=csvf.next()
        puma=row[pumaColNr]
        state=row[stColNr]
        col=row[colNr]
        # ignore N/A entries
        if (col == ''):
            continue

        if (int(puma) == 100 and int(state) == 35):
            pumaC += 1

        col=int(col)
        w.writerow([state,puma,col])

print("PumaC: ",pumaC)

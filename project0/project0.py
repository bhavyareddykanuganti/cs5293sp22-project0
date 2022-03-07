import urllib.request
import urllib
import tempfile
import PyPDF2
import sqlite3
import ssl
import re
###download data###
def fetchincidents(url):
    ssl._create_default_https_context = ssl._create_unverified_context

    headers = {}
    headers['User-Agent'] =  "Chrome/24.0.1312.27 Safari/537.17"

    data = urllib.request.urlopen(url)
    return data
###Extract Data###
def extractincidents(data):

    fp = tempfile.TemporaryFile()

    # Write the pdf data to a temp file
    fp.write(data.read())

    # Set the curser of the file back to the begining
    fp.seek(0)

    # Read the PDF
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    pagecount = pdfReader.getNumPages()

    # Now get all the other pages
    a=[]
    b=[]
    for pagenum in range(0, pagecount):
        pattern = re.compile(r'\d{1,2}[\/]\d{1,2}[\/]\d{4}\s\d{1,2}[\:]\d{1,2}')
        b= pattern.findall(pdfReader.getPage(pagenum).extractText())
        for date in b:
            if date not in a:
                a.append(date)
    result = []

    for pagenum in range(0,pagecount):
        p = pdfReader.getPage(pagenum).extractText().replace("NORMAN POLICE DEPARTMENT", "") \
            .replace("Daily Incident Summary (Public)", "")
        for date in a:
            replaceValue = "$"+date
            p = p.replace(date, replaceValue)
        result.append(p)
    finalOutput = []
    for page in result:
        finalOutput.append(page.replace("\n",",").split('$'))

    c0=[]
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    count=0
    excep=[]
    unknown=[]

    for i in range(0,len(finalOutput)):
        for j in range (0,len(finalOutput[i])):
            b=finalOutput[i][j]
            b= b.strip(",").split(",")
            if len(b) == 5:
                c0.append(b[0])
                c1.append(b[1])
                c2.append(b[2])
                c3.append(b[3])
                c4.append(b[4])
            try:
                if len(b) < 5:
                    unknown.append(b[3])
            except:
                if len(b) < 5 and len(b) >1:
                    count=count+1

            try:
                if len(b) == 6:
                    excep.append(b[4])
            except:
                print('')
            try:
                if len(b) > 6:
                    excep.append(b[4])
            except:
                print('')

    for i in range (0,len(excep)):
        c0.append('Null')
        c1.append('Null')
        c2.append('Null')
        c3.append(excep[i])
        c4.append('Null')
    x=len(c3)
    return c0,c1,c2,c3,c4,x,count

###create database###
def createdb():
    #create db
    con = sqlite3.connect('normanpd.db')
    #create cursor object
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS incidents''')
    table=('''CREATE TABLE IF NOT EXISTS incidents
                (incident_time TEXT,incident_number TEXT,incident_location TEXT,nature TEXT,incident_ori TEXT)''')
    cur.execute(table)
    con.close()
    return 'normanpd.db'

#insert into database
def populatedb(db,c0,c1,c2,c3,c4,x):
    con = sqlite3.connect('normanpd.db')
    # create cursor object
    db = ('''INSERT INTO incidents
             (incident_time,incident_number ,incident_location ,nature ,incident_ori) VALUES(?,?,?,?,?)''')
    cur = con.cursor()
    for i in range(0,x):
        cur.execute(db,(c0[i],c1[i],c2[i],c3[i],c4[i]))
    cur.execute('''SELECT * FROM incidents''')
    rrecords = cur.fetchall()
    con.commit()
    con.close()
    return rrecords

#required output
def status(db,count):
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
    cur.execute('''SELECT Nature,count(*)
                    FROM incidents GROUP BY Nature 
                    ORDER BY count(Nature) DESC, Nature ASC''')
    records = cur.fetchall()
    con.close()
    return records
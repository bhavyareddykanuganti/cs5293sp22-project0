import pytest
import project0
from project0 import project0
import sqlite3
url = "https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-21_daily_incident_summary.pdf"
database = 'normanpd.db'

def test_fetchincidents():
    data = project0.fetchincidents(url)
    assert data is not None

def test_extractincidents():
    data = project0.fetchincidents(url)
    c0,c1,c2,c3,c4,x,count = project0.extractincidents(data)
    assert c0 is not None
    assert c1 is not None
    assert c2 is not None
    assert c3 is not None
    assert c4 is not None
    assert x is not None

def test_createbd():
    db=project0.createdb()
    assert db == database

def test_populatedb():
    data = project0.fetchincidents(url)
    c0,c1,c2,c3,c4,x,count= project0.extractincidents(data)
    db = project0.createdb()
    rrecords=project0.populatedb(db,c0,c1,c2,c3,c4,x)
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.close()
    assert rrecords is not None
    cur.close()

def test_status():
    data = project0.fetchincidents(url)
    c0, c1, c2, c3, c4, x, count = project0.extractincidents(data)
    db = project0.createdb()
    rrecords = project0.populatedb(db, c0, c1, c2, c3, c4, x)
    records=project0.status(db,count)
    assert records is not None
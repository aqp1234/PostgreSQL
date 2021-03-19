import psycopg2

try:
    conn = psycopg2.connect(host="localhost", dbname="testdata", user="", password='')
    cur=conn.cursor()
    cur.execute("copy Concept from '"+__file__+"\..\concept2.csv' delimiter ',' csv header ENCODING 'iso8859-1';")
    cur.execute("copy Person from '"+__file__+"\..\person2.csv' delimiter ',' csv header ENCODING 'iso8859-1';")
    cur.execute("copy Visit_occurrence from '"+__file__+"\..\\visit_occurrence2.csv' delimiter ',' csv header ENCODING 'iso8859-1';")
    cur.execute("copy Condition_occurrence from '"+__file__+"\..\condition_occurrence2.csv' delimiter ',' csv header ENCODING 'iso8859-1';")
    cur.execute("copy Drug_exposure from '"+__file__+"\..\drug_exposure2.csv' delimiter ',' csv header ENCODING 'iso8859-1';")
    cur.execute("copy Death from '"+__file__+"\..\death2.csv' delimiter ',' csv header ENCODING 'iso8859-1';")
    cur.close()
    conn.commit()
    print('success')
    
except Exception as e:
    print(e)


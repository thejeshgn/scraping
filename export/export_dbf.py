#https://pythonhosted.org/dbf/
import dbf
some_table = dbf.from_csv(csvfile='./csv/example.csv', filename='./dbf/example',field_names='test1,test2,id'.split(","), to_disk=True)
import censys.certificates #Pip installed censys python libary, and imported the functions needed for the tastk
import csv

#my personal UID from account
UID = "ce6e7d8f-5763-4d4c-89a9-cd17da32792a" 
#my personal secret from my account
SECRET = "vaW9zzX9tKqNfIlP9CA9hP0h1WamgWhq" 

#authentication using my UID and secret
certificates = censys.certificates.CensysCertificates(UID, SECRET) 

#fields required for the task
fields = ["parsed.subject_dn", "parsed.fingerprint_sha256", "parsed.validity.start", "parsed.validity.end"] 

#creating and opening a csv file to write data two
f = open('csvfile2.csv','w') 

#The headings under which the data is classified into
data = "Subject DN, SHA-256 Fingerprint, Validity Start Timestamp, Validity End Timestamp\n" 
#writing this data to the csv file
f.write(data) 

#iterating through the query results where parsed name is censys.io and tags trusted
for c in certificates.search("parsed.names : censys.io and tags : trusted", fields=fields): 
    #Constructing a data string that is comma separated with values such as the Subject DN, the SHA 256 Fingerpting and Validity Start/End Timestamp from the query results
    #I constructed the string in this way as "f.write()" writes into a CSV file based on the commas on the string
    data =  c["parsed.subject_dn"] + ", " +  c["parsed.fingerprint_sha256"] +  ", " + c["parsed.validity.start"] + ", " + c["parsed.validity.end"] + "\n" 
    f.write(data)

f.close()


#Rough work

# print(data)

# for c in certificates.search("parsed.names : censys.io and tags : trusted", fields=fields):
#     print c["parsed.subject_dn"], c["parsed.fingerprint_sha256"], c["parsed.validity.start"], c["parsed.validity.end"]
#     # print (c["parsed.fingerprint_sha256"])
#     # print (c["parsed.validity.start"])
#     # print (c["parsed.validity.start"])
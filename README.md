# Python Code to scan Censys public database

Python code that scans censys X.509 Certificates

Run it on terminal using command "python demo.py"

demo.py conducts a simple python API search

It is a script that queries the certificates index and outputs a 
CSV of the the Subject DN, SHA256 fingerprints and validity start and end dates 
for all trusted (unexpired) X.509 certificates associated with the 
censys.io domain

Post Authentication, the scrip querys and looks for all trusted (unexpired)
X.509 certificates associated with thee censys.io domain whose query is

"parsed.names: censys.io and tags: trusted."

The script iterates through the certificates to find the ones that satisfy
the above condition. Post this, the script fetches the data an recronstructs
it in a way that it is comma delimited so that it can be output into a 
csv file using the .write() function

The script returns a csv (csvfile2) file containing the CSV of the the Subject DN, SHA256 fingerprints and validity start and end dates 
for all trusted (unexpired) X.509 certificates associated with the 
censys.io domain

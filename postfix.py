import os
import re

# Bounce Mail folder path
dir_path = os.environ.get('HOME')+'/Maildir/new'

# Patterns for data extraction from bounce
pattern_status = re.compile(r"^Status")
pattern_dsn = re.compile(r"^Diagnostic-Code")
pattern_xappid = re.compile(r"^x-appid")
pattern_from = re.compile(r"^From")
pattern_to = re.compile(r"^To:")
pattern_subject = re.compile(r"^Subject")

# list to store files
res = []

# Iterate Bounce Directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        #if not, it's a bounce !!!
        res.append(path)
        # let's be sure vars are empty
        status = ""
        dsn = ""
        xappid = ""
        # Open File
        with open(os.path.join(dir_path, path), 'r') as file:

            # extract  xappid      
            #print(split_data[3])
            # Iterate on lines ...
            for line in file:
                #Extract data from pattern
                #print(line)
                if pattern_status.match(line):
                    mail_status=line
                if pattern_dsn.match(line):
                    mail_dsn=line
                if pattern_xappid.match(line):
                    mail_xappid=line
                if pattern_from.match(line):
                    mail_from=line    
                if pattern_to.match(line):
                    mail_to=line
                if pattern_subject.match(line):
                    mail_subject=line  

            if (mail_status != "") and (mail_dsn != "") :
                print(mail_status + mail_dsn + mail_xappid + mail_from + mail_to + mail_subject)

#TODO Envoi + Suppression bounce

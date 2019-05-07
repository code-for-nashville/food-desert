# code to parse CPS_Suppl_Food_Security_2017_dec17pub.dat
# based on information provided in 
# CPS_Suppl_Food_Security2017_Record_Layout.pdf
# 
# Wesley Duffee-Braun
# April 2019
# -------------
# 

import csv

# Start of header row for the CSV
#
header = ['HRHHID','HRMONTH','HRYEAR4','HURESPLI','HUFINAL','HETENURE',
         'HEHOUSUT','HETELHHD','HETELAVL','HEPHONEO','HEFAMINC',
         'HUTYPEA','HUTYPB','HUTYPC','HWHHWGT','HRINTSTA','HRNUMHOU',
         'HRHTYPE','HRMIS','HUINTTYP','HUPRSCNT','HRLONGLK','HRHHID2',
         'HWHHWTLN','HUBUS','HUBUSL1','HUBUSL2','HUBUSL3','HUBUSL4',
         'GEREG','GEDIV','GESTFIPS','GTCBSA','GTCO','GTCBSAST',
         'GTMETSTA','GTINDVPC','GTCBSASZ','GTCSA','PERRP','PEPARENT',
         'PRTAGE','PRTFAGE','PEMARITL','PESPOUSE','PESEX','PEAFEVER' ]

# Create the to-be-written csv
#
with open('CPS_Suppl_Food_Security_2017_parsed.csv', 'wb+') as parsed_file:
    writer = csv.DictWriter(parsed_file, header, quoting=csv.QUOTE_ALL)
    writer.writeheader()

    # Open the dat file for reading. 
    # Probably should take file name as arg but...
    #
    with open("CPS_Suppl_Food_Security_2017_dec17pub.dat", 'rb') as dat_file:

        # Read in the line, start a counter
        #
        orig_line = dat_file.readline()
        cnt = 1

        # Run the loop while the file has content to be processed
        #
        while orig_line:
            
            # Replace all the dashes to keep the numbers tidy in the CSV
            #
            line = orig_line.replace("-","0")

            # Print the count and line to be split up and stored
            #
            print("Line {}: {}".format(cnt, line))
            cnt = cnt + 1
            try: 

                # Create the row to be written 
                # Pattern is pulled from Record Layout Attachment #6
                # Start of line segment is -1 relative to Attachment spec
                # because the spec starts with 1 but python strings 
                # start at location 0. 
                #
                row = {'HRHHID': line[0:15],
                       'HRMONTH': line[15:17],
                       'HRYEAR4': line[17:21],
                       'HURESPLI': line[21:23],
                       'HUFINAL': line[23:26],
                       'HETENURE': line[28:30],
                       'HEHOUSUT': line[30:32],
                       'HETELHHD': line[32:34],
                       'HETELAVL': line[34:36],
                       'HEPHONEO': line[36:38],
                       'HEFAMINC': line[38:40],
                       'HUTYPEA': line[40:42],
                       'HUTYPB': line[42:44],
                       'HUTYPC': line[44:46],
                       'HWHHWGT': line[46:56],
                       'HRINTSTA': line[56:58],
                       'HRNUMHOU': line[58:60],
                       'HRHTYPE': line[60:62],
                       'HRMIS': line[62:64],
                       'HUINTTYP': line[64:66],
                       'HUPRSCNT': line[66:68],
                       'HRLONGLK': line[68:70],
                       'HRHHID2': line[70:75],
                       'HWHHWTLN': line[75:77],
                       'HUBUS': line[78:80],
                       'HUBUSL1': line[80:82],
                       'HUBUSL2': line[82:84],
                       'HUBUSL3': line[84:86],
                       'HUBUSL4': line[86:88],
                       'GEREG': line[88:90],
                       'GEDIV': line[90:91],
                       'GESTFIPS': line[92:94],
                       'GTCBSA': line[95:100],
                       'GTCO': line[100:103]}

                # Write row to file, check for new line and loop
                #
                writer.writerow(row)
                orig_line = dat_file.readline()
            except UnicodeEncodeError:
                print "Unicode error for "+ orig_line
            except:
                print "Unknown error occurred."

# Print message indicating end of processing
#
print "----- END OF FILE ----------------------------------"

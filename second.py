from BeautifulSoup import BeautifulSoup
import re
import xlwt
import first




def split_status(inp_1):
    ## name
    inp=inp_1.__str__()

    if (len(inp) == 0) :
        return ''
    ## line.__str__xx
    try :
        firstStep = inp.split (">" )
        ## special handling for "status"
        ##print firstStep[0]
        if (firstStep[3].find("Passed") <> -1) :
            return "Passed"
        elif (firstStep[3].find("Failed") <> -1) :
            return "Failed"
        else :
            return "Error"
        
    except Exception, e:
        print " prob "
        return ""
    return secStep[0]

def split(inp_1):
    ## layoout input :
    ## <something>INTERESTING BIT</something>

    
    ## name
    inp=inp_1.__str__()

    if (len(inp) == 0) :
        return ''
    ## line.__str__xx
    try :
        firstStep = inp.split (">" )
        secStep = firstStep[1].split ("</" )
    except Exception, e:
        print " prob "
        return ""
    
    return secStep[0]

## start here:

## e = open("L:\\results 06062015\\2015-06-05_18.41.26\\Eng Serv W1 ePTC New\\3G_S4_SignleBox_Overnight_New\\default_ThreeGFdd_3G_S4_SignleBox_Overnight_New_2015-06-05_18.41.26.ptmres")
## e=     open("L:\\results 06062015\\2015-06-05_18.41.07\\Eng Serv W1 ePTC New\\3G_S4_SignleBox_Overnight_New\\default_ThreeGFdd_3G_S4_SignleBox_Overnight_New_2015-06-05_18.41.07.ptmres")
## e = open("L:\\results 06062015\\2015-06-06_02.25.32\\Eng Serv W1 ePTC New\\S4_3G_SingleBox_100\\default_ThreeGFdd_S4_3G_SingleBox_100_2015-06-06_02.25.32.ptmres")
## e=open ("K:\\2015-06-05_18.39.29\\2015-06-05_18.39.29\\SYS B camp 3 boxes 2 LTE 1 3G\\3G_S4_Singlebox_500\\ThreeGFdd\\default_ThreeGFdd_3G_S4_Singlebox_500_2015-06-05_18.39.29.ptmres")
## e=open ("K:\\2015-06-05_17.37.03\\2015-06-05_17.37.03\\SYS B camp 3 boxes 2 LTE 1 3G\\S4_500_LTE_Singlebox\\LteFdd\\default_LteFdd_S4_500_LTE_Singlebox_2015-06-05_17.37.03.ptmres")

e=open ("K:\\2015-06-05_17.36.27\\2015-06-05_17.36.27\\SYS B camp 3 boxes 2 LTE 1 3G\\S4_500_LTE_Singlebox\\LteFdd\\default_LteFdd_S4_500_LTE_Singlebox_2015-06-05_17.36.27.ptmres")

fileName = "SYS B camp 3 boxes 2 LTE 1 3G"

sheet = "LteFdd_S4_500_LTE_Singlebox"


fileName = fileName + ".xls"



y=BeautifulSoup(e)
tt=y.findAll("test")



## create a list of test that failed
fail = []
## and a list of tests that err
err = []

for res in tt:
    tt0=res.findAll("status")
    tt1=res.findAll("name")
    tt2=res.findAll("resultlocation")
    tt3=res.findAll("starttime")
    tt4=res.findAll("executionduration")


    stat = split_status(tt0)
    nam = split(tt1)
    
    print ' ------------------- '
    print "status", split_status(tt0)
    print "name", split(tt1)
    ##print "resultlocation", split(tt2)
    ##print "starttime", split(tt3)
    ##print "executionduration", split(tt4)
    print ' ------------------- '
    print ' '



    if stat == "Passed" :
        pass
    elif stat == "Failed" :
        fail.append(nam)
    elif stat == "Error" :
        err.append(nam)

    
    ##
    ##  START A SESSION WITH A RECOVERY FROM ERRORS.
    ## if the status is failed:
    ## compress the folder in resultlocation and copy it to a dest folder.
    ##


    ## import sys
    ## import os
    ## os.system(dir)
    ## next works but it si not used yet because I need to find the file name.
    ##import subprocess
    ##exe = "C:\\Program Files\\7-Zip\\7z.exe"
    ##source = "C:\\Python27\\PCT_work\\PCT_RESULTS\\RRC_D14wk36_v30-tc_8_2_2_19_2015-05-31_17.14.49"
    ##target="C:\Users\User\Documents\tmp.7z"
    ##
    ##subprocess.call(exe + " a -t7z \"" + target + "\" \"" + source + "\" -mx=9")
book = xlwt.Workbook()
sh = book.add_sheet(sheet)
row=10


## weed out tc that are there more than once


col = 2
print len(err), err
myset = set(err)
print myset
## If you use it further as a list, you should convert it back to list by doing
err_new = list(myset)
print len(err_new), err_new

for iii in range((len(err)-1)):
    try:
        sh.write(row, col+iii, err[iii])
    except :
        pass


row=11
col = 2
print len(fail), fail
myset = set(fail)

## If you use it further as a list, you should convert it back to list by doing
fail_new = list(myset)
print len(fail_new), fail_new
for iii in range((len(fail)-1)):
    try:
        sh.write(row, col+iii, fail[iii])
    except :
        pass

book.save(fileName)


    

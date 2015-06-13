from BeautifulSoup import BeautifulSoup
import re
import xlwt
import CONST

colInXLS = [5, 13, 64, 65, 66, 67, 68, 69, 144, 145, 149, 152 ]

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
##
##
##
def checkErrorReason(inp_1):
    retVal= ""
    try:
        inp=inp_1.__str__()    
        firstStep = inp.split (">" )
        ## special handling for "status"
        ##
        retVal = firstStep[1]
        retVal = retVal.split ("<" )
        retVal = retVal[0]
    except:
        pass
    return retVal




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



ColERROR = colInXLS[10]
ColFAIL  = colInXLS[11]




def writeXLSResults(sh, col, row, err, label):
    
    print len(err), err
    myset = set(err)
    print myset
    ## If you use it further as a list, you should convert it back to list by doing
    err_new = list(myset)
    print len(err_new), err_new
    errStr = label
    for iii in range((len(err_new)-1)):
        try:
            ## sh.write(row, col+iii, err[iii])
            errStr = errStr + ', ' + err_new[iii]
        except :
            pass
    sh.write(row, col, err)



    
    
    

## this part works on the ptmres
##
def second(nn, path, book, sh, row, col):

    new_path="\\".join(nn)
    print new_path

    
    ## e=open ("K:\\2015-06-05_17.36.27\\2015-06-05_17.36.27\\SYS B camp 3 boxes 2 LTE 1 3G\\S4_500_LTE_Singlebox\\LteFdd\\default_LteFdd_S4_500_LTE_Singlebox_2015-06-05_17.36.27.ptmres")
    e = open(new_path)

    ##fileName = "SYS B camp 3 boxes 2 LTE 1 3G"

    sheet = sh


    ## fileName = fileName + ".xls"



    y=BeautifulSoup(e)
    tt=y.findAll("test")



    ## create a list of test that failed
    fail = []
    ## and a list of tests that err
    err = []

    for res in tt:
        tt0=res.findAll("status")
        tt1=res.findAll("name")
        tt5=res.findAll("failurereason")
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

        if stat == "Error" :
            ## also check the error reason.
            ## chnage the nam to have ERROR reported + TC
            print tt5
            print res
            cause= checkErrorReason(tt5)
            ## returns: ERROR: Test Execution Timeout
            nam = cause.__str__() + ' ' + nam.__str__()
    

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
    ## book = xlwt.Workbook()
    ## sh = book.add_sheet(sheet)
    ## row = 10


    ## weed out tc that are there more than once


    writeXLSResults(sh, ColERROR, row, err, "ERROR: " )
    
    writeXLSResults(sh, ColFAIL, row, fail, "FAILED: " )
    
    ## book.save(fileName)
    

    

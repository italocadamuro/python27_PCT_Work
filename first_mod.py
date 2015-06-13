## not used: import xmltodict
## from bs4 import  BeautifulSoup
from BeautifulSoup import BeautifulSoup
import re
import xlwt
from second_mod import second
from HexConv import good_path
import CONST

colInXLS = [5, 13, 64, 65, 66, 67, 68, 69, 144, 145, 149, 152 ]


def writeXls_mod_ColHeaders (workbook, sh,  row):
    #You may need to group the variables together
    #for n, (v_desc, v) in enumerate(zip(desc, variables)):
    n=row
    #for v_desc, v in enumerate(zip(desc, variables)):
    #    sh.write(n, 0, v_desc)
    #    sh.write(n, 1, v)
    #    n=n+1
    #
    #
    # write folowing cols:
    # test in seq., tests run, num tests passed, num tests failed, duration, starting time
    colNames = ["name", "PC Name/Model",       "status", "test in seq.", "tests run", "test Skipped", "num tests passed","num tests failed", "duration", "starting time" ]
    ## colInXLS = [  5,              13,             64,             65,          66,             67,                 68,                69,         73,             80, 81, 85, 88
    ind=0
    for colName in colNames:
        sh.write(n, colInXLS[ind] , colName)
        ind=ind+1


    

def writeXls_mod (workbook, sh, one, two, three, four, five, six, seven, eight, row):
    
    variables = [one, "PCNAME/MODEL", two, five, six,"0", seven, eight, four, three ]

    one_name = "name"               
    two_name = "status  "
    three_name = "starttime "
    four_name = "executionduration"
    five_name = "totalnumoftests"
    six_name = "numoftestsrun   "
    seven_name = "totalnumofpasses  "
    eight_name = "totalnumoffailures "

    desc = [
        one_name 
        ,two_name 
        ,three_name 
        ,four_name 
        ,five_name 
        ,six_name 
        ,seven_name 
        ,eight_name ]

    #You may need to group the variables together
    #for n, (v_desc, v) in enumerate(zip(desc, variables)):
    n=row
    #for v_desc, v in enumerate(zip(desc, variables)):
    #    sh.write(n, 0, v_desc)
    #    sh.write(n, 1, v)
    #    n=n+1
    #
    #
    # write folowing cols:
    # test in seq., tests run, num tests passed, num tests failed, duration, starting time
    colNames = ["name", "status", "test in seq.", "tests run", "num tests passed","num tests failed", "duration", "starting time" ]
    #col=0
    #for colName in colNames:
    #    sh.write(n, col, colName)
    #    col=col+1

    col=0
    for val in variables:
        sh.write(n, colInXLS [col], val)
        col=col+1
    


def writeXls (filename, sheet, one, two, three, four, five, six, seven, eight):
    """
    import xlwt

    def output(filename, sheet, list1, list2, x, y, z):
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)

        variables = [x, y, z]
        x_desc = 'Display'
        y_desc = 'Dominance'
        z_desc = 'Test'
        desc = [x_desc, y_desc, z_desc]

        col1_name = 'Stimulus Time'
        col2_name = 'Reaction Time'

        #You may need to group the variables together
        #for n, (v_desc, v) in enumerate(zip(desc, variables)):
        for n, v_desc, v in enumerate(zip(desc, variables)):
            sh.write(n, 0, v_desc)
            sh.write(n, 1, v)

        n+=1

        sh.write(n, 0, col1_name)
        sh.write(n, 1, col2_name)

        for m, e1 in enumerate(list1, n+1):
            sh.write(m, 0, e1)

        for m, e2 in enumerate(list2, n+1):
            sh.write(m, 1, e2)

        book.save(filename)
    """
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)
    variables = [one, "PCNAME/MODEL", two, three, four, five, six, seven, eight]

    one_name = "name"               
    two_name = "status  "
    three_name = "starttime "
    four_name = "executionduration"
    five_name = "totalnumoftests"
    six_name = "numoftestsrun   "
    seven_name = "totalnumofpasses  "
    eight_name = "totalnumoffailures "

    desc = [
        one_name 
        ,two_name 
        ,three_name 
        ,four_name 
        ,five_name 
        ,six_name 
        ,seven_name 
        ,eight_name ]

    #You may need to group the variables together
    #for n, (v_desc, v) in enumerate(zip(desc, variables)):
    n=0
    for v_desc, v in enumerate(zip(desc, variables)):
        sh.write(n, 0, v_desc)
        sh.write(n, 1, v)
        n=n+1


    # write folowing cols:
    # test in seq., tests run, num tests passed, num tests failed, duration, starting time
    colNames = ["test in seq.", "tests run", "num tests passed","num tests failed", "duration", "starting time"]
    col=0
    for colName in colNames:
        sh.write(n, col, colName)
        col=col+1

    col=0
    n=n+1
    for val in variables:
        sh.write(n, col, val)
        col=col+1
 
    book.save(filename)
    






def split(inp_1):
    ## layoout input :
    ## <something>INTERESTING BIT</something>

    ## name
    inp=inp_1.__str__()
    secStep = []
    ## line.__str__xx
    try:
        firstStep = inp.split (">" )
        secStep = firstStep
        secStep = firstStep[1].split ("</" )
    except:
        print inp

        
    return secStep[0]



##
## starts here
##

## K_Drive = "\\LUT-NEPT-201\PCT_Results" the real K drive

## f = "J:\\2015-06-06_17.54.55\\Eng Serv W1 ePTC New\\default_Eng Serv W1 ePTC New_2015-06-06_17.54.55.campres"
## for J use:
##f = "J:\\2015-06-08_16.15.58\\Eng Serv D4 NON_PTC legacy and ePTC\\default_Eng Serv D4 NON_PTC legacy and ePTC_2015-06-08_16.15.58.campres"
##K_d ="J:"

## f = "K:\\2015-06-05_17.35.53\\2015-06-05_17.35.53\\SYS B camp 3 boxes 2 LTE 1 3G\\default_SYS B camp 3 boxes 2 LTE 1 3G_2015-06-05_17.35.53.campres"
## f = "K:\\2015-06-08_15.58.23\\2015-06-08_15.58.23\\Eng Serv D5 non PTC and Legacy LTE Syst B\\default_Eng Serv D5 non PTC and Legacy LTE Syst B_2015-06-08_15.58.23.campres"

## for K use:
## f = "K:\\2015-06-08_15.58.23\\2015-06-08_15.58.23\\Eng Serv D5 non PTC and Legacy LTE Syst B\\default_Eng Serv D5 non PTC and Legacy LTE Syst B_2015-06-08_15.58.23.campres"
## use:
##f =    "K:\\2015-06-09_16.20.34\\2015-06-09_16.20.34\\SYS B camp 3 boxes 2 LTE 1 3G\\default_SYS B camp 3 boxes 2 LTE 1 3G_2015-06-09_16.20.34.campres"
##K_d ="K:"
f =    "K:\\2015-06-10_18.21.10\\2015-06-10_18.21.10\\SYS B camp 3 boxes 2 LTE 1 3G\\default_SYS B camp 3 boxes 2 LTE 1 3G_2015-06-10_18.21.10.campres"
K_d ="K:"

## not used K_Drive = "\\LUT-NEPT-201\PCT_Results" ## the J drive 
K_Drive = "\\PCT_Results"  


## e = open("K:\\2015-06-05_17.35.53\\2015-06-05_17.35.53\\SYS B camp 3 boxes 2 LTE 1 3G\\default_SYS B camp 3 boxes 2 LTE 1 3G_2015-06-05_17.35.53.campres")
## e = open("K:\\2015-06-07_00.20.57\\2015-06-07_00.20.57\\SYS B camp 3 boxes 2 LTE 1 3G\\default_SYS B camp 3 boxes 2 LTE 1 3G_2015-06-07_00.20.57.campres")
e = open (f)

ff=f.split("\\")
           

##fileName = "CAG#43A Eng Serv W1 ePTC.xls"

fileName = ff[1] + ".xls"
print fileName
sheet = "Results"


y=BeautifulSoup(e)

res = y.findAll("campaign")
print res[0]
##print res[1]
##tt14= res[1]

##  print the camp's name
camName = res[0].findAll("name")
print "Camp Name------------->", slit(camName)



catalogVersion = res[0].findAll("resultsummary")
catalogVersion = catalogVersion[0].findAll("currenttestsequence")
catalogVersion = catalogVersion[0].findAll("totalnumoftestsequences")
catalogVersion = catalogVersion[0].findAll("numoftestsequencesrun")
catalogVersion = catalogVersion[0].findAll("estimatedtotalruntime")
catalogVersion = catalogVersion[0].findAll("catalogversion")
print "Catalog Version------------->  2  ", split(catalogVersion[0]) 



tt9=res[0].findAll("version")
##print "tt9", split(tt9)
##tt10=res[0].findAll("dateCreated") 
##tt11=res[0].findAll("ipAddress") 
##tt12=res[0].findAll("guid") 
##tt10=res.findAll(" 
##tt10=res.findAll(" 
##tt10=res.findAll(" 
##tt10=res.findAll(" 
##tt1_mod=split(tt1)
##print "tt10", "tt11", "tt12", tt10,tt11,tt12

##tt=y.campaign.findAll("resultSummary")
##print tt[0].findAll("catalogVersion")


tt=y.campaign.findAll("testsequence")



##last in the list :
tt[-1]
## and the <testsequence id="<last id>" type="<3G|LTE>">
row=10

## "thisFile.xls", "results"
book = xlwt.Workbook()
sh = book.add_sheet("results")
row=10
writeXls_mod_ColHeaders (book, sh,  row)
row=row+1
col= 10
for res in tt:
    tt0=res.findAll("status")
    tt1=res.findAll("name")
    tt2=res.findAll("resultlocation")
    tt3=res.findAll("starttime")
    tt4=res.findAll("executionduration")
    tt5=res.findAll("totalnumoftests")
    tt6=res.findAll("numoftestsrun")
    tt7=res.findAll("totalnumofpasses")
    tt8=res.findAll("totalnumoffailures")
    ## print tt0,tt1,tt2,tt3,tt4,tt5,tt6,tt7,tt8

    print " ================  "
    print "name               ",split(tt1)
    print "status             ",split(tt0)
    print "starttime          ",split(tt3)
    print "executionduration  ",split(tt4)
    print "totalnumoftests    ",split(tt5)
    print "numoftestsrun      ",split(tt6)
    print "totalnumofpasses   ",split(tt7)
    print "totalnumoffailures ",split(tt8)
    print " ================  "
    print "  "

 
    ##writeXls ("thisFile.xls", "results",split(tt1),split(tt0),split(tt3),
    ##          split(tt4),split(tt5),split(tt6),split(tt7),split(tt8),row)

    writeXls_mod (book,sh,split(tt1),split(tt0),split(tt3), split(tt4),split(tt5),split(tt6),split(tt7),split(tt8),row)




    ##
    ## read tt2=res.findAll("resultlocation")
    ## and find the resultd from the sequence 
    ##

    path = split(tt2)
    print path
    nn, path= good_path(path, K_Drive, K_d)
    print "from first_mod", path
    if len(path) <> 0:
        second(nn,path, book, sh, row, col)
    else :
        pass
    
    row=row+1


book.save(fileName)



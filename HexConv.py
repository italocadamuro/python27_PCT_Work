import string

## path="\\LUT-NEPT-201\PCT_Results\2015-06-05_17.36.27\2015-06-05_17.36.27\SYS B camp 3 boxes 2 LTE 1 3G\S4_500_LTE_Singlebox\LteFdd\default_LteFdd_S4_500_LTE_Singlebox_2015-06-05_17.36.27.ptmres"

def good_path(path, K_Drive, K_d ):
        ## K_Drive = "\\LUT-NEPT-201\PCT_Results"

        new_path = path.split(K_Drive)


        ##new_path_no_hex = ""
        ##tmp = []
        ##for c in new_path[1]:#
        ##	print hex(ord(c))
        ##	if (hex(ord(c)) == "0x81" ):
        ##		print "CC"
        ##		c="\\"
        ##		tmp.append(c)
        ##		c="1"
        ##	tmp.append(c)
        ##	##print tmp
        ##
        ##print tmp
        ##seq = ['1','3','7']
        ##sep="+"
        ##sep.join(seq)
        ##print sep
        ##print seq
        ##sep.join(tmp)
        ##print sep
        ##new_path_no_hex=sep
        ##
        ##print new_path_no_hex
        ##
        ##new_path_no_hex= "k:\\" + new_path_no_hex
        ##
        ##print new_path_no_hex


        try:
                cleaned = ''.join(c for c in new_path[1] if c in string.printable)
                print cleaned
                new_path_no_hex= K_d + cleaned
                print new_path_no_hex
                print new_path_no_hex.find("5-")
                nn=new_path_no_hex.split("\\")
                nn[0] = nn[0].replace("5-","\\2015-" )
                f = "".join(nn)

                f = f.replace("\\", "\\\\")

                print "from HexConv" , f
        except:
                
                nn = []
                f = ""

        return  nn,f

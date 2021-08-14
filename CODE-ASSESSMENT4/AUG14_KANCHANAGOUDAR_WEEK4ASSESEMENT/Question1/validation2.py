import re,logging
try:
    def validation(name,address,blood_group,mobile_number,place,emailid):
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",name)
        valaddress=re.search("[A-Z]{1}[^A-Z]{0,25}$",address)
        valblood=re.search("(A|B|AB|O)(\+|-)$",blood_group)  
        valmobile=re.search("(0|91)?[7-9][0-9]{9}",mobile_number)
        valplace=re.search("[A-Z]{1}[^A-Z]{0,25}$",place)
        valemail=re.search("^\w+[\._]?\w+[@]\w+[.]\w{2,3}$",emailid)

        if valname and valaddress and valmobile and valplace and valemail and valblood:
            return True
        else:
            return False
except:
    logging.error("unable to process")
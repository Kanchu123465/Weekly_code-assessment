import re,json,pymongo,logging,smtplib,validation2
donorlist=[]
donorlist2=[]
donorlist3=[]
email_list=[]
try:
    client=pymongo.MongoClient("mongodb://localhost:27017")
    mydatabase=client["Bloodgroupdb"]
    collection_name=mydatabase['Donors']
    class DonorDetails:
        def init(self,name,address,blood_group,pincode,mobile_number,last_donated_date,place,emailid):
            self.name=name
            self.address=address
            self.blood_group=blood_group
            self.pincode=pincode
            self.mobile_number=mobile_number
            self.localhost=last_donated_date
            self.place=place
            self.emailid=emailid
        def adddonordetail(self,name,address,blood_group,pincode,mobile_number,last_donated_date,place,emailid):
            
            dict1={"name":name,"address":address,"blood_group":blood_group,"pincode":pincode,"mobile_number":mobile_number,"last_donated_date":last_donated_date,"place":place,"emailid":emailid,"status":0} 
            return dict1


    obj=DonorDetails()
    if(__name__=="__main__"):     
        while True:
            print("1.add Donor")
            print("2.Search based on blood group")
            print("3.search based on blood group and place")
            print("4.update donor  based details based on mobilenumber")
            print("5.delete donor based on mobile number")
            print("6.To display total number of donors on each blood group")
            print("7.Immediate notification to all via a mail")
            print("8.View details")
            print("9.exit") 
            choice=int(input("Enter your choice : "))
            if choice==1:
                name=input("Enter the name : ")
                address=input("Enter the adress : ")
                blood_group=input("Enter bloodgroup: ")
                pincode=int(input("Enter the pincode : "))
                
                mobile_number=input("Enter the mobile_number : ")
                last_donated_date=input("Enter the last donated date : ")
                place=input("Enter the place : ")
                emailid=input("Enter the emailid of donors:")
                a=(validation2.validation(name,address,blood_group,mobile_number,place,emailid))
                if a:
                    data=obj.adddonordetail(name,address,blood_group,pincode,mobile_number,last_donated_date,place,emailid)
                    donorlist.append(data)
                    result=collection_name.insert_many(donorlist)
                    print(result.inserted_ids)
                else:
                    logging.error("Invalid data Enter again")
            if choice==2:
                group=input("Enter blood group  search:")
                result=collection_name.find({"blood_group":group,"status":0},{"_id":0})
                for i in result:
                    print(i)
            if choice==3:
                    blood_group1=input("Enter the bloodgroup to search :")
                    place1=input("Enter the place  to search:")
                    
                    result=collection_name.find({"$and":[{"blood_group":blood_group1,"place":place1,"status":0}]},{"_id":0})
                    for i in result:
                        print(i)
            if choice==4:
                    mobile_number=input("Enter mobile number of user that you want to update:")
                    name=input("Enter the name to update:")
                    address=input("Enter the address to update:")
                    blood_group1=input("Enter the bloodgroup to update : ")
                    pincode=int(input("Enter the pincode: "))
                    last_donated_date=input("Enter the last donated date : ")
                    place1=input("Enter the place : ")
                    emailid=input("Enter the emailid to update:")
                    result=collection_name.update_one({"$and":[{"mobile_number":mobile_number,"status":0}]},{"$set":{"name":name,"address":address,"blood_group":blood_group1,"pincode":pincode,"last_donated_date":last_donated_date,"place":place1,"emailid":emailid}})
                    if result.modified_count==1:
                        print("DONORS DATA UPDATED SUCCESSFULLY")
                    else:
                        print("UNABLE TO UPDATE")
            if choice==5:
                mobile_number=input("Enter mobile number of user that you want to delete:")
                result=collection_name.update_one({"mobile_number":mobile_number},{"$set":{"status":1}})
                if result.modified_count==1:
                    print("DONORS DATA DELETED SUCCESSFULLY")
                else:
                    print("UNABLE TO DELETE")
            if choice==6:
                result=collection_name.aggregate([{"$group":{"_id":"$blood_group","Number_Of_Donors":{"$sum":1}}}])
                for i in result:
                    print(i)
            if choice==7:
                blood_group1=input("Enter the blood group that is needed:")
                hospital=input("Enter the hospital name where it is needed:")
                mobile_number=input("Enter the mobile number to contact:")
                message="immediately want   "+blood_group1+"  blood group blood in  "+hospital+"  hospital"+"\n CONTACT DETAILS:"+mobile_number+"\n\n please join your hands with us"
                result=collection_name.find({"status":0},{"_id":0})
                for i in result:
                    donorlist2.append(i)
                for i in donorlist2:
                    email=i['emailid']
                    email_list.append(email)
                donorlist2.clear()   
                for i in email_list:
                        print(i)
                        connection=smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("kanchu954@gmail.com","Kanchu@8+")
                        connection.sendmail("kanchu954@gmail.com",i,message)
                        print("Email is successfully sent")
                connection.quit()
                break
            if choice==8:
                result=collection_name.find({"status":0},{"_id":0})
                for i in result:
                    donorlist3.append(i)
                print(donorlist3)
                donorlist2.clear() 

            if choice==9:
                break
except:
    logging.error("unable to process")
finally:
    print("THANK YOU")
                
        
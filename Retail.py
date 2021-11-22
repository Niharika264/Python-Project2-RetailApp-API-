from werkzeug.wrappers import Request,Response
from flask import Flask,jsonify,request
from pymongo import MongoClient
import datetime

client = MongoClient('localhost',27017)
db = client["Retail"]
 
#Collections

Soap=db["Soap"]
Shampoo=db["Shampoo"]
CreamLotion=db["CreamLotion"]
Beauty=db["Beauty"]
Pharmacy=db["Pharmacy"]
MenWear=db["MenWear"]
WomenWear=db["WomenWear"]
Fashion=db["Fashion"]
Mobile = db["Mobile"]
TV = db["TV"]
ElectricAppliances=db["ElectricAppliances"]
Snacks=db["Snacks"]
Veggies=db["Veggies"]
Food=db["Food"]
Products=db["Products"]

#get _id's
dict1 = Beauty.find_one({"_id":"bid"})
soap_id = dict1["Soap"]
shampoo_id = dict1["Shampoo"]
cream_id = dict1["CreamLotion"]
pharmacy_id = ["p1","p2","p3","p4","p5"]
dict2 = Food.find_one({"_id":"foodid"})
snack_id = dict2["Snacks"]

#products record
products={}

#converting date-string into ISO Date
list1=list
def convertDate(list1,list2,list3,list4,list5):
    if list1==soap_id:
        for i in Soap.find():
            date=i["exp_date"]
            d=datetime.datetime.strptime(date,"%Y-%m-%d")
            index=i["_id"]
            Soap.update_one({"_id":index},{"$set":{"exp_date":d}})
    if list2==shampoo_id:
        for i in range(len(shampoo_id)):
            date=Shampoo.find_one({"_id":shampoo_id[i]})["exp_date"]
            d=datetime.datetime.strptime(date,"%Y-%m-%d")
            Shampoo.update_one({"_id":shampoo_id[i]},{"$set":{"exp_date":d}})
    if list3==cream_id:
        for i in range(len(cream_id)):
            date=CreamLotion.find_one({"_id":cream_id[i]})["exp_date"]
            d=datetime.datetime.strptime(date,"%Y-%m-%d")
            CreamLotion.update_one({"_id":cream_id[i]},{"$set":{"exp_date":d}})
    if list4==pharmacy_id:
        for i in range(len(pharmacy_id)):
            date=Pharmacy.find_one({"_id":pharmacy_id[i]})["exp_date"]
            d=datetime.datetime.strptime(date,"%Y-%m-%d")
            Pharmacy.update_one({"_id":pharmacy_id[i]},{"$set":{"exp_date":d}})
    if list5==snack_id:
        for i in range(len(snack_id)):
            date=Snacks.find_one({"_id":snack_id[i]})["exp_date"]
            d=datetime.datetime.strptime(date,"%Y-%m-%d")
            Snacks.update_one({"_id":snack_id[i]},{"$set":{"exp_date":d}})


def Display():
    beauty_id = Products.find_one({"_id":"mainid"})["Beauty"]
    pharmacy_id = Products.find_one({"_id":"mainid"})["Pharmacy"]
    Fashion_id = Products.find_one({"_id":"mainid"})["Fashion"]
    Electronic_id = Products.find_one({"_id":"mainid"})["ElectricAppliances"]
    food_id = Products.find_one({"_id":"mainid"})["Food"]
    
    list1=[]
    for ele in Soap.find():
        name=ele["name"]
        list1.append(name)
    products["Soap"] = list1
    #list1.clear()
    
    list2=[]
    for ele in Shampoo.find():
        name=ele["name"]
        list2.append(name)
    products["Shampoo"] = list2
    #list2.clear()
    
    list3=[]
    for ele in CreamLotion.find():
        name=ele["name"]
        list3.append(name)
    products["CreamLotion"] = list3
    #list3.clear()
    
    list4=[]
    for ele in Pharmacy.find():
        name=ele["name"]
        list4.append(name)
    products["Pharmacy"] = list4
    #list4.clear()
    
    list5=[]
    for ele in Mobile.find():
        name=ele["name"]
        list5.append(name)
    products["Mobile"] = list5
    #list5.clear()
    
    list6=[]
    for ele in TV.find():
        name=ele["name"]
        list6.append(name)
    products["TV"] = list6
    #list6.clear()
    
    list7=[]
    for ele in MenWear.find():
        name=ele["name"]
        list7.append(name)
    products["MenWear"] = list7
    #list7.clear()
    
    list8=[]
    for ele in WomenWear.find():
        name=ele["name"]
        list8.append(name)
    products["WomenWear"] = list8
    #list8.clear()
    
    list9=[]
    for ele in Snacks.find():
        name=ele["name"]
        list9.append(name)
    products["Snacks"] = list9
    #list9.clear()
    
    list10=[]
    for ele in Veggies.find():
        name=ele["name"]
        list10.append(name)
    products["Veggies"] = list10
    #list10.clear()

    return jsonify(products)
  
def InsertIntoSoap():
    
    soap_doc=[{"_id":"sp6","name":"Milk&Honey","exp_date":"2020-10-01","price":199},
             {"_id":"sp7","name":"Assure","exp_date":"2021-11-01","price":99},
             {"_id":"sp8","name":"Santoor","exp_date":"2022-12-01","price":49},
             {"_id":"sp9","name":"Liril","exp_date":"2022-12-21","price":65},
             {"_id":"sp10","name":"Yardley","exp_date":"2023-11-01","price":299},
             {"_id":"sp11","name":"Medimix","exp_date":"2020-11-01","price":49},
             {"_id":"sp12","name":"Lifeboy","exp_date":"2021-12-01","price":30},
             {"_id":"sp13","name":"ParkAvenue","exp_date":"2022-01-01","price":210},
             {"_id":"sp14","name":"Neem","exp_date":"2023-01-11","price":50},
             {"_id":"sp15","name":"HoneyMade","exp_date":"2021-11-01","price":69}]
    
    new_soap_list=[]
    for i in range(10):
        new_soap_list.append(soap_doc[i]["_id"])
        
    Soap.insert_many(soap_doc)
    
    beauty_id=Products.find_one({"_id":"mainid"})["Beauty"]
    old_soap_list=Beauty.find_one({"_id":beauty_id})["Soap"]
    
    for ele in new_soap_list:
        old_soap_list.append(ele)
    
    Beauty.update_one({"_id":beauty_id},{"$set":{"Soap":old_soap_list}})
    return jsonify("Additional 10 Soaps Inserted Successfully")
   
def UpdateShampooPrice():
    
    before=[]
    after=[]
    beauty_id = Products.find_one({"_id":"mainid"})["Beauty"]
    shampoo_list = Beauty.find_one({"_id":beauty_id})["Shampoo"]
    
    for shampoo_id in shampoo_list:
        before.append(Shampoo.find_one({"_id":shampoo_id}))
        
    for shampoo_id in shampoo_list:
        cost=Shampoo.find_one({"_id":shampoo_id})["price"]
        Shampoo.update_one({"_id":shampoo_id},{"$set":{"price":cost+10}})
    
    for shampoo_id in shampoo_list:
        after.append(Shampoo.find_one({"_id":shampoo_id}))
    return jsonify( {"Before" : before} , {"After" : after} )
              
def DeleteExpiryProduct():
    #get _id's
    beauty_id = Products.find_one({"_id":"mainid"})["Beauty"]
    dict1 = Beauty.find_one({"_id":beauty_id})
    soap_list = dict1["Soap"]
    shampoo_list = dict1["Shampoo"]
    cream_list = dict1["CreamLotion"]
    pharmacy_list = ["p1","p2","p3","p4","p5"]
    food_id = Products.find_one({"_id":"mainid"})["Food"]
    dict2 = Food.find_one({"_id":food_id})
    snack_list = dict2["Snacks"]
    
    convertDate(soap_list,shampoo_list,cream_list,pharmacy_list,snack_list)
    
    current_date = datetime.datetime.now()
    
    #Deleting expired soap products
    for soap in Soap.find():
        index=soap["_id"]
        date=soap["exp_date"]

        if(date<current_date):
            Soap.delete_one({"_id":index})
            soap_list.remove(index)

    #Deleting expired Shampoo products
    for shampoo in Shampoo.find():
        index=shampoo["_id"]
        date=shampoo["exp_date"]
        if(date<current_date):
            Shampoo.delete_one({"_id":index})
            shampoo_list.remove(index)
    
    #Deleting expired CreamLotion products
    for cream in CreamLotion.find():
        index=cream["_id"]
        date=cream["exp_date"]
        if(date<current_date):
            CreamLotion.delete_one({"_id":index})
            cream_list.remove(index)

    #Deleting expired pharmacy products
    for tablet in Pharmacy.find():
        index=tablet["_id"]
        date=tablet["exp_date"]
        if(date<current_date):
            Pharmacy.delete_one({"_id":index})
            pharmacy_list.remove(index)
            
    #Deleting expired Snacks
    for snack in Snacks.find():
        index=snack["_id"]
        date=snack["exp_date"]
        if(date<current_date):
            Snacks.delete_one({"_id":index})
            snack_list.remove(index)

    Beauty.update_one({"_id":beauty_id},{"$set":{"Soap":soap_list,"Shampoo":shampoo_list,"CreamLotion":cream_list}})
    Food.update_one({"_id":food_id},{"$set":{"Snacks":snack_list}})
   
    #Call Display() to view remaining products after removing expired ones
    return jsonify("Deletion Successful")
    
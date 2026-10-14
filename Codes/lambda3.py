sales={

      101:{
       
    "name":"saif",
    "age":19,
    "course":"bsc-it",
    "qty":777,
    "price":price
    
      },

      102:{
             
              "name":"saif ali",
              "age":20,
              "course":"msc-it",
              "qty":789,
              "price":price,
      }
}
def add_record():
    rid=input("enter reocrd id:")
  if rid in sales:
      print("record id already exitst")
      name=input("enter your name")
      qty=input("enter qty:")  
      price=input("enter your price") 

sales[rid]{
    "name":name,
    "qty":qty,
    "price":price


    print("record added succesfully")
}

def min_sales():
    if len(sales)==0:
        print("no record availabel")
        return 

    minimum=min(
        sales.iteam(),
        key=lambda x:x[1]["price"]*x[1]["qty"]

    )
    rid=minimum[0]
    record=minimum[1]

    

while True:
  print("1 to add")
  print("2 for update")
  print("0 to exit")

ch=input("enter your choice")


match ch:

    case 1:
        add_record()

    case 2:
        update_record()
    case 0:
        print("exit")
        breck










































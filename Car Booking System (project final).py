import datetime
import random
class account :
    def __init__(self,name,password):
        self.name = name
        self.password = password
    #create register function that takes name and password as input , store it in a list and file both
    def register(self,name,password):
        with open('account.txt','a') as file:
            file.write(name+' '+password+'\n')
            print('registered successfully')
        with open('account.txt','r') as file:
            for line in file:
                print(line)
    #create login function that takes name and password as input , check if it is in the list
    def login(self,name,password):
        with open('account.txt','r') as file:
            for line in file:
                if name in line and password in line:
                    print('login successful')
                else:
                    print('login failed')
#create user class that inherits from account class
class user(account):
    def __init__(self,name,password,user_id,address,phone_no,age):
        self.user_id = user_id
        self.address = address
        self.phone_no = phone_no
        self.age = age
        super().__init__(name,password)
    def register(self,name,password,user_id,address,phone_no,age):
        with open('account.txt','a') as file:
            file.write(name+' '+password+' '+user_id+' '+address+' '+phone_no+' '+age+'\n')
            print('registered successfully')
        with open('account.txt','r') as file:
            for line in file:
                print(line)
    #login function that takes name,password as input and check if it is in the file
    def login(self,name,password):
        with open('account.txt','r') as file:
            for line in file:
                if name in line and password in line:
                    print('login successful')
                else:
                    print('login failed')

#create driver class that inherits from account class and contains vehicle object
class driver(account):
    def __init__(self,name,password,user_id,phoneno):
        self.user_id = user_id
        self.phoneno = phoneno
        super().__init__(name,password)
        #create vehicle object
        self.vehicle = vehicle(" "," ")
    #register function that takes name,password,user_id,address,phone_no,age as input and store it in a file
    def register(self,name,password,user_id,address,phone_no,age):
        with open('account.txt','a') as file:
            file.write(name+' '+password+' '+user_id+' '+address+' '+phone_no+' '+age+'\n')
            print('registered successfully')
        with open('account.txt','r') as file:
            for line in file:
                print(line)
    #login function that takes name,password as input and check if it is in the file
    def login(self,name,password):
        with open('account.txt','r') as file:
            for line in file:
                if name in line and password in line:
                    print('login successful')
                else:
                    print('login failed')

#create route class that contains pickup ,destination,date,time,price
class route:
    def __init__(self,pickup,destination,date,time,price):
        self.pickup = pickup
        self.destination = destination
        self.date = date
        self.time = time
        self.price = price

    


#create a vehicle class
class vehicle:
    def __init__(self,vehicle_name,model):
        self.vehicle_name = vehicle_name
        self.model = model
    #create register vehicle function that takes vehicle_name,model as input and store it in a list and file both
    def register_vehicle(self,vehicle_name,model):
        with open('vehicle.txt','a') as file:
            file.write(vehicle_name+' '+model+'\n')
            print('registered successfully')
        with open('vehicle.txt','r') as file:
            for line in file:
                print(line)
    #create login vehicle function that takes vehicle_name,model as input and check if it is in the list
    def login_vehicle(self,vehicle_name,model):
        with open('vehicle.txt','r') as file:
            for line in file:
                if vehicle_name in line and model in line:
                    print('login successful')
                else:
                    print('login failed')
    
    #create booking class that inherits from route class and contains user object and looks up for a driver using driver id
class booking:
    def __init__(self,user_id,car_id,name,address,email,phone_no,date,model,age,password,pickup,destination,time,price):
            self.car_id = car_id
            self.email = email
            self.date = date
            self.model = model
            self.obj_user=user(name,password,user_id,address,phone_no,age)
            self.obj_driver=driver(name,password,user_id,phone_no)
            self.obj_route=route(pickup,destination,0,time,price)
        #create register booking function that takes user_id,car_id,name,address,email,phone_no,date,model as input and store it in a file
    def register_booking(self,user_id,car_id,name,address,email,phone_no,date,model):
            with open('booking.txt','a') as file:
                file.write(user_id+' '+car_id+' '+name+' '+address+' '+email+' '+phone_no+' '+date+' '+model+'\n')
                print('registered successfully')
            with open('booking.txt','r') as file:
                for line in file:
                    print(line)
        #create login booking function that takes user_id,car_id,name,address,email,phone_no,date,model as input and check if it is in the list
    def login_booking(self,user_id,car_id,name,address,email,phone_no,date,model):
            with open('booking.txt','r') as file:
                for line in file:
                    if user_id in line and car_id in line and name in line and address in line and email in line and phone_no in line and date in line and model in line:
                        print('login successful')
                    else:
                        print('login failed')
        #create cancel booking function that takes user_id,car_id,name,address,email,phone_no,date,model as input and check if it is in the list and remove it from the file
    def cancel_booking(self,user_id,car_id,name,address,email,phone_no,date,model):
            with open('booking.txt','r') as file:
                for line in file:
                    if user_id in line and car_id in line and name in line and address in line and email in line and phone_no in line and date in line and model in line:
                        print('cancel successful')
                        file.remove(line)
                    else:
                        print('cancel failed')
        #create search booking function that takes user_id,car_id,name,address,email,phone_no,date,model as input and check if it is in the file
    def search_booking(self,user_id,car_id,name,address,email,phone_no,date,model):
            with open('booking.txt','r') as file:
                for line in file:
                    if user_id in line and car_id in line and name in line and address in line and email in line and phone_no in line and date in line and model in line:
                        print('search successful')
                        print(line)
                    else:
                        print('search failed')
        
#create function that creates files for user,driver,vehicle,route,booking and store them in the directory
def create_files():
    try:
        #create user file
        with open('user.txt','w') as file:
            file.write('user_id name password\n')
        with open('user.txt','a') as file:
            file.write('user1 user1 user1\n')
            file.write('user2 user2 user2\n')
            file.write('user3 user3 user3\n')
            file.write('user4 user4 user4\n')
            file.write('user5 user5 user5\n')
            file.write('user6 user6 user6\n')
            file.write('user7 user7 user7\n')
            file.write('user8 user8 user8\n')
            file.write('user9 user9 user9\n')
            file.write('user10 user10 user10\n')
        #create driver file
        with open('driver.txt','w') as file:
            file.write('user_id name password phoneno\n')
        #fill driver file with realistic data
        with open('driver.txt','a') as file:
            file.write('user1 user1 user1 9876543210\n')
            file.write('user2 user2 user2 9876543210\n')
            file.write('user3 user3 user3 9876543210\n')
            file.write('user4 user4 user4 9876543210\n')
            file.write('user5 user5 user5 9876543210\n')
            file.write('user6 user6 user6 9876543210\n')
            file.write('user7 user7 user7 9876543210\n')
            file.write('user8 user8 user8 9876543210\n')
            file.write('user9 user9 user9 9876543210\n')
            file.write('user10 user10 user10 9876543210\n')
        #create vehicle file
        with open('vehicle.txt','x') as file:
            file.write('vehicle_name model\n')
        #fill vehicle file with realistic data
        with open('vehicle.txt','a') as file:
            file.write('car1 car1\n')
            file.write('car2 car2\n')
            file.write('car3 car3\n')
            file.write('car4 car4\n')
            file.write('car5 car5\n')
            file.write('car6 car6\n')
            file.write('car7 car7\n')
            file.write('car8 car8\n')
            file.write('car9 car9\n')
            file.write('car10 car10\n')
        with open('booking.txt','x') as file:
            file.write('user_id car_id name address email phone_no date model\n')
        #fill booking file with realistic data
        with open('booking.txt','a') as file:
            file.write('user1 car1 user1 user1 user1 user1 user1 user1 user1\n')
            file.write('user2 car2 user2 user2 user2 user2 user2 user2 user2\n')
            file.write('user3 car3 user3 user3 user3 user3 user3 user3 user3\n')
            file.write('user4 car4 user4 user4 user4 user4 user4 user4 user4\n')
            file.write('user5 car5 user5 user5 user5 user5 user5 user5 user5\n')
            file.write('user6 car6 user6 user6 user6 user6 user6 user6 user6\n')
            file.write('user7 car7 user7 user7 user7 user7 user7 user7 user7\n')
            file.write('user8 car8 user8 user8 user8 user8 user8 user8 user8\n')
            file.write('user9 car9 user9 user9 user9 user9 user9 user9 user9\n')
            file.write('user10 car10 user10 user10 user10 user10 user10 user10 user10\n')
        with open('route.txt','x') as file:
            file.write('pickup destination date time price\n')
        #fill route file with realistic data
        with open('route.txt','a') as file:
            file.write('car1 car2 12/12/2021 12:00:00 100\n')
            file.write('car2 car3 12/12/2021 12:00:00 100\n')
            file.write('car3 car4 12/12/2021 12:00:00 100\n')
            file.write('car4 car5 12/12/2021 12:00:00 100\n')
            file.write('car5 car6 12/12/2021 12:00:00 100\n')
            file.write('car6 car7 12/12/2021 12:00:00 100\n')
            file.write('car7 car8 12/12/2021 12:00:00 100\n')
            file.write('car8 car9 12/12/2021 12:00:00 100\n')
            file.write('car9 car10 12/12/2021 12:00:00 100\n')
            file.write('car10 car1 12/12/2021 12:00:00 100\n')
        print('files created successfully')
    except:
        print('files already exist')
 

        

# create main function that asks for user login or register and then books a car by showing list of drivers to choose from or cancels a booking or search a booking
def main():
    create_files()
    print('Welcome to the car pooling system')
    print('1.Login')
    print('2.Register')
    choice=int(input('Enter your choice'))
    if choice==1:
        name=input('Enter your name')
        password=input('Enter your password')
        obj_user=user(name,password,0,0,0,0)
        obj_user.login(name,password)
        print('1.Book a car')
        print('2.Cancel a booking')
        print('3.Search a booking')
        choice1=int(input('Enter your choice'))
        if choice1==1:
            user_id=input('Enter your user id')
            car_id=input('Enter your car id')
            name=input('Enter your name')
            address=input('Enter your address')
            email=input('Enter your email')
            phone_no=input('Enter your phone no')
            date=input('Enter your date')
            model=input('Enter your model')
            #ask for pickup and destination
            print('Enter pickup')
            pickup=input('Enter pickup')
            print('Enter destination')
            destination=input('Enter destination')
            #create daate variable with current date
            date=" "
            #create time variable with current time
            time=" "
            #create price variable with random 3 digit price
            price=random.randint(100,1000)
            obj_booking=booking(user_id,car_id,name,address,email,phone_no,date,model,0,0,pickup,destination,time,price)
            obj_booking.register_booking(user_id,car_id,name,address,email,phone_no,date,model)
        elif choice1==2:
            user_id=input('Enter your user id')
            car_id=input('Enter your car id')
            name=input('Enter your name')
            address=input('Enter your address')
            email=input('Enter your email')
            phone_no=input('Enter your phone no')
            model=input('Enter your model')
            #create daate variable with current date
            date=" "
            #create time variable with current time
            time=" "
            #create price variable with random 3 digit price
            price=random.randint(100,1000)
            obj_booking.register_booking(user_id,car_id,name,address,email,phone_no,date,model)
            obj_booking.cancel_booking(user_id,car_id,name,address,email,phone_no,date,model)
        elif choice1==3:
            user_id=input('Enter your user id')
            car_id=input('Enter your car id')
            name=input('Enter your name')
            address=input('Enter your address')
            email=input('Enter your email')
            phone_no=input('Enter your phone no')
            date=input('Enter your date')
            model=input('Enter your model')
            obj_booking=booking(user_id,car_id,name,address,email,phone_no,date,model,0,0,pickup,destination,date,time,price)
            obj_booking.search_booking(user_id,car_id,name,address,email,phone_no,date,model)
    elif choice==2:
        name=input('Enter your name')
        password=input('Enter your password')
        obj_user=user(name,password,0,0,0,0)
        obj_user.register(name,password)
        print('1.Book a car')
        print('2.Cancel a booking')
        print('3.Search a booking')
        choice1=int(input('Enter your choice'))
        1
        if choice1==1:
            user_id=input('Enter your user id')
            car_id=input('Enter your car id')
            name=input('Enter your name')
            address=input('Enter your address')
            email=input('Enter your email')
            phone_no=input('Enter your phone no')
            date=input('Enter your date')
            model=input('Enter your model')
            #ask for pickup and destination
            print('Enter pickup')
            pickup=input('Enter pickup')
            print('Enter destination')
            destination=input('Enter destination')
            pickup=input('enter pickup')
            #create daate variable with current date
            date=" "
            #create time variable with current time
            time=" "
            #create price variable with random 3 digit price
            price=random.randint(100,1000)
            obj_booking=booking(user_id,car_id,name,address,email,phone_no,date,model,0,0,pickup,destination,time,price)
            obj_booking.register_booking(user_id,car_id,name,address,email,phone_no,date,model)
        elif choice1==2:
            user_id=input('Enter your user id')
            car_id=input('Enter your car id')
            name=input('Enter your name')
            address=input('Enter your address')
            email=input('Enter your email')
            phone_no=input('Enter your phone no')
            date=input('Enter your date')
            model=input('Enter your model')
            obj_booking=booking(user_id,car_id,name,address,email,phone_no,date,model,0,0,pickup,destination,date,time,price)
            obj_booking.cancel_booking(user_id,car_id,name,address,email,phone_no,date,model)
        elif choice1==3:
            user_id=input('Enter your user id')
            car_id=input('Enter your car id')
            name=input('Enter your name')
            address=input('Enter your address')
            email=input('Enter your email')
            phone_no=input('Enter your phone no')
            date=input('Enter your date')
            model=input('Enter your model')
            obj_booking=booking(user_id,car_id,name,address,email,phone_no,date,model,0,0,pickup,destination,date,time,price)
            obj_booking.search_booking(user_id,car_id,name,address,email,phone_no,date,model)
    else:
        print('wrong choice')

main()
    

        

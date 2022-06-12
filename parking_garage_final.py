class Zones:

    def __init__(self):
        Zone_1 = Parking_Garage()
        Zone_2 = Parking_Garage()
        Zone_3 = Parking_Garage()
        Zone_4 = Parking_Garage()
        Zone_1.name = "Zone 1"
        Zone_2.name = "Zone 2"
        Zone_3.name = "Zone 3"
        Zone_4.name = "Zone 4"
        self.floors = [Zone_1, Zone_2, Zone_3, Zone_4]
        self.totalspaces = Zone_1.parkingSpaces + Zone_2.parkingSpaces + Zone_3.parkingSpaces + Zone_4.parkingSpaces

    def checkAvailable(self):
        if self.totalspaces:
            print(f"""
            
            These Zones have spaces available:
            
            """)
            for zone in self.floors:
                if zone.parkingSpaces:
                    print(zone.name, end=" | ")
            self.enterZone()

        else:
            print("There are no more parking spaces available! Come back another time!")
            return
    
    def enterZone(self):
        proceed_park = input("Would you like to enter a lot? (y/n) ").lower().strip()
        if proceed_park == 'y':
            for zone in self.floors:
                print(zone.name, end=" | ")
            zone_choice = input("Which Zone would you like to choose? ").lower().strip()
            if zone_choice == "zone 1":
                self.floors[0].run2()
            elif zone_choice == "zone 2":
                self.floors[1].run2()
            elif zone_choice == "zone 3":
                self.floors[2].run2()
            elif zone_choice == "zone 4":
                self.floors[3].run2()
            else:
                print("invalid response")
                return
        else:
            print("Thank you!")
            return
    
    def run(self):
        print("""
        Welcome To LazyBoy! Home of Parking!
        
        
           - please drive up to proceed - """)
        self.checkAvailable()



class Customer:
    
    def __init__(self):
        self.ticket_num = None
        self.pay_status = ""


class Parking_Garage(Zones):

    def __init__(self):
        self.name = None
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.parkingSpaces = len(self.tickets)
        self.currentTicket = {} #instance of Customer: value self.pay_status,

  #takeTicket
    def take_ticket(self):
        if self.tickets:
            self.currentTicket[self.tickets.pop(0)] = ""
            print(self.tickets, self.currentTicket)
            print("Thank you. You are alloted 2 hours")
        else:
            print("Parking Spaces FULL")
            self.checkAvailable()
      


    def payForParking(self):
        ticket_num = int(input("You are about to pay for parking! What is your ticket number? "))

        while ticket_num not in self.currentTicket:
            print("INVALID TICKET")
            ticket_num = int(input("What is your ticket number? ('0' to quit | '911' for assistance"))
            if ticket_num == 0:
                return
            elif ticket_num == 911:
                self.Help()
                    
        if ticket_num in self.currentTicket:
            if self.currentTicket[ticket_num]:
                print("you already payed for your ticket!")
            else:
                self.currentTicket[ticket_num] = 'paid'
        else:
            print("INVALID TICKET")

    def Help(self):
        print("""
                
                """)
        return
  
  #leaveGarage  
    def leaveGarage(self):
        ticket_num = int(input("What is your ticket number? "))
        if ticket_num in self.currentTicket:
            if self.currentTicket[ticket_num]:
                del self.currentTicket[ticket_num]
                self.tickets.append(ticket_num)
            else:
                self.payForParking()
        else:
            print("INVALID TICKET")


  
    def run2(self):
      while True:
        response = input("""
                     Please press valid key:
                       [T] Take Ticket
                       [P] Pay For Ticket
                       [L] Leave   
                       """)
        if response.lower().strip() == 't':
            self.take_ticket()
        elif response.lower().strip() == 'p':
            self.payForParking()
        elif response.lower().strip() == 'l':
            self.leaveGarage()
        else:
            print("Please enter valid input: [P], [T], [L] ")

    

lucky = Zones()
lucky.run()




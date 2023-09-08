from Ticket import Ticket
from data import *


class TicketSystem:
    Ticket_list = []
    next_id = 2004


    # constructor
    def __init__(self):
        # existing tickets
        new_ticket = Ticket(2001, "Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working" )
        self.Ticket_list.append(new_ticket)

        new_ticket = Ticket(2002, "Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
        self.Ticket_list.append(new_ticket)

        new_ticket = Ticket(2003, "John", "JOHNS", "john@whitecliffe.co.nz", "Keyboard is not working")
        self.Ticket_list.append(new_ticket)
        
        # increment the next ticket id
        # self.next_id = 2004

    # display all tickets
    def display_all_tickets(self):

        if len(self.Ticket_list) == 0:
            print("No tickets available")

        for p in self.Ticket_list:
            p.display()

    #submit new ticket to system
    def add_new_ticket(self):
        print(f"\n{Magenta}===================================================" + RESET)
        print(f'''                Submit new Ticket         ''' )
        print(f"{Magenta}===================================================" + RESET)
        #ticket number automatically generated
        print(f'''\n{Default}   Ticket Number {DarkGray}(auto-generated):{Magenta}''' , self.next_id)
        # user input
        creator_name = input(f'''{Default}   Ticket Creator: {Magenta}''' )
        staff_id = input(f'''{Default}   Staff ID: {Magenta}''' )
        email= input(f'''{Default}   Email address: {Magenta}''')
        issue = input(f'''{Default}   Description of the issue: {Magenta}''')
        print(f'''\n{BackgroundDarkGray} Ticket has been successfully submitted! ''' + RESET) 
        
        # add the new ticket to list
        new_ticket = Ticket(self.next_id, creator_name , staff_id , email , issue)
        self.Ticket_list.append(new_ticket)
        self.next_id += 1

      

    #responding to tickets
    def respond(self):
     
        ticket_number = int(input(f'''\n{RESET}***************************************************
            {Magenta}Respond to Ticket          {RESET}
***************************************************
                 \n   Please enter ticket number: {Magenta}'''))
        for t in self.Ticket_list:
            if t.ticket_id == ticket_number:
                response = input(f'''{RESET}   IT response: {Magenta}''' )
                t.response = response
                t.ticket_status = "CLOSED"
                print(f'''\n{BackgroundDarkGray} Ticket has been successfully resolved and closed! ''' + RESET) 
                return
    
      
    #reopen a closed ticket
    def reopen(self):
       
        re_open= int(input(f'''\n{RESET}***************************************************
            {Magenta}Reopen a Ticket     {RESET}  
***************************************************
                 \n   Please enter ticket number: ''' + Magenta ))
        for r in self.Ticket_list:
            if r.ticket_id == re_open:
                r.ticket_status = "REOPENED"
                print(f'''\n{BackgroundDarkGray}  Ticket has been successfully reopened! Print the ticket to see the ticket information''' + RESET) 
        return




# #test 1 (displaying all tickets)
ts = TicketSystem()
# ts.display_all_tickets()

# #test 2 (submitting ticket)
# ts.add_new_ticket()

#test 3 reopen the ticket
# ts.reopen()

#test4 respond
# ts.respond()

 

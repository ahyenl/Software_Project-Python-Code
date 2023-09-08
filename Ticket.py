from data import *


class Ticket: 

    #constructor
    def __init__(self, ticket_id , creator_name ,  email , staff_id, issue):   
        self.ticket_id = ticket_id        
        self.creator_name = creator_name
        self.email = email
        self.staff_id = staff_id
        self.issue = issue
        self.response = "Not Yet Provided"
        self.ticket_status = "OPEN"

    
    #generate passwords  
        if self.issue.find("password") > -1 and self.issue.find("change") > -1:
            new_password = self.staff_id[:2] + self.creator_name[:3]            
            self.response = "\033[39mNew password = \033[32m " + new_password          
            self.ticket_status = "CLOSED"
            print(f'''\n{BackgroundDarkGray} NOTE: Password has been changed! Print the ticket to see the new password... ''' + RESET) 

  

    def display(self):
        print(f"\n{RESET}***************************************************")
        print(f'''  {LightGreen}            Printing Ticket         ''' + RESET)
        print(f"***************************************************")
        print(f'''   \n   Ticket Number \033[90m(auto-generated): {Magenta}''', self.ticket_id)
        print(f'''   {RESET}Ticket Creator: {GREEN}''' , self.creator_name )
        print(f'''   {RESET}Staff ID: {GREEN}''', self.staff_id )
        print(f'''   {RESET}Email address: {GREEN}''' , self.email )
        print(f'''   {RESET}Description of the issue: {GREEN}''' , self.issue )
        print(f'''   {RESET}Response: {GREEN}''' , self.response)
        print(f'''   {RESET}Ticket status: {RED}''' , self.ticket_status )
  
        



# #ticket test
# t1 = Ticket(2001, "Inna", "INNAM", "inna@whitecliffe.co.nz", "change password" )
# t1.display()











    
        
    

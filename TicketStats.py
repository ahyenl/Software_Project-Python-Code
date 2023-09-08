from Ticket import *
from TicketSystem import TicketSystem


class TicketStats():

    # def __init__(self, ticket_status ):
    #     self.ticket_status = ticket_status

    #displaying all the tickets
    def all_tickets(self): 
        return len(TicketSystem.Ticket_list)
    
    #counting the closed tickets
    def closed_tickets(self):
        count_Closed = 0
        for ticket_item in TicketSystem.Ticket_list:
            if ticket_item.ticket_status == "CLOSED":
                count_Closed += 1
        return int(count_Closed)

    #counting the open tickets
    def open_tickets(self):
        count_Open = 0
        for ticket_item in TicketSystem.Ticket_list:
            if ticket_item.ticket_status == "OPEN" or ticket_item.ticket_status == "REOPENED":
                count_Open = count_Open + 1
        return int(count_Open)
    
     #displaying ticket statistics
    def displayStats(self):
        print(f"\n{RESET}***************************************************")
        print(f'''  {Magenta}           Displaying Statistics         ''' + RESET)
        print(f"***************************************************")
        print(f"\n   Tickets Created: {Magenta}" , self.all_tickets()) 
        print(f"   {RESET}Tickets Resolved: {Magenta}" , self.closed_tickets())
        print(f"   {RESET}Tickets to Solve: {Magenta}" , self.open_tickets() , "\n")
        

#test 1 (displaying ticket statistics)
stats = TicketStats()
# stats.displayStats()


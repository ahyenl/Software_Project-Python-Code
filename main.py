from Ticket import *
from TicketSystem import *
from TicketStats import *
from data import *
import time

if __name__ == "__main__":



    while True:
        print(f"\n{RESET}===================================================")
        print(f'''  {BackgroundMagenta}***  Kia Ora! WELCOME TO HELPDESK TICKET  *** {RESET}''' )       
        print("===================================================")
        print(f''' \n{Magenta}   Please select a number to start {RESET}''' )
        print(f'''\n   To submit a ticket press {Magenta}'1' ''' + RESET)
        print(f'''   To print tickets press {Magenta}'2' ''' + RESET)
        print(f'''   To display the statistics press {Magenta}'3' ''' + RESET)
        print(f'''   To respond to a ticket press {Magenta}'4' ''' + RESET)
        print(f'''   To reopen a ticket press {Magenta}'5' ''' + RESET)
        print(f'''   To exit press {Magenta}'0' ''' + RESET)
        choice = input(f''' \n   Enter your choice: ''' + Magenta )
        if choice ==  "1":
            ts.add_new_ticket()
        elif choice == "2":
            ts.display_all_tickets()
        elif choice == "3":
            stats.displayStats()
        elif choice == "4":
            ts.respond()
        elif choice == "5":
            ts.reopen()
        elif choice == "0":
            print(f'''\n{BackgroundDarkGray} {Magenta}Thank you for using ticket system..Exiting in 5 seconds...\n''' + RESET)
            time.sleep(5) 
            exit ()
        else:
            print(f"\n{RED}Incorrect number!!! Please select from menu..")

        



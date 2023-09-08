
# Helpdesk Ticket System

Kia Ora, Welcome to the Helpdesk Ticket System! This simple command-line application allows you to manage and track support tickets. You can submit new tickets, view existing tickets, display statistics, respond to tickets, and reopen closed tickets. This README file provides an overview of how to use the system and explains the code structure.



# Getting Started

You will need the following Python files in your project directory:


    Ticket.py: Contains the Ticket class, which defines the structure of a support ticket.
    TicketSystem.py: Contains the TicketSystem class, which manages the ticket-related operations.
    TicketStats.py: Contains the TicketStats class, responsible for displaying statistics about the tickets.
    data.py: Contains data structures to store tickets and other data.
    main.py: The main application script you provided in the code snippet.






# Usage

To start using the ticketing system, follow the below procedure to run the system:

Command Prompt

    Open the Start menu or press the Windows key + R.
    Type cmd or cmd.exe in the Run command box.
    Press Enter.

Type cd followed by the path file of the python folder then enter

```bash
  cd C:\Users\devkd\Desktop\Software Project
```

Type the python main.py to run the menu

```bash
C:\Users\devkd\Desktop\Software Project> python main.py ```


You will be presented with a menu like this:


===================================================
  Kia Ora! WELCOME TO HELPDESK TICKET  *** 
===================================================

    Please select a number to start 

   To submit a ticket press '1' 
   To print tickets press'2' 
   To display the statistics press '3' 
   To respond to a ticket press '4' 
   To reopen a ticket press '5' 
   To exit press '0' 

   Enter your choice:   
 ```

Choose an option by entering the corresponding number and pressing Enter.

Depending on your choice, follow the on-screen instructions to perform the desired operation.

# Code Structure

Here is a brief overview of the code structure in main.py:

The script imports necessary modules and classes at the beginning.
The main program loop starts with while True to repeatedly display the menu and process user input.
User input is captured using the input() function, and the corresponding action is taken based on the choice entered.
The code is designed to be interactive and user-friendly, allowing you to perform various ticket management tasks seamlessly.

Exiting the System

To exit the Helpdesk Ticket System, simply choose option '0' from the menu. The system will display a thank you message and exit after a 5-second delay.

```bash
    Thank you for using the ticket system.. Exiting in 5 seconds... 
 ```  



Enjoy using the Helpdesk Ticket System! 



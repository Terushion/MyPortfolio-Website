""" Practical Task - OOP Email Simulator """

"""
# Attributes
has_been_read: Whether an email has already been read.
email address - anything, e.g. example@example.co.uk
subject line - Heading for an email, usually mentioning what email content will include
email content - content of an email 
"""

"""
# Methods
mark as read - Marks an Email as read.
has_been_read = False
def __init__(self, email_address):
    Creates an Email object with the given properties.
Args:
email_address(str): This email's address.

"""

class Email:

    """
        This program implements a simple Email simulator. 
        Classes:
        - Email: Stores email information.

        Functions:
        - populate_inbox: Adds example emails to the global `inbox` list.

        class Email:
        Represents an Email.

        """

    # Creating the class, constructor and methods to create a new Email object.
    # Declared the class variable, with default value, for emails. 
    # Initialised the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    

    # Created the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True



# Initialised an empty list to store the email objects.
inbox = []

# Building out the required functions for your program.
# Created 3 sample emails and add it to the Inbox list. 
def populate_inbox():
    first_email = Email("dev@hyperion.co.uk", "Welcome to Hyperiondev!",
                        "We are thrilled to welcome you onto our course!")
    second_email = Email("rep@hyperion.co.uk", "Great work on the bootcamp!",
                          "You are making great progress, Don't forget to take enough rests!")
    third_email = Email("lecturer1@hyperion.co.uk", "Your excellent marks!",
                    "Congratulations! You did a wonderful job, you should be proud!")
    
    inbox.append(first_email)
    inbox.append(second_email)
    inbox.append(third_email)


# Create a function which prints the email’s subject_line, along with a corresponding number.
def list_emails():
    print("\nInbox:")
    for idx, subject in enumerate(inbox):
        print(f"{idx+1}. {subject.subject_line}")
        # Using '.subject_line' ensures we print out every subject_line in the inbox
        # as opposed to a singular one e.g. first_email.subject_line
        # variable name 'subject' in for has to be same as one before
        # .subject_line


# Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.    
def read_email(index):

    # logic here is to retrieve an object from inbox list using index
    # The user's choice will be the index as seen below in the while loop
    # By using an 'if not' function, we can say if this is not true essentially

    email_object = inbox[index-1]
    if not email_object.has_been_read:
        print("\n:")
        print(f"From: {email_object.email_address}")
        print(f"Subject: {email_object.subject_line}")
        print(f"Content: {email_object.email_content}")
        email_object.mark_as_read()

    elif email_object.has_been_read:
        print(f"\nEmail {email_object.email_address} has been read")
    else:
        print("Invalid input")


# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
# Fill in the logic for the various menu operations.

menu = True
populate_inbox()

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
         
        list_emails()
        read_choice = int(input("\nWhich email do you want to read (enter selection): "))
        read_email(read_choice)
        
        # add logic here to read an email
    elif user_choice == 2:
        print("\nUnread Emails:")
        for idx, object in enumerate(inbox):
            if not object.has_been_read:
                print(f"{idx+1}. {object.subject_line}")

        # add logic here to view unread emails         
    elif user_choice == 3:
        # add logic here to quit appplication
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Oops - incorrect input.")



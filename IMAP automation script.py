from imap_tools import MailBox as Mail #I dislike the default imap tools for python. This is easier to use.


with Mail('imap.gmail.com').login('Email', 'App Password') as mail: #this logs into the email account, for the love of god don't use Gmail like me, it sucks for this.
    for msg in mail.fetch():
        mail.delete(msg.uid)
    print("instantiated") #These last 3 lines of code delete the whole inbox, because if there's already an email from the account "action@ifttt.com" it will read an unintended message.
    while True:
        mail.idle.wait(timeout=1)
        for msg in mail.fetch():
            if msg.from_ == "action@ifttt.com":
                print("Message received")
                mail.delete(msg.uid) #These lines of code wait for an email from the particular account. It is deleted for the same reason the inbox is deleted on launch.
                

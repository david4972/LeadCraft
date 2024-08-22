import smtplib


'''
# email notifications
class Email_System:

    def send_mail_for_account_recovery(cardNo=int, cardcode=str, mz=str):
        msg = "{} this is your new virtual card number. {} is your new card code, please keep secured and not protected}"
        new = (msg.format(cardNo, cardcode))

        sender_email = "monetarytransatlantic@gmail.com"
        rec_email = mz
        password = "ladfpscfaupnptmn"
        message = new
        # Gmail Accounts
        if "gmail" in mz:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            print("login success")
            server.sendmail(sender_email, rec_email, message)
            server.close()
        # Yahoo Accounts
        if "yahoo" in mz:
            fromMy = "openbank143@yahoo.com"
            to = mz
            subj = 'New Pin Number'

            msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

            username = "openbank143@yahoo.com"
            password2 = "uskgkpnokoilawmt"
            server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            server.starttls()
            server.login(username, password2)
            server.sendmail(fromMy, to, msg)
            server.close()
            return 'ok the email has sent '


    def send_mail_for_currency_exchange(curr=str, mz=str):
        msg = "you recently change the currency in which your account is in to {}. you were charged 1.3% upon exchange."
        new = (msg.format(curr))

        sender_email = "monetarytransatlantic@gmail.com"
        rec_email = mz
        password = "ladfpscfaupnptmn"
        message = new
        # Gmail Accounts
        if "gmail" in mz:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            print("login success")
            server.sendmail(sender_email, rec_email, message)
            server.close()
        # Yahoo Accounts
        if "yahoo" in mz:
            fromMy = "openbank143@yahoo.com"
            to = mz
            subj = 'New Pin Number'

            msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

            username = "openbank143@yahoo.com"
            password2 = "uskgkpnokoilawmt"
            server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            server.starttls()
            server.login(username, password2)
            server.sendmail(fromMy, to, msg)
            server.close()
            return 'ok the email has sent '


    def send_mail_for_newCrypt(Cryp=str, mz=str):
        msg = "{} this is your Digital Credit Code Please memorize the last 6 digits"
        new = (msg.format(Cryp))

        sender_email = "monetarytransatlantic@gmail.com"
        rec_email = mz
        password = "ladfpscfaupnptmn"
        message = new
        # Gmail Accounts
        if "gmail" in mz:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            print("login success")
            server.sendmail(sender_email, rec_email, message)
            server.close()
        # Yahoo Accounts
        if "yahoo" in mz:
            fromMy = "openbank143@yahoo.com"
            to = mz
            subj = 'New Pin Number'

            msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

            username = "openbank143@yahoo.com"
            password2 = "uskgkpnokoilawmt"
            server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            server.starttls()
            server.login(username, password2)
            server.sendmail(fromMy, to, msg)
            server.close()
            return 'ok the email has sent '


    def send_mail_for_Transactions(n=str, mail=str, amt=str):
        email = mail
        trans = amt
        name = n
        sender_email = "monetarytransatlantic@gmail.com"
        rec_email = email
        password = "ladfpscfaupnptmn"
        message = "You have received $ " + trans + " from " + name
        # Gmail Accounts
        if "gmail" in email:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, rec_email, message)
            server.close()
        # Yahoo Accounts
        if "yahoo" in email:
            fromMy = "openbank143@yahoo.com"
            to = email
            subj = 'Transaction'

            msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

            username = "openbank143@yahoo.com"
            password2 = " uskgkpnokoilawmt"
            server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            server.starttls()
            server.login(username, password2)
            server.sendmail(fromMy, to, msg)
            server.close()

'''
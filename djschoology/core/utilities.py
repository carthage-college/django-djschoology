import smtplib
from logging.handlers import SMTPHandler

from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders



def fn_send_mail(to, frum, body, subject):
    """
    Stock sendmail in core does not have reply to or split of to emails
    --email to addresses may come as list
    """

    print(to.split(','))

    server = smtplib.SMTP('localhost')

    try:
        msg = MIMEText(body)
        msg['To'] = to
        msg['From'] = frum
        msg['Subject'] = subject
        txt = msg.as_string()

        # print("ready to send")
        # show communication with the server
        # if debug:
        #     server.set_debuglevel(True)
        # print(msg['To'])
        # print(msg['From'])
        server.sendmail(frum, to.split(','), txt)

    except Exception as e:
        print(
                "Error in utilities.py fn_send_mail:  " + repr(e))
        # fn_write_error(
        #     "Error in utilities.py fn_send_mail.py:" + repr(e))

    finally:
        server.quit()
        # print("Done")
        pass

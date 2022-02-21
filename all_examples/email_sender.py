from basescript import BaseScript
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailSender(BaseScript):

    def __init__(self):
        """
        Initialize connections and emails
        """
        super().__init__()
        self.port = 465
        self.sender_email = "sender email"
        self.receiver_email = input("Enter receiver email")
        self.secure_conn = ssl.create_default_context()
        self.message = MIMEMultipart("alternative")
        self.text = "This is a mail sending test"
        self.mail_content = MIMEText(self.text, "plain")

    def message_maker(self):
        """
        Add from, to, subject of the email
        :return: nothing
        """
        self.message["subject"] = "Mail test"
        self.message["from"] = self.sender_email
        self.message["to"] = self.receiver_email

        self.message.attach(self.mail_content)

    def define_args(self, parser):
        parser.add_argument('password', type=str, help='Enter your mail password')

    def run(self):
        """
        Sends email to the given email address
        :return: nothing
        """
        self.message_maker()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.secure_conn) as server:
                server.login(self.sender_email, self.args.password)
                server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())
        except Exception as e:
            self.log.info(e)


if __name__ == '__main__':
    MailSender().start()


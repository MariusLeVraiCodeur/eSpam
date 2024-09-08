import smtplib
import customtkinter

root = customtkinter.CTk()
def send():
    while True:
        subject = subject_email.get()
        message = message_email.get()
        text = f"Subject : {subject}\n\n{message}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(send_email.get(), "ytbwlekfrdgcongh")
        server.sendmail(send_email.get(), receiver_email.get(), text)
root._set_appearance_mode("dark")
root.iconbitmap("email.ico")
root.title("eSpam")
root.minsize(300, 200)
root.maxsize(300, 200)

send_email = customtkinter.CTkEntry(root, width=200, height=30)
send_email.place(x=40, y=0)
send_email.insert(0, "Your email address")

receiver_email = customtkinter.CTkEntry(root, width=200, height=30)
receiver_email.place(x=40,y=30)
receiver_email.insert(0, "The receiver email address")

subject_email = customtkinter.CTkEntry(root, width=200, height=30)
subject_email.place(x=40,y=60)
subject_email.insert(0, "The subject")

message_email = customtkinter.CTkEntry(root, width=200, height=30)
message_email.place(x=40,y=90)
message_email.insert(0, "The message")

button = customtkinter.CTkButton(root, width=50, height=20, text="Send", command=send)
button.place(x=100, y=130)

root.mainloop()

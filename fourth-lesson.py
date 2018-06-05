from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8bc1528aa3592a5f04d47745b85c242f"
# Your Auth Token from twilio.com/console
auth_token  = "04ce159e3e4d3f97e4450e27f3df2545"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+55(11)986363991",
    from_="+1(864)301-6516",
    body="VAI TOMAR NO CÚ!")

print(message.sid)
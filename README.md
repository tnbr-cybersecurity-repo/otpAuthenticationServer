# OTP Authentication Server
## A1: Build an OTP Authentication Server

### Instructions
Implement a software client and server app simulating the OTP Authentication mechanism using the hashlib.sha256(input_message).hexdigest. 

The client will simulate sending ten (10) different login trials with ten (10) different OTPs, of which Two (2) of these trials will use incorrect OTPs. 

The server will respond to each trail by sending a response to the client: "<em><b>Access Granted</em></b>" OR "<b><em>Denied</em></b>" message. 

Both the client and the server will need to be in sync with the OTP seed used to calculate the OTPs and the index of the current OTP must be synced to both the client and server.

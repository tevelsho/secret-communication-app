This Python application I created allows users to encrypt and decrypt messages using a secret key. The GUI interface provides a text box to input messages, another text box for the secret key (which is hidden), and buttons to encrypt, decrypt, and clear inputs.

Modules Used

    base64: Used for encoding and decoding messages. (which can changed, according to user to modify the code)
    tkinter: Used for the graphical user interface.
    
Instructions

    Install Required Packages:
        Ensure you have tkinter installed (usually comes with Python).
        No additional installation steps required for base64.

    Run the Application:
        Run the Python script to start the application.

    python3 secret_communication_app.py

Usage

    Encrypting a Message:
        Enter the message in the "Enter Plaintext" box.
        Enter the secret key in the "Enter Secret Key" box (e.g. 1234).
        Click the "ENCRYPT" button.
        The encrypted message will be displayed in a new window.

    Decrypting a Message:
        Enter the encrypted message in the "Enter Plaintext" box.
        Enter the secret key in the "Enter Secret Key" box (e.g. 1234).
        Click the "DECRYPT" button.
        The decrypted message will be displayed in a new window.

    Clearing Inputs:
        Click the "CLEAR" button to clear both the message and the secret key inputs.


def send_email(to_email, data):
    msg = "Hi,\n\n"
    msg += "I hope this email finds you well.\n\n"
    msg += "We have received a new inquiry through the inquiry form. Below are the details submitted by the potential client:\n"

    for key, value in data.items():
        msg += f"{key.title()}: {value}\n"

    msg += "\n"
    msg += "Please review the information and reach out to the potential client to provide the necessary assistance. If you need any further information or assistance, feel free to let me know.\n\n"
    msg += "Thank you!\n\n"
    msg += "Best regards,\n"
    msg += "CyberKernel (bit.ly/cyberkernel)"
  
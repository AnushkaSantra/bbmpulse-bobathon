
def send_whatsapp_update(ticket_id, lang="en"):
    messages = {
      "en": f"Your complaint {ticket_id} is In Progress. Team assigned.",
      "kn": f"ನಿಮ್ಮ ದೂರು {ticket_id} ಪ್ರಗತಿಯಲ್ಲಿದೆ. ತಂಡ ನಿಯೋಜಿಸಲಾಗಿದೆ."
    }
    return messages.get(lang, messages["en"])

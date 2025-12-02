from notify_africa import NotifyAfrica

client = NotifyAfrica(apiToken="ntfy_db01f5be9e3ca6759876df010e3bfc93179f569522df632c66255814f6dc0b48")
response = client.send_single_message(
    phoneNumber="255717563837",
    message="Hello! How are you, this is a test message from the API",
    senderId="164"
)
print(f"Response: {response}")
print(f"Message ID: {response.messageId}")
print(f"Status: {response.status}")
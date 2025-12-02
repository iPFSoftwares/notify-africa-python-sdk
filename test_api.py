from notify_africa import NotifyAfrica

client = NotifyAfrica(apiToken="ntfy_...")
response = client.send_single_message(
    phoneNumber="2557XXXXXXXX",
    message="Hello! How are you, this is a test message from the API",
    senderId="164"
)
print(f"Response: {response}")
print(f"Message ID: {response.messageId}")
print(f"Status: {response.status}")
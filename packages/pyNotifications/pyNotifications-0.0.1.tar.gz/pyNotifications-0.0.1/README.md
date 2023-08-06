## Python Notifications

Send telegram messages through python. Telegram bot is needed.

### Usage

```
notifyer = PythonNotifications(token=TOKEN, id=CHAT_ID, appName='test')

notifyer.addMessage('Info test', 'info')
notifyer.addMessage('Warning test', 'warning')
notifyer.addMessage('Error test', 'error')

notifyer.sendMessage('error')
notifyer.sendMessage('warning')
notifyer.sendMessage('info')
```

# Email confirm

A simple python module designed to receive temporary mail and work with it.

Site 10minutemail.net


## Usage/Examples
```python
pip install requests
pip install beautifulsoup4
```
```python
from email_confirm import TempMail

tm = TempMail()
tm.create()
tm.get_mails()
```


## Documentation

After creating a TempMail instance, you can call methods on it.

create - get new temporary mail

get_mails - returns a dictionary of letters in the mail.

## Authors

- [@DarkGear](https://portfolio.darkgear.org)


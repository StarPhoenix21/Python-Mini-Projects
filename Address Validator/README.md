<!--Please do not remove this part-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# Address Validator

## 🛠️ Description

This program validates email addresses through multiple checks, including syntax validation, disposable domain detection, and DNS MX record verification. It ensures that the email address contains an '@' symbol, checks for proper length constraints, and verifies that the domain is not from a disposable email service. The program also supports internationalized domain names, enhancing its usability for a global audience.

## ⚙️ Languages and Packages Used

- **Language**: Python
- **Packages**:
  - `dnspython` - For DNS resolution and MX record checks
  - `idna` - To handle internationalized domain names

## 🌟 How to Run

Open the `AddressValidator.py` file with a Python IDE and hit run.

## 📦 Requirements

To install the necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
```
## 🤖 Authors

- **m-hassanqureshi** - Primary author of the renewed code
- **tommcgurn10** - Original author of the initial project

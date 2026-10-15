# OCI Ampere Instance Availability Monitor

A lightweight Python script to monitor the availability of Oracle Cloud Infrastructure (OCI) Ampere (`VM.Standard.A1.Flex`) instances in your tenancy and availability domains. When capacity becomes available, it logs the status in real-time and sends an automated email alert via Gmail SMTP.

## Features

- **Automated Polling:** Periodically checks capacity across all Availability Domains in your tenancy (every 15 minutes).
- **Console Feedback:** Uses `rich` for clean, color-coded console output with timestamps and status indicators.
- **Email Notifications:** Sends an email notification to your inbox as soon as host capacity is detected (status other than `OUT_OF_HOST_CAPACITY`).

## Prerequisites

- Python 3.8+
- An Oracle Cloud Infrastructure (OCI) account with an API signing key configured
- A Gmail account with a [Google App Password](https://myaccount.google.com/apppasswords) generated for email alerts

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd oci-amphere-server-availability-checker
   ```

2. **Install required dependencies:**
   ```bash
   pip install oci rich python-dotenv
   ```

## Configuration

### 1. OCI API Credentials

1. Copy or rename `example.config` to `config`:
   ```bash
   cp example.config config
   ```
2. Enter your OCI credentials in `config`:
   ```ini
   [DEFAULT]
   user=ocid1.user.oc1..aaaaaaa...
   fingerprint=xx:xx:xx:...
   tenancy=ocid1.tenancy.oc1..aaaaaaa...
   region=us-ashburn-1
   key_file=/path/to/your/oci_api_key.pem
   ```

### 2. Email Alert Settings

1. Copy or rename `example.env` to `.env`:
   ```bash
   cp example.env .env
   ```
2. Configure your email credentials in `.env`:
   ```env
   SENDER_EMAIL=your_sender_gmail@gmail.com
   RECEIVER_EMAIL=your_receiver_email@example.com
   SENDERS_GOOGLE_APP_PASSWORD=your_16_digit_app_password
   ```

> [!NOTE]
> `SENDERS_GOOGLE_APP_PASSWORD` requires a 16-character App Password generated from your Google Account (Security &rarr; 2-Step Verification &rarr; App Passwords), not your standard Gmail login password.

## Usage

Run the script to begin monitoring:

```bash
python start.py
```

The script will query your OCI availability domains every 15 minutes. As soon as capacity is available, it will print the status in green and trigger an email notification.

Press `Ctrl + C` at any time to exit.
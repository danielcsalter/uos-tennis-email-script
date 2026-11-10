# UoS Tennis Court Booking Emailer

A Python automation tool that streamlines court booking communications for the **University of Sheffield Tennis Club**.

The script connects to Google Sheets to retrieve court booking requests and automatically sends players either a booking confirmation containing their court details and access code, or an email notifying them that their requested slot is unavailable.

Designed to replace repetitive manual email administration and make managing tennis court bookings quicker and easier.

---

## Features

- **Automated booking confirmations** – Sends players an email containing their booking details, including the courts, date, time, court number and access code.
- **Booking rejection notifications** – Automatically informs players when their requested court slot is unavailable.
- **Google Sheets integration** – Retrieves booking information directly from a Google Sheet populated by booking form responses.
- **Duplicate email prevention** – Tracks completed bookings to prevent the same email being sent multiple times.
- **Automatic status updates** – Marks bookings as completed in Google Sheets once an email has been successfully sent.
- **Error handling** – Reports failed email attempts without marking the booking as completed, allowing it to be retried.

## How It Works

The application follows a simple automated workflow:

1. A player submits a court booking request through a Google Form.
2. The booking response is added to the connected Google Sheet.
3. An administrator assigns the appropriate court and access code, or marks the booking as rejected.
4. The administrator runs the Python script.
5. The script checks the spreadsheet for bookings that have not yet been completed.
6. Depending on the booking status:
   - **Accepted:** The player receives a confirmation email containing their booking details.
   - **Rejected:** The player receives an email explaining that their requested slot is unavailable.
7. Once the email is successfully sent, the corresponding row is marked as `TRUE` in the `Completed` column.

This ensures that previously processed bookings are skipped on subsequent runs.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application and automation logic |
| Google Sheets API | Accessing and managing booking information |
| gspread | Interacting with Google Sheets |
| google-auth | Google service account authentication |
| smtplib | Sending emails through Gmail SMTP |
| python-dotenv | Managing environment variables and credentials |

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/danielcsalter/uos-tennis-email-script.git
```

Navigate into the project directory:

```bash
cd uos-tennis-email-script
```

### 2. Install dependencies

Install the required Python packages:

```bash
pip install gspread google-auth python-dotenv
```

### 3. Configure Google Sheets API access

The application uses Google service account authentication to access the booking spreadsheet.

To configure this:

1. Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the Google Sheets API.
3. Create a service account and generate a JSON key.
4. Download the JSON credentials file.
5. Save the file in the root directory of the project as:

```text
credentials.json
```

6. Share the Google Sheet with the service account's email address, granting it permission to edit the spreadsheet.

**Important:** The application expects a worksheet named `Form responses 1`.

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
api_key=YOUR_GOOGLE_SPREADSHEET_ID

gmail_email=YOUR_GMAIL_ADDRESS
gmail_pass=YOUR_GMAIL_APP_PASSWORD
gmail_name=YOUR_SENDER_NAME
```

- `api_key`: The ID of the Google Spreadsheet.
- `gmail_email`: The Gmail account used to send booking emails.
- `gmail_pass`: The Gmail app password used for SMTP authentication.
- `gmail_name`: Sender name configuration (currently read by the script but not used in the outgoing email).

For Gmail, an app password requires a Google account with 2-Step Verification enabled.

**Security:** Never commit your `.env` file or `credentials.json` to GitHub. Both are excluded through `.gitignore`.

## Google Sheets Structure

The script expects the booking spreadsheet to contain the following column headers:

| Column | Description |
|---|---|
| `Email address` | Player's email address |
| `What is your full name?` | Player's full name |
| `Which courts?` | Requested tennis park/courts |
| `What day? Please remember to give at least 72 hours' notice before your desired time.` | Requested booking date |
| `What time? If booking for a ladder match each of you can book an hour back to back.` | Requested booking time |
| `Court` | Assigned court |
| `Code` | Court access code |
| `Rejected` | Indicates whether the booking is unavailable |
| `Completed` | Indicates whether the email has been successfully sent |

The `Completed` and `Rejected` columns must exist for the script to run.

**Booking status:**
- `Completed = TRUE`: Booking has already been processed and will be skipped.
- `Rejected = TRUE`: An unavailable-slot notification will be sent.
- `Rejected = FALSE`: A booking confirmation will be sent.

For accepted bookings, ensure the `Court` and `Code` fields have been populated before running the script.

## Usage

Once the Google Sheets and email configurations are complete, run:

```bash
python main.py
```

The script will automatically:

1. Connect to the configured Google Spreadsheet.
2. Retrieve all booking responses.
3. Skip bookings already marked as completed.
4. Send the appropriate email based on the rejection status.
5. Update the `Completed` column following successful email delivery.
6. Print the outcome of each email attempt in the terminal.

Example terminal output:

```text
Sent booking email to player@example.com
Sent unavailable email to player2@example.com
FAILED (booking email) for player3@example.com
```

Bookings that fail to send remain uncompleted and can be retried during the next execution.

## Project Structure

```text
uos-tennis-email-script/
│
├── main.py             # Main application and booking processing logic
├── sendEmail.py        # Email generation and SMTP functionality
├── sheetConnect.py     # Google Sheets API connection
│
├── .env                # Environment variables (not committed)
├── credentials.json    # Google service account credentials (not committed)
│
├── .gitignore          # Excludes sensitive and unnecessary files
└── README.md           # Project documentation
```


## Security

The application uses Google service account credentials and Gmail SMTP authentication.

Sensitive files, including `.env` and `credentials.json`, should never be committed to version control.

Ensure that access to the Google service account and sending Gmail account is restricted appropriately.


This project is currently maintained for the University of Sheffield Tennis Club.

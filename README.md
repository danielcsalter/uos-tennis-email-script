UoS Tennis Court Booking Emailer

A Python automation script that turns court booking requests from a Google Form into confirmation emails, with no copying and pasting. It reads new bookings from a Google Sheet, emails each player their court and access code, and marks the booking as done so nobody is emailed twice.

Built for the University of Sheffield Tennis Club to replace a manual, repetitive admin task.

A player submits the booking form, which adds a row to the linked Google Sheet.
Once a court and access code have been assigned in the sheet, the admin runs the script.
For every row not yet marked complete, the script emails the player their booking details.
On success, the script writes TRUE to that row's Completed column.

Uses Python, smtplib, Google Cloud API, gspread, google-auth, python-dotenv

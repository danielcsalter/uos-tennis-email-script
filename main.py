from sheetConnect import get_sheet
from sendEmail import send_email_booked, send_email_unavailable

def is_true(value):
    return str(value).strip().upper() == "TRUE"

sheet = get_sheet()
headers = sheet.row_values(1)

for required in ("Completed", "Rejected"):
    if required not in headers:
        raise SystemExit(f'Column "{required}" not found in the sheet. Check the header name.')

rows = sheet.get_all_records()
completed_col = headers.index("Completed") + 1

for i, row in enumerate(rows, start=2):  # row 1 is the header
    if is_true(row["Completed"]):
        continue

    email = row["Email address"]
    name = row["What is your full name?"]

    if is_true(row["Rejected"]):
        success = send_email_unavailable(email=email, name=name)
        label = "unavailable email"
    else:
        success = send_email_booked(
            email=email,
            name=name,
            park=row["Which courts?"],
            date=row["What day? Please remember to give at least 72 hours' notice before your desired time."],
            time=row["What time? If booking for a ladder match each of you can book an hour back to back."],
            court=row["Court"],
            code=row["Code"],
        )
        label = "booking email"

    if success:
        # Marking Completed stops this row being emailed again on the next run
        sheet.update_cell(i, completed_col, "TRUE")
        print(f"Sent {label} to {email}")
    else:
        print(f"FAILED ({label}) for {email}")
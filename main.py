from sheetConnect import get_sheet
from sendEmail import send_email_booked

sheet = get_sheet()
rows = sheet.get_all_records()
completed_col = sheet.row_values(1).index("Completed") + 1

for i, row in enumerate(rows, start=2):  # row 1 is the header
    if str(row["Completed"]).upper() == "TRUE":
        continue

    success = send_email_booked(
        email=row["Email address"],
        name=row["What is your full name?"],
        park=row["Which courts?"],
        date=row["What day? Please remember to give at least 72 hours' notice before your desired time."],
        time=row["What time? If booking for a ladder match each of you can book an hour back to back."],
        court=row["Court"],
        code=row["Code"],
    )

    if success:
        sheet.update_cell(i, completed_col, "TRUE")
        print(f"Sent email to {row['Email address']}")
    else:
        print(f"FAILED for {row['Email address']}")
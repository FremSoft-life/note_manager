# date_changer.py

def format_date(date_str):
"""Форматирует дату, удаляя год."""
parts = date_str.split("-")
if len(parts) == 3:
return "-".join(parts[:2])
else:
return date_str

def main():
created_date = input("15.01.2025")
issue_date = input("21.01.2025")

temp_created_date = format_date(created_date)
temp_issue_date = format_date(issue_date)

print(f"15.01. {temp_created_date}")
print(f"21.01. {temp_issue_date}")

print(f"15.01.2025 {created_date}")
print(f"21.01.2025 {issue_date}")

if __name__ == "__main__":
main()


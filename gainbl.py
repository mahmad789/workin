# import time
# import smtplib
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import datetime
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# BASE_URL = "https://gainblers.com/la/tipsters/latambet/pronosticos/"

# def send_email_alert(subject, body):
#     sender_email = "testingformerightnow@gmail.com"
#     receiver_email = "ahmadmubashir9009@gmail.com"
#     password = "jzvq wyhk xrkp qynt"  

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, password)
#         server.send_message(message)
#         print("Alert email sent!")

# def parse_date(date_str):
#     # Dummy parser; you can modify according to actual format
#     return date_str

# def scrape_data():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--fasle")  # Optional: run in background
#     service=Service("C:/Users/Cominn/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
#     driver = webdriver.Chrome(options=options,service=service)

#     driver.get(BASE_URL)

#     try:
#         # WebDriverWait(driver, 10).until(
#         #     EC.element_to_be_clickable((By.XPATH, "//*[@id='accept-age']"))
#         # ).click()

#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="modalPais"]/div/div[2]/div/a[1]'))
#         ).click()
#         time.sleep(3)
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//*[@id='accept-age']"))
#         ).click()

#         time.sleep(10)
#         soup = BeautifulSoup(driver.page_source, "html.parser")
#         rows = soup.find_all("div", class_="td flex7 f-row td-event-with-calendar")
#         picks = soup.find_all("li", class_="tr part")
#         print(picks)

#         pendiente_found = False

#         for i, row in enumerate(rows):
#             try:
#                 event_name = row.find("p", class_="event").text.strip().replace("Pronóstico", "").strip()
#                 country = row.find("p", class_="league").text.strip()
#                 date_str = row.find("span", class_="calendar").text.strip()
#                 event_date = parse_date(date_str)

#                 pick_div = picks[i]
#                 if "Pendiente" in pick_div.text:
#                     pendiente_found = True
#                     print(f"[ALERT] Pendiente found in event: {event_name} - {country} - {event_date}")
                
#             except Exception as e:
#                 print("Error in row parsing:", e)

#         if pendiente_found:
#             send_email_alert(
#                 subject="Pendiente Alert from Gainblers",
#                 body="One or more predictions are marked as 'Pendiente'. Please check the site: " + BASE_URL
#             )

#     finally:
#         driver.quit()
# scrape_data()




# import time
# import smtplib
# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import os

# BASE_URL = "https://gainblers.com/la/tipsters/latambet/pronosticos/"
# EXCEL_FILE = "predictions.xlsx"

# def send_email_alert(subject, body):
#     sender_email = "testingformerightnow@gmail.com"
#     receiver_email = "ahmadmubashir9009@gmail.com"
#     password = "jzvq wyhk xrkp qynt"

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, password)
#         server.send_message(message)
#         print("Alert email sent!")

# def parse_date(date_str):
#     return date_str.strip()

# def load_existing_data():
#     if os.path.exists(EXCEL_FILE):
#         return pd.read_excel(EXCEL_FILE)
#     else:
#         return pd.DataFrame(columns=["Event", "Country", "Date", "Status"])

# def save_data_to_excel(data):
#     df = pd.DataFrame(data, columns=["Event", "Country", "Date", "Status"])
#     df.to_excel(EXCEL_FILE, index=False)

# def scrape_data():
#     existing_data = load_existing_data()
#     new_data = []

#     options = webdriver.ChromeOptions()
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--fasle")  # for background execution
#     service = Service("C:/Users/Cominn/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
#     driver = webdriver.Chrome(options=options, service=service)

#     driver.get(BASE_URL)

#     try:
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="modalPais"]/div/div[2]/div/a[1]'))
#         ).click()
#         time.sleep(3)
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//*[@id='accept-age']"))
#         ).click()

#         time.sleep(5)
#         soup = BeautifulSoup(driver.page_source, "html.parser")
#         rows = soup.find_all("div", class_="td flex7 f-row td-event-with-calendar")
#         picks = soup.find_all("li", class_="tr part")

#         pendiente_found = False
#         new_pending_alerts = []

#         for i, row in enumerate(rows):
#             try:
#                 event_name = row.find("p", class_="event").text.strip().replace("Pronóstico", "").strip()
#                 country = row.find("p", class_="league").text.strip()
#                 date_str = row.find("span", class_="calendar").text.strip()
#                 event_date = parse_date(date_str)

#                 pick_div = picks[i]
#                 status = "Pendiente" if "Pendiente" in pick_div.text else "Other"

#                 # Check if already in Excel
#                 duplicate = (
#                     (existing_data["Event"] == event_name) &
#                     (existing_data["Country"] == country) &
#                     (existing_data["Date"] == event_date) &
#                     (existing_data["Status"] == status)
#                 )

#                 if not duplicate.any():
#                     new_data.append([event_name, country, event_date, status])
#                     if status == "Pendiente":
#                         pendiente_found = True
#                         new_pending_alerts.append(f"{event_name} - {country} - {event_date}")

#             except Exception as e:
#                 print("Error in row parsing:", e)

#         if pendiente_found:
#             alert_body = "New 'Pendiente' predictions found:\n\n" + "\n".join(new_pending_alerts) + f"\n\nURL: {BASE_URL}"
#             send_email_alert(
#                 subject="Pendiente Alert from Gainblers",
#                 body=alert_body
#             )

#         # Save the new data (append to old)
#         updated_data = pd.concat([existing_data, pd.DataFrame(new_data, columns=existing_data.columns)], ignore_index=True)
#         updated_data.drop_duplicates(inplace=True)
#         updated_data.to_excel(EXCEL_FILE, index=False)

#     finally:
#         driver.quit()

# scrape_data()



























# import os
# import time
# import smtplib
# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Constants
# BASE_URL = "https://gainblers.com/la/tipsters/latambet/pronosticos/"
# EXCEL_FILE = "predictions.xlsx"
# HEADERS = {
#     "User-Agent": "Mozilla/5.0"
# }

# SENDER_EMAIL = "testingformerightnow@gmail.com"
# RECEIVER_EMAIL = "ahmadmubashir9009@gmail.com"
# EMAIL_PASSWORD = "jzvq wyhk xrkp qynt"

# # Email Notification
# def send_email_alert(subject, body):
#     message = MIMEMultipart()
#     message["From"] = SENDER_EMAIL
#     message["To"] = RECEIVER_EMAIL
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(SENDER_EMAIL, EMAIL_PASSWORD)
#         server.send_message(message)
#         print("Alert email sent!")

# # Load/Save Functions
# def load_existing_data():
#     if os.path.exists(EXCEL_FILE):
#         return pd.read_excel(EXCEL_FILE)
#     return pd.DataFrame(columns=["Event", "Country", "Date", "Status"])

# def parse_date(date_str):
#     return date_str.strip()

# # Main Scraper
# def scrape_data():
#     existing_data = load_existing_data()
#     new_data = []
#     new_pending_alerts = []

#     try:
#         response = requests.get(BASE_URL, headers=HEADERS)
#         if response.status_code != 200:
#             print("Failed to fetch page:", response.status_code)
#             return

#         soup = BeautifulSoup(response.text, "html.parser")
#         rows = soup.find_all("div", class_="td flex7 f-row td-event-with-calendar")
#         picks = soup.find_all("li", class_="tr part")

#         for i, row in enumerate(rows):
#             try:
#                 event_name = row.find("p", class_="event").text.replace("Pronóstico", "").strip()
#                 country = row.find("p", class_="league").text.strip()
#                 date_str = row.find("span", class_="calendar").text.strip()
#                 event_date = parse_date(date_str)

#                 pick_div = picks[i]
#                 status = "Pendiente" if "Pendiente" in pick_div.text else "Other"

#                 is_duplicate = (
#                     (existing_data["Event"] == event_name) &
#                     (existing_data["Country"] == country) &
#                     (existing_data["Date"] == event_date) &
#                     (existing_data["Status"] == status)
#                 ).any()

#                 if not is_duplicate:
#                     new_data.append([event_name, country, event_date, status])
#                     if status == "Pendiente":
#                         new_pending_alerts.append(f"{event_name} - {country} - {event_date}")

#             except Exception as e:
#                 print(f"Error parsing row {i}:", e)

#         # Send email if needed
#         if new_pending_alerts:
#             alert_body = "New 'Pendiente' predictions found:\n\n" + "\n".join(new_pending_alerts) + f"\n\nURL: {BASE_URL}"
#             send_email_alert("Pendiente Alert from Gainblers", alert_body)

#         # Save updated data
#         updated_df = pd.concat([existing_data, pd.DataFrame(new_data, columns=existing_data.columns)], ignore_index=True)
#         updated_df.drop_duplicates(inplace=True)
#         updated_df.to_excel(EXCEL_FILE, index=False)

#     except Exception as e:
#         print("Error during scraping:", e)

# # Run it
# if __name__ == "__main__":
#     scrape_data()








# import os
# import pandas as pd
# import requests
# import streamlit as st
# from bs4 import BeautifulSoup
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Constants
# BASE_URL = "https://gainblers.com/la/tipsters/latambet/pronosticos/"
# EXCEL_FILE = "predictions.xlsx"
# HEADERS = {
#     "User-Agent": "Mozilla/5.0"
# }

# SENDER_EMAIL = "testingformerightnow@gmail.com"
# RECEIVER_EMAIL = "nikolab96@yahoo.com"
# EMAIL_PASSWORD = "jzvq wyhk xrkp qynt"

# # Email Notification
# def send_email_alert(subject, body):
#     message = MIMEMultipart()
#     message["From"] = SENDER_EMAIL
#     message["To"] = RECEIVER_EMAIL
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(SENDER_EMAIL, EMAIL_PASSWORD)
#         server.send_message(message)

# # Load/Save Functions
# def load_existing_data():
#     if os.path.exists(EXCEL_FILE):
#         return pd.read_excel(EXCEL_FILE)
#     return pd.DataFrame(columns=["Event", "Country", "Date", "Status"])

# def parse_date(date_str):
#     return date_str.strip()

# # Main Scraper
# def scrape_data():
#     status_log = []
#     existing_data = load_existing_data()
#     new_data = []
#     new_pending_alerts = []

#     try:
#         response = requests.get(BASE_URL, headers=HEADERS)
#         if response.status_code != 200:
#             status_log.append(f"❌ Failed to fetch page: {response.status_code}")
#             return status_log

#         soup = BeautifulSoup(response.text, "html.parser")
#         rows = soup.find_all("div", class_="td flex7 f-row td-event-with-calendar")
#         picks = soup.find_all("li", class_="tr part")

#         for i, row in enumerate(rows):
#             try:
#                 event_name = row.find("p", class_="event").text.replace("Pronóstico", "").strip()
#                 country = row.find("p", class_="league").text.strip()
#                 date_str = row.find("span", class_="calendar").text.strip()
#                 event_date = parse_date(date_str)

#                 pick_div = picks[i]
#                 status = "Pendiente" if "Pendiente" in pick_div.text else "Other"
                
#                 is_duplicate = (
#                     (existing_data["Event"] == event_name) &
#                     (existing_data["Country"] == country) &
#                     (existing_data["Date"] == event_date) &
#                     (existing_data["Status"] == status)
#                 ).any()

#                 if not is_duplicate:
#                     new_data.append([event_name, country, event_date, status])
#                     if status == "Pendiente":
#                         new_pending_alerts.append(f"{event_name} - {country} - {event_date}")

#             except Exception as e:
#                 status_log.append(f"⚠️ Error parsing row {i}: {e}")

#         if new_pending_alerts:
#             alert_body = "New 'Pendiente' predictions found:\n\n" + "\n".join(new_pending_alerts) + f"\n\nURL: {BASE_URL}"
#             send_email_alert("Pendiente Alert from Gainblers", alert_body)
#             status_log.append(f"✅ Sent email for {len(new_pending_alerts)} new 'Pendiente' predictions")

#         # Save data
#         if new_data:
#             updated_df = pd.concat([existing_data, pd.DataFrame(new_data, columns=existing_data.columns)], ignore_index=True)
#             updated_df.drop_duplicates(inplace=True)
#             updated_df.to_excel(EXCEL_FILE, index=False)
#             status_log.append(f"💾 Saved {len(new_data)} new records to Excel")

#         if not new_data:
#             status_log.append("ℹ️ No new data found.")

#     except Exception as e:
#         status_log.append(f"❌ Error during scraping: {e}")

#     return status_log


# # Streamlit App
# st.set_page_config(page_title="Gainblers Scraper", layout="centered")
# st.title("🔎 Gainblers Scraper")
# st.markdown("This scraper runs automatically when the page is loaded (useful for UptimeRobot pinging).")

# # Run on load
# with st.spinner("Scraping in progress..."):
#     logs = scrape_data()

# st.success("✅ Done")
# st.markdown("### Logs:")
# for log in logs:
#     st.write(log)






import os
import pandas as pd
import requests
import streamlit as st
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
BASE_URL = "https://gainblers.com/la/tipsters/latambet/pronosticos/"
EXCEL_FILE = "predictions.xlsx"
NOTIFIED_FILE = "notified_alerts.txt"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

SENDER_EMAIL = "testingformerightnow@gmail.com"
RECEIVER_EMAIL = "nikolab96@yahoo.com"
EMAIL_PASSWORD = "jzvq wyhk xrkp qynt"

# Email Notification
def send_email_alert(subject, body):
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.send_message(message)

# Load/Save Functions
def load_existing_data():
    if os.path.exists(EXCEL_FILE):
        return pd.read_excel(EXCEL_FILE)
    return pd.DataFrame(columns=["Event", "Country", "Date", "Status"])

def load_notified():
    if os.path.exists(NOTIFIED_FILE):
        with open(NOTIFIED_FILE, "r") as f:
            return set(line.strip() for line in f.readlines())
    return set()

def save_notified(new_alerts):
    with open(NOTIFIED_FILE, "a") as f:
        for alert in new_alerts:
            f.write(alert + "\n")

def parse_date(date_str):
    return date_str.strip()

# Main Scraper
def scrape_data():
    status_log = []
    existing_data = load_existing_data()
    notified_set = load_notified()

    new_data = []
    new_pending_alerts = []

    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        if response.status_code != 200:
            status_log.append(f"❌ Failed to fetch page: {response.status_code}")
            return status_log

        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all("div", class_="td flex7 f-row td-event-with-calendar")
        picks = soup.find_all("li", class_="tr part")

        for i, row in enumerate(rows):
            try:
                event_name = row.find("p", class_="event").text.replace("Pronóstico", "").strip()
                country = row.find("p", class_="league").text.strip()
                date_str = row.find("span", class_="calendar").text.strip()
                event_date = parse_date(date_str)

                pick_div = picks[i]
                status = "Pendiente" if "Pendiente" in pick_div.text else "Other"

                is_duplicate = (
                    (existing_data["Event"] == event_name) &
                    (existing_data["Country"] == country) &
                    (existing_data["Date"] == event_date) &
                    (existing_data["Status"] == status)
                ).any()

                alert_key = f"{event_name} - {country} - {event_date}"

                if not is_duplicate:
                    new_data.append([event_name, country, event_date, status])
                    if status == "Pendiente" and alert_key not in notified_set:
                        new_pending_alerts.append(alert_key)

            except Exception as e:
                status_log.append(f"⚠️ Error parsing row {i}: {e}")

        if new_pending_alerts:
            alert_body = "New 'Pendiente' predictions found:\n\n" + "\n".join(new_pending_alerts) + f"\n\nURL: {BASE_URL}"
            send_email_alert("Pendiente Alert from Gainblers", alert_body)
            save_notified(new_pending_alerts)
            status_log.append(f"✅ Sent email for {len(new_pending_alerts)} new 'Pendiente' predictions")

        if new_data:
            updated_df = pd.concat([existing_data, pd.DataFrame(new_data, columns=existing_data.columns)], ignore_index=True)
            updated_df.drop_duplicates(inplace=True)
            updated_df.to_excel(EXCEL_FILE, index=False)
            status_log.append(f"💾 Saved {len(new_data)} new records to Excel")

        if not new_data:
            status_log.append("ℹ️ No new data found.")

    except Exception as e:
        status_log.append(f"❌ Error during scraping: {e}")

    return status_log

# Streamlit App
st.set_page_config(page_title="Gainblers Scraper", layout="centered")
st.title("🔎 Gainblers Scraper")
st.markdown("This scraper runs automatically when the page is loaded (useful for UptimeRobot pinging).")

# Run on load
with st.spinner("Scraping in progress..."):
    logs = scrape_data()

st.success("✅ Done")
st.markdown("### Logs:")
for log in logs:
    st.write(log)





# import streamlit as st
# import time
# import smtplib
# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import os

# BASE_URL = "https://gainblers.com/la/tipsters/latambet/pronosticos/"
# EXCEL_FILE = "predictions.xlsx"

# def send_email_alert(subject, body):
#     sender_email = "testingformerightnow@gmail.com"
#     receiver_email = "ahmadmubashir9009@gmail.com"
#     password = "jzvq wyhk xrkp qynt"

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, password)
#         server.send_message(message)

# def parse_date(date_str):
#     return date_str.strip()

# def load_existing_data():
#     if os.path.exists(EXCEL_FILE):
#         return pd.read_excel(EXCEL_FILE)
#     else:
#         return pd.DataFrame(columns=["Event", "Country", "Date", "Status"])

# def scrape_data():
#     existing_data = load_existing_data()
#     new_data = []

#     options = webdriver.ChromeOptions()
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--headless")  # for background execution

#     # Replace with your own path or remove if not needed
#     service = Service("C:/Users/Cominn/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
#     driver = webdriver.Chrome(options=options, service=service)

#     driver.get(BASE_URL)

#     try:
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="modalPais"]/div/div[2]/div/a[1]'))
#         ).click()
#         time.sleep(3)
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//*[@id='accept-age']"))
#         ).click()

#         time.sleep(5)
#         soup = BeautifulSoup(driver.page_source, "html.parser")
#         rows = soup.find_all("div", class_="td flex7 f-row td-event-with-calendar")
#         picks = soup.find_all("li", class_="tr part")

#         pendiente_found = False
#         new_pending_alerts = []

#         for i, row in enumerate(rows):
#             try:
#                 event_name = row.find("p", class_="event").text.strip().replace("Pronóstico", "").strip()
#                 country = row.find("p", class_="league").text.strip()
#                 date_str = row.find("span", class_="calendar").text.strip()
#                 event_date = parse_date(date_str)

#                 pick_div = picks[i]
#                 status = "Pendiente" if "Pendiente" in pick_div.text else "Other"

#                 duplicate = (
#                     (existing_data["Event"] == event_name) &
#                     (existing_data["Country"] == country) &
#                     (existing_data["Date"] == event_date) &
#                     (existing_data["Status"] == status)
#                 )

#                 if not duplicate.any():
#                     new_data.append([event_name, country, event_date, status])
#                     if status == "Pendiente":
#                         pendiente_found = True
#                         new_pending_alerts.append(f"{event_name} - {country} - {event_date}")

#             except Exception as e:
#                 print("Error in row parsing:", e)

#         if pendiente_found:
#             alert_body = "New 'Pendiente' predictions found:\n\n" + "\n".join(new_pending_alerts) + f"\n\nURL: {BASE_URL}"
#             send_email_alert(
#                 subject="Pendiente Alert from Gainblers",
#                 body=alert_body
#             )

#         updated_data = pd.concat([existing_data, pd.DataFrame(new_data, columns=existing_data.columns)], ignore_index=True)
#         updated_data.drop_duplicates(inplace=True)
#         updated_data.to_excel(EXCEL_FILE, index=False)

#         return updated_data

#     finally:
#         driver.quit()

# # Streamlit UI
# st.title("Gainblers Prediction Monitor")
# st.write("Scraping data...")

# with st.spinner("Running scraper..."):
#     df = scrape_data()
#     st.success("Done!")
#     st.dataframe(df)

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client

# Load user input from JSON
INPUT_JSON = '''
{
    "departure": "New York (JFK)",
    "destination": "London (LHR)",
    "departure_date": "2025-02-15",
    "return_date": "2025-02-25",
    "price_threshold": 500,
    "whatsapp_group": "whatsapp:+14155238886"
}
'''
input_data = json.loads(INPUT_JSON)

# Twilio credentials
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio Sandbox number

# Function to send WhatsApp alerts
def send_whatsapp_alert(message, to):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=to
        )
        print(f"WhatsApp alert sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send WhatsApp alert: {e}")

# Function to scrape Skyscanner
def check_flight_price():
    # Set up WebDriver
    driver = webdriver.Chrome()  # Use the correct WebDriver (e.g., for Chrome)
    driver.get("https://www.skyscanner.com")

    try:
        # Input departure location
        from_input = driver.find_element(By.ID, "fsc-origin-search")
        from_input.clear()
        from_input.send_keys(input_data["departure"])
        time.sleep(1)
        from_input.send_keys(Keys.ENTER)

        # Input destination location
        to_input = driver.find_element(By.ID, "fsc-destination-search")
        to_input.clear()
        to_input.send_keys(input_data["destination"])
        time.sleep(1)
        to_input.send_keys(Keys.ENTER)

        # Input departure date
        depart_input = driver.find_element(By.ID, "depart-fsc-datepicker-button")
        depart_input.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-id='" + input_data["departure_date"] + "']"))
        ).click()

        # Input return date
        return_input = driver.find_element(By.ID, "return-fsc-datepicker-button")
        return_input.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-id='" + input_data["return_date"] + "']"))
        ).click()

        # Click search
        search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()

        # Wait for results to load
        time.sleep(15)

        # Get price details
        price_elements = driver.find_elements(By.CSS_SELECTOR, ".BpkText_bpk-text__NzCwA")
        prices = []
        for price_element in price_elements:
            try:
                price_text = price_element.text.replace("$", "").replace(",", "")
                prices.append(int(price_text))
            except ValueError:
                continue

        # Find the lowest price
        if prices:
            min_price = min(prices)
            print(f"Lowest price found: ${min_price}")
            if min_price < input_data["price_threshold"]:
                send_whatsapp_alert(
                    message=f"The flight price has dropped to ${min_price}. Book now!",
                    to=input_data["whatsapp_group"]
                )
        else:
            print("No prices found.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

# Schedule the script to run periodically
if __name__ == "__main__":
    check_flight_price()

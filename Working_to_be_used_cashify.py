import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime


# Read the CSV file and get values
csv_file_path = input("Enter File Path: ")  # Replace with the path to your CSV file
links_df = pd.read_csv(csv_file_path)  # Assuming columns A to G have necessary data

# Extract values from CSV
links = links_df.iloc[:, 0].tolist()  # Links from column A
step2_values = links_df.iloc[:, 1].tolist()  # Step 2 values from column B
dropdown_values = links_df.iloc[:, 2:5].values.tolist()  # Columns C (dropdown 1), D (dropdown 2), E (dropdown 3)
step5_values = links_df.iloc[:, 5:7].values.tolist()  # Columns F (Step 5 Option 1) and G (Step 5 Option 2)
step6_values = links_df.iloc[:, 7:10].values.tolist()  # Columns H (Step 6 Option 1), I (Step 6 Option 2) and J (Step 6 Option 3)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# Initialize WebDriver

driver.get('https://www.cashify.in/')
input("Please login and press enter.")
wait = WebDriverWait(driver, 10)


# Function to process each link
def process_link(link, step2_value, dropdown_selection, step5_selection, step6_selection):
    driver.get(link)

    wait = WebDriverWait(driver, 10)
    time.sleep(5)

    try:
        # Step 1: Click the "Get Exact Value" button
        continue_button_xpath = "//button[contains(@class, 'flex flex-row justify-center items-center rounded-md bg-cta') and .//span[text()='Get Exact Value']]"
        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, continue_button_xpath)))
        ActionChains(driver).move_to_element(continue_button).click().perform()
        print("Continue button clicked.")
        time.sleep(2)

        # Step 2: Click the radio button based on the value from column B
        radio_button_xpath = f"//div[contains(@class, 'body2') and text()='{step2_value}']"
        yes_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, radio_button_xpath)))
        ActionChains(driver).move_to_element(yes_radio_button).click().perform()
        print(f"Radio button with value '{step2_value}' clicked.")
        time.sleep(2)

        # Step 3: Select dropdown values
        for index, value in enumerate(dropdown_selection):
            dropdown_xpath = f"(//div[@class='visible flex flex-col'])[{index + 1}]"
            dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
            dropdown.click()
            print(f"Dropdown {index + 1} clicked.")
            time.sleep(5)
            option_xpath = f"//li[contains(@class, 'flex flex-col')]//span[text()='{value}']"
            option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
            option.click()
            print(f"Option '{value}' selected.")
            time.sleep(2)
            if index == 1:
                driver.execute_script("window.scrollBy(0, 200);")
                print("Scrolled down.")

        # Step 4: Click the Continue button
        continue_button_xpath = "//button[contains(@class, 'flex flex-row justify-center items-center rounded-md bg-cta') and .//span[text()='Continue']]"
        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, continue_button_xpath)))
        ActionChains(driver).move_to_element(continue_button).click().perform()
        print("Continue button clicked.")

        # Step 5: Select dynamic radio buttons based on columns F and G
        selections = [
            {"label": step5_selection[0], "xpath": f"//div[contains(@class, 'inherit body2 flex-1') and text()='{step5_selection[0]}']"},
            {"label": step5_selection[1], "xpath": f"//div[contains(@class, 'inherit body2 flex-1') and text()='{step5_selection[1]}']"}
        ]

        for selection in selections:
            radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, selection["xpath"])))
            ActionChains(driver).move_to_element(radio_button).click().perform()
            print(f"{selection['label']} radio button clicked.")
            time.sleep(2)

        # Step 6: Click the Continue button
        continue_button_xpath = "//button[contains(@class, 'flex flex-row justify-center items-center rounded-md bg-cta') and .//span[text()='Continue']]"
        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, continue_button_xpath)))
        ActionChains(driver).move_to_element(continue_button).click().perform()
        print("Continue button clicked.")

        # Step 7: Click the Continue button
        continue_button_xpath = "//button[contains(@class, 'flex flex-row justify-center items-center rounded-md bg-cta') and .//span[text()='Continue']]"
        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, continue_button_xpath)))
        ActionChains(driver).move_to_element(continue_button).click().perform()
        print("Continue button clicked.")

        # Step 8: Select additional radio buttons

        try:
            # Try to select 'flawless'
            flawless_xpath = f"//div[contains(@class, 'inherit body2') and text()='flawless']"
            flawless_button = wait.until(EC.element_to_be_clickable((By.XPATH, flawless_xpath)))
            ActionChains(driver).move_to_element(flawless_button).click().perform()
            print("'flawless' radio button clicked.")
            time.sleep(2)
        except Exception as e:
            print("'flawless' not available. Trying 'good'.")
            try:
                # Fallback to 'good' if 'flawless' is not available
                good_xpath = f"//div[contains(@class, 'inherit body2') and text()='Good']"
                good_button = wait.until(EC.element_to_be_clickable((By.XPATH, good_xpath)))
                ActionChains(driver).move_to_element(good_button).click().perform()
                print("'good' radio button clicked.")
                time.sleep(2)
            except Exception as e:
                print("'good' also not available.")
        selections_2 = [
            
            {"label": step6_selection[1], "xpath": f"//div[contains(@class, 'inherit body2') and text()='{step6_selection[1]}']"},
            {"label": step6_selection[2], 
            "xpath": f"//div[contains(@class, 'inherit body2') and (text()='{step6_selection[2]}')]"}
        ]
        for selection_2 in selections_2:
            radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, selection_2["xpath"])))
            ActionChains(driver).move_to_element(radio_button).click().perform()
            print(f"{selection_2['label']} radio button clicked.")
            time.sleep(2)

        # Step 9: Extract the price
        price_div = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'flex flex-row justify-between items-center')]")))
        price_div_text = price_div.text
        print(f"Price for {link}: {price_div_text}")

        return price_div_text

    except Exception as e:
        print(f"Error processing link {link}: {e}")
        return None

# Get current date for header
current_date = datetime.now().strftime("%B %d, %Y")

# Initialize a list to store the prices
prices = []

# Loop through each link in the CSV and process it
for index, (link, step2_value, dropdown_selection, step5_selection, step6_selection) in enumerate(zip(links, step2_values, dropdown_values, step5_values, step6_values)):
    print(f"Processing link {index + 1}/{len(links)}: {link} with Step 2 value: {step2_value}, dropdown values: {dropdown_selection}, step 5 values: {step5_selection}, and step 6 values: {step6_selection}")
    
    # Process the link and get the price
    price = process_link(link, step2_value, dropdown_selection, step5_selection, step6_selection)
    
    # Append the price to the DataFrame
    links_df.at[index, current_date] = price
    print(f"Price appended for link {index + 1}: {price}")
    
    # Save the updated DataFrame back to the CSV
    links_df.to_csv(csv_file_path, index=False)
    print(f"CSV file updated after processing link {index + 1}.")
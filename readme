# Cashify Price Extraction Automation

Automate product price extraction from Cashify using Selenium WebDriver. This script reads input data from a CSV, navigates Cashify's valuation process, and records extracted prices back into the CSV.

---

## **Features**

- Automated navigation through Cashify's valuation process  
- Reads input parameters (URLs, dropdown selections, radio button values) from a CSV  
- Extracts product prices and appends them to the CSV with a timestamp  

---

## **Prerequisites**

- Python 3.7+
- Google Chrome browser
- ChromeDriver (matching the installed Chrome version)

---

## **Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/cashify-price-extraction.git
cd cashify-price-extraction
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `pandas`
- `selenium`

---

## **Usage**

### **Using Python Script**

1. **Prepare Input CSV:** Ensure the CSV has the following columns:

   | Links | Step 2 | Dropdown 1 | Dropdown 2 | Dropdown 3 | Radio 1 | Radio 2 | Radio 3 | Radio 4 | Radio 5 |
   |-------|--------|------------|------------|------------|---------|---------|---------|---------|---------|
   | https://www.cashify.in/product-1 | Option1 | Value1 | Value2 | Value3 | Yes | No | Yes | No | Yes |
   | https://www.cashify.in/product-2 | Option2 | Value4 | Value5 | Value6 | No  | Yes | No  | Yes | No  |

2. **Run the Script:**

   ```bash
   python script_name.py
   ```

3. **Follow Instructions:**
   - Enter the path to the CSV file when prompted.
   - Manually log in to Cashify and press Enter to continue.

4. **Output:**
   - Extracted prices are saved in the CSV under a new column with the current date.

### **Using Executable (Windows)**

1. Navigate to the `dist` folder.
2. Double-click `cashify.exe` to run.
3. Follow on-screen instructions for CSV input and login.

---

## **Project Structure**

```
├── dist/
│   └── cashify.exe          # Windows executable version
├── script_name.py           # Main automation script
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── input.csv                # Input file with URLs and options
```

---

## **Troubleshooting**

- Ensure ChromeDriver is installed and added to the system PATH.
- Match ChromeDriver version with your Chrome browser version.
- Increase `time.sleep()` durations if page load issues occur.

---

## **License**

This project is licensed under the **MIT License**.

---

## **Acknowledgements**

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)


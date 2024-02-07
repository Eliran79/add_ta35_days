 **# Add TA35 Days**

**This script adds TA35 trading days to a CSV file in TradeStation format.**

**## Installation**

1. **Create a virtual environment:**

   ```bash
   python3 -m venv env
   ```

2. **Activate the virtual environment:**

   - **Windows:**

     ```bash
     env\Scripts\activate
     ```

   - **Linux/macOS:**

     ```bash
     source env/bin/activate
     ```

3. **Install required packages:**

   ```bash
   pip install numpy pandas exchange-calendars
   ```

**## Usage**

1. **Run the script:**

   ```bash
   python add_ta53_days.py <input_file.csv> <output_file.csv>
   ```

   - Replace `<input_file.csv>` with the path to your input CSV file.
   - Replace `<output_file.csv>` with the desired path for the output CSV file.

**## Example**

```bash
python add_ta53_days.py input_data.csv output_data.csv
```

**## Additional Information**

- **Author:** Eliran Sabag
- **Purpose:** Add TA35 trading days to a CSV file in TradeStation format.
- **Libraries used:** NumPy, pandas, exchange-calendars

**## Contributing**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

**## License**
WTFPL
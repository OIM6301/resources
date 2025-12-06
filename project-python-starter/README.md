# Python Final Project Starter Pack

This folder contains starter files for the OIM6301 Python Final Project.

## What's Included

### Data Files (Option A)
- `data/customers.csv` - 30 sample customers
- `data/products.csv` - 20 sample products
- `data/orders.csv` - 100 sample orders

### Template Scripts
- `setup_database.py` - Database creation and CSV import
- `analyze_data.py` - 5 analytical queries (to be completed)
- `generate_report.py` - Report generation and CSV export
- `api_demo.py` - Simple API demonstration (to be completed)

### Configuration
- `.env.example` - Template for API keys (copy to `.env` if using APIs that require keys)
- `.gitignore` - Prevents committing sensitive files

## Getting Started

### 1. Set Up API Keys (for Part 2, optional)

If you plan to use APIs that require keys (like OpenWeather or OpenAI):

```bash
cp .env.example .env
```

Then edit `.env` and add your API keys.

**Note**: Part 2 can be completed with APIs that don't require keys (like REST Countries or Public Holidays API). See project-python.md for recommended APIs.

### 2. Complete the Scripts

Follow the TODO comments in each file:
- Fill in missing SQL queries
- Implement functions
- Test your code incrementally

### 3. Run the Scripts

```bash
# Step 1: Set up database
python setup_database.py

# Step 2: Run analysis
python analyze_data.py

# Step 3: Generate reports
python generate_report.py

# Step 4: API demonstration
python api_demo.py
```

## Project Structure

```
project-python-starter/
├── data/                    # CSV files and database
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   └── ecommerce.db        # (generated)
├── reports/                 # (created when running scripts)
│   ├── top_products.csv
│   ├── summary_report.txt
│   └── ai_insights.txt
├── setup_database.py        # TODO: Complete this
├── analyze_data.py          # TODO: Complete this
├── generate_report.py       # TODO: Complete this
├── api_demo.py              # TODO: Complete this
├── api_integration.py       # TODO: Optional
├── .env                     # Your API keys (DO NOT COMMIT - optional)
├── .env.example             # Template
├── .gitignore
└── README.md
```

## Tips

- **Start with setup_database.py** - Get your data loaded first
- **Test queries individually** - Don't wait until the end
- **Use the class demo** - Reference `s13_sqlite_demo.py`
- **Read error messages carefully** - They usually tell you what's wrong
- **Ask for help early** - Don't struggle for hours alone

## Common Issues

### Database Locked Error
- Make sure you close DBeaver connections to the database
- Use `with` statements for automatic cleanup

### CSV Import Fails
- Check that CSV files exist in `data/` folder
- Verify column count matches table schema
- Check for encoding issues (should be UTF-8)

### API Errors
- Verify `.env` file exists and has correct keys
- Check API key is valid
- Ensure you have internet connection

## Need Help?

- Review project requirements: `project-python.md`
- Check class demo: `code/s13_sqlite_demo.py`
- Post on GitHub Issues
- Email instructor with specific questions

Good luck! 🚀

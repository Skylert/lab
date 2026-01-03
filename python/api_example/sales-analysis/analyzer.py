import os

# Check if we're in the right place
print("Starting directory:", os.getcwd())

# Change to script's directory
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
except NameError:
    # Running in Interactive Window
    if not os.path.exists('data'):
        os.chdir('sales-analysis')

print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")
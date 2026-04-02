import pandas as pd

# Define file paths (makes code easier to maintain)
RAW_PATH = "data/raw/sales_raw.csv"
PROCESSED_PATH = "data/processed/sales_clean.csv"

def main():
    """
    Main function that runs the ETL pipeline:
    1. Read raw data
    2. Clean data
    3. Transform data
    4. Save processed data
    5. Reload and analyze
    6. Run validation checks
    """

    try:
        # =========================
        # Step 1: Read raw data
        # =========================
        print("Step 1: Reading raw data...")

        # Read CSV file using ';' as separator
        df_raw = pd.read_csv(RAW_PATH, sep=';')

        # =========================
        # Step 2: Clean data
        # =========================
        print("Step 2: Cleaning data...")

        # Remove rows with missing customer_id
        df_clean = df_raw.dropna(subset=['customer_id'])

        # Keep only rows with positive quantity
        df_clean = df_clean[df_clean["quantity"] > 0]

        # Create a safe copy to avoid pandas warnings
        df_clean = df_clean.copy()

        # Print row counts for visibility
        print("Raw rows:", len(df_raw))
        print("Clean rows:", len(df_clean))

        # =========================
        # Step 3: Transform data
        # =========================
        print("Step 3: Adding total_amount...")

        # Calculate total revenue per row
        df_clean["total_amount"] = df_clean["quantity"] * df_clean["unit_price"]

        # Print total revenue for quick check
        print("Total revenue:", df_clean["total_amount"].sum())

        # =========================
        # Step 4: Save clean data
        # =========================
        print("Step 4: Saving clean data...")

        # Save processed dataset (no index column)
        df_clean.to_csv(PROCESSED_PATH, index=False)

        # =========================
        # Step 5: Reload data
        # =========================
        print("Step 5: Reloading clean data...")

        # Reload processed data (simulates downstream usage)
        df = pd.read_csv(PROCESSED_PATH)

        # Show first 3 rows for quick inspection
        print(df.head(3))

        # =========================
        # Step 6: Aggregation
        # =========================
        print("Step 6: Aggregating revenue per product...")

        # Group by product and calculate total revenue
        df_agg = df.groupby("product", as_index=False)["total_amount"].sum()

        print(df_agg)

        # =========================
        # Step 7: Data validation
        # =========================
        print("Step 7: Running validation checks...")

        # Count invalid values
        negative_quantity = (df["quantity"] < 0).sum()
        null_customer = df["customer_id"].isna().sum()
        invalid_total = (df["total_amount"] <= 0).sum()

        print("Negative quantity:", negative_quantity)
        print("Null customer_id:", null_customer)
        print("Invalid total_amount:", invalid_total)

        # =========================
        # Final message
        # =========================
        print("Pipeline completed successfully")

    except Exception as e:
        # Catch any error and print it
        print("Pipeline failed:", e)


# Entry point of the script
if __name__ == "__main__":
    main()
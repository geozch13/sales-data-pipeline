# 📊 Sales Data Pipeline

## 📌 Overview

This project demonstrates a simple end-to-end **ETL (Extract, Transform, Load) pipeline** built with Python and pandas.

The pipeline processes raw sales data, cleans invalid records, applies transformations, and performs validation checks to ensure data quality.

---

## ⚙️ Pipeline Steps

1. **Ingestion**

   * Reads raw CSV data from `data/raw/`

2. **Data Cleaning**

   * Removes rows with missing `customer_id`
   * Filters out invalid `quantity` values (≤ 0)

3. **Transformation**

   * Creates a new column:

     ```
     total_amount = quantity * unit_price
     ```

4. **Storage**

   * Saves cleaned data to `data/processed/`

5. **Validation**

   * Checks for:

     * Negative quantities
     * Missing customer IDs
     * Invalid total amounts

---

## 📁 Project Structure

```
sales-data-pipeline/
│
├── data/
│   ├── raw/         # Raw input data (includes sample dataset)
│   └── processed/   # Cleaned output data (ignored in Git)
│
├── src/
│   └── sales_pipeline.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the pipeline:

```
python src/sales_pipeline.py
```

---

## 📊 Example Output

```
Step 1: Reading raw data...
Step 2: Cleaning data...
Raw rows: 4
Clean rows: 2
Step 3: Adding total_amount...
Total revenue: 80
Step 4: Saving clean data...
Step 5: Reloading clean data...
Step 6: Aggregating revenue per product...
Step 7: Running validation checks...
Pipeline completed successfully
```

---

## 📄 Sample Data

A sample dataset is included:

```
data/raw/sales_raw_sample.csv
```

You can modify or replace this file to test different scenarios.

---

## 🧠 Key Concepts Demonstrated

* ETL pipeline design
* Data cleaning and validation
* Data transformation with pandas
* File-based data storage
* Basic error handling

---

## 🚀 Future Improvements

* Add configuration file for dynamic paths
* Replace print statements with logging
* Add unit tests (pytest)
* Containerize with Docker
* Scale with Spark or cloud tools (e.g., Azure Data Factory)

---

## 👨‍💻 Author

Built as a hands-on project to practice data engineering fundamentals.

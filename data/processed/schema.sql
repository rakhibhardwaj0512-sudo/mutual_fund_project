CREATE TABLE nav_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    schema_name TEXT,
    nav_date DATE,
    nav_value REAL
);
CREATE TABLE dim_fund(
    fund_id INTEGER PRIMARY KEY,
    fund name TEXT,
);
CREATE TABLE dim_date(
    date_id INTEGER PRIMARY KEY,
    date DATE
);
CREATE TABLE fact_nav(
    id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    nav_value REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
    
);
# Python Sales & Customer Analysis

## Project Overview

This project uses Python to analyse sales, profitability, regional performance, product categories, and customer contribution using a structured business sales dataset.

The analysis combines data preparation, descriptive analysis, business KPIs, grouped summaries, pivot tables, visualisations, and Excel exports.

## Business Objective

The objective is to use Python to answer practical business questions such as:

* What is the overall sales and profit performance?
* Which regions generate the most sales and profit?
* Which product categories perform best?
* Which customers contribute the most profit?
* How do sales and profit vary across regions and categories?
* Are there duplicate orders in the dataset?
* How can analytical summaries be exported for further reporting?

## Tools Used

**Python | Pandas | Matplotlib | Excel Output Through Pandas**

## Dataset

The project uses a manually created sales dataset containing 20 orders.

The dataset includes:

* Order ID
* Customer
* Region
* Category
* Sales
* Profit

## Analysis Performed

### 1. Data Understanding

The dataset was loaded into a Pandas DataFrame and inspected to understand its structure and key dimensions.

Basic analysis included:

* Number of unique customers
* Number of regions
* Number of categories
* Category frequency
* Duplicate Order ID checking

### 2. Business KPIs

Calculated:

* Total sales
* Total profit
* Overall profit margin

These metrics provide a high-level view of business performance.

### 3. Regional Analysis

Regional performance was analysed using grouped summaries containing:

* Total sales
* Total profit
* Average sales

The analysis also identified the region with the highest total sales and the region with the highest total profit.

### 4. Category Analysis

Product categories were compared using sales and profitability measures.

A region-by-category pivot table was also created to examine how category sales varied across regions.

### 5. Customer Analysis

Customer-level summaries were created to evaluate:

* Total sales
* Total profit

The analysis identified the customer contributing the highest total profit.

### 6. Visual Analysis

Matplotlib was used to create:

* Sales by region bar chart
* Sales sequence line chart
* Sales versus profit scatter plot

The sales sequence chart shows the order of sales values in the dataset and is not treated as a time-series analysis because the dataset does not contain dates.

### 7. Excel Export

Key analytical summaries were exported to Excel for potential use in further reporting:

* Regional summary
* Category summary
* Customer summary

## Key Python Techniques Demonstrated

* Pandas DataFrames
* Data inspection
* Duplicate detection
* `groupby()`
* `nunique()`
* `idxmax()`
* Aggregation with `agg()`
* Pivot tables
* Sorting and filtering
* Unique-value analysis
* KPI calculations
* Matplotlib visualisation
* Excel export
* Reading exported Excel Files

## Business Analysis

The project demonstrates how Python can transform transactional sales data into structured business information.

Regional and category analysis provides a view of where sales and profitability are concentrated, while customer analysis helps identify important contributors to overall profit.

The visualisations provide additional ways to identify differences and relationships within the dataset.

## Business Value

The analysis can support:

* Regional performance monitoring
* Category evaluation
* Customer contribution analysis
* Profitability review
* Identification of unusual or duplicate records
* Preparation of summary outputs for management reporting

The findings identify patterns in the dataset, while decisions about pricing, marketing, product strategy, or customer management would require additional business context.

## Skills Demonstrated

* Python data analysis
* Pandas
* Matplotlib
* Data cleaning and validation
* Data aggregation
* Pivot-table analysis
* Business KPI calculation
* Data visualisation
* Excel output generation
* Business-focused interpretation

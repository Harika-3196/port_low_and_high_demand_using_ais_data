# Port Data Analysis

  

## Overview

This project involves analyzing port data and Automatic Identification System (AIS) data to identify and track vessel movements, particularly cargo vessels, within specified regions. The aim is to provide valuable insights and data for port operations and logistics.

  

## Project Structure

├── scripts/

│ ├── query_port_coordinates.py
│ ├── demand_identification.py

├── tests/
│ ├── test_query_port_coordinates.py
│ ├── test_demand_identification.py

├── db/
│ ├── connection.py
│ ├── postgres_sql_script.py

├── plots folder
│ ├── distribution_of_vessels_hourly.png
│ ├──variance_plot_daily.png
│ ├──variance_plot_hourly.png

├── output_file_after_analysis
│ ├── daily_time_and_vessels_analysis.csv
│ ├── hourly_time_and_vessels_analysis.csv

├── .env
├── .gitignore
├── README.md
├── requirements.txt

  
  

## Prerequisites

- Python 3.8+

- PostgreSQL

- Required Python packages (listed in `requirements.txt`)

  

## Setup

##  1. Clone the Repository

git  clone  https://github.com/your-username/port-data-analysis.git

cd  port-data-analysis

## 2. Create Virtual Environment and Activate

python3  -m  venv  venv

source  venv/bin/activate  #in mac

## 3.Install Dependencies
pip  install  -r  requirements.txt

##  4. Set Up PostgreSQL Database

Ensure  PostgreSQL  is  installed  and  running. 

Create  a  database  and  a  user  with  appropriate  permissions  mentioned  in  postgres_commands.docx. follow the commands by copy pasting 

I have also written a python script 

  

## 5. Create .env file and add following values

Update  the  .env  file  with  your  PostgreSQL  connection  details:

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
  

## Scripts

connection.py  -  Establishes  a  connection  to  the  PostgreSQL  database  using  environment  variables.

  

## query_port_coordinates.py

Contains  functions  to  query  port  coordinates  from  the  database.

### Functions:

1) get_port_coordinates(port_name):

Retrieves  the  coordinates  of  a  specified  port  by  name.

  

## demand_identification.py

Contains  functions  to  identify  and  analyze  vessel  movements  within  a  specified  bounding  box.

  

### Functions:

get_cargo_vessels_within_bounding_box(port_name,  width,  height,  cargo_vessel_types): Retrieves cargo vessels within a defined bounding box around a specified port.

count_unique_vessels_by_time(port_name,  width,  height,  cargo_vessel_types,  time_interval): Counts unique vessels by specified time intervals.

  
  

## Tests

### test_query_port_coordinates.py

Contains  unit  tests  for  query_port_coordinates.py.

### test_demand_identification.py

Contains  unit  tests  for  demand_identification.py.

  

## Usage

see  inference.py in the folder or see the notebook test_inference.py

## Outputs
The output of results in CSV are saved in an output folder called outfile_file_after_analysis


## Plotly Graphs in plots_folder

## Hour Shift Variance:

The visualizations created for hour shifts reveal significant variance in vessel counts between day 1 and day 2. This indicates that the number of vessels fluctuates considerably over these two days.

## Day Shift Variance 

A new plot has been added to represent the day shift. Although the current dataset includes only two days of data, this plot is prepared for future data additions.
As more days of data become available, this plot will become more insightful and relevant, providing a broader view of the trends over multiple days.

## Distribution plot

Plot which allows us to see the distribution of vessels.

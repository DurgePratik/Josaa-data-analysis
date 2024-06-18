# JOSAA-data-analysis
This project aims to provide a comprehensive platform that allows users to explore the seat allotment statistics of JOSAA (Joint Seat Allocation Authority) from 2016 to 2022. This project utilises web scraping techniques to gather data from the JOSAA website, performs data cleaning and analysis, and presenting the insights through visualizations on a website frontend. The website presents the findings through interactive charts and tables, enabling users to gain valuable insights into the trends and patterns of seat allotments over the years.

## Objectives:
+ Data Collection: Scraping and aggregating seat allotment data from the JOSAA website for multiple years.
+ Data Processing: Cleaning and preprocessing the collected data to ensure accuracy and consistency.
+ Visualization: Presenting the analyzed data through interactive charts and tables to facilitate easy understanding and exploration of trends.
+ User Interaction: Enabling users to interact with the data, filter information, and gain valuable insights into the patterns of seat allotments across institutes and branches over the years

## Features:
+ Data Visualisation: Interactive charts and tables to visualise seat allotment statistics.
+ Branch Popularity Analysis: Track and analyse the popularity of various branches over the years.
+ Institute Insights: Understand the flow of students amongg different IITs and other institutes.
+ Yearly Comparison: Compare seat allotment data across different years.
+ User-Friendly Interface: Intutive and responsive design for a seamless user experience.

## Tech Stack/Frameworks:
- Frontend: HTML, CSS, JavaScript
* Backend: Django
+ Database: SQLite
- Data Scraping: Beautiful Soup
* Data Cleaning: NumPy, Pandas
+ Data Visualization: Chart.js

## Command to run the project locally
- python manage.py runserver
- Then run the server locally on port 8000

## Home page
The home page of the JOSAA Analysis portal provides a user-friendly interface to explore and analyze the JOSAA seat allotment statistics. It offers several insightful sections to delve into the data and gain valuable information. Here's a breakdown of each section:
- View Institute wise cut-off
- Analyze institute wise cut-off trends
- Roundwise cut-off Analysis 

![home](https://github.com/Vidya132/JOSAA-data-analysis/assets/95306028/1d752e47-ef2d-4b4c-bf66-77fc8817c09d)

## View Institute wise cut-off list page
- Upon clicking this option, a list of all IITs is shown along with their NIRF ranking(2022), Location and their established year. So the users can select specific institutes of their interest and explore the corresponding cut-off data.
![iit list](https://github.com/Vidya132/JOSAA-data-analysis/assets/95306028/f4f562e1-c93b-48a5-a114-4c321b296fe6)
 
  - ### For each IIT
      - By selecting a specific IIT, users can explore the trends and changes in the cut-off ranks throughout the various rounds of the seat allocation process over the years 2016 to 2022.
      - It can further narrow down their search by choosing specific programs offered by the selected institutes along with seat type and gender.
      - This feature helps users understand the cut-off trends for different programs in their preferred institutes.
      ![first graph](https://github.com/Vidya132/JOSAA-data-analysis/assets/95306028/5c411f78-ea17-4218-a0d6-9a8740ad78b5)

## Analyze institute wise cut-off trends
Institute trends section highlight the trends of various programs offered by a particular institute over the years. This helps understand the popularity and perception of programs offered by the institute, and thus helps understand the demand for a particular program in the institute during the counselling process.
![Screenshot (20)](https://github.com/Vidya132/JOSAA-data-analysis/assets/95306028/45d3feab-6bf4-4611-91fb-91580b6a90ce)
  
  - ### Features
      - Understand the demand trends for specific programs and courses offered by the institute during the counseling process
      - Upon selecting the gender, seat type and institute, users will get the cut-off analysis for each branch present at that IIT.
      ![Screenshot (22)](https://github.com/Vidya132/JOSAA-data-analysis/assets/95306028/1db046fe-c44c-4627-8282-c8143bf0a88a)

## Roundwise cut-off Analysis
Round trends section highlight the general trend of closing ranks throughout the rounds of the counselling process. This helps understand the likely range of changes in the closing ranks across various institutes and branches over multiple rounds.
  - ### Features
      - Users can get the round wise analysis for specific IIT by selecting the gender,seat type and branch. 
      - User can switch between different IITs by clicking on "Go to iit-list" button.
      ![Screenshot (25)](https://github.com/Vidya132/JOSAA-data-analysis/assets/95306028/3206dd19-d8fb-4e88-ace9-84a743db723e)



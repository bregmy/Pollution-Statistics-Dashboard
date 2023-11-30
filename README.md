# Pollution Statistics Dashboard

## Introduction
Air pollution is a critical environmental issue that significantly impacts public health and the overall well-being of communities. The Pollution Statistics Dashboard is a powerful tool designed to address the need for comprehensive visualization and analysis of air quality data. Developed as a Senior Project (COSC 490) at Morgan State University, this web application leverages the capabilities of Dash and Plotly to provide an interactive platform for exploring and understanding air pollution trends across different U.S. states.

## Features
### Choropleth Map
- The choropleth map visually represents air pollution levels across the United States, utilizing color-coded regions for easy interpretation.
- Clicking on a specific state on the map dynamically updates the remaining graphs, offering detailed pollution statistics for the selected region.

### Time Series Graphs
- Four time series graphs showcase the mean values of key pollutants (NO2, O3, SO2, CO) over the years.
- Each graph enables users to discern patterns and variations in pollution levels, fostering a deeper understanding of the temporal aspects of air quality.

### Bar-Line Graph
- The bar-line graph combines NO2 and O3 mean values for the selected state over multiple years.
- Facilitates a direct comparison of two pollutants on a single graph, providing insights into their respective contributions to air pollution.

### Pie Chart
- A pie chart offers a clear representation of the distribution of pollution types (NO2, O3, SO2, CO) for the selected state.
- Enhances visualization by illustrating the proportion of each pollutant in the overall pollution profile.

### Pollution Types and Effects
- Informational content outlines the effects of each major pollutant (NO2, O3, SO2, CO) on human health.
- Describes the respiratory and overall health impacts associated with these pollutants, fostering awareness among users.

## How to Use
1. Execute the provided code to run the application.
2. Access the web application through your preferred browser.
3. Explore the choropleth map by clicking on different states to reveal detailed pollution statistics.
4. Analyze the time series graphs, bar-line graph, and pie chart to gain insights into pollution trends and distributions.
5. Utilize the provided information on pollutant effects to understand the potential health implications.

## Requirements
- Python 3.x

## Installation
1. Unzip the compressed pollution data file (`pollution_data.zip`) in the same project folder.
2. Run the following commands to install the required packages:

```bash
# Install required packages
pip install dash
pip install plotly
pip install pandas

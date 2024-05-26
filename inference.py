from scripts import demand_identification,query_port_coordinates,plot_generations
main_port_name="Long Beach"
port_code = "USLGB"  # Example port code for Long Beach Port
width = 0.5  # Width of the bounding box in decimal degrees
height = 0.5  # Height of the bounding box in decimal degrees
cargo_vessel_types = ('70', '71', '72', '73', '74', '79')  # Example cargo vessel types


print("Query Coordinates for USLGB port",query_port_coordinates.get_long_beach_port(main_port_name="Long Beach"))

# hourly analysis
unique_vessels_hourly_df = demand_identification.count_unique_vessels_by_time(main_port_name,port_code, width, height, cargo_vessel_types, time_interval='h')
unique_vessels_hourly_df.to_csv("./output_file_after_analysis/hourly_time_and_vessels_analysis.csv")

# daily analysis
unique_vessels_daily_df = demand_identification.count_unique_vessels_by_time(main_port_name,port_code, width, height, cargo_vessel_types, time_interval='d')
unique_vessels_daily_df.to_csv("./output_file_after_analysis/daily_time_and_vessels_analysis.csv")
# Example usage
# Assuming unique_vessels_count is the DataFrame containing hourly unique vessel counts
plot_generations.plot_demand_variation_plotly(unique_vessels_hourly_df, file_name_to_save="variance_plot_hourly.png",time_resolution='h')
# daily variance
plot_generations.plot_demand_variation_plotly(unique_vessels_hourly_df,file_name_to_save="variance_plot_daily.png",time_resolution='d')
# distrubtion of vessels
plot_generations.plot_histogram(unique_vessels_hourly_df,file_name_to_save="distribution_of_vessels_hourly.png")
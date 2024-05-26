import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

save_path = "./plots_folder"
os.makedirs(save_path, exist_ok=True)


def plot_histogram(df: pd.DataFrame,file_name_to_save:str) -> None:
    """
        Generates a histogram plot of the 'UniqueVessels' column in the given DataFrame.
    
        Parameters:
            df (pandas.DataFrame): The DataFrame containing the data to be plotted.
                - Columns:
                    - 'UniqueVessels' (int or float): The column containing the data to be plotted.
    
        Returns:
            None
    """
        
    fig = px.histogram(df, x='UniqueVessels', title='Distribution of Unique Vessels')
    fig.write_image(os.path.join(save_path, file_name_to_save))
    fig.show()

def plot_demand_variation_plotly(unique_vessels_count: pd.DataFrame,file_name_to_save:str,time_resolution: str = 'H') -> None:
    """
    Plots the variation in demand over time.

    Args:
        unique_vessels_count (pandas.DataFrame): DataFrame containing the count of unique vessels
            for each time interval. The DataFrame should have a 'BaseDateTime' column for the
            time intervals and a 'UniqueVessels' column for the number of unique vessels.
        time_resolution (str, optional): The time resolution to resample the data by. Defaults to 'H'.

    Raises:
        KeyError: If the DataFrame is missing the 'BaseDateTime' column.

    Returns:
        None
    """
    # Ensure that the DataFrame contains the necessary columns
    if 'BaseDateTime' not in unique_vessels_count.columns:
        raise KeyError("Column 'BaseDateTime' is missing in the DataFrame.")
    
    # Set the 'BaseDateTime' column as the index
    reindexed_df = unique_vessels_count.set_index('BaseDateTime')
    
    # Resample the data to the specified time resolution and aggregate by counting unique vessels
    resampled_data = reindexed_df.resample(time_resolution).agg({'UniqueVessels': 'mean'})
    
    # Reset index to make 'BaseDateTime' a column again
    resampled_data.reset_index(inplace=True)
    
    # Plot demand variation using Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=resampled_data['BaseDateTime'], y=resampled_data['UniqueVessels'], mode='markers+lines', name='Demand Variation', 
                             marker=dict(size=8), line=dict(shape='spline')))
    
    # Update the x-axis title
    fig.update_xaxes(title='Time', tickangle=45)
    
    # Update the y-axis title
    fig.update_yaxes(title='Number of Unique Cargo Vessels')
    
    # Update the figure title
    fig.update_layout(title='Demand Variation Over Time')
    fig.write_image(os.path.join(save_path, file_name_to_save))
    fig.show()


import dash
from dash import dcc, html
import pandas as pd

# Load the data
df = pd.read_csv("pollution_data.csv")

# Convert 'Date Local' column to datetime
df['Date Local'] = pd.to_datetime(df['Date Local'])

# Extract year from the 'Date Local' column
df['Year'] = df['Date Local'].dt.year

# Create a Dash web application
app = dash.Dash(__name__)

# Define the layout of the application
app.layout = html.Div([
    html.H1("Pollution Statistics Dashboard"),

    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': state, 'value': state} for state in df['State'].unique()],
        value=df['State'].iloc[0],
        multi=False,
        style={'width': '50%'}
    ),

    html.Div([
        dcc.Graph(id='no2-graph', className='graph-container', style={'width': '25%'}),
        dcc.Graph(id='o3-graph', className='graph-container', style={'width': '25%'}),
        dcc.Graph(id='so2-graph', className='graph-container', style={'width': '25%'}),
        dcc.Graph(id='co-graph', className='graph-container', style={'width': '25%'}),
    ], className='row', style={'display': 'flex'})
])

# Define callback to update graphs based on dropdown selection
@app.callback(
    [dash.dependencies.Output('no2-graph', 'figure'),
     dash.dependencies.Output('o3-graph', 'figure'),
     dash.dependencies.Output('so2-graph', 'figure'),
     dash.dependencies.Output('co-graph', 'figure')],
    [dash.dependencies.Input('state-dropdown', 'value')]
)
def update_graphs(selected_state):
    filtered_df = df[df['State'] == selected_state]

    # Group data by year and calculate the mean for each year
    yearly_df = filtered_df.groupby('Year').mean().reset_index()

    # Common layout settings for all graphs
    common_layout = {
        'title': 'Pollution',
        'xaxis': {'title': 'Year'},
        'yaxis': {'title': 'Mean Value'},
        'mode': 'lines+markers',
    }

    # Smaller graph height
    smaller_height = 300

    # NO2 Graph
    no2_graph = {
        'data': [
            {'x': yearly_df['Year'], 'y': yearly_df['NO2 Mean'], 'type': 'scatter', 'name': 'NO2 Mean'},
            # Add other NO2 related data here if needed
        ],
        'layout': {**common_layout, 'height': smaller_height}
    }

    # O3 Graph
    o3_graph = {
        'data': [
            {'x': yearly_df['Year'], 'y': yearly_df['O3 Mean'], 'type': 'scatter', 'name': 'O3 Mean'},
            # Add other O3 related data here if needed
        ],
        'layout': {**common_layout, 'height': smaller_height}
    }

    # SO2 Graph
    so2_graph = {
        'data': [
            {'x': yearly_df['Year'], 'y': yearly_df['SO2 Mean'], 'type': 'scatter', 'name': 'SO2 Mean'},
            # Add other SO2 related data here if needed
        ],
        'layout': {**common_layout, 'height': smaller_height}
    }

    # CO Graph
    co_graph = {
        'data': [
            {'x': yearly_df['Year'], 'y': yearly_df['CO Mean'], 'type': 'scatter', 'name': 'CO Mean'},
            # Add other CO related data here if needed
        ],
        'layout': {**common_layout, 'height': smaller_height}
    }

    return no2_graph, o3_graph, so2_graph, co_graph

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)

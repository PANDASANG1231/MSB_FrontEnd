import dash
from dash import html, dcc, dash_table, Input, Output, State
import pandas as pd
import base64
import dash_bootstrap_components as dbc

# Choose a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN, dbc.icons.FONT_AWESOME])

# Encode the image (assuming OIP.png is in the same directory)
with open("OIP.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('ascii')

# Sample data
data = [
    {'Column 1': 'Text 1', 'Column 2': 'More text A', 'Column 3': 'More text A', 'Column 4': 'More text A', 'Column 5': 'More text A', 'Column 6': 'More text A', 'Column 7': 'More text A', 'Column 8': 'More text A', 'Column 9': 'More text A', 'Image': f'<img src="data:image/png;base64,{encoded_image}" style="height:100px; width:300px;">'},
    {'Column 1': 'Text 1', 'Column 2': 'More text A', 'Column 3': 'More text A', 'Column 4': 'More text A', 'Column 5': 'More text A', 'Column 6': 'More text A', 'Column 7': 'More text A', 'Column 8': 'More text A', 'Column 9': 'More text A', 'Image': f'<img src="data:image/png;base64,{encoded_image}" style="height:100px; width:300px;">'},
    {'Column 1': 'Text 1', 'Column 2': 'More text A', 'Column 3': 'More text A', 'Column 4': 'More text A', 'Column 5': 'More text A', 'Column 6': 'More text A', 'Column 7': 'More text A', 'Column 8': 'More text A', 'Column 9': 'More text A', 'Image': f'<img src="data:image/png;base64,{encoded_image}" style="height:100px; width:300px;">'},
]
df = pd.DataFrame(data)

# --- Layout Definition ---
app.layout = html.Div([
    # Navbar
    dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand("My Beautiful Dashboard", href="#", className="ms-2"),
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Home", href="#")),
                        dbc.NavItem(dbc.NavLink("Dashboard", href="#")),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("Page 1"),
                                dbc.DropdownMenuItem("Page 2"),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="More",
                        ),
                    ],
                    className="ms-auto",
                    navbar=True,
                ),
            ]
        ),
        color="primary",
        dark=True,
        className="mb-4",
    ),

    # Main Content Container
    dbc.Container(
        [
            html.H1("Dashboard Overview", className="text-center mb-4 display-4"),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Key Metric 1", className="card-title"),
                                    html.P("Value: 1,234", className="card-text"),
                                ]
                            ),
                            className="shadow-sm mb-4",
                        ),
                        md=4,
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Key Metric 2", className="card-title"),
                                    html.P("Value: 56.7%", className="card-text"),
                                ]
                            ),
                            className="shadow-sm mb-4",
                        ),
                        md=4,
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Key Metric 3", className="card-title"),
                                    html.P("Value: $8,901", className="card-text"),
                                ]
                            ),
                            className="shadow-sm mb-4",
                        ),
                        md=4,
                    ),
                ],
                className="mb-4",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H3("Image Data Table", className="card-title mb-3"),
                                    # The DataTable component
                                    dash_table.DataTable(
                                        id='table-with-images',
                                        columns=[
                                            {'id': c, 'name': c, 'presentation': 'markdown'} if c == 'Image' else {'id': c, 'name': c}
                                            for c in df.columns
                                        ],
                                        data=df.to_dict('records'),
                                        sort_action="native",  # Enable sorting
                                        sort_mode="multi",     # Allow multi-column sorting
                                        markdown_options={'html': True},
                                        style_data_conditional=[
                                            {
                                                'if': {'column_id': 'Image'},
                                                'padding': '5px'
                                            }
                                        ],
                                        style_cell={
                                            'height': '30px', # Squeeze cell height
                                            'minHeight': '30px', # Ensure minimum height is also squeezed
                                            'width': 'auto',
                                            'textAlign': 'center',
                                            'fontSize': '12px', # Smaller font size for cell text
                                            'lineHeight': '1'   # Adjust line height for squeezing
                                        },
                                        style_header={
                                            'backgroundColor': '#f8f9fa',
                                            'fontWeight': 'bold',
                                            'textAlign': 'center',
                                            'borderBottom': '2px solid #dee2e6',
                                            'fontSize': '12px',  # Smaller font size
                                            'height': '25px',    # Squeeze the header
                                            'minHeight': '25px', # Ensure minimum height is also squeezed
                                            'lineHeight': '1'    # Adjust line height for squeezing
                                        },
                                        style_data={
                                            'borderBottom': '1px solid #dee2e6'
                                        },
                                        style_as_list_view=True,
                                        css=[
                                            {'selector': '.dash-spreadsheet-container', 'rule': 'border: none'},
                                            {'selector': '.dash-spreadsheet-cell', 'rule': 'display: flex; align-items: center; justify-content: center;'}
                                        ]
                                    ),
                                ]
                            ),
                            className="shadow-sm mb-4",
                        ),
                        width=12,
                    )
                ]
            )
        ]
    ),

    # Modernized Modal for displaying larger image
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Enlarged Image")),
            dbc.ModalBody(html.Img(id='modal-image', style={'maxWidth': '100%', 'height': 'auto'})),
            dbc.ModalFooter(
                dbc.Button("Close", id="modal-close-button", className="ms-auto")
            ),
        ],
        id="image-modal",
        size="lg",
        is_open=False,
    ),

])

# --- Callbacks ---
@app.callback(
    Output('image-modal', 'is_open'),
    Output('modal-image', 'src'),
    Input('table-with-images', 'active_cell'),
    Input('modal-close-button', 'n_clicks'),
    State('table-with-images', 'data'),
    State('image-modal', 'is_open')
)
def toggle_image_modal(active_cell, n_clicks, table_data, is_open):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, "" # No input triggered yet

    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == 'table-with-images' and active_cell and active_cell['column_id'] == 'Image':
        row = active_cell['row']
        image_html = table_data[row]['Image']
        # Extract the base64 string from the img tag
        start_index = image_html.find('base64,') + len('base64,')
        end_index = image_html.find('" style=')
        base64_image_data = image_html[start_index:end_index]
        return True, f'data:image/png;base64,{base64_image_data}'
    elif trigger_id == 'modal-close-button' and n_clicks:
        return False, ""

    return is_open, dash.no_update


if __name__ == '__main__':
    app.run(debug=True)

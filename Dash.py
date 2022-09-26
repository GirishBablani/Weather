from dash import Dash, dcc, html,State
from dash.dependencies import Input, Output
from Api import current_temperature,forecast_temp,date,historical_data
import dash_bootstrap_components as dbc
from datetime import datetime,timedelta
import pytz
import sys
import numpy as np





IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)
app = Dash(__name__,meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=2.0, maximum-scale=1.2, minimum-scale=0.5'}])



app.layout = html.Div( 
    [   
      html.Div([
          html.H1("Weather Dash App",style={'text-align': 'center','font-size':'50px','color':'aqua','marginTop':'1px'}),
          html.H3("Search for your city weather",style={'text-align': 'center','font-size':'30px','color':'aqua','marginTop':'0px'}),
        html.B("City :",style={"color":"aqua",'text-align': 'center',"font-size":"30px"}),
        dcc.Input(id="input-on-submit", type="text", placeholder="Please Enter City", style={"border-radius":"8px","height":"25px","width":"150px",'marginLeft':'10px',"background-color":"Black","color":"aqua","border-color":"white","border-style":"solid",'text-align': 'center'}),
       
        html.Br(),
        html.Button('Submit', id='submit-val', n_clicks=0,style={"border-radius":"8px","marginTop":"20px","height":"30px","width":"85px","background-color":"aqua","marginBottom":"20px","color":"Black","font-decoration":"bold"}),
        html.Br()],style={"text-align":"center"}),
       
        
         
    
    html.Div([
         html.Div([
              html.Div(id='live_text1',style={"text-align":"center"}),html.Br(),html.Br(),
              html.Div(id="live_text2"),html.Br(),html.Br(),html.Br(),html.Div(id="live_graph"),html.Br(),html.Br(),
              html.Div(id="live_graph1"),html.Div(id="live_graph2")

         ], style = {"background-color":"Black","color":"aqua"}),
    ])],style={"background-color":"Black","height":"1000px","padding":0,"width":"100%"})


@app.callback(
    Output("live_text1", "children"),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks,value):
    if value != None :   
        city = value
        obj_1 = forecast_temp(city)
        obj = current_temperature(city)
        Centrigrate = u"\u2103"
        if isinstance(obj,str)==True:
            return obj
        else:
            return [ html.H1(f"Current Weather of City : {obj_1[6]}",style={'text-align': 'center','font-size':'30px','color':'aqua','marginTop':'1px'}),html.Br(),html.Div([dbc.Card(
    [
        dbc.Row(
            [
               html.Img(src=obj_1[0],style={"height":"30px","width":"30px","background-color":"None","Float":"Right"}),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Current Conditions", className="card-title"),
                            html.P(
                                f"Sky : {obj[0]} ",
                               
                                className="card-text",
                            ),html.P(
                                f"Temperature : {obj[1]} {Centrigrate}",
                               
                                className="card-text",
                            ),html.P(
                                f"Feels Like : {obj[2]}  {Centrigrate}",
                               
                                className="card-text",
                            ),html.P(
                                f"Maximum Temperature : {obj[3]}  {Centrigrate}",
                               
                                className="card-text",
                            ),html.P(
                                f"Minimum Temperature : {obj[4]}  {Centrigrate}",
                               
                                className="card-text",
                            ),
                            html.Small(
                                f"**Updated at {datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z')}",
                                className="card-text text-muted",style={"color":'red'}
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "540px","background-color":"black","color":"aqua","marginLeft":"50px","flex":1,"box-shadow":"2px 2px 10px 10px purple "}
),dbc.Card(
    [
        dbc.Row(
            [
                
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Other Conditions", className="card-title"),
                            html.P(
                                f"Pressure : {obj[5]} mb",
                               
                                className="card-text",
                            ),html.P(
                                f"Humidity : {obj[6]} %",
                               
                                className="card-text",
                            ),html.P(
                                f"Visibility : {obj[7]} km ",
                               
                                className="card-text",
                            ),html.P(
                                f"Wind_Speed : {obj[8]}  km/hr",
                               
                                className="card-text",
                            ),html.P(
                                f"Sunrise : {obj[9]} ",
                               
                                className="card-text",
                            ),html.P(
                                f"Sunset : {obj[10]} ",
                               
                                className="card-text",
                            )
                            
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "540px","background-color":"black","color":"aqua","marginLeft":"100px","float":"right","flex":2,"box-shadow":"2px 2px 10px 10px purple"}
)],style={"display":"flex"})
            ] 
    
    else :
        return [
            html.P("**Error : The city field should be filled",style={"color":"red","text-align":"center"}),
        ]  
@app.callback(
    Output("live_text2", "children"),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_forecast(n_clicks,value):
     if value != None  :
        city = value
        obj1 = forecast_temp(city)
        obj = current_temperature(city)
        date_u = date()
        Centrigrate = u"\u2103"
      
        if isinstance(obj,str)==True:
            return False
        else:
            
            return[html.H1("Predicted Weather",style={'text-align': 'center','font-size':'30px','color':'aqua','marginTop':'1px'}),html.Br(),html.Div([ 
                dbc.Card( ##Card1
    [
        dbc.CardImg(src=f"{obj1[5][1]}", top=True,style={"height":"50px","width":"50px"}),html.Br(),
        dbc.CardBody(
            [
                html.H4("Weather Details", className="card-title"),
                html.P([
                 html.P(f"Date:{date_u[0]}"),
                   html.P( f"Day:{obj1[1][1]}"),
                   html.P( f"Sky:{obj1[2][1]}"),
                   html.P( f"Max :{obj1[3][1]}"),
                    html.P(f"Min :{obj1[4][1]}"),
                ] ,className="card-text",
                ),
               
            ]
        ),
    ],
    style={"width": "14rem","background-color":"black","flex":1,"marginLeft":"30px","box-shadow":"2px 2px 10px 10px purple","maxWidth": "200px","text-align":"center"}),

    dbc.Card( ##Card2
    [
        dbc.CardImg(src=f"{obj1[5][2]}", top=True,style={"height":"50px","width":"50px"}),
        dbc.CardBody(
            [
                html.H4("Weather Details", className="card-title"),
                html.P([
                 html.P(f"Date:{date_u[1]}"),
                   html.P( f"Day:{obj1[1][2]}"),
                   html.P( f"Sky:{obj1[2][2]}"),
                   html.P( f"Max :{obj1[3][2]}"),
                    html.P(f"Min :{obj1[4][2]}"),
                ] ,className="card-text",
                ),
               
            ]
        ),
    ],
    style={"width": "14rem","background-color":"black","flex":2,"marginLeft":"50px","box-shadow":"2px 2px 10px 10px purple","maxWidth": "200px","text-align":"center"}),

     dbc.Card( ##Card3
    [
        dbc.CardImg(src=f"{obj1[5][3]}", top=True,style={"height":"50px","width":"50px"}),
        dbc.CardBody(
            [
                html.H4("Weather Details", className="card-title"),
                html.P([
                 html.P(f"Date:{date_u[2]}"),
                   html.P( f"Day:{obj1[1][3]}"),
                   html.P( f"Sky:{obj1[2][3]}"),
                   html.P( f"Max :{obj1[3][3]}"),
                    html.P(f"Min :{obj1[4][3]}"),
                ] ,className="card-text",
                ),
               
            ]
        ),
    ],
    style={"width": "14rem","background-color":"black","flex":3,"marginLeft":"50px","box-shadow":"2px 2px 10px 10px purple","maxWidth": "200px","text-align":"center"}),

    dbc.Card( ##Card4
    [
        dbc.CardImg(src=f"{obj1[5][4]}", top=True,style={"height":"50px","width":"50px"}),
        dbc.CardBody(
            [
                html.H4("Weather Details", className="card-title"),
                html.P([
                 html.P(f"Date:{date_u[3]}"),
                   html.P( f"Day:{obj1[1][4]}"),
                   html.P( f"Sky:{obj1[2][4]}"),
                   html.P( f"Max :{obj1[3][4]}"),
                    html.P(f"Min :{obj1[4][4]}"),
                ] ,className="card-text",
                ),
               
            ]
        ),
    ],
    style={"width": "14rem","background-color":"black","flex":3,"marginLeft":"50px","box-shadow":"2px 2px 10px 10px purple","maxWidth": "200px","text-align":"center"}),

     dbc.Card( ##Card5
    [
        dbc.CardImg(src=f"{obj1[5][4]}", top=True,style={"height":"50px","width":"50px"}),
        dbc.CardBody(
            [
                html.H4("Weather Details", className="card-title"),
                html.P([
                 html.P(f"Date:{date_u[4]}"),
                   html.P( f"Day:{obj1[1][5]}"),
                   html.P( f"Sky:{obj1[2][5]}"),
                   html.P( f"Max :{obj1[3][5]}"),
                    html.P(f"Min :{obj1[4][5]}"),
                ] ,className="card-text",
                ),
               
            ]
        ),
    ],
    style={"width": "14rem","background-color":"black","flex":3,"marginLeft":"50px","box-shadow":"2px 2px 10px 10px purple","maxWidth": "200px","text-align":"center"})
               ],style={"display":"flex"})   ]

     else:
        return[False]       
@app.callback(
    Output("live_graph", "children"),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def graph_forecast(n_clicks,value):
     if value != None :
        city = value
        obj = current_temperature(city)
        obj1 = forecast_temp(city)
        date_u = date()
        if isinstance(obj,str)==True:
            return False
        else:
         return [dcc.Graph(
    figure={
        'data': [
            {'x': date_u, 'y': obj1[3], 'type': 'line', 'name': 'Maximum Temperature','line':{'color':'purple'}},
            {'x': date_u, 'y': obj1[4], 'type': 'line', 'name': 'Minimum Temperature','line':{'color':'blue'}},
        ],
        'layout': {
            'title': f'Predicted Weather For {obj1[6]}',
            'plot_bgcolor': 'Black',
             'height':'auto',
            'paper_bgcolor':'Black',
            'hovermode':'x unified',
            'font': {
                    'color': 'aqua'
                },
              
        }
    }
)   ]
     else:
        return False  
@app.callback(
    Output("live_graph1", "children"),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def graph_forecast2(n_clicks,value):
     if value != None :
         city = value
         obj1 = forecast_temp(city)
         obj = current_temperature(city)
         
         if isinstance(obj,str)==True:
            return False
         else:
            obj_1 = historical_data(obj[11], obj[12])
            return [dcc.Graph(
    figure={
        'data': [
            {'x': obj_1.index, 'y': obj_1.tmax, 'type': 'line', 'name': 'Maximum Temperature','line':{'color':'purple'}},
            {'x': obj_1.index, 'y': obj_1.tmin, 'type': 'line', 'name': 'Minimum Temperature','line':{'color':'blue'}},
            {'x': obj_1.index, 'y': obj_1.tavg, 'type': 'line', 'name': 'Average Temperature','line':{'color':'Green'}},
        ],
        'layout': {
            'title': f'Historical Weather Of {obj1[6]} For Past 30 Days',
            'plot_bgcolor': 'Black',
            'height':'auto',
            'paper_bgcolor':'Black',
            'hovermode':'x unified',
            'font': {
                    'color': 'aqua'
                }
        }
    }
)   ]
     else:
        return False  
@app.callback(
    Output("live_graph2", "children"),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def graph_forecast2(n_clicks,value):
     if value != None  :
         city = value
         obj1 = forecast_temp(city)
         obj = current_temperature(city)
         
         if isinstance(obj,str)==True:
            return False
         else:
            obj_1 = historical_data(obj[11], obj[12])
            return [dcc.Graph(
    figure={
        'data': [
            {'x': obj_1.index, 'y': obj_1.prcp, 'type': 'line', 'name': 'Precipitation in mm','line':{'color':'Blue'}},
            {'x': obj_1.index, 'y': obj_1.wspd, 'type': 'line', 'name': 'Wind Speed in Km/hr','line':{'color':'Orange'}},
            
        ],
        'layout': {
            'title': f'',
            'plot_bgcolor': 'Black',
            'height':'auto',
            'paper_bgcolor':'Black',
            'hovermode':'x unified',
            'font': {
                    'color': 'aqua'
                }
        }
    }
)   ]
     else:
        return False          

           
    
if __name__ == "__main__":
    app.run_server()

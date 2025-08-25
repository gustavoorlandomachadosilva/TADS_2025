import yfinance as yf
import plotly.express as px

def plot(ticker: str):
    """_summary_
    Plot a time Series

    Args:
        ticker (str): the company ticker.

    Returns:
        _type_: return fig
    """  

    data = yf.download(ticker, period='max', multi_level_index=False)
    df = data.reset_index()[['Date','Close']]   

    fig = px.line(df,
                   x='Date', 
                   y='Close',
                   title=f"Historico de {ticker}"
                   )

    return fig
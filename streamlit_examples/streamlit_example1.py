### tutorial link: https://www.youtube.com/watch?v=k4bjv6e5goo
import investpy as ip
from datetime import datetime, timedelta
import plotly.graph_objs as go
import streamlit as st
import pandas as pd
print('Imports: OK')

countries = ['brazil', 'united states']
# acoes = ip.get_stocks_list(country='brazil')

dt_start = datetime.today() - timedelta(days=30)
dt_end = datetime.today()

@st.cache
def consultar_acao(stock,country, from_date, to_date, interval):
    df = ip.get_stock_historical_data(stock=stock, country=country, from_date=from_date, to_date=to_date, interval=interval)
    return df

def format_date(dt, format = '%d/%m/%Y'):
    return dt.strftime(format)

print(format_date(dt_start))

intervals = ['Daily', 'Week', 'Monthly']
df = ip.get_stock_historical_data(stock='ENGI4',
                                  country='Brazil',
                                  from_date=format_date(dt_start),
                                  to_date=format_date(dt_end),
                                  interval='Daily')

# Plot candle
def plot_candle_stick(df, acao='ticket'):
    trace1 = {
        'x': df.index,
        'open': df.Open,
        'close': df.Close,
        'high': df.High,
        'low': df.Low,
        'type': 'candlestick',
        'name': acao,
        'showlegend': False
    }

    data = [trace1]
    layout = go.Layout()

    fig = go.Figure(data=data, layout=layout)
    return fig

# barra lateral

barra_lateral = st.sidebar.empty()

country_select = st.sidebar.selectbox("Selecione o pais:", countries)

acoes = ip.get_stocks_list(country=country_select)

stock_select = st.sidebar.selectbox("Selecione o ativo:", acoes)

from_date = st.sidebar.date_input('De:', dt_start)
to_date = st.sidebar.date_input('Para:', dt_end)

interval_select = st.sidebar.selectbox("Selecione o intervalo:", intervals)

carregar_dados = st.sidebar.checkbox("Carregar dados")

### elementos centrais na página

st.title('Stock Monitor')
st.header('Ações')
st.subheader('Visualização gráfica')

grafico_candle = st.empty()
grafico_line = st.empty()

if from_date > to_date:
    st.sidebar.error('Data de início maior do que data final.')
else:
    df = consultar_acao(stock_select, country_select, format_date(from_date), format_date(to_date), interval_select)
    try:
        fig = plot_candle_stick(df)
        grafico_candle = st.plotly_chart(fig)
        grafico_line = st.line_chart(df.Close)

        if carregar_dados:
            st.subheader('Dados')
            dados = st.dataframe(df)
    except Exception as e:
        st.error(e)
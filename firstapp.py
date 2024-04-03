import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
st.markdown("<h1 style='text-align: center; font-size: 40px;'>FinanceChart</h1>", unsafe_allow_html=True)

st.title('Gráfico Histórico de Precios de Activos Financieros')

# Widget de entrada de texto para ingresar el ticker
ticker_input = st.text_input('Ingrese el ticker del activo financiero (ejemplo: AAPL)')

# Verificar si se ingresó un ticker
if ticker_input:
    # Obtener los datos históricos del ticker
    try:
        data = yf.download(ticker_input, start='2020-01-01', end='2022-01-01')
        
        # Mostrar el gráfico
        st.subheader('Gráfico de Precios de Cierre')
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(data['Close'])
        ax.set_title(f'Precio de Cierre de {ticker_input}')
        ax.set_xlabel('Fecha')
        ax.set_ylabel('Precio de Cierre')
        st.pyplot(fig)
        
        # Mostrar los datos en forma de tabla
        st.subheader('Datos Históricos')
        st.write(data)
        
    except Exception as e:
        st.error(f'Ocurrió un error al obtener los datos: {e}')

from flask import render_template, session
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64

def apps_plot():
    
    engine = create_engine('sqlite:///' + filename + 'sqlclassestabela.db')
    df = pd.read_sql('Apolice_Cliente', con=engine)

  
    df['data_efetiva'] = pd.to_datetime(df['data_efetiva'], format='%Y/%m/%d')


    df = df[(df['data_efetiva'].dt.year == 2025) & (df['data_efetiva'].dt.month.isin([1, 2]))]


    df['mes'] = df['data_efetiva'].dt.month.map({1: 'Janeiro', 2: 'Fevereiro'})

    resultado = df.groupby(['mes', 'estado']).size().unstack(fill_value=0)


    fig, ax = plt.subplots()
    resultado.plot(kind='bar', ax=ax, width=0.7)

    plt.xlabel('Mês')
    plt.ylabel('Número de Apólices')
    plt.title('Apólices por Estado (Jan e Fev 2025)')
    plt.xticks(rotation=0)
    plt.legend(title='Estado')
    plt.tight_layout()

  
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image = base64.b64encode(buf.getvalue()).decode('utf-8')


    return render_template("plot.html", image=image, ulogin=session.get("user"))

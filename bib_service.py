import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")
sites = ["PORTBUNATI","PASOPATI","AWSKGU","AWSKGB"]

wx_icon_dict = {"Cerah":"https://www.bmkg.go.id/asset/img/weather_icon/ID/cerah-am.png",
                "Cerah Berawan":"https://www.bmkg.go.id/asset/img/weather_icon/ID/cerah%20berawan-am.png",
                2:"https://www.bmkg.go.id/asset/img/weather_icon/ID/cerah%20berawan-am.png",
                "Berawan":"https://www.bmkg.go.id/asset/img/weather_icon/ID/berawan-am.png",
                "Berawan Tebal":"https://www.bmkg.go.id/asset/img/weather_icon/ID/berawan tebal-am.png",
                "Asap":"https://www.bmkg.go.id/asset/img/weather_icon/ID/asap-am.png",
                "Kabut":"https://www.bmkg.go.id/asset/img/weather_icon/ID/kabut-am.png",
                "Hujan Ringan":"https://www.bmkg.go.id/asset/img/weather_icon/ID/hujan%20ringan-am.png",
                "Hujan Sedang":"https://www.bmkg.go.id/asset/img/weather_icon/ID/hujan%20sedang-am.png",
                "Hujan Lebat":"https://www.bmkg.go.id/asset/img/weather_icon/ID/hujan%20lebat-am.png",
                "Hujan Petir":"https://www.bmkg.go.id/asset/img/weather_icon/ID/hujan%20petir-am.png",
                97:"https://www.bmkg.go.id/asset/img/weather_icon/ID/hujan%20petir-am.png"}
def custom_date_parser(date_string):
    return pd.to_datetime(date_string, format='%HZ%d%b%Y')

#load dataframe:
df_bunati = pd.read_csv("https://web.meteo.bmkg.go.id//media/data/bmkg/BIB/Alt/PORTBUNATI.csv",sep=";",parse_dates=["local_time1","local_time"], date_parser=custom_date_parser)
df_pasopati = pd.read_csv("https://web.meteo.bmkg.go.id//media/data/bmkg/BIB/Alt/PASOPATI.csv",sep=";",parse_dates=["local_time1","local_time"], date_parser=custom_date_parser)
df_awskgu = pd.read_csv("https://web.meteo.bmkg.go.id//media/data/bmkg/BIB/Alt/AWSKGU.csv",sep=";",parse_dates=["local_time1","local_time"], date_parser=custom_date_parser)
df_awskgb = pd.read_csv("https://web.meteo.bmkg.go.id//media/data/bmkg/BIB/Alt/AWSKGB.csv",sep=";",parse_dates=["local_time1","local_time"], date_parser=custom_date_parser)
df_list = [df_bunati,df_pasopati,df_awskgu,df_awskgb]
st.header("BIB Weather Service")

st.write("## Sites")
tabs = st.tabs(sites)
for tab,df in zip(tabs,df_list):
    cols = tab.columns(8)
    count=0
    for index,data in df.iterrows():
        with cols[count]:
            st.markdown("""
                <style>
                [data-testid=column] [data-testid=stVerticalBlock]{
                    gap: 0.2rem;
                }
                </style>
                """, unsafe_allow_html=True)
            st.write(f"**{data['local_time1']:%d/%m %H:%M} LT**")
            st.image(wx_icon_dict[data["wx"]],width=50)
            st.write(data["wx"])
            st.write(f"{data['prec']} mm")
            st.write(f"{data['t2m']} C | {data['rh']} %")
            st.write(f"Angin")
            st.write(f"{data['wd']}")
            st.write(f"{data['ws']} knot")
            st.write(f"Vis {data['vis_text']} km")
            st.divider()
            count += 1
            if count >= 8:
                count = 0

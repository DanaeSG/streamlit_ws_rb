import streamlit as st
from  gpt_wrapper import gpt_wrapper_message

# Titulo de la aplicacion
st.title("GPT wrapper")

# Linea divisora
st.divider()

st.subheader("Interactua con LLMs")

st.image("kuromi.jpg")

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.line_chart(chart_data)

prompt = st.text_input("Escribe tu msj")

if st.button("Enviar"):
    gpt_wrapper_message(prompt)
    st.success("Respuesta generada")
else:
    st.warning("Envia tu msj")


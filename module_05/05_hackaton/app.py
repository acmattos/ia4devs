import cv2
import streamlit as st
from PIL import Image
import io

from model_predict import predict

# importe aqui sua função de predição YOLO
# por exemplo, se ela estiver em predict.py:
# from predict import predict_image
def predict_image(img: Image.Image) -> Image.Image:
    """
    Stub de exemplo: recebe PIL.Image, executa YOLO e retorna PIL.Image
    com as caixas desenhadas.
    Você deve substituir essa função pelo seu script real.
    """

    trained_dir_name: str = 'yolo11n_custom_100'
    trained_model_best_path = f"../runs/detect/{trained_dir_name}/weights/best.pt"
    results = predict(
        trained_dir_name,
        trained_model_best_path,
        img,
        conf = 0.5
    )

    return Image.fromarray(cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB))

st.set_page_config(page_title="YOLO Detection", layout="wide")
st.title("🖼️ Analisador de Ameaças STRIDE em Diagramas AWS - Demo")

uploaded_file = st.file_uploader("📤 Escolha uma imagem", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # lê bytes e converte em PIL.Image
    img_bytes = uploaded_file.read()
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    st.image(img, caption="Imagem enviada", use_column_width=True)

    if st.button("▶️ Executar detecção"):
        with st.spinner("Rodando o modelo YOLO..."):
            # chama sua função de predição
            result_img = predict_image(img)

        st.success("Detecção concluída!")
        st.image(result_img, caption="Resultado YOLO", use_column_width=True)

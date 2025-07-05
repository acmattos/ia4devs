import os
import io
import cv2
import streamlit as st
from PIL import Image

from model_predict import predict
from report_generator import generate_report  # importa sua função atualizada


def predict_image(img: Image.Image) -> Image.Image:
    """
    Recebe PIL.Image, executa YOLO e retorna PIL.Image
    com as caixas desenhadas.
    """
    trained_dir_name     = 'yolo11n_custom_100'
    trained_model_best   = f"../runs/detect/{trained_dir_name}/weights/best.pt"
    # predict agora devolve (results, detailed_json_in_memory)
    results, detailed_json = predict(
        trained_dir_name,
        trained_model_best,
        img,
        conf=0.5
    )
    # retorna a imagem anotada
    annotated = cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB)
    return Image.fromarray(annotated), detailed_json


st.set_page_config(page_title="YOLO Detection", layout="wide")
st.title("🖼️ Analisador de Ameaças STRIDE em Diagramas AWS - Demo")

uploaded_file = st.file_uploader("📤 Escolha uma imagem", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = Image.open(io.BytesIO(uploaded_file.read())).convert("RGB")
    st.image(img, caption="🔍 Imagem enviada", use_column_width=True)

    if st.button("▶️ Executar detecção"):
        with st.spinner("⚙️ Rodando o modelo YOLO..."):
            # aqui agora recebemos também o JSON em memória
            result_img, detections_json = predict_image(img)

        st.success("✅ Detecção concluída!")
        st.image(result_img, caption="Resultado YOLO", use_column_width=True)

        # ———————————————— GERAÇÃO DE RELATÓRIO ————————————————
        # monta pasta de saída
        reports_path = os.path.join("data", "reports", "yolo11n_custom_100")
        os.makedirs(reports_path, exist_ok=True)

        with st.spinner("📄 Gerando relatório STRIDE..."):
            # como generate_report retorna o HTML completo, capturamos aqui
            html_report = generate_report(
                reports_json_path=detections_json,    # passa a lista de dicts
                stride_yaml_path="data/stride/stride_map.yaml",
                controls_yaml="data/stride/controls_by_threat.yaml",
                conf_threshold=0.2,
                reports_path=reports_path
            )
        st.success(f"✅ Relatório salvo em `{reports_path}`")

        # ———————————————— EXIBE O RELATÓRIO ————————————————
        st.header("🌐 Threat Model Report (HTML)")
        st.components.v1.html(html_report, height=600, scrolling=True)
        # opcional: botão de download do HTML
        st.download_button(
            label="⬇️ Baixar report.html",
            data=html_report,
            file_name="report.html",
            mime="text/html"
        )

# import cv2
# import streamlit as st
# from PIL import Image
# import io
#
# from model_predict import predict
#
# # importe aqui sua função de predição YOLO
# # por exemplo, se ela estiver em predict.py:
# # from predict import predict_image
# def predict_image(img: Image.Image) -> Image.Image:
#     """
#     Stub de exemplo: recebe PIL.Image, executa YOLO e retorna PIL.Image
#     com as caixas desenhadas.
#     Você deve substituir essa função pelo seu script real.
#     """
#
#     trained_dir_name: str = 'yolo11n_custom_100'
#     trained_model_best_path = f"../runs/detect/{trained_dir_name}/weights/best.pt"
#
#     results, json = predict(
#         trained_dir_name,
#         trained_model_best_path,
#         img,
#         conf = 0.5
#     )
#
#     return Image.fromarray(cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB))
#
# st.set_page_config(page_title="YOLO Detection", layout="wide")
# st.title("🖼️ Analisador de Ameaças STRIDE em Diagramas AWS - Demo")
#
# uploaded_file = st.file_uploader("📤 Escolha uma imagem", type=["jpg", "jpeg", "png"])
# if uploaded_file is not None:
#     img_bytes = uploaded_file.read()
#     img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
#     st.image(img, caption="Imagem enviada", use_column_width=True)
#
#     if st.button("▶️ Executar detecção"):
#         with st.spinner("Rodando o modelo YOLO..."):
#             # chama sua função de predição
#             result_img = predict_image(img)
#
#         st.success("Detecção concluída!")
#         st.image(result_img, caption="Resultado YOLO", use_column_width=True)

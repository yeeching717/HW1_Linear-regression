
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# --- 1. 商業理解 (Business Understanding) ---
# 目標: 建立一個Web應用程式，讓使用者可以透過視覺化的方式理解簡單線性回歸。
# 需求: 使用者能調整線性方程式 y = ax + b 中的係數 a、雜訊(noise)的大小，以及生成資料點的數量。

st.set_page_config(layout="wide")
st.title("互動式簡單線性回歸分析 (CRISP-DM)")

st.markdown("""
這是一個遵循 **CRISP-DM** 流程的簡易資料科學專案。
- **商業理解:** 我們的目標是視覺化線性回歸。
- **資料理解 & 準備:** 您可以在左側的側邊欄中動態生成您的資料。
- **模型建立:** 我們將使用 Scikit-learn 的 `LinearRegression` 模型進行擬合。
- **模型評估:** 結果將以圖表形式視覺化呈現。
- **部署:** 這個 Streamlit 應用程式本身就是部署的成果。
""")

st.sidebar.header("資料生成參數 (Data Understanding & Preparation)")

# --- 2. 資料理解 & 3. 資料準備 (Data Understanding & Preparation) ---
# 讓使用者透過UI元件來定義資料
a_coeff = st.sidebar.slider("係數 (a)", -10.0, 10.0, 2.5, 0.1)
b_intercept = st.sidebar.slider("截距 (b)", -10.0, 10.0, 0.0, 0.1)
num_points = st.sidebar.slider("資料點數量", 10, 500, 100, 10)
noise_level = st.sidebar.slider("雜訊大小", 0.0, 10.0, 2.0, 0.1)

# 根據使用者輸入生成資料
@st.cache_data
def generate_data(a, b, n_points, noise):
    """根據給定參數生成線性資料"""
    x = np.linspace(0, 10, n_points)
    # 加上一些隨機雜訊
    random_noise = np.random.normal(0, noise, n_points)
    y = a * x + b + random_noise
    return x, y

x_data, y_data = generate_data(a_coeff, b_intercept, num_points, noise_level)
df = pd.DataFrame({'x': x_data, 'y': y_data})

# --- 4. 模型建立 (Modeling) ---
# 準備 Scikit-learn 需要的資料格式
X = df[['x']] # Scikit-learn 需要 2D array
y = df['y']

# 建立並訓練模型
model = LinearRegression()
model.fit(X, y)

# 取得模型預測結果
y_pred = model.predict(X)


# --- 5. 模型評估 (Evaluation) ---
st.header("模型評估與視覺化")

col1, col2 = st.columns(2)

with col1:
    st.subheader("回歸分析圖")
    fig, ax = plt.subplots()
    # 繪製原始資料點
    ax.scatter(x_data, y_data, label='原始資料 (Generated Data)', alpha=0.6)
    # 繪製回歸線
    ax.plot(x_data, y_pred, color='red', linewidth=2, label='回歸線 (Regression Line)')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

with col2:
    st.subheader("模型參數")
    st.markdown(f"""
    根據您生成的資料，我們訓練出的模型結果如下：

    - **模型斜率 (Coefficient):** `{model.coef_[0]:.4f}`
    - **模型截距 (Intercept):** `{model.intercept_:.4f}`

    您在側邊欄設定的原始參數為：
    - **原始係數 (a):** `{a_coeff}`
    - **原始截距 (b):** `{b_intercept}`

    比較兩者可以看出雜訊對模型訓練的影響。
    """)
    st.subheader("原始資料")
    st.dataframe(df.head())


st.info("您可以嘗試調整左側的參數，觀察回歸線如何隨著資料的變化而即時更新。")


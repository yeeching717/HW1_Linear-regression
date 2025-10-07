# 實作流程 (CRISP-DM)

這是一個根據 `originalPlan.md` 的內容所制定的實作流程。

這個流程將遵循 CRISP-DM 方法論來解決一個簡單的線性回歸問題，並建立一個互動式的 Web 應用程式。

## 1. 商業理解 (Business Understanding)
*   **目標:** 建立一個 Web 應用程式，讓使用者可以透過視覺化的方式理解簡單線性回歸。
*   **需求:** 使用者需要能夠調整線性方程式 `y = ax + b` 中的係數 `a`、雜訊 (noise) 的大小，以及生成資料點的數量，並即時看到回歸線的變化。

## 2. 資料理解 (Data Understanding)
*   **資料來源:** 我們將不使用現有資料集，而是根據使用者輸入的參數 `a`、`noise` 和 `number of points` 來動態生成合成資料 (synthetic data)。
*   **資料特性:** 資料將包含一組 (x, y) 座標，其中 y 值會根據 `y = ax + noise` 的公式產生，`noise` 會是隨機分佈的。

## 3. 資料準備 (Data Preparation)
*   **資料生成:** 撰寫一個 Python 函式，該函式接收 `a`、`noise` 和 `number of points` 作為輸入，並輸出一組 x 和 y 值的陣列。
*   **資料格式:** 將生成的資料轉換為 Pandas DataFrame，以便於後續模型訓練和視覺化。

## 4. 模型建立 (Modeling)
*   **模型選擇:** 使用 `scikit-learn` 函式庫中的 `LinearRegression` 模型。這是一個適合此問題的標準模型。
*   **模型訓練:** 使用者每次調整參數並重新生成資料後，都將重新訓練 `LinearRegression` 模型。

## 5. 模型評估 (Evaluation)
*   **視覺化:** 核心評估方式是透過視覺化。我們將使用 `matplotlib` 或 `plotly` 等函式庫繪製散點圖來顯示生成的資料點，並在同一張圖上繪製出模型計算出的回歸線。
*   **指標:** (可選) 我們可以計算並顯示 R-squared (R²) 分數，以量化模型的擬合優度。

## 6. 部署 (Deployment)
*   **框架選擇:** 使用 Streamlit 框架。它非常適合快速開發資料科學和機器學習的 Web 應用程式。
*   **使用者介面 (UI):**
    *   使用 `st.slider` 或 `st.number_input` 來讓使用者調整 `a`、`noise` 和 `number of points`。
    *   使用 `st.pyplot` 或 `st.plotly_chart` 來顯示結果圖表。
*   **應用程式流程:**
    1.  顯示標題和說明。
    2.  在側邊欄或主頁上提供參數調整的 UI 元件。
    3.  根據使用者的輸入生成資料。
    4.  訓練線性回歸模型。
    5.  繪製並顯示資料點和回歸線。
    6.  (可選) 顯示 R² 分數。


# **Mood Analysis Project**
![Mood Analysis Flow](image/mood_image.jpg "Overview of Mood Analysis Flow")

## **Overview**

The Mood Analysis Project is a machine learning-based solution designed to analyze user input and classify it into one of six emotional categories: **Sadness**, **Fear**, **Love**, **Joy**, **Anger**, and **Surprise**. It employs a **Bidirectional GRU (Gated Recurrent Unit)** model for mood prediction, ensuring high accuracy and efficiency.  

The project follows **modular coding principles** for better maintainability and scalability. Custom logs and exceptions provide detailed insights into execution and error handling. Additionally, an `artifacts` folder is included to document all processing techniques, while large files like the model and tokenized training data are stored in a `release` folder.

---

## **Features**

- **Mood Classification:** Predicts one of six moods based on user-provided text.
- **Pipeline Modularity:** Separate modules for each data processing and modeling step.
- **Configurable Settings:** Centralized configuration via `config.yaml`
- **Bidirectional GRU Model:** A robust deep learning model optimized for sequential data.
- **Processing Artifacts:** Comprehensive documentation of processing techniques in the `artifacts` folder.
- **Custom Logging and Exceptions:** Enhance debugging and provide execution insights.
- **Modular Codebase:** Well-structured modules for scalability and clarity.
- **Processing Artifacts:** Comprehensive documentation of preprocessing steps in the `artifacts` folder.

---
## Datasets
-The datasets (in CSV format) are hosted as part of the app, with Flask and Render serving the files directly through URL links.
  - Github link - https://github.com/Lathacharujenny/DatasetsUrl.git
  - App link - https://datasetsurl-9cc6ccd16e07.Renderapp.com/

## Pipeline Design
The project is structured into the following reusable modules:

**1. Data Ingestion:**
Handles loading of raw data from various sources and prepares it for processing.

**2. Data Cleaning:**
Implements a cleaning pipeline to remove noise, such as special characters, stopwords, and redundant whitespace.

**3. Data Transformation:**
Converts cleaned text into numerical representations for model compatibility.

**4. Data Tokenization:**
Tokenizes and pads the text data, preparing it for input to the Bidirectional GRU model.

**5. Model Training:**
Trains the Bidirectional GRU model on the tokenized and transformed data.

**6. Model Evaluation:**
Evaluates the trained model’s performance using metrics like accuracy, and Consfusion Matrix.

Each module can be independently updated or reused, adhering to modular programming principles.

## **How It Works**

1. **Centralized Configuration:**
   - The `config.yaml` file stores all configuration details such as file paths, model 
    parameters, and hyperparameters..
   - This approach enables flexibility and easier experimentation..
2. **Execution Workflow:**
   - The project follows a systematic pipeline, starting with data ingestion, cleaning, transformation, and tokenization, followed by model training and evaluation..
3. **Output:**
   - Returns the predicted mood label (e.g., "Joy") for the given input.

---

## **Artifacts and Releases**

- **Artifacts Folder:**  
  The `artifacts` folder contains detailed documentation of the processing techniques used in the project. It serves as a reference for how the data was prepared, tokenized, and processed before being used by the model.

- **Release Folder:**  
  Large files, including the trained model and tokenized training data (`x_train`), are stored in the `release` folder for convenience and to avoid version control issues with large files.
  - Model-https://github.com/Lathacharujenny/MoodAnalysis/releases/download/model_pickle/model.pkl
  - x_train - https://github.com/Lathacharujenny/MoodAnalysis/releases/download/X_train_tokenized_data/X_train.npy

---

## **Modular Coding Design**

The project adheres to **modular coding principles**, dividing functionality into independent modules. This ensures the codebase is:

- **Maintainable:** Each module can be updated or debugged independently.
- **Scalable:** New features can be added seamlessly.
- **Reusable:** Components can be reused in similar projects.

### **Key Modules**
- **Data Preprocessing Module:** Manages text cleaning, tokenization, and embedding generation.
- **Model Module:** Handles the implementation and usage of the Bidirectional GRU model.
- **Logger Module:** Records logs for process flow, warnings, and errors.
- **Exception Module:** Includes custom exceptions for improved error handling.

---

## **Technologies Used**

- **Programming Language:** Python
- **Deep Learning Framework:** TensorFlow/Keras
- **Model Architecture:** Bidirectional GRU
- **Data Processing Libraries:** NumPy, Pandas
- **Logging and Debugging:** Custom Logging and Exception Handling

---

## **Steps to Run the Project**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mood-analysis.git
   cd mood-analysis
2. Install Dependencies
   ``` pip install -r requirements.txt```
3. Run the code
   ``` python main.py ```

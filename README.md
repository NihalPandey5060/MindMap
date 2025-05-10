# AI Model Inference Web App

A minimalistic Streamlit web application for running inference with pre-trained AI models. The app provides a clean interface for model loading, prediction, and interaction history tracking.

## Features

- Upload and load pre-trained models (.pkl or .h5 files)
- Simple and intuitive user interface
- Multiple input types (numbers, dropdowns, sliders)
- Automatic interaction history logging
- Clean and responsive design

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Upload your pre-trained model using the file uploader in the sidebar
2. Fill in the input fields according to your model's requirements
3. Click "Predict" to get the model's prediction
4. View your interaction history in the "Recent Interactions" section

## Customization

- Modify the input fields in `app.py` to match your model's requirements
- Adjust the prediction logic in `model_utils.py` if needed
- Change the data storage method in `data_utils.py` if required

## Project Structure

- `app.py`: Main Streamlit application
- `model_utils.py`: Model loading and prediction functions
- `data_utils.py`: Interaction history management
- `requirements.txt`: Project dependencies
- `interactions.json`: Database file for storing interaction history (created automatically)

## Notes

- The app uses TinyDB for storing interaction history
- Model files are temporarily stored during loading
- All interactions are logged with timestamps 

## Credits

- Nihal Pandey
- Ishan Pandey(GOAT)
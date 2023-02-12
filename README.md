# Paper-Barcode-Parser-Web-App
A Paper Barcode Parser Model built using Open CV, tesseract-ocr and finally deployed on webpage using Streamlit. 


# Install :
pip install streamlit

pip install opencv-python

pip install pillow

sudo apt install tesseract-ocr

sudo apt install libtesseract-dev

pip install pytesseract

## Linux : copy ara.traineddata to /usr/share/tesseract/tessdata/ 

command :

sudo cp ara.traineddata /usr/share/tesseract/tessdata/ara.traineddata

# Run : 
streamlit run webapp.py

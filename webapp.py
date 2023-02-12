import streamlit as st
import cv2
from PIL import Image
import numpy as np
import pytesseract

languages_url = "https://github.com/tesseract-ocr/tessdata"



psm_mode = "11"
language = "eng"

def image_detect_barcodes(our_image):
    barcodes = ""
    print(psm_mode)
    tesseract_config = r"--psm " + psm_mode + " --oem 3"
    text = pytesseract.image_to_string(our_image,config=tesseract_config,lang=language)
    barcodes = text
    return [our_image,barcodes]

def realtime_video_detect_barcodes():
    pass

def main():
    """Barcode Recognition App"""

    st.title("Ywmaa's Inventions : Barcode Invention 0.2")

    st.sidebar.title('BI 0.2 Sidebar')

    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Barcode Recognition WebApp</h2>
    </div>
    </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    app_mode = st.sidebar.selectbox('Choose the App mode',
    ['Run on Image','Run on Video','About App']
    )
    psm_text = st.sidebar.selectbox('Page segmentation modes',
        [
        '0    Orientation and script detection (OSD) only.',
        '1    Automatic page segmentation with OSD.',
        '2    Automatic page segmentation, but no OSD, or OCR. (not implemented)',
        '3    Fully automatic page segmentation, but no OSD. (Default)',
        '4    Assume a single column of text of variable sizes.',
        '5    Assume a single uniform block of vertically aligned text.',
        '6    Assume a single uniform block of text.',
        '7    Treat the image as a single text line.',
        '8    Treat the image as a single word.',
        '9    Treat the image as a single word in a circle.',
        '10    Treat the image as a single character.',
        '11    Sparse text. Find as much text as possible in no particular order.',
        '12    Sparse text with OSD.',
        '13    Raw line. Treat the image as a single text line',
        ]
    )
    global psm_mode
    psm_mode = (psm_text[0] + psm_text[1]).strip()
    global language
    language = st.sidebar.selectbox('Choose the Language mode',
    ['eng','ara']
    )

    if app_mode == 'Run on Video':
        pass

    if app_mode == 'Run on Image':
        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Original Image")
            st.image(our_image)

        if st.button("Recognise"):
            result_img= image_detect_barcodes(our_image)
            st.image(result_img[0])
            st.text("Barcodes : ")
            st.text(result_img[1])


    if app_mode == 'About App':
        st.markdown('''
        # About Me \n
        Made By : ywmaa \n
        Contact :



        
        
        '''
        , unsafe_allow_html=True)




if __name__ == '__main__':
    main()




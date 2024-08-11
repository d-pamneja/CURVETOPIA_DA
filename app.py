from src.utils import * 

# Set page title
st.title('CURVETOPIA 2024 - Image Classification App')
st.subheader('This project is a part of the Curvetopia 2024 Hackathon powered by Adobe.')

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    with open("temp_pred_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    predicted_class = prediction("temp_pred_image.jpg")
    
    if(predicted_class is not None):
        if(predicted_class == 'line'):
            st.write('Predicted Class: Line')
        elif(predicted_class == 'circle'):
            st.write('Predicted Class: Circle')
        elif(predicted_class == 'ellipse'):
            st.write('Predicted Class: Ellipse')
        elif(predicted_class == 'rectangle'):
            st.write('Predicted Class: Rectangle')
        elif(predicted_class == 'rounded_rectangle'):
            st.write('Predicted Class: Rounded Rectangle')
        elif(predicted_class == 'regular_polygon'):
            st.write('Predicted Class: Regular Polygon')
        elif(predicted_class == 'star'):
            st.write('Predicted Class: Star')

    os.remove("temp_pred_image.jpg")
    
# Footer 
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        Made by Dhruv and Abhay | 
        <a href="https://www.geeksforgeeks.org/hackathon/adobe-gensolve-innovate-to-impact" target="_blank">Curvetopia 2024</a> | 
        <a href="https://www.adobe.com/" target="_blank">Adobe</a>
    </div>
    """,
    unsafe_allow_html=True,
)

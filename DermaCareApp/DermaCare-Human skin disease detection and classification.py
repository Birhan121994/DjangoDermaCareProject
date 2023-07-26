import streamlit as st
import wikipedia
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from IPython.display import  HTML
import os
# from dataprep.datasets import load_dataset
import wikipedia
import streamlit.components.v1 as com
from tensorflow.keras.applications import imagenet_utils
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit.components.v1 as com
import wikipedia
import wikipediaapi
import sqlite3
# import sys
# sys.path.insert(1, "C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/DermaCareApp/models.py") 
# from DermaCareApp.models import User

im = Image.open('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/DermaCareApp/static/images/jira_logo_icon_147274.png')
st.set_page_config(page_title="DermaCare Skin Disease Detection and Classification App", page_icon = im)

st.write("<style>.css-18ni7ap{display:none;}</style>", unsafe_allow_html=True)
st.write("<style>.block-container css-1y4p8pa egzxvld4{padding:1rem 1rem;margin-top:0px;}</style>", unsafe_allow_html = True)
hide_streamlit_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            .nav-link.active[data-v-ef155198] {
                background-color: #4b8eff;
            }
            .menu.nav-item.nav-link{
                background-color:cef8f7;
                color:white;
                font-weight:600;
            }
            .st-bz{
                font-family: "Source Sans Pro", sans-serif;
                text-align:justify;
                font-size:70px;
            }
            .edgvbvh10{
                border:1px solid rgba(52,122,204,0.73);
                background-color:#ffffff;
            }

            .edgvbvh10:hover{
                color:black;
                border:1px solid rgba(52,122,204,0.73);
                background-color:#ffffff;
            }

            .e16nr0p34{
                font-family: "Source Sans Pro", sans-serif;
                text-align:justify;
                font-size:70px;
            }

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.image('static/images/Sepe-Recovered.png', width=300)
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Browse File', 'Take Camera', 'Help'],
        icons=['steam', 'yin-yang','file-bar-graph-fill'],
        menu_icon='cast',
        default_index=0,
        orientation="vertical"
    )

if selected == "Browse File":
    st.info("Dear user, for you to get an access for medical diagnosise, you should be willing that your image / photo that you will upload will be saved within our database to be used for other researcher to be used as input.")
    file_uploader = st.file_uploader("Upload an image file", '.jpg')
    if file_uploader is not None:
        query1 = "Melanoma"
        query2 = "Eczema"
        query3 = "Atopic Dermatis"
        query4 = "Basal Cell Carcinoma"
        query5 = "melanocytic nevus"
        query6 = 'seborrheic keratosis'
        query7 = 'Psoriasis'
        query8 = 'Tinea corporis'
        query9 = 'Molluscum contagiosum'
        wp_page = wikipedia.page(query1)
        wp_page2 = wikipedia.page(query2)
        wp_page3 = wikipedia.page(query3)
        wp_page4 = wikipedia.page(query4)
        wp_page5 = wikipedia.page(query5)
        wp_page6 = wikipedia.page(query6)
        wp_page7 = wikipedia.page(query7)
        wp_page8 = wikipedia.page(query8)
        wp_page9 = wikipedia.page(query9)

        list_img_urls = wp_page.images
        list_img_urls2 = wp_page2.images
        list_img_urls3 = wp_page3.images
        list_img_urls4 = wp_page4.images
        list_img_urls5 = wp_page5.images
        list_img_urls6 = wp_page6.images
        list_img_urls7 = wp_page7.images
        list_img_urls8 = wp_page8.images
        list_img_urls9 = wp_page9.images

        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page('Melanoma')
        page_py2 = wiki_wiki.page('Eczema')
        page_py3 = wiki_wiki.page('Atopic dermatitis')
        page_py4 = wiki_wiki.page('Basal Cell Carcinoma')
        page_py5 = wiki_wiki.page('melanocytic nevus ')
        page_py6 = wiki_wiki.page('seborrheic keratosis')
        page_py7 = wiki_wiki.page('Psoriasis')
        page_py8 = wiki_wiki.page('Tinea corporis')
        page_py9 = wiki_wiki.page('Molluscum contagiosum')

        wiki_wiki = wikipediaapi.Wikipedia(
        language='am',
        extract_format=wikipediaapi.ExtractFormat.WIKI
        )
        p_wiki = wiki_wiki.page("Melanoma")
        melanoma_causes = wiki_wiki.page("Melanoma causes")
        wiki_html = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.HTML
        )
        p_html = wiki_html.page("Melanoma")

        st.image(file_uploader)
        
        loaded_model = tf.keras.models.load_model('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/SkinDiseaseModel/FinalModel.h5')
        loaded_model2 = tf.keras.models.load_model('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/SkinDiseaseModel/keras_model.h5', compile=False)
        loaded_model3 = tf.keras.models.load_model('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/SkinDiseaseModel/skin_disease_mobilenet.h5')

        class_labels = ['Atopic Dermatitis', 'BCC', 'BKL', 'Eczema', 'Melanoma', 'NV', 'Psoriasis', 'Seborrheic Keratoses', 'Tinea Ringworm Candidiasis', 'Warts Molluscum']
        img1 = image.load_img(file_uploader, target_size = (224, 224))
        img2 = image.load_img(file_uploader, target_size=(224, 224))
        img3 = image.load_img(file_uploader, target_size=(224, 224))


        test_image = image.img_to_array(img1)
        test_image2 = image.img_to_array(img2)

        test_image3 = image.img_to_array(img3)
        test_image3 /= 255.0

        test_image3 = np.expand_dims(test_image3, axis=0)
        predictions = loaded_model3.predict(test_image3)
        for i in range(len(class_labels)):
            print(f"{class_labels[i]}: {predictions[0][i]}")
        
        predicted_class_index = np.argmax(predictions)

        predicted_class_label = class_labels[predicted_class_index]

        test_image = np.expand_dims(test_image, axis=0)
        test_image2= np.expand_dims(test_image2, axis=0)

        images = np.vstack([test_image])
        images2 = np.vstack([test_image2])


        val = loaded_model.predict(images)
        val2 = loaded_model2.predict(images2)
        array2 = np.array(val2)
        array = np.array(val)
        print(array[0][0])
        print(array2[0][0])
        

        if st.button("Detect Skin Disease", key=90):

            if array[0][0] == 1:
                st.error("Skin disease has been detected.")
            elif array[0][1] == 1:
                st.success("No ,skin disease has been detected.")
            elif array[0][0] != 0 or array[0][0] != 1:
                st.info("Invalid image format is uploaded")

        # if st.button("Detect Disease Severity" , key= 78):
        #     if array2[0][0] < 0.5:
        #         st.success("Severity status: Mild . Treat yourself.")
        #     else:
        #         st.error("Severity status: Severe . Visit dermatologist.")

        if st.button("Classify Skin Disease",key=900):
            conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/DataStoreFolder/DataStoreImageDatabe.db')
            cursor = conn.cursor()
            name = "Uploaded Image From Folder"
            conn.execute("""
            INSERT INTO Uploaded_Image_Table (Name,Data) VALUES(?,?)""", (predicted_class_label, file_uploader.name))
            conn.commit()
            cursor.close()
            conn.close()
            if predicted_class_label == "Atopic Dermatits":
                st.info("Atopic Dermatits")
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-top-left-radius:0.5rem;
                            border-top-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>Atopic Dermatits</h2>
                    <h4>Also called : as eczema</h4>
                    </div>
                """, width=715, height=70)
                ta1,ta2,ta3, ta4, ta5, ta6, ta7= st.tabs(['OVERVIEW','SYMPTOMS','TREATMENTS','SPECIALISTS', 'SEVERITY','PRED STATUS','CHARTS'])  
                with ta1:
                    st.image(list_img_urls3[1])     
                    st.write(page_py3.summary[0:420])
                    col1, col2 = st.columns(2)
                    with col1:
                        # st.subheader('')
                        st.subheader('')
                        # st.subheader("Basic informations") 
                        
                        with st.expander("Causes of Atopic Dermatits"):
                            st.write(page_py3.summary[1089:1483])
                        with st.expander("Effects of Atopic dermatits"):
                            st.write(page_py3.summary[421:1089])
                        with st.expander("Prevention of Atopic dermatits"):
                            st.write("The major prevention techniques of atopic dermatits include Moisturize your skin at least twice a day, Take a daily bath or shower, Use a gentle, nonsoap cleanser and Pat dry.")
                    with col2: 
                        # st.subheader("Related conditions") 
                        taa1, taa2 , taa3 = st.tabs(['Related image1', 'Related image2', 'Related image3'])
                        with taa1:
                            st.image(list_img_urls3[0])
                        with taa2:
                            st.image(list_img_urls2[5])
                        with taa3:
                            st.image(list_img_urls2[3])
                
                with ta2:
                    page_pys = wiki_wiki.page('Melanoma')
                    ta2col1, ta2col2 = st.columns(2)
                    with ta2col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ul{
                                font-family:'Calibri';
                                font-size:19px;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Symptom of Atopic dermatits:</h2>
                            <ul>
                                <li>Dry, cracked skin.</li>
                                <li>Itchiness (pruritus)</li>
                                <li>Rash on swollen skin that varies in color depending on your skin color.</li>
                                <li>Small, raised bumps, on brown or Black skin.</li>
                                <li>Oozing and crusting.</li>
                                <li>Thickened skin.</li>
                                <li>Darkening of the skin around the eyes.</li> 
                                <li>Raw, sensitive skin from scratching.</li>
                            </ul>
                        </div>
                        """,width=370, height = 400)
                    with ta2col2:
                        st.image(list_img_urls3[0])
                        st.image(list_img_urls3[1])

                with ta3:
                    ta3col1, ta3col2 = st.columns(2)
                    with ta3col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ol{
                                font-family:'Calibri';
                                font-size:19px;
                                margin-right:2rem;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Treatment for atopic dermatits</h2>
                            <ol>
                                <li>
                                <strong>Emollients (moisturisers)</strong>
                                <p>It is mainly used every day to stop the skin becoming dry</p>
                                </li>
                                <li><strong>Topical corticosteroids</strong>
                                <p>creams and ointments used to reduce swelling and redness during flare-ups.</p>
                                </li>
                                <li><strong>Antihistamines</strong>
                                <p>Antihistamines are a type of medicine that block the effects of a substance in the blood called histamine.They can help relieve the itching associated with atopic eczema.</p>
                                </li>
                                <li><strong>Bandages and wet wraps</strong>
                                <p>
                                These can either be used over emollients or with topical corticosteroids to prevent scratching, allow the skin underneath to heal, and stop the skin drying out.
                                </p>
                                </li>
                            </ol>
                        </div>
                        """,width=380, height = 700)
                    
                    with ta3col2:
                        st.header("")
                        st.header("")
                        st.image("media/latestnews_images/b1-370x270.jpg")
                        st.image("media/latestnews_images/b3-370x270.jpg")
                with ta4:
                    conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/db.sqlite3')
                    cursor = conn.cursor()
                    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
                    with col1:
                        st.write("Username")
                    with col2:
                        st.write("First name")
                    with col3:
                        st.write("Last name")
                    with col4:
                        st.write("Email")
                    with col5:
                        st.write("Speciality")
                    with col6:
                        st.write("Phone")
                    with col7:
                        st.write("Location")
                    for row in cursor.execute('SELECT username , first_name , last_name , email,speciality, phone, location FROM DermaCareApp_user WHERE speciality == "Atopic dermatits" '):
                        col1, col2, col3, col4, col5, col6, col7  = st.columns(7)
                        with col1:
                            st.write(row[0])
                        with col2:
                            st.write(row[1])
                        with col3:
                            st.write(row[2])

                        with col4:
                            st.write(row[3])
                        with col5:
                            st.write(row[4])
                        with col6:
                            st.write(row[5])
                        with col7:st.write(row[6])
                    # conn.execute("""
                    # INSERT INTO my_table (name,data) VALUES(?,?)""", (name, file_uploader.name))

                    conn.commit()
                    cursor.close()
                    conn.close()

                with ta5:
                    if array2[0][0] < 0.5:
                        st.success("Severity status: Mild .")
                        st.success("Please try to treat yourself with the treatement methods stated in recommendation.")
                    else:
                        st.error("Severity status: Severe.")
                        st.error("Warning: Please try to contact or make an appointement with the dermatologist recommended in the speciality recommendation provider as soon as possible")
     
                with ta6:
                    for i in range(len(class_labels)):
                        st.write(f"{class_labels[i]}  : {(predictions[0][i])*100}%")
                with ta7:
                    # Flatten the predictions array
                    predictions_flat = np.array(predictions).flatten()

                    predictions_2d = np.array(predictions).reshape(1, -1)

                    fig3, ax3 = plt.subplots()
                    ax3.scatter(class_labels, predictions)
                    ax3.set_xlabel('Class labels')
                    ax3.set_ylabel('Predictions')
                    ax3.set_xticklabels(class_labels, fontsize=6)
                    ax3.set_title('Scatter plot of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig3)
                    # fig2, ax2 = plt.subplots()
                    # im = ax2.imshow(predictions_2d, cmap='YlGn')
                    # ax2.set_xticks(np.arange(len(class_labels)))
                    # ax2.set_yticks([0])
                    # ax2.set_xticklabels(class_labels, fontsize=5)
                    # ax2.set_title('Heatmap of predictions')

                    # Add the values to the heatmap
                    # for i in range(len(class_labels)):
                    #     for j in range(1):
                    #         text = ax2.text(i, j, predictions_2d[j, i], ha='center', va='center', color='black')

                    
                    # st.pyplot(fig2)

                    # Create a bar chart
                    fig, ax = plt.subplots()
                    ax.bar(np.repeat(class_labels, len(predictions)), predictions_flat)
                    ax.set_xlabel('Class labels')
                    ax.set_ylabel('Predictions')
                    ax.set_xticklabels(class_labels, fontsize=6)
                    ax.set_title('Bar chart of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig)

                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-bottom-left-radius:0.5rem;
                            border-bottom-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>DermaCare</h2>
                    <h4>Human Skin Disease Classifier</h4>
                    </div>
                """, width=715, height=70)

            elif predicted_class_label == "BCC":
                st.info("BCC")
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-top-left-radius:0.5rem;
                            border-top-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>Basal Cell Carcinoma</h2>
                    <h4>Also called : as BCC</h4>
                    </div>
                """, width=715, height=70)

                ta1,ta2,ta3, ta4 , ta5 ,ta6, ta7= st.tabs(['OVERVIEW','SYMPTOMS','TREATMENTS','SPECIALISTS', 'SEVERITY','PRED STATUS','CHARTS'])  
                with ta1:
                    st.image(list_img_urls4[0])     
                    st.write(page_py4.summary[0:401])
                    col1, col2 = st.columns(2)
                    with col1:
                        # st.subheader('')
                        st.subheader('')
                        # st.subheader("Basic informations") 
                        
                        with st.expander("Causes of BCC"):
                            st.write(page_py4.summary[401:692])
                        with st.expander("Effects of BCC"):
                            st.write("It can also look like a red, scaly patch. There's sometimes some brown or black pigment within the patch. The lump slowly gets bigger and may become crusty, bleed or develop into a painless ulcer. Basal cell carcinoma does not usually spread to other parts of the body.")
                        with st.expander("Prevention of BCC"):
                            st.write('Basal-cell carcinoma is a common skin cancer and occurs mainly in fair-skinned patients with a family history of this cancer. Sunlight is a factor in about two-thirds of these cancers; therefore, doctors recommend sunscreens with at least SPF 30. ')
                    with col2: 
                        # st.subheader("Related conditions") 
                        taa1, taa2 , taa3 = st.tabs(['Related image1', 'Related image2', 'Related image3'])
                        with taa1:
                            st.image(list_img_urls4[2])
                        with taa2:
                            st.image(list_img_urls4[3])
                        with taa3:
                            st.image(list_img_urls4[4])
                
                with ta2:
                    page_pys = wiki_wiki.page('Melanoma')
                    ta2col1, ta2col2 = st.columns(2)
                    with ta2col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ul{
                                font-family:'Calibri';
                                font-size:19px;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Symptom of Basal Cell Carcinoma:</h2>
                            <ul>
                                <li>A shiny, skin-colored bump</li>
                                <li>A brown, black or blue lesion</li>
                                <li>A flat, scaly patch</li>
                                <li>A white, waxy, scar-like lesion</li>
                            </ul>
                        </div>
                        """,width=370, height = 400)
                    with ta2col2:
                        st.header("")
                        st.image(list_img_urls4[4])
                with ta3:
                    ta3col1, ta3col2 = st.columns(2)
                    with ta3col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ol{
                                font-family:'Calibri';
                                font-size:19px;
                                margin-right:2rem;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Treatment for BCC</h2>
                            <ol>
                                <li>
                                <strong>Electrosurgery</strong>
                                <p>Curettage and electrodesiccation can be effective for most small BCC lesions. In these instances, the procedure has cure rates close to 95 percent.</p>
                                </li>
                                <li><strong>Mohs surgery</strong>
                                <p>Mohs surgery is performed during a single visit, in stages. The surgeon removes the visible tumor and a very small margin of tissue around and beneath the tumor site. The surgeon color-codes the tissue and draws a map correlated to the patient’s surgical site.</p>
                                </li>
                                <li><strong>Excisional surgery</strong>
                                <p>For small, early BCCs that have not spread, excisional surgery is frequently the only treatment required. Cure rates are above 95 percent in most body areas, similar to those of curettage and electrodesiccation.</p>
                                </li>
                                <li><strong>Radiation therapy</strong>
                                <p>
                            it is primarily used for BCCs that are hard to treat with surgery, and in elderly patients or people in poor health for whom surgery is not advised.
                                </p>
                                </li>
                            </ol>
                        </div>
                        """,width=380, height = 700)
                    
                    with ta3col2:
                        st.header("")
                        st.header("")
                        st.image("DermaCareProject/media/latestnews_images/b1-370x270.jpg")
                        st.image("DermaCareProject/media/latestnews_images/b3-370x270.jpg")
                with ta4:
                    conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/db.sqlite3')
                    cursor = conn.cursor()
                    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
                    with col1:
                        st.write("Username")
                    with col2:
                        st.write("First name")
                    with col3:
                        st.write("Last name")
                    with col4:
                        st.write("Email")
                    with col5:
                        st.write("Speciality")
                    with col6:
                        st.write("Phone")
                    with col7:
                        st.write("Location")
                    for row in cursor.execute('SELECT username , first_name , last_name , email,speciality, phone, location FROM DermaCareApp_user WHERE speciality == "Basal Cell Carcinoma" '):
                        col1, col2, col3, col4, col5, col6, col7  = st.columns(7)
                        with col1:
                            st.write(row[0])
                        with col2:
                            st.write(row[1])
                        with col3:
                            st.write(row[2])

                        with col4:
                            st.write(row[3])
                        with col5:
                            st.write(row[4])
                        with col6:
                            st.write(row[5])
                        with col7:
                            st.write(row[6])
                    # conn.execute("""
                    # INSERT INTO my_table (name,data) VALUES(?,?)""", (name, file_uploader.name))

                    conn.commit()
                    cursor.close()
                    conn.close()

                with ta5:
                    if array2[0][0] < 0.5:
                        st.success("Severity status: Mild .")
                        st.success("Please try to treat yourself with the treatement methods stated in recommendation.")
                    else:
                        st.error("Severity status: Severe.")
                        st.error("Warning: Please try to contact or make an appointement with the dermatologist recommended in the speciality recommendation provider as soon as possible")
     
                with ta6:
                    for i in range(len(class_labels)):
                        st.write(f"{class_labels[i]}  : {(predictions[0][i])*100}%")
                with ta7:
                    # Flatten the predictions array
                    predictions_flat = np.array(predictions).flatten()

                    predictions_2d = np.array(predictions).reshape(1, -1)

                    fig3, ax3 = plt.subplots()
                    ax3.scatter(class_labels, predictions)
                    ax3.set_xlabel('Class labels')
                    ax3.set_ylabel('Predictions')
                    ax3.set_xticklabels(class_labels, fontsize=6)
                    ax3.set_title('Scatter plot of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig3)
                    # fig2, ax2 = plt.subplots()
                    # im = ax2.imshow(predictions_2d, cmap='YlGn')
                    # ax2.set_xticks(np.arange(len(class_labels)))
                    # ax2.set_yticks([0])
                    # ax2.set_xticklabels(class_labels, fontsize=5)
                    # ax2.set_title('Heatmap of predictions')

                    # Add the values to the heatmap
                    # for i in range(len(class_labels)):
                    #     for j in range(1):
                    #         text = ax2.text(i, j, predictions_2d[j, i], ha='center', va='center', color='black')

                    
                    # st.pyplot(fig2)

                    # Create a bar chart
                    fig, ax = plt.subplots()
                    ax.bar(np.repeat(class_labels, len(predictions)), predictions_flat)
                    ax.set_xlabel('Class labels')
                    ax.set_ylabel('Predictions')
                    ax.set_xticklabels(class_labels, fontsize=6)
                    ax.set_title('Bar chart of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig)

                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-bottom-left-radius:0.5rem;
                            border-bottom-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>DermaCare</h2>
                    <h4>Human Skin Disease Classifier</h4>
                    </div>
                """, width=715, height=70)

            elif predicted_class_label == "BKL":
                st.info("BKL")
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-top-left-radius:0.5rem;
                            border-top-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>Benign keratosis</h2>
                    <h4>Also called : as BKL skin lesions</h4>
                    </div>
                """, width=715, height=70)
                ta1,ta2,ta3, ta4 , ta5, ta6, ta7= st.tabs(['OVERVIEW','SYMPTOMS','TREATMENTS','SPECIALISTS', 'SEVERITY','PRED STATUS','CHART'])  
                with ta1:
                    st.image(list_img_urls6[1])     
                    st.write(page_py6.summary[0:356])
                    col1, col2 = st.columns(2)
                    with col1:
                        # st.subheader('')
                        st.subheader('')
                        # st.subheader("Basic informations") 
                        
                        with st.expander("Causes of Benign keratosis"):
                            st.write("The first is age: seborrheic keratoses are especially common in adults over 50, and they tend to multiply as people get older. Some studies suggest that sun exposure may increase their occurrence. They also appear more frequently in families, which suggests that genetics may play a role. They are not viral or bacterial. They don’t spread and they aren’t contagious.")
                        with st.expander("Effects of Benign keratosis"):
                            st.write("They usually don’t have an impact, but people sometimes report:Itching,Irritation from friction,Bleeding.")
                        with st.expander("Prevention of Benign keratosis"):
                            st.write('You should always have new skin growths clinically diagnosed to make sure they aren’t cancerous. Different kinds of skin growths can be hard to tell apart from each other. If your healthcare provider is in any doubt about your growth, they might want to remove it for biopsy.')
                    with col2: 
                        # st.subheader("Related conditions") 
                        taa1, taa2 , taa3 = st.tabs(['Related image1', 'Related image2', 'Related image3'])
                        with taa1:
                            st.image(list_img_urls4[2])
                        with taa2:
                            st.image(list_img_urls4[3])
                        with taa3:
                            st.image(list_img_urls4[4])
                
                with ta2:
                    page_pys = wiki_wiki.page('Melanoma')
                    ta2col1, ta2col2 = st.columns(2)
                    with ta2col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ul{
                                font-family:'Calibri';
                                font-size:19px;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                                font-size:19px;
                                width:95%;
                                line-height:
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Symptom of Bengin keratosis</h2>
                            <p>Benign moles are usually brown, tan, pink or black (especially on dark-colored skin). They are circular or oval and are usually small (commonly between 1–3 mm), though some can be larger than the size of a typical pencil eraser (>5 mm). Some moles produce dark, coarse hair.</p>
                        </div>
                        """,width=370, height = 300)
                    with ta2col2:
                        st.header("")
                        st.image(list_img_urls4[4])
                with ta3:
                    ta3col1, ta3col2 = st.columns(2)
                    with ta3col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ol{
                                font-family:'Calibri';
                                font-size:19px;
                                margin-right:2rem;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Treatment for Benign keratosis</h2>
                            <ol>
                                <li>
                                <strong>Freezing the growth</strong>
                                <p>Freezing a growth with liquid nitrogen (cryotherapy) can be an effective way to remove a seborrheic keratosis. It doesn't always work on raised, thicker growths.
                                This method carries the risk of permanent loss of pigment, especially on Black or brown skin.</p>
                                </li>
                                <li><strong>Scraping (curettage) </strong>
                                <p>First your doctor will numb the area and then use a scalpel blade to remove the growth. Sometimes shaving or scraping is used along with cryosurgery to treat thinner or flat growths.</p>
                                </li>
                                <li><strong>Burning with an electric current</strong>
                                <p>First your doctor will numb the area and then destroy the growth with electrocautery. This method can be used alone or with scraping, especially when removing thicker growths.</p>
                                </li>
                            </ol>
                        </div>
                        """,width=380, height = 700)
                    
                    with ta3col2:
                        st.header("")
                        st.header("")
                        st.image("DermaCareProject/media/latestnews_images/b1-370x270.jpg")
                        st.image("DermaCareProject/media/latestnews_images/b3-370x270.jpg")
                with ta4:
                    conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/db.sqlite3')
                    cursor = conn.cursor()
                    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
                    with col1:
                        st.write("Username")
                    with col2:
                        st.write("First name")
                    with col3:
                        st.write("Last name")
                    with col4:
                        st.write("Email")
                    with col5:
                        st.write("Speciality")
                    with col6:
                        st.write("Phone")
                    with col7:
                        st.write("Location")
                    for row in cursor.execute('SELECT username , first_name , last_name , email,speciality, phone, location FROM DermaCareApp_user WHERE speciality == "Benign keratosis" '):
                        col1, col2, col3, col4, col5, col6, col7  = st.columns(7)
                        with col1:
                            st.write(row[0])
                        with col2:
                            st.write(row[1])
                        with col3:
                            st.write(row[2])

                        with col4:
                            st.write(row[3])
                        with col5:
                            st.write(row[4])
                        with col6:
                            st.write(row[5])
                        with col7:
                            st.write(row[6])
                    # conn.execute("""
                    # INSERT INTO my_table (name,data) VALUES(?,?)""", (name, file_uploader.name))

                    conn.commit()
                    cursor.close()
                    conn.close()

                with ta5:
                    if array2[0][0] < 0.5:
                        st.success("Severity status: Mild .")
                        st.success("Please try to treat yourself with the treatement methods stated in recommendation.")
                    else:
                        st.error("Severity status: Severe.")
                        st.error("Warning: Please try to contact or make an appointement with the dermatologist recommended in the speciality recommendation provider as soon as possible")
     
                with ta6:
                    for i in range(len(class_labels)):
                        st.write(f"{class_labels[i]}  : {(predictions[0][i])*100}%")
                with ta7:
                    # Flatten the predictions array
                    predictions_flat = np.array(predictions).flatten()

                    predictions_2d = np.array(predictions).reshape(1, -1)

                    fig3, ax3 = plt.subplots()
                    ax3.scatter(class_labels, predictions)
                    ax3.set_xlabel('Class labels')
                    ax3.set_ylabel('Predictions')
                    ax3.set_xticklabels(class_labels, fontsize=6)
                    ax3.set_title('Scatter plot of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig3)
                    # fig2, ax2 = plt.subplots()
                    # im = ax2.imshow(predictions_2d, cmap='YlGn')
                    # ax2.set_xticks(np.arange(len(class_labels)))
                    # ax2.set_yticks([0])
                    # ax2.set_xticklabels(class_labels, fontsize=5)
                    # ax2.set_title('Heatmap of predictions')

                    # Add the values to the heatmap
                    # for i in range(len(class_labels)):
                    #     for j in range(1):
                    #         text = ax2.text(i, j, predictions_2d[j, i], ha='center', va='center', color='black')

                    
                    # st.pyplot(fig2)

                    # Create a bar chart
                    fig, ax = plt.subplots()
                    ax.bar(np.repeat(class_labels, len(predictions)), predictions_flat)
                    ax.set_xlabel('Class labels')
                    ax.set_ylabel('Predictions')
                    ax.set_xticklabels(class_labels, fontsize=6)
                    ax.set_title('Bar chart of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig)

                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-bottom-left-radius:0.5rem;
                            border-bottom-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>DermaCare</h2>
                    <h4>Human Skin Disease Classifier</h4>
                    </div>
                """, width=715, height=70)

            elif predicted_class_label == "Eczema":
                st.info("Eczema")
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-top-left-radius:0.5rem;
                            border-top-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>Eczema</h2>
                    <h4>Also called : skin inflammation</h4>
                    </div>
                """, width=715, height=70)
                ta1,ta2,ta3, ta4 , ta5,ta6, ta7= st.tabs(['OVERVIEW','SYMPTOMS','TREATMENTS','SPECIALISTS', 'SEVERITY','PRED STATUS','CHARTS'])  
                with ta1:
                    st.image(list_img_urls2[1])     
                    st.write(page_py2.summary[0:380])
                    col1, col2 = st.columns(2)
                    with col1:
                        # st.subheader('')
                        st.subheader('')
                        # st.subheader("Basic informations") 
                        
                        with st.expander("Causes of Eczema"):
                            st.write(page_py2.summary[380:600])
                        with st.expander("Effects of Eczema "):
                            st.write(page_py2.summary[612:810])
                        with st.expander("Prevention of Eczema "):
                            st.write(page_py2.summary[810:1218])
                    with col2: 
                        # st.subheader("Related conditions") 
                        taa1, taa2 , taa3 = st.tabs(['Related image1', 'Related image2', 'Related image3'])
                        with taa1:
                            st.image(list_img_urls2[4])
                        with taa2:
                            st.image(list_img_urls2[5])
                        with taa3:
                            st.image(list_img_urls2[3])
                
                with ta2:
                    page_pys = wiki_wiki.page('Melanoma')
                    ta2col1, ta2col2 = st.columns(2)
                    with ta2col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ul{
                                font-family:'Calibri';
                                font-size:19px;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Major Symptom of Eczema:</h2>
                            <ul>
                                <li>Dry, cracked skin.</li>
                                <li>Itchiness (pruritus)</li>
                                <li>Rash on swollen skin that varies in color depending on your skin color.</li>
                                <li>Small, raised bumps, on brown or Black skin.</li>
                                <li>Oozing and crusting.</li>
                                <li>Thickened skin.</li>
                                <li>Darkening of the skin around the eyes.</li> 
                                <li>Raw, sensitive skin from scratching.</li>
                            </ul>
                        </div>
                        """,width=370, height = 400)
                    with ta2col2:
                        st.image(list_img_urls2[1])
                        st.image(list_img_urls2[5])

                with ta3:
                    ta3col1, ta3col2 = st.columns(2)
                    with ta3col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ol{
                                font-family:'Calibri';
                                font-size:19px;
                                margin-right:2rem;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Treatment for Eczema</h2>
                            <ol>
                                <li>
                                <strong>Emollients (moisturisers)</strong>
                                <p>It is mainly used every day to stop the skin becoming dry</p>
                                </li>
                                <li><strong>Topical corticosteroids</strong>
                                <p>creams and ointments used to reduce swelling and redness during flare-ups.</p>
                                </li>
                                <li><strong>Antihistamines</strong>
                                <p>Antihistamines are a type of medicine that block the effects of a substance in the blood called histamine.They can help relieve the itching associated with atopic eczema.</p>
                                </li>
                                <li><strong>Bandages and wet wraps</strong>
                                <p>
                                These can either be used over emollients or with topical corticosteroids to prevent scratching, allow the skin underneath to heal, and stop the skin drying out.
                                </p>
                                </li>
                            </ol>
                        </div>
                        """,width=380, height = 700)
                    
                    with ta3col2:
                        st.header("")
                        st.header("")
                        st.image("https://www.sridevihospital.com/wp-content/uploads/2020/01/dermatologist.jpg")
                        st.image("https://www.cozmoderm.com/wp-content/uploads/2023/02/skin-special.jpg")
                with ta4:
                    conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/db.sqlite3')
                    cursor = conn.cursor()
                    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
                    with col1:
                        st.write("Username")
                    with col2:
                        st.write("First name")
                    with col3:
                        st.write("Last name")
                    with col4:
                        st.write("Email")
                    with col5:
                        st.write("Speciality")
                    with col6:
                        st.write("Phone")
                    with col7:
                        st.write("Location")
                    for row in cursor.execute('SELECT username , first_name , last_name , email,speciality, phone, location FROM DermaCareApp_user WHERE speciality == "Eczema" '):
                        col1, col2, col3, col4, col5, col6, col7  = st.columns(7)
                        with col1:
                            st.write(row[0])
                        with col2:
                            st.write(row[1])
                        with col3:
                            st.write(row[2])

                        with col4:
                            st.write(row[3])
                        with col5:
                            st.write(row[4])
                        with col6:
                            st.write(row[5])
                        with col7:st.write(row[6])
                    # conn.execute("""
                    # INSERT INTO my_table (name,data) VALUES(?,?)""", (name, file_uploader.name))

                    conn.commit()
                    cursor.close()
                    conn.close()

                with ta5:
                    if array2[0][0] < 0.5:
                        st.success("Severity status: Mild .")
                        st.success("Please try to treat yourself with the treatement methods stated in recommendation.")
                    else:
                        st.error("Severity status: Severe.")
                        st.error("Warning: Please try to contact or make an appointement with the dermatologist recommended in the speciality recommendation provider as soon as possible")
     
                with ta6:
                    for i in range(len(class_labels)):
                        st.write(f"{class_labels[i]}  : {(predictions[0][i])*100}%")
                with ta7:
                    # Flatten the predictions array
                    predictions_flat = np.array(predictions).flatten()

                    predictions_2d = np.array(predictions).reshape(1, -1)

                    fig3, ax3 = plt.subplots()
                    ax3.scatter(class_labels, predictions)
                    ax3.set_xlabel('Class labels')
                    ax3.set_ylabel('Predictions')
                    ax3.set_xticklabels(class_labels, fontsize=6)
                    ax3.set_title('Scatter plot of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig3)
                    # fig2, ax2 = plt.subplots()
                    # im = ax2.imshow(predictions_2d, cmap='YlGn')
                    # ax2.set_xticks(np.arange(len(class_labels)))
                    # ax2.set_yticks([0])
                    # ax2.set_xticklabels(class_labels, fontsize=5)
                    # ax2.set_title('Heatmap of predictions')

                    # Add the values to the heatmap
                    # for i in range(len(class_labels)):
                    #     for j in range(1):
                    #         text = ax2.text(i, j, predictions_2d[j, i], ha='center', va='center', color='black')

                    
                    # st.pyplot(fig2)

                    # Create a bar chart
                    fig, ax = plt.subplots()
                    ax.bar(np.repeat(class_labels, len(predictions)), predictions_flat)
                    ax.set_xlabel('Class labels')
                    ax.set_ylabel('Predictions')
                    ax.set_xticklabels(class_labels, fontsize=6)
                    ax.set_title('Bar chart of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig)

                com.html("""
                        <style>
                            .Header_box{
                                display:flex;
                                flex-direction:column;
                                background:rgba(52,122,204,0.73);
                                color:white;
                                font-family:Calibri;
                                border:1px solid rgba(52,122,204,0.73);
                                border-bottom-left-radius:0.5rem;
                                border-bottom-right-radius:0.5rem;
                                padding-left:10px;
                                padding-top:5px;
                                padding-bottom:5px;
                            }
                            h2{
                                margin-top:0rem;
                                margin-bottom:0rem;
                                font-weight:400;
                            }
                            h4{
                                margin-top:0rem;
                                font-weight:400;
                                margin-bottom:0rem;
                            }
                        </style>
                        <div class="Header_box">
                        <h2>DermaCare</h2>
                        <h4>Human Skin Disease Classifier</h4>
                        </div>
                    """, width=715, height=70)

                 
            elif predicted_class_label == "Melanoma":
                st.info("Melanoma")
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-top-left-radius:0.5rem;
                            border-top-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>Melanoma</h2>
                    <h4>Also called : malignant melanoma</h4>
                    </div>
                """, width=715, height=70)
                ta1,ta2,ta3, ta4 , ta5, ta6, ta7= st.tabs(['OVERVIEW','SYMPTOMS','TREATMENTS','SPECIALISTS','SEVERITY', 'PRED STATUS','CHART'])  
                with ta1:
                    st.image(list_img_urls[11])     
                    st.write(page_py.summary[0:541])
                    col1, col2 = st.columns(2)
                    with col1:
                        # st.subheader('')
                        st.subheader('')
                        # st.subheader("Basic informations") 
                        
                        with st.expander("Causes of Melanoma"):
                            st.write(p_html.summary[596:1000])
                        with st.expander("Effects of Melanoma "):
                            st.write(page_py.summary[1779:])
                        with st.expander("Prevention of Melanoma "):
                            st.write('Prevention There is no evidence to support or refute adult population screening for malignant melanoma.Ultraviolet radiation Minimizing exposure to sources of ultraviolet radiation (the sun and sunbeds), following sun protection measures and wearing sun protective clothing (long-sleeved shirts, long trousers, and broad-brimmed hats) can offer protection. Using artificial light for tanning was once believed to help prevent skin cancers, but it can actually lead to an increased incidence of melanomas.UV nail lamps, which are used in nail salons to dry nail polish, are another common and widespread source of UV radiation that could be avoided.')
                    with col2: 
                        # st.subheader("Related conditions") 
                        taa1, taa2 , taa3 = st.tabs(['Related image1', 'Related image2', 'Related image3'])
                        with taa1:
                            st.image(list_img_urls[27])
                        with taa2:
                            st.image(list_img_urls[25])
                        with taa3:
                            st.image(list_img_urls[30])
                
                with ta2:
                    page_pys = wiki_wiki.page('Melanoma')
                    ta2col1, ta2col2 = st.columns(2)
                    with ta2col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ul{
                                font-family:'Calibri';
                                font-size:19px;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Major Symptom of Melanoma are the following:</h2>
                            <ul>
                                <li>Hard or swollen lymph nodes.</li>
                                <li>Hard lump on your skin.</li>
                                <li>Unexplained pain.</li>
                                <li>Feeling very tired or unwell.</li>
                                <li>Unexplained weight loss.</li>
                                <li>Yellowing of eyes and skin (jaundice)</li>
                                <li>Build up of fluid in your tummy (abdomen) - ascites.</li> 
                                <li>Tummy pain.</li>
                            </ul>
                        </div>
                        """,width=370, height = 400)
                    with ta2col2:
                        st.image(list_img_urls[12])
                        st.image(list_img_urls[12])

                with ta3:
                    ta3col1, ta3col2 = st.columns(2)
                    with ta3col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ol{
                                font-family:'Calibri';
                                font-size:19px;
                                margin-right:2rem;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Treatment for melanoma</h2>
                            <ol>
                                <li>
                                <strong>Surgery</strong>
                                <p>You may need surgery if the melanoma has spread to other areas of your body or if it has come back again after being removed.</p>
                                </li>
                                <li><strong>Radiotherapy</strong>
                                <p>Radiotherapy is sometimes used to reduce the size of large melanomas and help control and relieve your symptoms.</p>
                                </li>
                                <li><strong>Chemotherapy</strong>
                                <p>Chemotherapy uses medicines to kill cancer cells.It's sometimes used to treat advanced melanoma (where it's spread to another part of the body).</p>
                                </li>
                                <li><strong>Targeted medicines and immunotherapy</strong>
                                <p>
                                Targeted medicines aim to stop the cancer growing.Immunotherapy medicines help your immune system find and kill the cancer cells.
                                </p>
                                </li>
                            </ol>
                        </div>
                        """,width=380, height = 700)
                    
                    with ta3col2:
                        st.header("")
                        st.header("")
                        st.image("https://www.sridevihospital.com/wp-content/uploads/2020/01/dermatologist.jpg")
                        st.image("https://www.cozmoderm.com/wp-content/uploads/2023/02/skin-special.jpg")
                with ta4:
                    conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/db.sqlite3')
                    cursor = conn.cursor()
                    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
                    with col1:
                        st.write("Username")
                    with col2:
                        st.write("First name")
                    with col3:
                        st.write("Last name")
                    with col4:
                        st.write("Email")
                    with col5:
                        st.write("Speciality")
                    with col6:
                        st.write("Phone")
                    with col7:
                        st.write("Location")
                    for row in cursor.execute('SELECT username , first_name , last_name , email,speciality, phone, location FROM DermaCareApp_user WHERE speciality == "Melanoma" '):
                        col1, col2, col3, col4, col5, col6, col7  = st.columns(7)
                        with col1:
                            st.write(row[0])
                        with col2:
                            st.write(row[1])
                        with col3:
                            st.write(row[2])

                        with col4:
                            st.write(row[3])
                        with col5:
                            st.write(row[4])
                        with col6:
                            st.write(row[5])
                        with col7:st.write(row[6])
                    # conn.execute("""
                    # INSERT INTO my_table (name,data) VALUES(?,?)""", (name, file_uploader.name))

                    conn.commit()
                    cursor.close()
                    conn.close()



                with ta5:
                    if array2[0][0] < 0.5:
                        st.success("Severity status: Mild .")
                        st.success("Please try to treat yourself with the treatement methods stated in recommendation.")
                    else:
                        st.error("Severity status: Severe.")
                        st.error("Warning: Please try to contact or make an appointement with the dermatologist recommended in the speciality recommendation provider as soon as possible")
     
                with ta6:
                    for i in range(len(class_labels)):
                        st.write(f"{class_labels[i]}  : {(predictions[0][i])*100}%")
                with ta7:
                    # Flatten the predictions array
                    predictions_flat = np.array(predictions).flatten()

                    predictions_2d = np.array(predictions).reshape(1, -1)

                    fig3, ax3 = plt.subplots()
                    ax3.scatter(class_labels, predictions)
                    ax3.set_xlabel('Class labels')
                    ax3.set_ylabel('Predictions')
                    ax3.set_xticklabels(class_labels, fontsize=6)
                    ax3.set_title('Scatter plot of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig3)
                    # fig2, ax2 = plt.subplots()
                    # im = ax2.imshow(predictions_2d, cmap='YlGn')
                    # ax2.set_xticks(np.arange(len(class_labels)))
                    # ax2.set_yticks([0])
                    # ax2.set_xticklabels(class_labels, fontsize=5)
                    # ax2.set_title('Heatmap of predictions')

                    # Add the values to the heatmap
                    # for i in range(len(class_labels)):
                    #     for j in range(1):
                    #         text = ax2.text(i, j, predictions_2d[j, i], ha='center', va='center', color='black')

                    
                    # st.pyplot(fig2)

                    # Create a bar chart
                    fig, ax = plt.subplots()
                    ax.bar(np.repeat(class_labels, len(predictions)), predictions_flat)
                    ax.set_xlabel('Class labels')
                    ax.set_ylabel('Predictions')
                    ax.set_xticklabels(class_labels, fontsize=6)
                    ax.set_title('Bar chart of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig)

                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-bottom-left-radius:0.5rem;
                            border-bottom-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>DermaCare</h2>
                    <h4>Human Skin Disease Classifier</h4>
                    </div>
                """, width=715, height=70)

            elif predicted_class_label == "NV":
                st.info("NV")
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-top-left-radius:0.5rem;
                            border-top-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>Melanocytic navy</h2>
                    <h4>Also called : as NV</h4>
                    </div>
                """, width=715, height=70)
                ta1,ta2,ta3, ta4 , ta5, ta6, ta7= st.tabs(['OVERVIEW','SYMPTOMS','TREATMENTS','SPECIALISTS', 'SEVERITY','PRED STATUS', 'CHART'])  
                with ta1:
                    st.image(list_img_urls5[5])     
                    st.write(page_py5.summary[0:356])
                    col1, col2 = st.columns(2)
                    with col1:
                        # st.subheader('')
                        st.subheader('')
                        # st.subheader("Basic informations") 
                        
                        with st.expander("Causes of Melanocytic navy"):
                            st.write("The cause is not clearly understood, but is thought to be caused by a defect in embryologic development. This is in the first twelve weeks of pregnancy. The defect is thought to cause a proliferation of melanocytes.Genetics and sunlight can be considered as other causes.")
                        with st.expander("Effects of Melanocytic navy"):
                            st.write("Change in color,Change in shape,Rapid increase in size,Itching or pain,Bleeding or crusting,New raised or bumpy areas are the major effects of melanocytic navi.")
                        with st.expander("Prevention of Melanocytic navy"):
                            st.write('Avoid spending time in the sun and avoid tanning beds,Wear sunscreen every day when outdoors with an SPF of 30 or more,Wear protective clothing when you are in the sun,Check your own skin frequently,Visit your dermatologist regularly to have skin exams are the major prevention mechanisms.')
                    with col2: 
                        # st.subheader("Related conditions") 
                        taa1, taa2 , taa3 = st.tabs(['Related image1', 'Related image2', 'Related image3'])
                        with taa1:
                            st.image(list_img_urls5[2])
                        with taa2:
                            st.image(list_img_urls5[3])
                        with taa3:
                            st.image(list_img_urls5[4])
                
                with ta2:
                    page_pys = wiki_wiki.page('Melanoma')
                    ta2col1, ta2col2 = st.columns(2)
                    with ta2col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ul{
                                font-family:'Calibri';
                                font-size:19px;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                                font-size:19px;
                                width:95%;
                                line-height:
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Symptom of Melanocytic navi</h2>
                            <p>Benign moles are usually brown, tan, pink or black (especially on dark-colored skin). They are circular or oval and are usually small (commonly between 1–3 mm), though some can be larger than the size of a typical pencil eraser (>5 mm). Some moles produce dark, coarse hair.</p>
                        </div>
                        """,width=370, height = 300)
                    with ta2col2:
                        st.header("")
                        st.image(list_img_urls4[4])
                with ta3:
                    ta3col1, ta3col2 = st.columns(2)
                    with ta3col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ol{
                                font-family:'Calibri';
                                font-size:19px;
                                margin-right:2rem;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Treatment for NV</h2>
                            <ol>
                                <li>
                                <strong>Laser treatment</strong>
                                <p>Controlled beam of light are used to cause the removal of the mark but inducing newer collagen production. </p>
                                </li>
                                <li><strong>Excision biopsy</strong>
                                <p>This treatment can be used when the mole is flat and suspicious-looking. In this method a punch device or a scalpel is used to cut-out the mole along with a part of the surrounding skin.</p>
                                </li>
                                <li><strong>Shave biopsy</strong>
                                <p>This treatment can be used if you have a protruding mole. In this method, the area around the mole is first numbed, and then a small blade is used to cut the mole.</p>
                                </li>
                            </ol>
                        </div>
                        """,width=380, height = 600)
                    
                    with ta3col2:
                        st.header("")
                        st.header("")
                        st.image("https://www.sridevihospital.com/wp-content/uploads/2020/01/dermatologist.jpg")
                        st.image("https://www.cozmoderm.com/wp-content/uploads/2023/02/skin-special.jpg")
                with ta4:
                    conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/db.sqlite3')
                    cursor = conn.cursor()
                    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
                    with col1:
                        st.write("Username")
                    with col2:
                        st.write("First name")
                    with col3:
                        st.write("Last name")
                    with col4:
                        st.write("Email")
                    with col5:
                        st.write("Speciality")
                    with col6:
                        st.write("Phone")
                    with col7:
                        st.write("Location")
                    for row in cursor.execute('SELECT username , first_name , last_name , email,speciality, phone, location FROM DermaCareApp_user WHERE speciality == "Melanocytic nevi" '):
                        col1, col2, col3, col4, col5, col6, col7  = st.columns(7)
                        with col1:
                            st.write(row[0])
                        with col2:
                            st.write(row[1])
                        with col3:
                            st.write(row[2])

                        with col4:
                            st.write(row[3])
                        with col5:
                            st.write(row[4])
                        with col6:
                            st.write(row[5])
                        with col7:
                            st.write(row[6])
                    # conn.execute("""
                    # INSERT INTO my_table (name,data) VALUES(?,?)""", (name, file_uploader.name))

                    conn.commit()
                    cursor.close()
                    conn.close()

                with ta5:
                    if array2[0][0] < 0.5:
                        st.success("Severity status: Mild .")
                        st.success("Please try to treat yourself with the treatement methods stated in recommendation.")
                    else:
                        st.error("Severity status: Severe.")
                        st.error("Warning: Please try to contact or make an appointement with the dermatologist recommended in the speciality recommendation provider as soon as possible")
     
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-bottom-left-radius:0.5rem;
                            border-bottom-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>DermaCare</h2>
                    <h4>Human Skin Disease Classifier</h4>
                    </div>
                """, width=715, height=70)

            elif predicted_class_label == "Psoriasis":
                st.info("Psoriasis")
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-top-left-radius:0.5rem;
                            border-top-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>Psoriasis</h2>
                    <h4>Also called : as licehn planus</h4>
                    </div>
                """, width=715, height=70)
                ta1,ta2,ta3, ta4 , ta5, ta6 , ta7 = st.tabs(['OVERVIEW','SYMPTOMS','TREATMENTS','SPECIALISTS','SEVERITY','PRED STATUS', 'CHART'])  
                with ta1:
                    st.image(list_img_urls7[1])     
                    st.write(page_py7.summary[0:356])
                    col1, col2 = st.columns(2)
                    with col1:
                        # st.subheader('')
                        st.subheader('')
                        # st.subheader("Basic informations") 
                        
                        with st.expander("Causes of Psoriasis"):
                            st.write("Psoriasis is thought to be caused by a problem with the immune system, which causes your body to make too many skin cells.")
                        with st.expander("Effects of Psoriasis"):
                            st.write("They normally appear on your elbows, knees, scalp and lower back, but can appear anywhere on your body. The plaques can be itchy or sore, or both. In severe cases, the skin around your joints may crack and bleed.")
                        with st.expander("Prevention of Psoriasis"):
                            st.write('You should always have new skin growths clinically diagnosed to make sure they aren’t cancerous. Different kinds of skin growths can be hard to tell apart from each other. If your healthcare provider is in any doubt about your growth, they might want to remove it for biopsy.')
                    with col2: 
                        # st.subheader("Related conditions") 
                        taa1, taa2 , taa3 = st.tabs(['Related image1', 'Related image2', 'Related image3'])
                        with taa1:
                            st.image(list_img_urls7[2])
                        with taa2:
                            st.image(list_img_urls7[3])
                        with taa3:
                            st.image(list_img_urls7[4])
                
                with ta2:
                    page_pys = wiki_wiki.page('Melanoma')
                    ta2col1, ta2col2 = st.columns(2)
                    with ta2col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ul{
                                font-family:'Calibri';
                                font-size:19px;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                                font-size:19px;
                                width:95%;
                                line-height:
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Symptom of Psoriasis</h2>
                            <p>The main symptoms of psoriasis are patches of skin that are dry, red and covered in silver scales.
                            Psoriasis typically causes patches of skin that are dry, red and covered in silver scales. Some people find their psoriasis causes itching or soreness.
                            There are several different types of psoriasis. Many people have only 1 form at a time, although 2 different types can occur together. One form may change into another or become more severe.</p>
                        </div>
                        """,width=370, height = 300)
                    with ta2col2:
                        st.header("")
                        st.image(list_img_urls4[4])
                with ta3:
                    ta3col1, ta3col2 = st.columns(2)
                    with ta3col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ol{
                                font-family:'Calibri';
                                font-size:19px;
                                margin-right:2rem;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Treatment for Psoriasis</h2>
                            <ol>
                                <li>
                                <strong>Emollients</strong>
                                <p>Emollients are moisturising treatments applied directly to the skin to reduce water loss and cover it with a protective film. If you have mild psoriasis, an emollient is probably the first treatment your GP will suggest.</p>
                                </li>
                                <li><strong>Steroid creams or ointments</strong>
                                <p>Steroid creams or ointments (topical corticosteroids) are commonly used to treat mild to moderate psoriasis in most areas of the body. The treatment works by reducing inflammation. This slows the production of skin cells and reduces itching.</p>
                                </li>
                                <li><strong>Vitamin D analogues</strong>
                                <p>Vitamin D analogue creams are commonly used along with or instead of steroid creams for mild to moderate psoriasis affecting areas such as the limbs, trunk or scalp.</p>
                                </li>

                                <li><strong>Coal tar</strong>
                                <p>It may be used to treat psoriasis affecting the limbs, trunk or scalp if other topical treatments are not effective. </p>
                                </li>
                            </ol>
                        </div>
                        """,width=380, height = 700)
                    
                    with ta3col2:
                        st.header("")
                        st.header("")
                        st.image("https://www.sridevihospital.com/wp-content/uploads/2020/01/dermatologist.jpg")
                        st.image("https://www.cozmoderm.com/wp-content/uploads/2023/02/skin-special.jpg")
                with ta4:
                    conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/db.sqlite3')
                    cursor = conn.cursor()
                    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
                    with col1:
                        st.write("Username")
                    with col2:
                        st.write("First name")
                    with col3:
                        st.write("Last name")
                    with col4:
                        st.write("Email")
                    with col5:
                        st.write("Speciality")
                    with col6:
                        st.write("Phone")
                    with col7:
                        st.write("Location")
                    for row in cursor.execute('SELECT username , first_name , last_name , email,speciality, phone, location FROM DermaCareApp_user WHERE speciality == "Psoriasis" '):
                        col1, col2, col3, col4, col5, col6, col7  = st.columns(7)
                        with col1:
                            st.write(row[0])
                        with col2:
                            st.write(row[1])
                        with col3:
                            st.write(row[2])

                        with col4:
                            st.write(row[3])
                        with col5:
                            st.write(row[4])
                        with col6:
                            st.write(row[5])
                        with col7:
                            st.write(row[6])
                    # conn.execute("""
                    # INSERT INTO my_table (name,data) VALUES(?,?)""", (name, file_uploader.name))

                    conn.commit()
                    cursor.close()
                    conn.close()


                with ta5:
                    if array2[0][0] < 0.5:
                        st.success("Severity status: Mild .")
                        st.success("Please try to treat yourself with the treatement methods stated in recommendation.")
                    else:
                        st.error("Severity status: Severe.")
                        st.error("Warning: Please try to contact or make an appointement with the dermatologist recommended in the speciality recommendation provider as soon as possible")
     
                with ta6:
                    for i in range(len(class_labels)):
                        st.write(f"{class_labels[i]}  : {(predictions[0][i])*100}%")
                with ta7:
                    # Flatten the predictions array
                    predictions_flat = np.array(predictions).flatten()

                    predictions_2d = np.array(predictions).reshape(1, -1)

                    fig3, ax3 = plt.subplots()
                    ax3.scatter(class_labels, predictions)
                    ax3.set_xlabel('Class labels')
                    ax3.set_ylabel('Predictions')
                    ax3.set_xticklabels(class_labels, fontsize=6)
                    ax3.set_title('Scatter plot of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig3)
                    # fig2, ax2 = plt.subplots()
                    # im = ax2.imshow(predictions_2d, cmap='YlGn')
                    # ax2.set_xticks(np.arange(len(class_labels)))
                    # ax2.set_yticks([0])
                    # ax2.set_xticklabels(class_labels, fontsize=5)
                    # ax2.set_title('Heatmap of predictions')

                    # Add the values to the heatmap
                    # for i in range(len(class_labels)):
                    #     for j in range(1):
                    #         text = ax2.text(i, j, predictions_2d[j, i], ha='center', va='center', color='black')

                    
                    # st.pyplot(fig2)

                    # Create a bar chart
                    fig, ax = plt.subplots()
                    ax.bar(np.repeat(class_labels, len(predictions)), predictions_flat)
                    ax.set_xlabel('Class labels')
                    ax.set_ylabel('Predictions')
                    ax.set_xticklabels(class_labels, fontsize=6)
                    ax.set_title('Bar chart of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig)

                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-bottom-left-radius:0.5rem;
                            border-bottom-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>DermaCare</h2>
                    <h4>Human Skin Disease Classifier</h4>
                    </div>
                """, width=715, height=70)

            elif predicted_class_label == "Seborrheic Keratoses":
                st.info("Seborrheic Keratoses")
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-top-left-radius:0.5rem;
                            border-top-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>Seborrheic keratoses</h2>
                    <h4>Also called : as seborrheic skin lesions</h4>
                    </div>
                """, width=715, height=70)
                ta1,ta2,ta3, ta4 , ta5 , ta6, ta7= st.tabs(['OVERVIEW','SYMPTOMS','TREATMENTS','SPECIALISTS','SEVERITY','PRED STATUS','CHART'])  
                with ta1:
                    st.image(list_img_urls6[1])     
                    st.write(page_py6.summary[0:356])
                    col1, col2 = st.columns(2)
                    with col1:
                        # st.subheader('')
                        st.subheader('')
                        # st.subheader("Basic informations") 
                        
                        with st.expander("Causes of Seborrheic keratoses"):
                            st.write("The first is age: seborrheic keratoses are especially common in adults over 50, and they tend to multiply as people get older. Some studies suggest that sun exposure may increase their occurrence. They also appear more frequently in families, which suggests that genetics may play a role. They are not viral or bacterial. They don’t spread and they aren’t contagious.")
                        with st.expander("Effects of Seborrheic keratoses"):
                            st.write("They usually don’t have an impact, but people sometimes report:Itching,Irritation from friction,Bleeding.")
                        with st.expander("Prevention of Seborrheic keratoses"):
                            st.write('You should always have new skin growths clinically diagnosed to make sure they aren’t cancerous. Different kinds of skin growths can be hard to tell apart from each other. If your healthcare provider is in any doubt about your growth, they might want to remove it for biopsy.')
                    with col2: 
                        # st.subheader("Related conditions") 
                        taa1, taa2 , taa3 = st.tabs(['Related image1', 'Related image2', 'Related image3'])
                        with taa1:
                            st.image(list_img_urls6[2])
                        with taa2:
                            st.image(list_img_urls6[3])
                        with taa3:
                            st.image(list_img_urls6[3])          
                with ta2:
                    page_pys = wiki_wiki.page('Melanoma')
                    ta2col1, ta2col2 = st.columns(2)
                    with ta2col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ul{
                                font-family:'Calibri';
                                font-size:19px;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                                font-size:19px;
                                width:95%;
                                line-height:
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Symptom of Seborrheic keratoses</h2>
                            <p>Benign moles are usually brown, tan, pink or black (especially on dark-colored skin). They are circular or oval and are usually small (commonly between 1–3 mm), though some can be larger than the size of a typical pencil eraser (>5 mm). Some moles produce dark, coarse hair.</p>
                        </div>
                        """,width=370, height = 300)
                    with ta2col2:
                        st.header("")
                        st.image(list_img_urls4[4])
                with ta3:
                    ta3col1, ta3col2 = st.columns(2)
                    with ta3col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ol{
                                font-family:'Calibri';
                                font-size:19px;
                                margin-right:2rem;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Treatment for Seborrheic keratoses</h2>
                            <ol>
                                <li>
                                <strong>Freezing the growth</strong>
                                <p>Freezing a growth with liquid nitrogen (cryotherapy) can be an effective way to remove a seborrheic keratosis. It doesn't always work on raised, thicker growths.
                                This method carries the risk of permanent loss of pigment, especially on Black or brown skin.</p>
                                </li>
                                <li><strong>Scraping (curettage) </strong>
                                <p>First your doctor will numb the area and then use a scalpel blade to remove the growth. Sometimes shaving or scraping is used along with cryosurgery to treat thinner or flat growths.</p>
                                </li>
                                <li><strong>Burning with an electric current</strong>
                                <p>First your doctor will numb the area and then destroy the growth with electrocautery. This method can be used alone or with scraping, especially when removing thicker growths.</p>
                                </li>
                            </ol>
                        </div>
                        """,width=380, height = 700)
                    
                    with ta3col2:
                        st.header("")
                        st.header("")
                        st.image("https://www.sridevihospital.com/wp-content/uploads/2020/01/dermatologist.jpg")
                        st.image("https://www.cozmoderm.com/wp-content/uploads/2023/02/skin-special.jpg")
                with ta4:
                    conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/db.sqlite3')
                    cursor = conn.cursor()
                    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
                    with col1:
                        st.write("Username")
                    with col2:
                        st.write("First name")
                    with col3:
                        st.write("Last name")
                    with col4:
                        st.write("Email")
                    with col5:
                        st.write("Speciality")
                    with col6:
                        st.write("Phone")
                    with col7:
                        st.write("Location")
                    for row in cursor.execute('SELECT username , first_name , last_name , email,speciality, phone, location FROM DermaCareApp_user WHERE speciality == "Seborrheic keratoses" '):
                        col1, col2, col3, col4, col5, col6, col7  = st.columns(7)
                        with col1:
                            st.write(row[0])
                        with col2:
                            st.write(row[1])
                        with col3:
                            st.write(row[2])

                        with col4:
                            st.write(row[3])
                        with col5:
                            st.write(row[4])
                        with col6:
                            st.write(row[5])
                        with col7:
                            st.write(row[6])
                    # conn.execute("""
                    # INSERT INTO my_table (name,data) VALUES(?,?)""", (name, file_uploader.name))

                    conn.commit()
                    cursor.close()
                    conn.close()

                with ta5:
                    if array2[0][0] < 0.5:
                        st.success("Severity status: Mild .")
                        st.success("Please try to treat yourself with the treatement methods stated in recommendation.")
                    else:
                        st.error("Severity status: Severe.")
                        st.error("Warning: Please try to contact or make an appointement with the dermatologist recommended in the speciality recommendation provider as soon as possible")
     
                with ta6:
                    for i in range(len(class_labels)):
                        st.write(f"{class_labels[i]}  : {(predictions[0][i])*100}%")
                with ta7:
                    # Flatten the predictions array
                    predictions_flat = np.array(predictions).flatten()

                    predictions_2d = np.array(predictions).reshape(1, -1)

                    fig3, ax3 = plt.subplots()
                    ax3.scatter(class_labels, predictions)
                    ax3.set_xlabel('Class labels')
                    ax3.set_ylabel('Predictions')
                    ax3.set_xticklabels(class_labels, fontsize=6)
                    ax3.set_title('Scatter plot of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig3)
                    # fig2, ax2 = plt.subplots()
                    # im = ax2.imshow(predictions_2d, cmap='YlGn')
                    # ax2.set_xticks(np.arange(len(class_labels)))
                    # ax2.set_yticks([0])
                    # ax2.set_xticklabels(class_labels, fontsize=5)
                    # ax2.set_title('Heatmap of predictions')

                    # Add the values to the heatmap
                    # for i in range(len(class_labels)):
                    #     for j in range(1):
                    #         text = ax2.text(i, j, predictions_2d[j, i], ha='center', va='center', color='black')

                    
                    # st.pyplot(fig2)

                    # Create a bar chart
                    fig, ax = plt.subplots()
                    ax.bar(np.repeat(class_labels, len(predictions)), predictions_flat)
                    ax.set_xlabel('Class labels')
                    ax.set_ylabel('Predictions')
                    ax.set_xticklabels(class_labels, fontsize=6)
                    ax.set_title('Bar chart of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig)

                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-bottom-left-radius:0.5rem;
                            border-bottom-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>DermaCare</h2>
                    <h4>Human Skin Disease Classifier</h4>
                    </div>
                """, width=715, height=70)

            elif predicted_class_label == "Tinea Ringworm Candidiasis":
                st.info("Tinea Ringworm Candidiasis")
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-top-left-radius:0.5rem;
                            border-top-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>Tinea corporis</h2>
                    <h4>Also called : as tinea ringworm</h4>
                    </div>
                """, width=715, height=70)
                ta1,ta2,ta3, ta4 , ta5 ,ta6, ta7= st.tabs(['OVERVIEW','SYMPTOMS','TREATMENTS','SPECIALISTS','SEVERITY','PRED STATUS','CHART'])  
                with ta1:
                    st.image(list_img_urls8[1])     
                    st.write(page_py8.summary[0:356])
                    col1, col2 = st.columns(2)
                    with col1:
                        # st.subheader('')
                        st.subheader('')
                        # st.subheader("Basic informations") 
                        
                        with st.expander("Causes of Tinea corporis"):
                            st.write("Ringworm of the body (tinea corporis) is a rash caused by a fungal infection.")
                        with st.expander("Effects of Tinea corporis"):
                            st.write("Slightly raised, expanding rings A round, flat patch of itchy skinOverlapping rings")
                        with st.expander("Prevention of Tinea corporis"):
                            st.write('Educate yourself and others, Keep clean, Stay cool and dry, Avoid infected animals are the main prevention of tinea ringworm.')
                    with col2: 
                        # st.subheader("Related conditions") 
                        taa1, taa2 , taa3 = st.tabs(['Related image1', 'Related image2', 'Related image3'])
                        with taa1:
                            st.image(list_img_urls8[2])
                        with taa2:
                            st.image(list_img_urls8[3])
                        with taa3:
                            st.image(list_img_urls8[4])          
                with ta2:
                    page_pys = wiki_wiki.page('Melanoma')
                    ta2col1, ta2col2 = st.columns(2)
                    with ta2col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ul{
                                font-family:'Calibri';
                                font-size:19px;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                                font-size:19px;
                                width:95%;
                                line-height:
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Symptom of Tinea ringworm</h2>
                            <p>Signs and symptoms of ringworm may include : A scaly ring-shaped area, typically on the buttocks, trunk, arms and legs
                            Itchiness A clear or scaly area inside the ring, perhaps with a scattering of bumps whose color ranges from red on white skin to reddish, purplish, brown or gray on black and brown skin
                            Slightly raised, expanding rings A round, flat patch of itchy skin Overlapping rings.</p>
                        </div>
                        """,width=370, height = 300)
                    with ta2col2:
                        st.header("")
                        st.image(list_img_urls4[4])
                with ta3:
                    ta3col1, ta3col2 = st.columns(2)
                    with ta3col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ol{
                                font-family:'Calibri';
                                font-size:19px;
                                margin-right:2rem;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Treatment for tinea ringworm</h2>
                            <ol>
                                <li>
                                <p>
                                If over-the-counter treatments don't work, you may need prescription-strength antifungal medications — such as a lotion, cream or ointment that you apply to the affected skin. If your infection is particularly severe or extensive, your doctor might prescribe antifungal pills.</p>
                                </li>
                            </ol>
                        </div>
                        """,width=380, height = 300)
                    
                    with ta3col2:
                        st.header("")
                        st.header("")
                        st.image("https://www.sridevihospital.com/wp-content/uploads/2020/01/dermatologist.jpg")
                        st.image("https://www.cozmoderm.com/wp-content/uploads/2023/02/skin-special.jpg")
                with ta4:
                    conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/db.sqlite3')
                    cursor = conn.cursor()
                    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
                    with col1:
                        st.write("Username")
                    with col2:
                        st.write("First name")
                    with col3:
                        st.write("Last name")
                    with col4:
                        st.write("Email")
                    with col5:
                        st.write("Speciality")
                    with col6:
                        st.write("Phone")
                    with col7:
                        st.write("Location")
                    for row in cursor.execute('SELECT username , first_name , last_name , email,speciality, phone, location FROM DermaCareApp_user WHERE speciality == "Tinea ringworm" '):
                        col1, col2, col3, col4, col5, col6, col7  = st.columns(7)
                        with col1:
                            st.write(row[0])
                        with col2:
                            st.write(row[1])
                        with col3:
                            st.write(row[2])

                        with col4:
                            st.write(row[3])
                        with col5:
                            st.write(row[4])
                        with col6:
                            st.write(row[5])
                        with col7:
                            st.write(row[6])
                    # conn.execute("""
                    # INSERT INTO my_table (name,data) VALUES(?,?)""", (name, file_uploader.name))

                    conn.commit()
                    cursor.close()
                    conn.close()


                with ta5:
                    if array2[0][0] < 0.5:
                        st.success("Severity status: Mild .")
                        st.success("Please try to treat yourself with the treatement methods stated in recommendation.")
                    else:
                        st.error("Severity status: Severe.")
                        st.error("Warning: Please try to contact or make an appointement with the dermatologist recommended in the speciality recommendation provider as soon as possible")
     
                with ta6:
                    for i in range(len(class_labels)):
                        st.write(f"{class_labels[i]}  : {(predictions[0][i])*100}%")
                with ta7:
                    # Flatten the predictions array
                    predictions_flat = np.array(predictions).flatten()

                    predictions_2d = np.array(predictions).reshape(1, -1)

                    fig3, ax3 = plt.subplots()
                    ax3.scatter(class_labels, predictions)
                    ax3.set_xlabel('Class labels')
                    ax3.set_ylabel('Predictions')
                    ax3.set_xticklabels(class_labels, fontsize=6)
                    ax3.set_title('Scatter plot of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig3)
                    # fig2, ax2 = plt.subplots()
                    # im = ax2.imshow(predictions_2d, cmap='YlGn')
                    # ax2.set_xticks(np.arange(len(class_labels)))
                    # ax2.set_yticks([0])
                    # ax2.set_xticklabels(class_labels, fontsize=5)
                    # ax2.set_title('Heatmap of predictions')

                    # Add the values to the heatmap
                    # for i in range(len(class_labels)):
                    #     for j in range(1):
                    #         text = ax2.text(i, j, predictions_2d[j, i], ha='center', va='center', color='black')

                    
                    # st.pyplot(fig2)

                    # Create a bar chart
                    fig, ax = plt.subplots()
                    ax.bar(np.repeat(class_labels, len(predictions)), predictions_flat)
                    ax.set_xlabel('Class labels')
                    ax.set_ylabel('Predictions')
                    ax.set_xticklabels(class_labels, fontsize=6)
                    ax.set_title('Bar chart of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig)

                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-bottom-left-radius:0.5rem;
                            border-bottom-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>DermaCare</h2>
                    <h4>Human Skin Disease Classifier</h4>
                    </div>
                """, width=715, height=70)

            elif predicted_class_label == "Warts Molluscum":
                st.info("Warts Molluscum")
                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-top-left-radius:0.5rem;
                            border-top-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>Warts Molluscum </h2>
                    <h4>Also called : as Poxvirus</h4>
                    </div>
                """, width=715, height=70)
                ta1,ta2,ta3, ta4, ta5, ta6, ta7= st.tabs(['OVERVIEW','SYMPTOMS','TREATMENTS','SPECIALISTS','SEVERITY','PRED STATUS','CHART'])  
                with ta1:
                    st.image(list_img_urls9[2])     
                    st.write(page_py9.summary[0:356])
                    col1, col2 = st.columns(2)
                    with col1:
                        # st.subheader('')
                        st.subheader('')
                        # st.subheader("Basic informations") 
                        
                        with st.expander("Causes of Warts Molluscum"):
                            st.write("Molluscum contagiosum is an infection caused by a poxvirus (molluscum contagiosum virus).")
                        with st.expander("Effects of Warts Molluscum"):
                            st.write("The result of the infection is usually a benign, mild skin disease characterized by lesions (growths) that may appear anywhere on the body. Within 6-12 months, Molluscum contagiosum typically resolves without scarring but may take as long as 4 years.")
                        with st.expander("Prevention of Warts Molllscum"):
                            st.write('You should always have new skin growths clinically diagnosed to make sure they aren’t cancerous. Different kinds of skin growths can be hard to tell apart from each other. If your healthcare provider is in any doubt about your growth, they might want to remove it for biopsy.')
                    with col2: 
                        # st.subheader("Related conditions") 
                        taa1, taa2 , taa3 = st.tabs(['Related image1', 'Related image2', 'Related image3'])
                        with taa1:
                            st.image(list_img_urls9[1])
                        with taa2:
                            st.image(list_img_urls9[2])
                        with taa3:
                            st.image(list_img_urls9[3])
                
                with ta2:
                    page_pys = wiki_wiki.page('Melanoma')
                    ta2col1, ta2col2 = st.columns(2)
                    with ta2col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ul{
                                font-family:'Calibri';
                                font-size:19px;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                                font-size:19px;
                                width:95%;
                                line-height:
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Symptom of Warts molluscum</h2>
                            <p>Molluscum contagiosum signs and symptoms include:

                                Raised, round, skin-colored bumps
                                Small bumps — typically under about 1/4 inch (smaller than 6 millimeters) in diameter
                                Bumps with a small dent or dot at the top near the center
                                Itchy, pink bumps
                                Bumps on the face, trunk, arms or legs of children
                                Bumps on the genitals, lower abdomen or inner thighs of adults if the infection was sexually transmitted.
                            </p>
                        </div>
                        """,width=370, height = 300)
                    with ta2col2:
                        st.header("")
                        st.image(list_img_urls9[2])
                with ta3:
                    ta3col1, ta3col2 = st.columns(2)
                    with ta3col1:
                        com.html("""
                        <style>
                            .melanomaSymptoms{
                                display:flex;
                                flex-direction:column;
                                width:100%;
                                font-family:'Calibri';
                                
                                text-align:left;
                            }
                            h2{
                                margin-bottom:0rem;
                                color:rgba(0,0,0,0.85);
                            }
                            ol{
                                font-family:'Calibri';
                                font-size:19px;
                                margin-right:2rem;
                                color:rgba(0,0,0,0.8);
                            }

                            li{
                                font-family:'Calibri';
                                margin-bottom:0.75rem;
                            }
                            p{
                                text-align:justify;
                            }
                        </style>

                        <div class="melanomaSymptoms">
                            <h2>Treatment for warts molluscum</h2>
                            <ol>
                                <li>
                                <strong>Wash your hands</strong>
                                <p>Freezing a growth with liquid nitrogen (cryotherapy) can be an effective way to remove a seborrheic keratosis. It doesn't always work on raised, thicker growths.
                                This method carries the risk of permanent loss of pigment, especially on Black or brown skin.</p>
                                </li>
                                <li><strong>Scraping (curettage) </strong>
                                <p>First your doctor will numb the area and then use a scalpel blade to remove the growth. Sometimes shaving or scraping is used along with cryosurgery to treat thinner or flat growths.</p>
                                </li>
                                <li><strong>Burning with an electric current</strong>
                                <p>First your doctor will numb the area and then destroy the growth with electrocautery. This method can be used alone or with scraping, especially when removing thicker growths.</p>
                                </li>
                            </ol>
                        </div>
                        """,width=380, height = 700)
                    
                    with ta3col2:
                        st.header("")
                        st.header("")
                        st.image("https://www.sridevihospital.com/wp-content/uploads/2020/01/dermatologist.jpg")
                        st.image("https://www.cozmoderm.com/wp-content/uploads/2023/02/skin-special.jpg")
                with ta4:
                    conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/db.sqlite3')
                    cursor = conn.cursor()
                    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
                    with col1:
                        st.write("Username")
                    with col2:
                        st.write("First name")
                    with col3:
                        st.write("Last name")
                    with col4:
                        st.write("Email")
                    with col5:
                        st.write("Speciality")
                    with col6:
                        st.write("Phone")
                    with col7:
                        st.write("Location")
                    for row in cursor.execute('SELECT username , first_name , last_name , email,speciality, phone, location FROM DermaCareApp_user WHERE speciality == "Benign keratosis" '):
                        col1, col2, col3, col4, col5, col6, col7  = st.columns(7)
                        with col1:
                            st.write(row[0])
                        with col2:
                            st.write(row[1])
                        with col3:
                            st.write(row[2])

                        with col4:
                            st.write(row[3])
                        with col5:
                            st.write(row[4])
                        with col6:
                            st.write(row[5])
                        with col7:
                            st.write(row[6])
                    # conn.execute("""
                    # INSERT INTO my_table (name,data) VALUES(?,?)""", (name, file_uploader.name))

                    conn.commit()
                    cursor.close()
                    conn.close()

                with ta5:
                    if array2[0][0] < 0.5:
                        st.success("Severity status: Mild .")
                        st.success("Please try to treat yourself with the treatement methods stated in recommendation.")
                    else:
                        st.error("Severity status: Severe.")
                        st.error("Warning: Please try to contact or make an appointement with the dermatologist recommended in the speciality recommendation provider as soon as possible")
     
                with ta6:
                    for i in range(len(class_labels)):
                        st.write(f"{class_labels[i]}  : {(predictions[0][i])*100}%")
                with ta7:
                    # Flatten the predictions array
                    predictions_flat = np.array(predictions).flatten()

                    predictions_2d = np.array(predictions).reshape(1, -1)

                    fig3, ax3 = plt.subplots()
                    ax3.scatter(class_labels, predictions)
                    ax3.set_xlabel('Class labels')
                    ax3.set_ylabel('Predictions')
                    ax3.set_xticklabels(class_labels, fontsize=6)
                    ax3.set_title('Scatter plot of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig3)
                    # fig2, ax2 = plt.subplots()
                    # im = ax2.imshow(predictions_2d, cmap='YlGn')
                    # ax2.set_xticks(np.arange(len(class_labels)))
                    # ax2.set_yticks([0])
                    # ax2.set_xticklabels(class_labels, fontsize=5)
                    # ax2.set_title('Heatmap of predictions')

                    # Add the values to the heatmap
                    # for i in range(len(class_labels)):
                    #     for j in range(1):
                    #         text = ax2.text(i, j, predictions_2d[j, i], ha='center', va='center', color='black')

                    
                    # st.pyplot(fig2)

                    # Create a bar chart
                    fig, ax = plt.subplots()
                    ax.bar(np.repeat(class_labels, len(predictions)), predictions_flat)
                    ax.set_xlabel('Class labels')
                    ax.set_ylabel('Predictions')
                    ax.set_xticklabels(class_labels, fontsize=6)
                    ax.set_title('Bar chart of predictions')

                    # Display the chart in the Streamlit app
                    st.pyplot(fig)

                com.html("""
                    <style>
                        .Header_box{
                            display:flex;
                            flex-direction:column;
                            background:rgba(52,122,204,0.73);
                            color:white;
                            font-family:Calibri;
                            border:1px solid rgba(52,122,204,0.73);
                            border-bottom-left-radius:0.5rem;
                            border-bottom-right-radius:0.5rem;
                            padding-left:10px;
                            padding-top:5px;
                            padding-bottom:5px;
                        }
                        h2{
                            margin-top:0rem;
                            margin-bottom:0rem;
                            font-weight:400;
                        }
                        h4{
                            margin-top:0rem;
                            font-weight:400;
                            margin-bottom:0rem;
                        }
                    </style>
                    <div class="Header_box">
                    <h2>DermaCare</h2>
                    <h4>Human Skin Disease Classifier</h4>
                    </div>
                """, width=715, height=70)
elif selected == "Take Camera":
    taken_photo = st.camera_input("Take photo")
    if taken_photo is not None:
        img2 = image.load_img(taken_photo)
        st.image(img2)
        loaded_model = tf.keras.models.load_model('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/SkinDiseaseModel/Skin Disease Detection.h5')
        img = tf.image.resize(img2,size=[224,224])
        test_image = image.img_to_array(img)
        test_image = np.expand_dims(test_image, axis=0)
        images = np.vstack([test_image])
        val = loaded_model.predict(images)
        array = np.array(val)

        if array[0][0] == 1:
            st.error("You have skin disease ")
        elif array[0][0] == 0:
            st.success("You have no skin disease")
        if st.button("Donate Image", key = 99):
            conn = sqlite3.connect('C:/Users/GL/Desktop/Final_Year_Project/Final_Year_Project_Django_Project/DermaCare_Project/DermaCareProject/DataStoreFolder/DataStoreImageDatabe.db')
            cursor = conn.cursor()
            name = "Camera Taken Photo"
            conn.execute("""
            INSERT INTO Camera_Taken_Photo_Collection (Name,Data) VALUES(?,?)""", (name, taken_photo.name))
            conn.commit()
            cursor.close()
            conn.close()
            st.success("Saved Success, thank you for your donation.")
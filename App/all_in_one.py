import nltk
import streamlit as st
from textblob import TextBlob
from streamlit_option_menu import *
from streamlit_extras.keyboard_url import keyboard_to_url
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
import json as js
import time
import googletrans
from googletrans import Translator
from googletrans import LANGUAGES
import gtts
from gtts import gTTS
import os
import requests
import pandas as pd
#__________________________________________________________


class language_ai :

    def method(self):
        st.set_page_config(page_title='Language AI Project By Praveen', layout="wide")


        with st.sidebar:  # Navbar
            selected = option_menu(
                menu_title="Language AI",
                options=['Intro', "Sentiment Analysis", "Language Translator",'Speech Synthesis', 'Summarization','Table Question Answering System','Question Answering System'
                         ],
                icons=['mic-fill', '', '', '', ''],
                menu_icon='alexa',
                default_index=0,
            )

        def lottie(filepath):
            with open(filepath, 'r') as file:
                return js.load(file)

        if selected == 'Sentiment Analysis':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            col1, col2 ,col3= st.columns([4,7 ,3])

            col2.markdown(
                "<h1 style='font-size: 90px;'><span style='color: cyan;'>Sentiment</span> <span style='color: white;'>Analysis</span> </h1>",
                unsafe_allow_html=True)
            col2.write("")
            col2.write("")
            col1, col2, col3, col4 = st.columns([10, 10, 10, 10])
            with col1:
                file = lottie("smile_emoji.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=350,
                    key=None
                )
            col3.write("")
            col3.write('')
            with col2:
                file = lottie("angry_emoji.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=350,
                    key=None
                )
            col3.write("")
            with col3:
                file = lottie("sad.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=250,
                    key=None
                )
            with col4:
                file = lottie("love_emoji.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=340,
                    key=None
                )
            col1.write("")
            col1.write("")
            col1.write("")
            col1, col2, col3 = st.columns([3, 7, 3])

            # Sentiment analyszer
            with col2:
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: white;'>Enter </span><span style='color: cyan;'>   Review</span>  </h1>",
                    unsafe_allow_html=True)
                input = st.text_input("")

            col1, col2, col3 = st.columns([8.5, 7, 3])
            if col2.button('Proceed'):
                blob = TextBlob(input)
                sentiment = blob.sentiment
                score = round(sentiment.polarity,2)
                col1, col2, col3 = st.columns([7, 9, 3])
                col2.write("")
                col2.write("")
                col2.write('')
                col2.write('')
                if score < 0.0 :
                    col2.markdown(

                        f"<h1 style='font-size: 40px;'><span style='color: cyan;'>Negative </span><span style='color: white;'> Review : </span> <span style='color: cyan;'> {score}</span></h1>",
                        unsafe_allow_html=True)
                elif score > 0.0 and score <= 0.5 :
                    col2.markdown(
                        f"<h1 style='font-size: 40px;'><span style='color: cyan;'>Neutral </span><span style='color: white;'> Review : </span> <span style='color: cyan;'> {score}</span></h1>",
                        unsafe_allow_html=True)
                elif score > 0.5 :
                    col2.markdown(

                        f"<h1 style='font-size: 40px;'><span style='color: cyan;'>Positive </span><span style='color: white;'> Review : </span> <span style='color: cyan;'> {score}</span></h1>",
                        unsafe_allow_html=True)

                else :
                    col2.markdown(
                        f"<h1 style='font-size: 40px;'><span style='color: cyan;'>Neutral </span><span style='color: white;'> Review : </span> <span style='color: cyan;'>1.0</span></h1>",
                        unsafe_allow_html=True)

#___________________________________________________________________________________________________________________________________________
        elif selected == 'Language Translator':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([6, 10, 3])
            col2.markdown(
                "<h1 style='font-size: 60px;'><span style='color: white;'>Language</span> <span style='color: cyan;'>Translator</span> </h1>",
                unsafe_allow_html=True)
            col1, col2, col3 = st.columns([6, 10, 7])
            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            col1, col2 = st.columns([10, 10])
            col1.markdown(
                "<h1 style='font-size: 30px;'><span style='color: white;'>Provide</span> <span style='color: cyan;'>Text</span> </h1>",
                unsafe_allow_html=True)
            col2.markdown(
                "<h1 style='font-size: 30px;'><span style='color: white;'>Select </span> <span style='color: cyan;'> Language</span> </h1>",
                unsafe_allow_html=True)

            col1, col2 = st.columns([10, 10])
            text = col1.text_input("      ")

            # Creation of translator object
            translator = Translator()

            languages = []  # Adding all languages and their code

            for code, name in LANGUAGES.items():
                languages.append({name: code})

            # Collecting Languages and their codes
            languages_name = [list(i.keys())[0] for i in languages]  # Collection of Languages Name
            lan_codes = [list(i.values())[0] for i in languages]  # Collection of Language codes

            selected_lan = col2.selectbox('', languages_name)

            x = languages_name.index(selected_lan)

            target_language = lan_codes[x]

            translated = translator.translate(text, dest=target_language)
            translated_text = translated.text

            col1, col2, col3 = st.columns([18, 10, 10])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            if col2.button('Convert'):
                # Target Language

                with st.spinner('Converting...'):
                    time.sleep(3)

                col3, col1, col2, col4 = st.columns([9, 45, 20, 10])
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                # col2.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.markdown(
                    f"<h1 style='font-size: 30px;'><span style='color: cyan;'>Provided Text : </span> <span style='color: white;'>{text}</span></h1>",
                    unsafe_allow_html=True)

                col2.markdown(
                    f"<h1 style='font-size: 30px;'><span style='color: cyan;'>Converted Text : </span><span style='color: white;'>{translated_text}</span></h1>",
                    unsafe_allow_html=True)
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )
#___________________________________________________________________________________________________________________________________________
        elif selected == 'Speech Synthesis':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns([4, 7, 3])

            col2.markdown(
                "<h1 style='font-size: 100px;'><span style='color: cyan;'>Speech</span> <span style='color: white;'>Synthesis</span> </h1>",
                unsafe_allow_html=True)
            col1, col2, col3 = st.columns([4, 7, 3.7])
            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70", )
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            col4, col1, col2, col3 = st.columns([3, 10, 3, 10])
            with col1:
                file = lottie("text.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=500,
                    key=None
                )
            with col3:
                file = lottie("speech.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=500,
                    key=None
                )

            col1, col2, col3 = st.columns([4, 7, 4.3])
            col2.markdown(
                "<h1 style='font-size: 40px;'><span style='color: cyan;'>Provide</span> <span style='color: white;'>Text</span> </h1>",
                unsafe_allow_html=True)

            input = col2.text_input("")
            with col2:
                if st.button('Proceed'):
                    # English Language Specified Here
                    language = 'en'

                    # Object Creation for gTTS Class
                    text_to_speech = gTTS(text=input, lang=language, slow=False)

                    # Save Audio File
                    text_to_speech.save("output.mp3")

                    os.system("start output.mp3")
#___________________________________________________________________________________________________________________________________________
        elif selected == "Summarization":
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            col1, col2, col3 = st.columns([3, 7, 2])

            col2.markdown(
                "<h1 style='font-size: 90px;'><span style='color: cyan;'>Summarization</span> <span style='color: white;'>Process</span> </h1>",
                unsafe_allow_html=True)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col4, col1, col2, col3 = st.columns([12, 10, 3, 10])

            with col1:
                file = lottie("summarization.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=400,
                    width=500,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            API_URL = ""
            headers = {"Authorization": "Bearer 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"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            try:
                col1, col2, col3 = st.columns([3, 7, 3])
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                with col2:
                    col2.markdown(
                        "<h1 style='font-size: 40px;'><span style='color: cyan;'>Provide</span> <span style='color: white;'>Text</span> </h1>",
                        unsafe_allow_html=True)
                    text = st.text_area("")
                    if st.button('Proceed'):
                        output = query({
                            "inputs": text,
                        })

                        res = output[0]['summary_text']
                        col2.write("")
                        col2.write("")
                        col2.write("")
                        col2.write("")
                        col2.markdown(
                            "<h1 style='font-size: 40px;'><span style='color: cyan;'>Summarised</span> <span style='color: white;'>Information</span> </h1>",
                            unsafe_allow_html=True)
                        st.code(res)
            except:
                col1, col2, col3 = st.columns([3, 7, 3])
                col2.success('Provide Information Again !!!')
#_____________________________________________________________________________________________________________________________________
        elif selected == 'Table Question Answering System':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1, 7, 1])

            col2.markdown(
                "<h1 style='font-size: 80px;'><span style='color: cyan;'>Table </span> <span style='color: white;'>Questioning </span><span style='color: white;'>Answering </span><span style='color: cyan;'> System</span> </h1>",
                unsafe_allow_html=True)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            API_URL = ""
            headers = {"Authorization": "Bearer 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"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            data = {
                "name": ["praveen", "thambey", "shabarinath", 'viswanathan', 'anna lakshmi', 'pavan', 'vigesh',
                         'vengatesh', 'nivas'],
                "age": ["21", "30", "38", '21', '45', '25', '25', '25', '26'],
                "height": ["170", "160", "159", '168', '159', '168', '176', '180', '160'],
                "skills": [
                    "NLP , Python , Ml", "Ml", "Python", "ML", "DL", "Ml", "Python", "ML", "DL"
                ]
            }
            col1, col2, col3 = st.columns([1, 7, 1])
            with col2:
                st.table(data)

            col2.markdown(
                "<h1 style='font-size: 40px;'><span style='color: cyan;'></span> <span style='color: white;'>Provide </span><span style='color:cyan;'>Question</span><span style='color: cyan;'></span> </h1>",
                unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 7, 1])
            try :
                with col2 :
                    input = st.text_input('')
                with col2:
                        if st.button("Proceed"):
                            output = query({
                                "inputs": {
                                    "query": input,
                                    "table": data
                                },
                            })
                            st.markdown(
                                "<h1 style='font-size: 40px;'><span style='color: cyan;'></span> <span style='color: cyan;'>Result </span><span style='color:white;'>:)</span><span style='color: cyan;'></span> </h1>",
                                unsafe_allow_html=True)

                            st.code(f'Question : {input} , Answer : {output["answer"]}')
            except :
                col2.success('Correct Question Words !!!')
#_______________________________________________________________________________________________________________________________________
        elif selected == 'Question Answering System':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns([2, 7, 1])

            col2.markdown(
                "<h1 style='font-size: 80px;'><span style='color: cyan;'></span> <span style='color: cyan;'>Questioning </span><span style='color: white;'>Answering </span><span style='color: cyan;'> System</span> </h1>",
                unsafe_allow_html=True)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            API_URL = ""
            headers = {"Authorization": "Bearer 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"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            col1, col2, col3 = st.columns([1, 7, 1])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Provide </span> <span style='color: white;'>Context </span> </h1>",
                    unsafe_allow_html=True)
                context = st.text_area("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Provide </span> <span style='color: white;'>Question</span> </h1>",
                    unsafe_allow_html=True)
                try:
                    question = st.text_input("")
                    if st.button("Proceed"):
                        output = query({
                            "inputs": {
                                "question": question,
                                "context": context
                            },
                        })
                        st.markdown(
                            "<h1 style='font-size: 40px;'><span style='color: cyan;'>Result </span> <span style='color: white;'>:)</span> </h1>",
                            unsafe_allow_html=True)
                        st.code(f'Question : {question} , Answer : {output["answer"]}')

                except:
                    st.success("Provide Correct Question !!!")
#______________________________________________________________________________________________________________________________________
        elif selected == 'Intro':

            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            # Start Intro
            col1, col2 = st.columns([11, 7])
            with col1:
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")

                st.markdown(
                    "<h1 style='font-size: 79px;'><span style='color:white;'>Howdy ,</span> <span style='color: white;'>I'm </span><span style='color: cyan;'> Praveen</span> </h1>",
                    unsafe_allow_html=True)

                # keyboard_to_url(key="P", url="https://www.linkedin.com/in/praveen-n-2b4004223/")

            with col2:
                file = lottie("intro1.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=700,
                    key=None
                )

            st.write("")
            st.write('')
            st.write("")
            st.write('')
            st.write("")
            st.write("")
            st.write('')
            st.write("")
            with col1:
                file = lottie("sound.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=240,
                    width=600,
                    key=None
                )

            col1,col2,col3 = st.columns([2,10,2])
            with col2:
               st.markdown(
                    "<h1 style='font-size: 85px;'><span style='color:white;'> I'm a </span> <span style='color: cyan;'> Data Scientist </span> <span style='color: white;'> From India </span></h1>",
                    unsafe_allow_html=True)

            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("cyan_boy_lap2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=700,
                    width=1100,
                    key=None
                )

            st.write("")
            st.markdown(
                    "<h1 style='font-size: 85px;'><span style='color:white;'>About </span> <span style='color:cyan;'>Language AI </span></h1>",
                    unsafe_allow_html=True)


            col1, col2, col3 = st.columns([2, 10, 2])
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("lang_ai.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=750,
                    width=1000,
                    key=None
                )

            st.markdown(
                "<h1 style='font-size: 85px;'><span style='color:white;'>Understanding </span> <span style='color:cyan;'>NLP </span></h1>",
                unsafe_allow_html=True)

            col1, col2, col3 = st.columns([2, 15, 2])
            col2.write("")
            col2.write("")
            col2.markdown(
                "<h1 style='font-size: 70px;'><span style='color: white;'>Process of Training</span> <span style='color: cyan;'>Language Models:</span><span style='color: white;'></span> </h1>",
                unsafe_allow_html=True)
            col1, col2, col3 = st.columns([6, 15, 2])

            with col2:
                file = lottie("model_training.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=700,
                    width=800,
                    key=None
                )
            col1, col2, col3 = st.columns([1, 15, 2])
            col2.markdown(
                "<h1 style='font-size: 70px;'><span style='color: cyan;'>Initialization </span><span style='color: white;'>(Birth)</span> </h1>",
                unsafe_allow_html=True)
            col1, col2 = st.columns([10, 10])
            with col2:
                file = lottie("parameter'.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=600,
                    width=800,
                    key=None
                )
            with col1:
                file = lottie("baby.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=600,
                    width=800,
                    key=None
                )
            col1, col2, col4, col3 = st.columns([2, 10, 1.7, 10])
            col2.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>( </span><span style='color: white;'>Baby is born with a brain ready to learn</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col3.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>( </span><span style='color: white;'>Model is initialized with random parameters</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.write('')
            st.write("")
            # ________________________________________________________________________________________________________________________

            col1, col2, col3 = st.columns([1, 15, 2])
            col2.markdown(
                "<h1 style='font-size: 70px;'><span style='color: cyan;'>Exposure to Language</span> </h1>",
                unsafe_allow_html=True)
            col1, col2 = st.columns([10, 10])
            with col2:
                file = lottie("ml_learn.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=800,
                    key=None
                )
            with col1:
                file = lottie("baby_1.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=600,
                    width=800,
                    key=None
                )
            col1, col2, col4, col3 = st.columns([2, 10, 1.7, 10])
            col2.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>( </span><span style='color: white;'>Listening to caregivers and observing their surroundings</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col3.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>( </span><span style='color: white;'>Exposed to vast amounts of text data in   multiple languages</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)

            # ___________________________________________________________________________________________________________________
            st.write("")
            st.write("")
            st.write('')
            st.write("")

            col1, col2, col3 = st.columns([1, 15, 2])
            col2.markdown(
                "<h1 style='font-size: 70px;'><span style='color: cyan;'>Learning Patterns</span> </h1>",
                unsafe_allow_html=True)
            col1, col2 = st.columns([10, 10])
            with col2:
                file = lottie("ml_pattern.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=600,
                    width=800,
                    key=None
                )
            with col1:
                file = lottie("babypattern.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=600,
                    width=800,
                    key=None
                )
            col1, col2, col4, col3 = st.columns([2, 10, 1.7, 10])
            col2.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>( </span><span style='color: white;'>Learns grammar, vocabulary, and context through exposure and interaction</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col3.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>( </span><span style='color: white;'>Language patterns, semantics, and context from the data it processes</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            # ________________________________________________________________________________________________________________________
            st.write("")
            st.write("")
            st.write('')
            st.write("")

            col1, col2, col3 = st.columns([1, 15, 2])
            col2.markdown(
                "<h1 style='font-size: 70px;'><span style='color: cyan;'>Feedback and Correction</span> </h1>",
                unsafe_allow_html=True)
            col1, col2 = st.columns([10, 10])
            with col2:
                file = lottie("ml_learn_2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=800,
                    key=None
                )
            with col1:
                file = lottie("baby_cry_2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=800,
                    key=None
                )
            col1, col2, col4, col3 = st.columns([2, 10, 1.7, 10])
            col2.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>( </span><span style='color: white;'>Feedback from caregivers, corrects mistakes, and refines language skills over time</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col3.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>( </span><span style='color: white;'>Correcting errors, and improving translation accuracy based on training data</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            # ________________________________________________________________________________________________________________________

            st.write("")
            st.write("")
            st.write('')
            st.write("")

            col1, col2, col3 = st.columns([1, 15, 2])
            col2.markdown(
                "<h1 style='font-size: 70px;'><span style='color: cyan;'>Practice and Improvement</span> </h1>",
                unsafe_allow_html=True)
            col1, col2 = st.columns([10, 10])
            with col2:
                file = lottie("ml_practice.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=800,
                    key=None
                )
            with col1:
                file = lottie("baby_last.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=800,
                    key=None
                )
            col1, col2, col4, col3 = st.columns([2, 10, 1.7, 10])
            col2.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>( </span><span style='color: white;'>Continually practices speaking and listening to improve language skills</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col3.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'>( </span><span style='color: white;'>Continuously fine-tunes and updates its model with more data</span><span style='color: cyan;'> )</span> </h1>",
                unsafe_allow_html=True)
            col1, col2, col3, = st.columns([5,10,5])

            col2.markdown(
                f"<h1 style='font-size: 30px;'><span style='color: cyan;'> </span> </h1>",
                unsafe_allow_html=True)

        


            colored_header(
                label="",
                description="",
                color_name="blue-green-70"
            )
#____________________________________________________________________________________________________________________________________



# Object Creation

object = language_ai()
object.method()

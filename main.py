import sys
import tkinter
from io import StringIO
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open, SaveAs
import cv2
import numpy as np
import pandas as pd
from PIL import Image

from subprocess import  call
def open_my_file(fileOpen):
    call(["python", fileOpen])

import streamlit as st
from streamlit_option_menu import option_menu

import GiamDanDaoHam.Bai01 as GDDH_01
import GiamDanDaoHam.Bai02 as GDDH_02
import GiamDanDaoHam.Bai02a as GDDH_2a
import GiamDanDaoHam.Bai03 as GDDH_03
import GiamDanDaoHam.Bai04 as GDDH_04
import GiamDanDaoHam.Bai05 as GDDH_05
import GiamDanDaoHam.temp as GDDH_temp
import GiamDanDaoHamMomentum.Bai01 as GDDHM_01

import HoiQuy.Bai01 as HQ_01
import HoiQuy.Bai02 as HQ_02
import HoiQuy.Bai03 as HQ_03
import HoiQuy.Bai04 as HQ_04
import HoiQuy.Bai05 as HQ_05

import Overfitting.Bai01 as OF_01
import Overfitting.Bai02 as OF_02
import Overfitting.Bai03 as OF_03
import Overfitting.Bai04 as OF_04

import SVM.Bai01 as SVM_01
import SVM.Bai02 as SVM_02
import SVM.Bai03 as SVM_03
import SVM.Bai04 as SVM_04

class Main():
    def __init__(self):
        self.initUI()


    def initUI(self):
        with st.sidebar:
            st.sidebar.header="Menu"
            selected = option_menu("Main Menu", ['Giảm dần đạo hàm','Giảm dần đạo hàm momentum',"Hồi quy", "KNN","Overfitting", "SVM"],
                icons=['bookmarks','bookmarks', 'bookmark-star','bookmark-star','bookmark-check','bookmark-check'], menu_icon="grid-1x2-fill", default_index=1)
            selected

        
        if selected=='Giảm dần đạo hàm':
            st.title("Giảm dần đạo hàm")
            col1, col2 = st.columns([0.5, 0.5], gap="large")
            with col1:
                option = st.selectbox("Function", (
                    "None", "Bai01", 'Bai02', "Bai02a", "Bai03", "Bai04", "Bai05","Temp"))

                if option == "None":
                    st.write("Vui lòng chọn option!")
                else:
                    st.write("")
                if option == "Bai01":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Bai02":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Bai02a":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Bai03":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Bai04":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Bai05":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
                if option == "Temp":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")

            with col2:
                if option == "Bai01":
                    GDDH_01.executeThisFunction()
                if option == "Bai02":
                    GDDH_02.executeThisFunction()
                if option == "Bai02a":
                    GDDH_2a.executeThisFunction()
                if option == "Bai03":
                    GDDH_03.executeThisFunction()
                if option == "Bai04":
                    GDDH_04.executeThisFunction()
                if option == "Bai05":
                    GDDH_05.executeThisFunction()
                if option == "Temp":
                    GDDH_temp.executeThisFunction()

        elif selected == 'Giảm dần đạo hàm momentum':
            st.title("Giảm dần đạo hàm momentum")

            col1, col2 = st.columns([0.5, 0.5], gap="large")
            with col1:
                option = st.selectbox("Function", (
                    "None", "Bai01"))

                if option == "None":
                    st.write("Vui lòng chọn option!")
                else:
                    st.write("")
                if option == "Bai01":
                    st.write(
                        "A negative of an image is an image where its lightest areas appear as darkest and the darkest areas appear as lightest.")
                    st.write(
                        "The appearance change from lightest to darkest and darkest to lightest is basically done in gray scale image and refers to the change of pixel intensity values from highest to lowest and lowest to highest.")
            with col2:
                if option == "None":
                    st.write("")
                if option == "Bai01":
                    GDDHM_01.executeThisFunction()


        elif selected=='Hồi quy':
            st.title("Hồi quy")

            col1, col2 = st.columns([0.5, 0.5], gap="large")
            with col1:
                option = st.selectbox("Function", (
                    "None", "Bai01", "Bai02", "Bai03", "Bai04", "Bai05"))
                if option == "None":
                    st.write("Vui lòng chọn option!")
                else:
                    st.write("")
            with col2:
                if option == "None":
                    st.write("")
                if option == "Bai01":
                    HQ_01.executeThisFunction()
                if option == "Bai02":
                    HQ_02.executeThisFunction()
                if option == "Bai03":
                    HQ_03.executeThisFunction()
                if option == "Bai04":
                    HQ_04.executeThisFunction()
                if option == "Bai05":
                    HQ_05.executeThisFunction()

        elif selected == 'KNN':
            st.title("KNN")

            col1, col2 = st.columns([0.5, 0.5], gap="large")
            with col1:
                option = st.selectbox("Function", (
                    "None", "Bai01", "Bai02", "Bai03", "Bai03a", "Bai04", "Bai05"))
                if option == "None":
                    st.write("Vui lòng chọn option!")
                else:
                    st.write("")
            
            with col2:
                if option == "None":
                    st.write("")
                

        elif selected == 'Overfitting':
            st.title("Overfitting")

            col1, col2 = st.columns([0.5, 0.5], gap="large")
            with col1:
                option = st.selectbox("Function", (
                    "None", "Bai01", "Bai02", "Bai03", "Bai04"))
                if option == "None":
                    st.write("Vui lòng chọn option!")
                else:
                    st.write("")
            with col2:
                if option == "None":
                    st.write("")
                if option == "Bai01":
                    OF_01.executeThisFunction()
                if option == "Bai02":
                    OF_02.executeThisFunction()
                if option == "Bai03":
                    OF_03.executeThisFunction()
                if option == "Bai04":
                    OF_04.executeThisFunction()

        elif selected == 'SVM':
            st.title("SVM")

            col1, col2 = st.columns([0.5, 0.5], gap="large")
            with col1:
                option = st.selectbox("Function", (
                    "None", "Bai01", "Bai02", "Bai03", "Bai04"))
                if option == "None":
                    st.write("Vui lòng chọn option!")
                else:
                    st.write("")
            with col2:
                if option == "None":
                    st.write("")
                if option == "Bai01":
                    SVM_01.executeThisFunction()
                if option == "Bai02":
                    SVM_02.executeThisFunction()
                if option == "Bai03":
                    SVM_03.executeThisFunction()
                if option == "Bai04":
                    SVM_04.executeThisFunction()

        else:
            st.title("Nhận diện phép toán")

        #st.file_uploader("Hello", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False, label_visibility="visible")

    # def run(runfile):
    #     with open(runfile, "r") as rnf:
    #         exec(rnf.read())

    def onGiamDanDaoHamBai01(self):
        open_my_file("GiamDanDaoHam\\Bai01.py")
p = Main()
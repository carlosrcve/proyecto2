from django.contrib import admin
from django.urls import path
from .views import homePage, informe_empleado, generate_pdf, generar_informe_word,descargar_word_ruta,descargar_archivo_txt,descargar_archivo_word1,descargar_archivo_word2,prueba,bcv1,descargar_informes_financieros,descargar_excel_ruta,descargar_pdf_ruta

urlpatterns = [
    path('', homePage, name='home'),
    path('informe_empleado/', informe_empleado, name='informe_empleado'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),
    path('generar-informe/', generar_informe_word, name='generar_informe'),
    path('descargar_word_ruta/', descargar_word_ruta, name = "descargar_word_ruta"),
    path('descargar_archivo_txt/', descargar_archivo_txt, name = "descargar_archivo_txt"),
    path('descargar_archivo_word1/', descargar_archivo_word1, name = "descargar_archivo_word1"),
    path('descargar_archivo_word2/', descargar_archivo_word2, name = "descargar_archivo_word2"),
    path('prueba/', prueba, name = "prueba"),
    path('bcv1/', bcv1, name = "bcv1"),
    path('descargar_informes_financieros/', descargar_informes_financieros, name = "descargar_informes_financieros"),
    path('descargar_excel_ruta/', descargar_excel_ruta, name = "descargar_excel_ruta"),
    path('descargar_pdf_ruta/', descargar_pdf_ruta, name = "descargar_pdf_ruta"),
]
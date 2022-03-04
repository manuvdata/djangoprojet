
from django.shortcuts import render, redirect
from .forms import AnnivForm
from bs4 import BeautifulSoup
from nltk import word_tokenize
import os
import pandas as pd
import numpy as np
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, PageBreak
from reportlab.lib.pagesizes import letter



def pb(request):
    return render(request, 'listings/pb.html')

def bravo(request):
    return render(request, 'listings/bravo.html'
                  )


def home(request):
    if request.method == 'POST':
        form = AnnivForm(request.POST, request.FILES)
        if form.is_valid():
            testt= form.save(commit=False)
            ugo = testt.pdf.path
            testt.save()
            try:
                file = open("planningdirect.pdf")
                file.close()
                print("fichier present")
                try:
                    os.remove("planningdirect.pdf")
                    conversion(ugo, "planningdirect.pdf")
                    os.startfile("planningdirect.pdf")
                    os.remove(ugo)
                except PermissionError:
                    print("fichier ouvert")
                    return render(request, 'listings/pb.html')
                return redirect('bravo')
            except FileNotFoundError:
                conversion(ugo, "planningdirect.pdf")
                os.startfile("planningdirect.pdf")
                os.remove(ugo)
                return redirect('bravo')
    else:
        form = AnnivForm()
    return render(request, 'listings/home.html', {'form': form})

def conversion(chemin, sortie):
    filin = open(chemin, 'r', encoding='UTF-8')
    page = filin.read()
    soup = BeautifulSoup(page, "html.parser")
    data = pd.read_html(chemin)
    hh = data[0].columns[0][0]
    tt = soup.find_all("title")
    k = pd.DataFrame(tt)
    jour_anniv = k.values
    base = pd.DataFrame(data[0])
    base.columns = ["Lieux", "Enfant", "S1", "Formule", "Parents", "Details", "Enfants_Commentaire", "S2", "S3", "S4"]
    base.drop(['S1', 'S2', 'S3', 'S4'], axis=1, inplace=True)
    base = base.dropna(subset=['Lieux'])
    l = base['Lieux'].tolist()
    horaire = ['De 10:00 à 12:00', 'De 14:00 à 16:00', 'De 16:30 à 18:30']
    base['des_tok'] = [tokenize(text) for text in (base['Formule'])]
    base['Formule'] = [" ".join(x) for x in base['des_tok']]
    base['des_tok'] = [tokenize(text) for text in (base['Details'])]
    base['Details'] = [" ".join(x) for x in base['des_tok']]
    base.drop('des_tok', axis=1, inplace=True)

    if hh == 'De 10:00 à 12:00':
        heure = []

        if horaire[1] in l:
            ap1 = l.index('De 14:00 à 16:00')
        else:
            ap1 = 100
        ap1

        if horaire[2] in l:
            ap2 = l.index('De 16:30 à 18:30')
        else:
            ap2 = 100

        final = len(base) - ap1 - 2

        if ap2 == 100:
            for i in range(0, ap1):
                heu = 'c1'
                heure.append(heu)
            for i in range(0, 2):
                heu = 'Vide'
                heure.append(heu)
            for i in range(0, final):
                heu = 'c2'
                heure.append(heu)

        if ap2 != 100 and ap1 != 100:
            t2 = ap2 - ap1 - 2
            t3 = len(base) - ap2 - 2

            for i in range(0, ap1):
                heu = 'c1'
                heure.append(heu)
            for i in range(0, 2):
                heu = 'Vide'
                heure.append(heu)
            for i in range(0, t2):
                heu = 'c2'
                heure.append(heu)
            for i in range(0, 2):
                heu = 'Vide'
                heure.append(heu)
            for i in range(0, t3):
                heu = 'c3'
                heure.append(heu)

    if hh == 'De 14:00 à 16:00':
        heure = []


        if horaire[2] in l:
            ap3 = l.index('De 16:30 à 18:30')
        else:
            ap3 = 100

        if ap3 == 100:
            for i in range(0, len(base)):
                heu = 'c2'
                heure.append(heu)

        if ap3 != 100:

            t3 = len(base) - ap3 - 2

            for i in range(0, ap3):
                heu = 'c2'
                heure.append(heu)
            for i in range(0, 2):
                heu = 'Vide'
                heure.append(heu)
            for i in range(0, t3):
                heu = 'c3'
                heure.append(heu)
    if hh == 'De 16:30 à 18:30':
        heure = []
        for i in range(0, len(base)):
            heu = 'c3'
            heure.append(heu)
    print(heure)
    base['heure'] = heure
    base = base.fillna('Inconnu')
    anniv1 = base[base['heure'] == 'c1']
    anniv2 = base[base['heure'] == 'c2']
    anniv3 = base[base['heure'] == 'c3']
    filemane = sortie
    elems = []
    pdf = SimpleDocTemplate(filemane, pagesize=letter, rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)
    col = [55, 50, 90, 200, 205]
    col2 = [120, 120, 120, 120, 120]
    vide = ["", "", "", "", ""]
    styles = getSampleStyleSheet()
    k = jour_anniv.tolist()
    heure = ['De 10:00 à 12:00', 'De 14:00 à 16:00', 'De 16:30 à 18:30']
    XX = [anniv1, anniv2, anniv3]

    for h in range(0, 3):
        anniv = XX[h].drop('heure', axis=1)
        detail = anniv["Enfants_Commentaire"].tolist()
        anniv = anniv.drop('Enfants_Commentaire', axis=1)
        dd = np.array(anniv).tolist()
        idd = anniv.columns.tolist()
        nbanniv = len(anniv)
        k.append([heure[h]])
        kk = k[0][0] + "  " + k[h + 1][0]

        para = Paragraph(kk, style=styles['Normal'])
        j = Table([[kk]])
        style4 = TableStyle(
            [("BACKGROUND", (0, 0), (-1, -1), colors.deepskyblue),
             ("GRID", (0, 0), (-1, -1), 1, colors.black),
             ("FONT", (0, 0), (-1, -1), "Times-BoldItalic", 20),
             ])
        j.setStyle(style4)
        elems.append(j)
        elems.append(Spacer(1, 40))
        nn = 1
        for i in range(0, nbanniv):

            taille = 20
            nbm = len(detail[i])
            if nbm > 65:
                taille = 15
            if nbm > 90:
                taille = 6
            details = Table([[detail[i]]])
            style3 = TableStyle(
                [("BACKGROUND", (0, 0), (-1, -1), colors.aquamarine),
                 ("GRID", (0, 0), (-1, -1), 1, colors.black),
                 ("FONT", (0, 0), (-1, -1), "Times-BoldItalic", taille),
                 ])
            details.setStyle(style3)
            elems.append(details)

            entete = Table([idd], colWidths=col)
            style = TableStyle([("GRID", (0, 0), (-1, -1), 1, colors.black),
                                ("BACKGROUND", (0, 0), (-1, -1), colors.deeppink),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER')
                                ])
            entete.setStyle(style)
            elems.append(entete)
            corps = Table([dd[i]], colWidths=col)
            style2 = TableStyle([("GRID", (0, 0), (-1, -1), 1, colors.black),
                                 ("BACKGROUND", (0, 0), (-1, -1), colors.yellow)
                                 ])
            corps.setStyle(style2)
            elems.append(corps)

            for i in range(1, 4):
                vid = Table([vide], colWidths=col2)
                style3 = TableStyle([("GRID", (0, 0), (-1, -1), 1, colors.black),
                                     ("BACKGROUND", (0, 0), (-1, -1), colors.beige)
                                     ])
                vid.setStyle(style3)
                elems.append(vid)

            elems.append(Spacer(1, 20))
            nn = 1 + nn
            if nn % 6 == 0:
                elems.append(PageBreak())
                elems.append(j)
                elems.append(Spacer(1, 40))
        elems.append(PageBreak())
    pdf.build(elems)


def tokenize(text):
    stop_words = ['Formule', 'Gâteaux', 'Gâteau', 'Anniversaires', 'Thème', 'déco']
    res = word_tokenize(text, language='english')
    res = [token for token in res if token not in stop_words]
    return res







import aspose.pdf as ap
def create_pdf():
    # Initialiser l'objet document
    document = ap.Document()

    # Ajouter une page
    page = document.pages.add()

    # Initialiser l'objet textfragment
    text_fragment = ap.text.TextFragment("Hello,world! bien ou bien ? ")

    # Ajouter un fragment de texte à une nouvelle page
    page.paragraphs.add(text_fragment)

    # Enregistrer le PDF mis à jour
    document.save("test.pdf")

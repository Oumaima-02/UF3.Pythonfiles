MSG="Introdueix el teu nom:"
MSG2="Introdueix el teu cognom:"
MSG3="Introdueix la teva edat:"
MSG4="Indica la tecnologia que vols: "
T1="1.Tecnologia flexible."
T2="2.Tecnologia fija."
T3="3.Tecnologia blanda."
T4="4.Tecnologia dura."
T5="5.Tecnologia limpia"
def identificador(nom,cognom):
    NOM=nom.upper()[:2]
    COGNOM=cognom.upper()[0]+cognom.upper()[len(cognom)-1]
    return NOM,COGNOM





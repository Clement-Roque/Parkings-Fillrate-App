parking_labels_to_filenames = {
    'Antigone': 'FR_MTP_ANTI.xml',
    'Comédie': 'FR_MTP_COME.xml',
    'Corum': 'FR_MTP_CORU.xml',
    'Europa': 'FR_MTP_EURO.xml',
    'Foch': 'FR_MTP_FOCH.xml',
    'Gambetta': 'FR_MTP_GAMB.xml',
    'Gare': 'FR_MTP_GARE.xml',
    'du Triangle': 'FR_MTP_TRIA.xml',
    'Arc de Triomphe': 'FR_MTP_ARCT.xml',
    'Pitot': 'FR_MTP_PITO.xml',
    'Circe': 'FR_MTP_CIRC.xml',
    'Sabines': 'FR_MTP_SABI.xml',
    'Garcia Lorca': 'FR_MTP_GARC.xml',
    'Sablassou': 'FR_MTP_SABL.xml',
    'Mosson': 'FR_MTP_MOSS.xml',
    'Saint Jean Le Sec': 'FR_STJ_SJLC.xml',
    'Euromédecine': 'FR_MTP_MEDC.xml',
    'Occitanie': 'FR_MTP_OCCI.xml',
    'Vicarello': 'FR_CAS_VICA.xml',
    'Gaumont EST': 'FR_MTP_GA109.xml',
    'Gaumont OUEST': 'FR_MTP_GA250.xml',
    'Charles de Gaulle': 'FR_CAS_CDGA.xml',
}

parking_labels = [
    'Antigone',
    'Comédie',
    'Corum',
    'Europa',
    'Foch',
    'Gambetta',
    'Gare',
    'du Triangle',
    'Arc de Triomphe',
    'Pitot',
    'Circe',
    'Sabines',
    'Garcia Lorca',
    'Sablassou',
    'Mosson',
    'Saint Jean Le Sec',
    'Euromédecine',
    'Occitanie',
    'Vicarello',
    'Gaumont EST',
    'Gaumont OUEST',
    'Charles de Gaulle',
]

parking_fields = ['DateTime', 'Name', 'Status', 'Free', 'Total']
PARKING_URL = "http://data.montpellier3m.fr/sites/default/files/ressources/"
parking_json_schema = {
    "type": "object",
    "properties": {
        "Name": {"type": "string"},
        "Status": {"type": "string"},
        "Free": {"type": "number"},
        "Total": {"type": "number"},
        "DateTime": {"type": "string"},
    },
    "required": ["Name", "Status", "Free", "Total", "DateTime"]
}

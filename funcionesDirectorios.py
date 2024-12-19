import json

def abrirBase ():
    with open('./campuslands.json', 'r') as abrir:
        baseDatos = json.load(abrir)
    return (baseDatos)
 
def guardarBase (base):
    with open('./campuslands.json', 'w') as abrir:
        json.dump(base, abrir, indent=4)

def contarCampers ():
    base = abrirBase()
    cantidadCampers = len(base['Campers'])
    return (cantidadCampers)

def contarRutas ():
    base = abrirBase()
    cantidadRutas = len(base['rutasEntrenamiento'])
    return (cantidadRutas)

def contarTrainers ():
    base = abrirBase()
    cantidadTrainers = len(base['trainers'])
    return (cantidadTrainers)

def contarGrupos ():
    base = abrirBase()
    cantidadGrupos = len(base['grupos'])
    return (cantidadGrupos)

def buscarTrainer (numIdentificacionTrainer):
    base = abrirBase()
    for trainerid, trainer in base["trainers"].items():
        if trainer["numIdentificacion"] == numIdentificacionTrainer:
            return(trainer["nombresTrainer"] + " " + trainer["apellidosTrainer"])
    else :
        print (f'El id {numIdentificacionTrainer} no Fue encontrado en la base de datos.')
    
def buscarCamper (numIdentificacionCamper):
    base = abrirBase()
    for camperid, camper in base['Campers'].items():
        if camper['numIdentificacion'] == numIdentificacionCamper:
            return(camper["nombres"] + " " + camper["apellidos"])
    else :
        print (f'El id {numIdentificacionCamper} no Fue encontrado en la base de datos.')

def validarHorarioDis (salonbus):
    base = abrirBase()
    horarioDis = []
    for salon, franja in base['infraestructura'].items():
        if salon == salonbus:
            if franja['1AM'] == 'ninguno':
                horarioDis.append("1AM")
            if franja['2AM'] == 'ninguno':
                horarioDis.append("2AM")
            if franja['1PM'] == 'ninguno':
                horarioDis.append("1PM")
            if franja['2PM'] == 'ninguno':
                horarioDis.append("2PM")
    return(horarioDis)
 
def validarGrupo(grupo):
    base = abrirBase()
    for nombreGrupo, dirGrupos in base['grupos'].items():
        if nombreGrupo == grupo:
            return(True)
    return(False)

def validarRutasTrainer(trainer):
    base = abrirBase()
    for nombreTrainer, dirTrainer in base['trainers'].items():
        if dirTrainer['numIdentificacion'] == trainer:
           return(dirTrainer['rutasEntrenamiento'])

def ValidarRutasDispo():
    base = abrirBase()
    rutasDis = []
    for nombreRuta, dirRuta in base ['rutasEntrenamiento'].items():
        rutasDis.append(dirRuta)
    return(rutasDis)
      






    






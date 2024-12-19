import json
import modulos.funcionesDirectorios as fdir
import modulos.mensajes as msg
import modulos.menus as menu
import utils.ctrlActions as ctrl
    
def agregarCamper ():
    ctrl.borrar_pantalla()
    print('Favor ingresar los siguientes datos: ')
    numIdentificacion = input('Numero de indentificacion (Solo numeros): ')
    nombres = input('Nombres: ')
    apellidos = input('Apellidos: ')
    direccion = input('Direccion: ')
    acudiente = input('Nombre del acudiente (menor de 18 años) ó Contacto de Emergencia (mayor de 18 años): ')
    celular = input('Celular: ')
    fijo = input('Telefono Fijo: ')
    nuevoCamper = {
        "numIdentificacion" : numIdentificacion,
        "nombres" : nombres,
        "apellidos" : apellidos,
        "direccion" : direccion,
        "acudiente" : acudiente,
        "celular" : celular,
        "fijo" : fijo,
        "estado" : "Inscrito",
        "grupo" :"Ninguno",
        "riesgo" : "Ninguno",
        "notasIngreso" : [ ],
        "notas" : {
            "mod1" : {
                "quisTrab" : [ ],
                "proyecto" : 0,
                "examen" : 0,
                "notaModulo": 0
            },
            "mod2" : {
                "quisTrab" : [ ],
                "proyecto" : 0,
                "examen" : 0,
                "notaModulo": 0
            },
            "mod3" : {
                "quisTrab" : [ ],
                "proyecto" : 0,
                "examen" : 0,
                "notaModulo": 0
            },
            "mod4" : {
                "quisTrab" : [ ],
                "proyecto" : 0,
                "examen" : 0,
                "notaModulo": 0
            },
            "mod5" : {
                "quisTrab" : [ ],
                "proyecto" : 0,
                "examen" : 0,
                "notaModulo": 0
            },
            "mod6" : {
                "quisTrab" : [ ],
                "proyecto" : 0,
                "examen" : 0,
                "notaModulo": 0
            },
            "mod7" : {
                "quisTrab" : [ ],
                "proyecto" : 0,
                "examen" : 0,
                "notaModulo": 0
            },
            "mod8" : {
                "quisTrab" : [ ],
                "proyecto" : 0,
                "examen" : 0,
                "notaModulo": 0
            },
            "mod9" : {
                "quisTrab" : [ ],
                "proyecto" : 0,
                "examen" : 0,
                "notaModulo": 0
            },
            "mod10" : {
                "quisTrab" : [ ],
                "proyecto" : 0,
                "examen" : 0,
                "notaModulo": 0
            },
            "notaFinal": 0
        }
    }
    numeroCampers = fdir.contarCampers()
    nombreCamper = "camper" + str(numeroCampers)
    with open('./campuslands.json', 'r+') as abrir:
        baseDatos = json.load(abrir)
        baseDatos['Campers'][nombreCamper] = nuevoCamper
        abrir.seek(0)
        json.dump(baseDatos, abrir, indent=4)
    print(msg.mensajeNuevoCamper)
    ctrl.borrar_pantalla()
    print(f'Su usuario es: {nombreCamper} y su contraseña es: {numIdentificacion}')

def calificarNuevoCamper ():
    ctrl.borrar_pantalla()
    print('Favor ingresar el numero de identificacion del Camper que desea ingresar sus notas de ingreso: ')
    id = input('/: ')
    baseDatos = fdir.abrirBase()
    for camperDatos, camper in baseDatos['Campers'].items():
        if camper['numIdentificacion'] == id:
            notaTeorica = int(input('Favor Ingresar la Nota Teorica: '))
            notaPractica = int(input('Favor Ingresar la Nota Practica: '))
            notasNuevas = [ notaTeorica, notaPractica]
            baseDatos['Campers'][camperDatos]['notasIngreso'].extend(notasNuevas)
            print("Las notas del Camper fueron ingresadas correctamente")
            print(f"Notas de ingreso actualizadas para {camper['nombres']} {camper['apellidos']}.")
            if (notaTeorica + notaPractica) >= 60:
                nuevoEstado = 'Aprobado'
                camper['estado'] = nuevoEstado
                print(f"El estado del camper {camper['nombres']} {camper['apellidos']} cambio a Aprobado")
            else:
                nuevoEstado = 'Rechazado'
                camper['estado'] = nuevoEstado
                print(f"El estado del camper {camper['nombres']} {camper['apellidos']} cambio a Rechazado")
    fdir.guardarBase(baseDatos)

def agregarTrainer ():
    ctrl.borrar_pantalla()
    baseDatos = fdir.abrirBase()
    print('Favor ingresar los siguientes datos: ')
    numIdentificacion = input('Numero de indentidifacion (Solo numeros): ')
    nombres = input('Nombres: ')
    apellidos = input('Apellidos: ')
    direccion = input('Direccion: ')
    celular = input('Celular: ')
    fijo = input('Telefono Fijo: ')
    print (f'Ingrese la ruta de entrenamiento que maneja el trainer entre la siguiente lista:\n{[baseDatos["rutasEntrenamiento"]]}')
    rutas = input(':/ ')  
    nuevoTrainer ={   
            "numIdentificacion": numIdentificacion,
            "nombresTrainer": nombres,
            "apellidosTrainer": apellidos,
            "direccionTrainer": direccion,
            "celularTrainer": celular,
            "telFijoTrainer": fijo,
            "estadoTrainer": "Activo",
            "rutasEntrenamiento": [rutas]
    }
    numeroTrainers = fdir.contarTrainers()
    nombreTrainer = "trainer" + str(numeroTrainers)
    with open('./campuslands.json', 'r+') as abrir:
        baseDatos = json.load(abrir)
        baseDatos['trainers'][nombreTrainer] = nuevoTrainer
        abrir.seek(0)
        json.dump(baseDatos, abrir, indent=4)
    ctrl.borrar_pantalla()
    print(f'Su usuario es: {nombreTrainer} y su contraseña es: {numIdentificacion}')

def agregarRutas ():
    ctrl.borrar_pantalla()
    print('Favor ingresar el Nombre de la nueva Ruta de Aprendizaje: ')
    numeroRutas = fdir.contarRutas()
    nombreRuta = "ruta" + str(numeroRutas+1)
    nuevaRuta = input('/: ')
    baseDatos = fdir.abrirBase()
    baseDatos['rutasEntrenamiento'][nombreRuta] = nuevaRuta
    fdir.guardarBase(baseDatos)
    print('La nueva Ruta Se Agrego Correctamente ')

def eliminarRutas ():
    ctrl.borrar_pantalla()
    print('Favor ingresar el Nombre de la Ruta de Aprendizaje que desea eliminar: ')
    rutaEliminar = input('/: ')
    baseDatos = fdir.abrirBase()
    for RutasDatos, ruta in baseDatos['rutasEntrenamiento'].items():
        if rutaEliminar in baseDatos["rutasEntrenamiento"][RutasDatos]:
            del baseDatos["rutasEntrenamiento"][RutasDatos]
            print(f'La Ruta: {rutaEliminar} se a eliminado de las rutas de aprendizaje disponibles en Campus Lands')
            fdir.guardarBase(baseDatos)
            break
    else :
        print(f'La Ruta: {rutaEliminar} no existe las rutas de aprendizaje disponibles en Campus Lands actualmente')

def agregarGrupo():
    ctrl.borrar_pantalla()
    print('Favor ingresar los siguientes datos: ')
    trainerAsignado = input('Numero de indentidifacion del Trainer del grupo: ')
    nombreTrainer = fdir.buscarTrainer(trainerAsignado)
    print (f'Se asignara el Trainer: {nombreTrainer} ')
    print(msg.MensajeSalones)
    salon = input('Salon: ')
    print(msg.MensajeHorarios)
    horarioDis = fdir.validarHorarioDis(salon)
    print(f'Los horarios disponibles en el salon: {horarioDis} elija alguno: ')
    horario = input('horario: ')
    rutasDisponibles = fdir.validarRutasTrainer(trainerAsignado) 
    print(f'Las rutas de entrenamiento del trainer: {nombreTrainer} son: {rutasDisponibles} elija alguno: ')
    ruta = input('Ruta: ')
    nuevoGrupo = {
            "LimCampers": 33,
            "trainerAsignado": trainerAsignado,
            "salon": salon,
            "horario": horario,
            "ruta": ruta,
            "campers": []
        }
    numeroGrupos = fdir.contarGrupos()
    nombreGrupo = "grupo" + str(numeroGrupos)
    cambioEstadoHorario(salon, horario, nombreGrupo)
    with open('./campuslands.json', 'r+') as abrir:
        baseDatos = json.load(abrir)
        baseDatos['grupos'][nombreGrupo] = nuevoGrupo
        abrir.seek(0)
        json.dump(baseDatos, abrir, indent=4)

def validarEstado(camperId):
    base = fdir.abrirBase()
    for campers, camper in base["Campers"].items():
        if camper["numIdentificacion"] == camperId:
            return (camper["estado"])
    else:
        print(f'El {camperId} ingresado no corresponde a algun camper inscrito')

def cambioEstadoHorario (salonMod, franjaCam, grupoAsig):
    base = fdir.abrirBase()
    for salon, franja in base['infraestructura'].items():
        if salon == salonMod:
            franja[franjaCam] = grupoAsig
    print(f'Se realizo el cambio en el Salon: {salonMod} en Franja: {franjaCam} el grupos asignado al: {grupoAsig}')
    fdir.guardarBase(base)

def cambioEstadoCamper(id, nuevoEstado):
    base = fdir.abrirBase()
    estado = validarEstado(id)
    match estado:
        case 'Aprobado':
            for camperDatos, camper in base['Campers'].items():
                if camper['numIdentificacion'] == id:
                    camper['estado'] = nuevoEstado
                    fdir.guardarBase(base)
                    break
        case 'Cursando':
            for camperDatos, camper in base['Campers'].items():
                if camper['numIdentificacion'] == id:
                    camper['estado'] = nuevoEstado
                    fdir.guardarBase(base)
                    break
        case 'Inscrito':
            print(f'El camper:{id} esta pendiente calificar prubeas de ingreso')
            ctrl.pausar_pantalla()

def trabajarNotas():
    print('Favor ingresar el numero de identificacion del Camper para trabajar Notas: ')
    id = input('/: ')
    camper = fdir.buscarCamper(id)
    estado = validarEstado(id)
    match estado:
        case 'Cursando':
            print(f'Se trabajaran las notas del Camper: {camper}')
            print('Favor Ingresar el modulo que desea trabajar notas')
            modulo = "mod" + (input(':/ '))
            print(menu.menuTrainerNotas)
            opcionPrincipal = int(input(':/ '))
            match opcionPrincipal:
                case 1:
                    agregarNotasCamper(modulo,id)
                case 2:
                    modificarNotasCamper(modulo,id)   
                case _:
                    ctrl.borrar_pantalla()
                    print(msg.mensajeError)
                    ctrl.pausar_pantalla()
        case _:
            print(f'El estado del camper {camper} es: {estado} no se puede trabajar sus notas')
            ctrl.pausar_pantalla()

def agregarCampersGrupo():
    ctrl.borrar_pantalla()
    base = fdir.abrirBase()
    isValid =  True
    while (isValid):
        print('Favor Ingrese el nombre del grupo que desea agregar Campers: ')
        grupo = input('/: ')
        estadoGrupo = fdir.validarGrupo(grupo)
        match estadoGrupo:
            case False:
                print(f'El {grupo} no existe')
                ctrl.pausar_pantalla()
                break
            case True:
                pass
        for nombreGrupo, dirGrupo in base['grupos'].items():
            if nombreGrupo == grupo:
                if dirGrupo['LimCampers'] > 0:
                    print('Favor Ingrese el numero de identificacion del Camper que desea agregar: ')
                    camper = input('/: ')
                    estado = validarEstado(camper)
                    match estado:
                        case 'Aprobado':
                            dirGrupo['campers'].append(camper)
                            dirGrupo['LimCampers'] -= 1
                            salir = int(input('Ingrese "1" si desea continuar ingresando campers o "2" si desea salir: '))
                            match salir:
                                case 1:
                                    pass
                                case 2:
                                    fdir.guardarBase(base)
                                    isValid = False
                        case _:
                            print(f'El estado del camper es: {estado} no es apto para agregar a grupo ')
                else:
                    print('Se alcanzo el limite de campers en el grupo indicado')
                    isValid = False
        nuevoEstado = 'Cursando'
        cambioEstadoCamper(camper, nuevoEstado)

def agregarNotasCamper(modulo, id):
    base = fdir.abrirBase()
    ctrl.borrar_pantalla()
    print(menu.menuTrainerAgregarNotas)
    opcionSeg = int(input(':/ '))
    match opcionSeg:
        case 1:
            for camperDatos, camper in base['Campers'].items():
                if camper['numIdentificacion'] == id:
                    print('Favor Ingresar la nota del Quis o trabajo')
                    nota = int(input(':/ '))
                    camper['notas'][modulo]['quisTrab'].append(nota)
                    fdir.guardarBase(base)
                    print('La nota se agrego correctamente')
                    ctrl.pausar_pantalla()
        case 2:
            for camperDatos, camper in base['Campers'].items():
                if camper['numIdentificacion'] == id:
                    print('Favor Ingresar la nota del Proyecto')
                    nota = int(input(':/ '))
                    camper['notas'][modulo]['proyecto'] = nota
                    fdir.guardarBase(base)
                    print('La nota se agrego correctamente')
                    ctrl.pausar_pantalla()
        case 3:
            for camperDatos, camper in base['Campers'].items():
                if camper['numIdentificacion'] == id:
                    print('Favor Ingresar la nota del examen')
                    nota = int(input(':/ '))
                    camper['notas'][modulo]['examen'] = nota
                    fdir.guardarBase(base)
                    print('La nota se agrego correctamente')
                    ctrl.pausar_pantalla()
        case _:
            ctrl.borrar_pantalla()
            print(msg.mensajeError)
            ctrl.pausar_pantalla()

def modificarNotasCamper(modulo,id):
    base = fdir.abrirBase()
    ctrl.borrar_pantalla()
    print(menu.menuTrainerModificarNotas)
    opcionSeg = int(input(':/ '))
    match opcionSeg:
        case 1:
            for camperDatos, camper in base['Campers'].items():
                if camper['numIdentificacion'] == id:
                    print('Favor Ingresar el numero del Quis o trabajo que desea modificar')
                    posicion = int(input(':/ '))
                    print('Favor Ingresar la nota del Quis o trabajo')
                    nota = int(input(':/ '))
                    camper['notas'][modulo]['quisTrab'][posicion] = nota
                    fdir.guardarBase(base)
                    print('La nota se modifico correctamente')
                    ctrl.pausar_pantalla()
        case 2:
            for camperDatos, camper in base['Campers'].items():
                if camper['numIdentificacion'] == id:
                    print('Favor Ingresar la nota del Proyecto')
                    nota = int(input(':/ '))
                    camper['notas'][modulo]['proyecto'] = nota
                    fdir.guardarBase(base)
                    print('La nota se modifico correctamente')
                    ctrl.pausar_pantalla()
        case 3:
            for camperDatos, camper in base['Campers'].items():
                if camper['numIdentificacion'] == id:
                    print('Favor Ingresar la nota del examen')
                    nota = int(input(':/ '))
                    camper['notas'][modulo]['examen'] = nota
                    fdir.guardarBase(base)
                    print('La nota se modifico correctamente')
                    ctrl.pausar_pantalla()
        case _:
            ctrl.borrar_pantalla()
            print(msg.mensajeError)
            ctrl.pausar_pantalla()

def validarInicioSesion(tipo:int, usuario, contraseña):
    base = fdir.abrirBase()
    match tipo:
        case 1:
            for campers, camper in base['Campers'].items():
                if camper["numIdentificacion"] == contraseña and campers == usuario:
                    print(f'Su estado es: {camper["estado"]} Accceso concedido camper: {camper["nombres"]} {camper["apellidos"]}') 
                    ctrl.pausar_pantalla()
                    return(1)
            print('Usuario y/o Contraseña no coniciden o no existen')
            ctrl.pausar_pantalla()
            return(4)
        case 2:
            for trainers, trainer in base['trainers'].items():
                if trainer["numIdentificacion"] == contraseña and trainers == usuario:
                    print(f'Su estado es: {trainer["estadoTrainer"]} Accceso concedido Trainer: {trainer["nombresTrainer"]} {trainer["apellidosTrainer"]}')
                    ctrl.pausar_pantalla() 
                    return(2)
            print('Usuario y/o Contraseña no coniciden o no existen')
            ctrl.pausar_pantalla()
            return(4)
        case 3:
            for cordinadores, cordinador in base['coordinadores'].items():
                if cordinador["numIdentificacion"] == contraseña and cordinadores == usuario:
                    print(f'Su estado es: {cordinador["estadoCoordinador"]} Accceso concedido Trainer: {cordinador["nombresCoordinador"]} {cordinador["apellidosCoordinador"]}') 
                    ctrl.pausar_pantalla()
                    return(3)
            print('Usuario y/o Contraseña no coniciden o no existen')
            ctrl.pausar_pantalla()
            return(4)
        case _:
            pass

def calificarModulo():
    base = fdir.abrirBase()
    print('Favor ingresar el numero de identificacion del Camper para calificar modulo: ')
    id = input('/: ')
    camper = fdir.buscarCamper(id)
    estado = validarEstado(id)
    match estado:
        case 'Cursando':
            print(f'Se trabajaran el modulo del Camper: {camper}')
            print('Favor Ingresar el modulo que desea calificar')
            modulo = "mod" + (input(':/ '))
            for camperNum, dirCamper in base['Campers'].items():
                if dirCamper['numIdentificacion'] == id:
                    notaQuisLista = dirCamper['notas'][modulo]["quisTrab"]
                    sumaNotasQT = sum(notaQuisLista)
                    cantidadNotasQT = len(notaQuisLista)
                    notaQuis= sumaNotasQT/cantidadNotasQT
                    notaProyecto:int = dirCamper['notas'][modulo]["proyecto"]
                    notaExamen:int = dirCamper['notas'][modulo]["examen"]
                    notaMod = (notaQuis*0.1)+(notaProyecto*0.6)+(notaExamen*0.3)
                    dirCamper['notas'][modulo]['notaModulo'] = notaMod
                    fdir.guardarBase(base)
                    print(f'La nota del modulo {modulo} es: {notaMod} guardada correctamente')
                    ctrl.pausar_pantalla()
        case _:
            print(f'El estado del camper {camper} es: {estado} no se puede trabajar sus notas')
            ctrl.pausar_pantalla()

def finalizarCurso():
    base = fdir.abrirBase()
    print('Favor ingresar el numero de identificacion del Camper para finalizar curso: ')
    id = input('/: ')
    camper = fdir.buscarCamper(id)
    estado = validarEstado(id)
    notaFinal = 0
    match estado:
        case 'Cursando':
            for camperNum, dirCamper in base['Campers'].items():
                if dirCamper['numIdentificacion'] == id:
                    if (dirCamper['notas']["mod10"]['notaModulo'] > 0):
                        for i in range(1, 11, 1):
                            modulo = "mod" + str(i)
                            notaModulo = dirCamper['notas'][modulo]['notaModulo']
                            notaFinal += notaModulo
                        else:
                            notaFinal = notaFinal / 10 
                            dirCamper['notas']['notaFinal'] = notaFinal
                            fdir.guardarBase(base)
                            if notaFinal > 60:
                                nuevoEstado = 'Graduado'
                                cambioEstadoCamper(id, nuevoEstado)
                                print(f'El camper {id} cambio su estado a Graduado')
                                ctrl.pausar_pantalla()
                            elif notaFinal < 60 and notaFinal > 0:
                                nuevoEstado = 'Reprobado'
                                cambioEstadoCamper(id, nuevoEstado)
                                print(f'El camper {id} cambio su estado a Reprobado')
                                ctrl.pausar_pantalla()          
        case _:
            print(f'El estado del camper {camper} es: {estado} no se puede trabajar sus notas')
            ctrl.pausar_pantalla()

def datosPersonalesCamper(camperId):
    ctrl.borrar_pantalla()
    base = fdir.abrirBase()
    for camper, dirCamper, in base['Campers'].items():
        if dirCamper ["numIdentificacion"] == camperId:
            print(f"nombre:{dirCamper['nombres']}\n apellidos:{dirCamper['apellidos']}\n Numero de identificacion: {dirCamper['numIdentificacion']} \n direccion: {dirCamper['direccion']} \n acudiente: {dirCamper['acudiente']} \n celular: {dirCamper['celular']} \n fijo: {dirCamper['fijo']}")






    

import utils.ctrlActions as ctrl
import modulos.menus as menu
import modulos.mensajes as msg
import modulos.funcionesDirectorios as fdir

def moduloReportes():
    while(True):
        base = fdir.abrirBase()
        print(menu.menuModuloDeReportes)
        opcionPrincipal = int(input(':/'))
        match opcionPrincipal:
            case 1: #Lista Campers Por Estado 
                ctrl.borrar_pantalla()
                print(msg.MensajeEstadosCampers)
                print('Ingrese de la lista anterior el estado que quiere generar la lista')
                estado = input('/: ')
                print(f'Lista Campers Por {estado}:\n')
                for nomCamper, dirCamper in base['Campers'].items():
                    if dirCamper['estado'] == estado:
                        print(f'Nombre: {dirCamper["nombres"]} {dirCamper["apellidos"]}\nNumero Documento: {dirCamper["numIdentificacion"]}\n')
                ctrl.pausar_pantalla()

            case 2: #Lista de Trainers Activos
                ctrl.borrar_pantalla()
                print(msg.MensajeEstadosTrainer)
                print('Ingrese de la lista anterior el estado que quiere generar la lista')
                estado = input('/: ')
                print(f'Lista Trainers Por {estado}:\n')
                for nomTrainer, dirTrainer in base['trainers'].items():
                    if dirTrainer['estadoTrainer'] == estado:
                        print(f'Nombre: {dirTrainer["nombresTrainer"]} {dirTrainer["apellidosTrainer"]}\nNumero Documento: {dirTrainer["numIdentificacion"]}\n')
                ctrl.pausar_pantalla()

            case 3: #Lista Campers con Bajo Rendimiento
                ctrl.borrar_pantalla()
                notaAcomulada = 0
                print(f'Lista Campers con Bajo Rendimiento:\n')
                for nomCamper, dirCamper in base['Campers'].items():                   
                    for i in range(1, 11, 1):
                        modulo = "mod" + str(i)
                        notaModulo = dirCamper['notas'][modulo]['notaModulo']
                        if notaModulo > 0:
                            notaAcomulada += notaModulo
                    if notaAcomulada < 60:
                        print(f'Nombre: {dirCamper["nombres"]} {dirCamper["apellidos"]}\nNumero Documento: {dirCamper["numIdentificacion"]}\nNota Acomulativa: {notaAcomulada}\n')
                ctrl.pausar_pantalla()

            case 4: #Lista Campers ó Trainers en una Ruta 
                ctrl.borrar_pantalla()
                rutasDis = fdir.ValidarRutasDispo()
                print(f'Las rutas disponibles son: {rutasDis}')
                print('Ingrese de las opciones anteriores la Ruta que quiere generar la lista')
                ruta = input('/: ')
                print('Si desea generar la lista para Trainers ingrese "1" para Campers ingrese "2"')
                opcion2 = int(input('/: '))
                match opcion2:
                    case 1:
                        print(f'Lista Trainers en ruta {ruta}:\n')
                        for nomTrainer, dirTrainer in base['trainers'].items():
                            rutasTrainer = fdir.validarRutasTrainer(dirTrainer['numIdentificacion'])
                            for rutas in rutasTrainer:
                                if rutas == ruta:
                                    print(f'Nombre: {dirTrainer["nombresTrainer"]} {dirTrainer["apellidosTrainer"]}\nNumero Documento: {dirTrainer["numIdentificacion"]}\n\n')
                        ctrl.pausar_pantalla()
                    case 2:
                        print(f'Lista Campers en ruta {ruta}:\n')
                        for nomGrupo, dirGrupo in base['grupos'].items():
                            if  dirGrupo['ruta'] == ruta:
                                campersGrupo = dirGrupo['campers']
                                for camperG in campersGrupo:
                                    nombreCamper = fdir.buscarCamper(camperG)
                                    print(f'Nombre: {nombreCamper}\nNumero Documento: {camperG}\n\n')
                        ctrl.pausar_pantalla()
                    case _:
                        ctrl.borrar_pantalla()
                        print(msg.mensajeError)
                        ctrl.pausar_pantalla()

            case 5: #Lista Campers Aprobaron ó Reprobaron por Ruta
                ctrl.borrar_pantalla()
                rutasDis = fdir.ValidarRutasDispo()
                print(f'Las rutas disponibles son: {rutasDis}')
                print('Ingrese de las opciones anteriores la Ruta que quiere generar la lista')
                ruta = input('/: ')




        

            


import utils.ctrlActions as ctrl
import modulos.mensajes as msg
import modulos.menus as menu
import modulos.funcionalidades as fun

def moduloTRainers ():
        ctrl.borrar_pantalla()
        print(menu.menuTrainerPrincipal)
        opcionPrincipal = int(input(':/ '))
        match opcionPrincipal:
            case 1:
                ctrl.borrar_pantalla()
                print(menu.menuTrainerGrupos)
                ctrl.pausar_pantalla()
            case 2:
                ctrl.borrar_pantalla()
                fun.trabajarNotas()
            case 3:
                ctrl.borrar_pantalla()
                print(msg.mensajeSalida)
                ctrl.pausar_pantalla()
                exit()
            case _:
                ctrl.borrar_pantalla()
                print(msg.mensajeError)
                ctrl.pausar_pantalla()
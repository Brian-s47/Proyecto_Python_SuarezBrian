import utils.ctrlActions as ctrl
import modulos.menus as menu
import modulos.funcionalidades as fun
import modulos.mensajes as msg

def moduloCampers():
    while(True):
        ctrl.borrar_pantalla()
        print(menu.menuCampersIngreso)
        opcion = int(input(':/'))
        match opcion:
            case 1:
                ususario = input('Ingrese su usuario: ')
                contraseña = input('Ingrese su contraseña: ')
                camperId = contraseña
                fun.validarInicioSesion(opcion, ususario,contraseña)
                ctrl.borrar_pantalla()
                print(menu.menuInformacion)               
                fun.datosPersonalesCamper(camperId)
                ctrl.pausar_pantalla()
            case 2: 
                ctrl.borrar_pantalla()
                fun.agregarCamper()
                ctrl.pausar_pantalla()
            case 3:
                ctrl.borrar_pantalla()
                print(msg.mensajeSalida)
                ctrl.pausar_pantalla()
                exit()
            case _:
                ctrl.borrar_pantalla()
                print(msg.mensajeError)
                ctrl.pausar_pantalla()





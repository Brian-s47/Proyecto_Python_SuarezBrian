import utils.ctrlActions as ctrl
import modulos.mensajes as msg
import modulos.menus as menu
import modulos.moduloCampers as mCam
import modulos.moduloCordinador as mCor
import modulos.moduloTrainers as mTra
import modulos.funcionalidades as fun
if __name__ == '__main__':
    while(True):
        ctrl.borrar_pantalla()
        print(msg.mensajeInicial)
        print(menu.menuLogin)
        opcionTipo = int(input('/: '))
        if opcionTipo == 1:
            ctrl.borrar_pantalla()
            mCam.moduloCampers()
        else: 
            ususario = input('Ingrese su usuario: ')
            contraseña = input('Ingrese su contraseña: ')
            opcionPrincipal = fun.validarInicioSesion(opcionTipo, ususario,contraseña)
        match opcionPrincipal:
            case 1:
                ctrl.borrar_pantalla()
                mCam.moduloCampers()
            case 2:
                ctrl.borrar_pantalla()
                mTra.moduloTRainers() 
            case 3:
                ctrl.borrar_pantalla()
                mCor.moduloCordinador()
            case 4: 
                ctrl.borrar_pantalla()
                print(msg.mensajeSalida)
                ctrl.pausar_pantalla()
                break
            case _:
                ctrl.borrar_pantalla()
                print(msg.mensajeError)
                ctrl.pausar_pantalla()

        
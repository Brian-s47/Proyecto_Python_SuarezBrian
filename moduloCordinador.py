import utils.ctrlActions as ctrl
import modulos.menus as menu
import modulos.mensajes as msg
import modulos.funcionalidades as fun
import modulos.moduloReportes as mrep

def moduloCordinador():
    ctrl.borrar_pantalla()
    print(menu.menuCordinadorPrincipal)
    opcion = int(input(':/'))
    match opcion:
        case 1:
            ctrl.borrar_pantalla()
            fun.calificarNuevoCamper()
            ctrl.pausar_pantalla()
        case 2:
            ctrl.borrar_pantalla()
            print(menu.menuCordinadorGrupos)
            opcion1 = int(input('/: '))
            match opcion1:
                case 1:
                    ctrl.borrar_pantalla()
                    fun.agregarGrupo()
                    ctrl.pausar_pantalla()
                case 2:
                    ctrl.borrar_pantalla()
                    fun.agregarCampersGrupo()
                case 3:
                    ctrl.borrar_pantalla()
                    ctrl.pausar_pantalla()
                case _:
                    ctrl.borrar_pantalla()
                    print(msg.mensajeError)
                    ctrl.pausar_pantalla()
        case 3:
            ctrl.borrar_pantalla()
            print(menu.menuCordinadorCampers)
            opcion1 = int(input('/: '))
            match opcion1:
                case 1:
                    ctrl.borrar_pantalla()
                    fun.trabajarNotas()
                case 2:
                    ctrl.borrar_pantalla()
                    ctrl.pausar_pantalla()
                case 3:
                    ctrl.borrar_pantalla()
                    fun.calificarModulo()
                case 4:
                    ctrl.borrar_pantalla()
                    fun.finalizarCurso()
                case 5:
                    ctrl.borrar_pantalla()
                    ctrl.pausar_pantalla()
                case _:
                    ctrl.borrar_pantalla()
                    print(msg.mensajeError)
                    ctrl.pausar_pantalla()

        case 4:
            ctrl.borrar_pantalla()
            print(menu.menuCordinadorTrainers)
            opcion2 = int(input('/: '))
            match opcion2:
                case 1:
                    ctrl.borrar_pantalla()
                    fun.agregarTrainer()
                    ctrl.pausar_pantalla()
                case 2:
                    pass
                case 3:
                    ctrl.borrar_pantalla()
                    ctrl.pausar_pantalla()
                case _:
                    ctrl.borrar_pantalla()
                    print(msg.mensajeError)
                    ctrl.pausar_pantalla()
        case 5:
            ctrl.borrar_pantalla()
            print(menu.menuCordinadorRutasAprendizaje)
            opcion3 = int(input('/: '))
            match opcion3:
                case 1:
                    ctrl.borrar_pantalla()
                    fun.agregarRutas()
                    ctrl.pausar_pantalla()
                case 2:
                    ctrl.borrar_pantalla()
                    fun.eliminarRutas()
                    ctrl.pausar_pantalla()
                case 3:
                    ctrl.borrar_pantalla()
                    ctrl.pausar_pantalla()
                case _:
                    ctrl.borrar_pantalla()
                    print(msg.mensajeError)
                    ctrl.pausar_pantalla()
        case 6:
            ctrl.borrar_pantalla()
            mrep.moduloReportes()
        case 7:
            ctrl.borrar_pantalla()
            print(msg.mensajeSalida)
            ctrl.pausar_pantalla()
            exit()
        case _:
            ctrl.borrar_pantalla()
            print(msg.mensajeError)
            ctrl.pausar_pantalla()
               

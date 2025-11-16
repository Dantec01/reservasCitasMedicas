import time
import random
from datetime import datetime, timedelta

"""
--------------------------------------------------------
 PATRONES IMPLEMENTADOS:
 - Factory Method (Creacional)
 - Decorator (Estructural)
 - Observer (Comportamiento)
--------------------------------------------------------
"""

# ======================================================
# Delay animado EXACTO (2 segundos)
# ======================================================
def esperar_con_puntos():
    for _ in range(2):
        print(".", end="", flush=True)
        time.sleep(1)
    print()


# ======================================================
# FACTORY METHOD
# ======================================================
"""
Explicación:
Se usa Factory Method para crear distintos tipos de citas
(Medico General, Pediatra, Dentista) sin que el código cliente
tenga que conocer la clase concreta que instanciará.

Esto evita condicionales como:
if tipo == "general": return CitaGeneral()
"""

class Cita:
    def descripcion(self):
        pass

class CitaPediatra(Cita):
    def descripcion(self):
        return "Cita con Pediatra"

class CitaGeneral(Cita):
    def descripcion(self):
        return "Cita con Médico General"

class CitaDentista(Cita):
    def descripcion(self):
        return "Cita con Dentista"

class CitaFactory:
    def crear_cita(self, tipo):
        if tipo == "pediatra":
            return CitaPediatra()
        elif tipo == "general":
            return CitaGeneral()
        elif tipo == "dentista":
            return CitaDentista()
        else:
            raise ValueError("Tipo no válido")


# ======================================================
# DECORATOR — PERO SIN MODIFICAR EL TEXTO BASE
# ======================================================
"""
Explicación:
El Decorator permite añadir funcionalidad extra a un objeto
sin modificar su estructura original.

Usamos decoradores para añadir:
  - Recordatorio por correo
  - Registro en historial
"""

class CitaDecorator(Cita):
    def __init__(self, cita):
        self.cita = cita

    def descripcion(self):
        return self.cita.descripcion()   # NO AGREGA TEXTO AQUÍ


class RecordatorioEmailDecorator(CitaDecorator):
    def etiqueta(self):
        return "Recordatorio por Email"


class HistorialDecorator(CitaDecorator):
    def etiqueta(self):
        return "Guardado en Historial"


# ======================================================
# OBSERVER
# ======================================================
"""
Explicación:
Observer permite notificar automáticamente a varios observadores
cuando se crea una cita.

Subject = GestorCitas
Observers = NotificadorEmail, NotificadorSMS (suscriptores)
"""

class Observer:
    def update(self, mensaje):
        pass

class NotificadorEmail(Observer):
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

    def update(self, mensaje):
        print(f"[EMAIL] Notificación enviada a usuario {self.usuario_id}: {mensaje}")
        esperar_con_puntos()

class NotificadorSMS(Observer):
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

    def update(self, mensaje):
        print(f"[SMS] Notificación enviada a usuario {self.usuario_id}: {mensaje}")
        esperar_con_puntos()


class GestorCitas:
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id
        self.observers = []

    def agregar_observer(self, obs):
        self.observers.append(obs)

    def notificar(self, mensaje):
        for obs in self.observers:
            obs.update(mensaje)

    def registrar_cita(self, cita, fecha_hora, decoradores):
        # Línea principal EXACTA
        print(f"Cita registrada para usuario [{self.usuario_id}]: {cita.descripcion()} {fecha_hora}")
        esperar_con_puntos()

        # Mostrar decoradores EXACTAMENTE como pidió
        for deco in decoradores:
            print(f"- {deco.etiqueta()}")
        esperar_con_puntos()

        print("\nProcesando notificaciones...", end="")
        esperar_con_puntos()

        mensaje = f"Se creó una nueva cita médica. {cita.descripcion()} {fecha_hora}"
        print()
        self.notificar(mensaje)

        print("RESERVA EXITOSA.")


# ======================================================
# FECHA Y HORA RANDOM
# ======================================================
def generar_fecha_hora_random():
    fecha = datetime.now() + timedelta(days=random.randint(1, 10))
    hora = f"{random.randint(8, 18)}:{random.choice(['00', '15', '30', '45'])}"
    return f"[{hora}], [{fecha.strftime('%d/%m/%Y')}]"


# ======================================================
# PROGRAMA PRINCIPAL
# ======================================================
if __name__ == "__main__":
    usuario_id = "id123"

    factory = CitaFactory()
    cita = factory.crear_cita("pediatra")

    # Decoradores SIN afectar la descripción
    decorador1 = RecordatorioEmailDecorator(cita)
    decorador2 = HistorialDecorator(cita)

    decoradores = [decorador1, decorador2]

    fecha_hora = generar_fecha_hora_random()

    gestor = GestorCitas(usuario_id)
    gestor.agregar_observer(NotificadorEmail(usuario_id))
    gestor.agregar_observer(NotificadorSMS(usuario_id))

    gestor.registrar_cita(cita, fecha_hora, decoradores)

# Sistema de Reservas de Citas Médicas
Proyecto que implementa 3 Patrones de Diseño (Factory Method, Decorator y Observer) en un caso de uso real: la reserva de citas médicas para un usuario.

El programa funciona en consola e implementa:
- Fecha y hora aleatoria
- Notificaciones por correo y SMS
- Decoradores para agregar funcionalidades a la cita
- Delay animado de 2 segundos entre mensajes

---

## Patrones de Diseño Implementados

### 1. Factory Method (Creacional)
Se usa para crear distintos tipos de citas médicas sin condicionales complejos.  
Permite extender el sistema fácilmente añadiendo nuevos tipos de citas.

### 2. Decorator (Estructural)
Agrega funcionalidades adicionales a la cita sin modificar la clase original:
- Recordatorio por Email
- Guardado en Historial

Permite extender comportamiento sin afectar la estructura base.

### 3. Observer (Comportamiento)
Se utiliza para enviar notificaciones automáticas cuando se registra una cita.  
Los observadores incluidos son:
- Notificador por Email  
- Notificador por SMS  

Ambos reciben e imprimen el mensaje final incluyendo los datos de la cita.

---

## Caso de Uso
El usuario **id123** agenda una cita médica. El sistema:
1. Genera la cita con Factory Method  
2. Le añade funcionalidades extra mediante Decorator  
3. La registra en el sistema  
4. Imprime la información de la cita  
5. Envía notificaciones automáticas por distintos canales usando Observer  
6. Aplica delays animados de 2 segundos entre cada bloque de salida  

---

## Ejecución

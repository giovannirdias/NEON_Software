# Controlador Proporcional-Derivativo
Kp = 0.5
Kd = 0.3
last_error = 0

def control(left_sensor, right_sensor, speed):
    global last_error, Kp, Kd
    # Calculo do erro atual
    error = right_sensor - left_sensor 
    # Ajuste dos motores
    adjust = Kp*error + Kd*(error - last_error)
    # Ajuste do torque dos motores
    if speed > 120:
        torque = 500
    elif speed<100:
        torque = 5000
    else:
        torque = 4400
    last_error = error # Armazenar o erro para calculo do parametro derivativo
    
    return {
        'engineTorque': torque,
        'brakingTorque': 0,
        'steeringAngle': adjust,
        'log': [
            { 'name': 'Speed', 'value': speed, 'min': 0, 'max': 200 },
            { 'name': 'Left_sensor', 'value': left_sensor, 'min': 0, 'max': 1 },
            { 'name': 'Right_sensor', 'value': right_sensor, 'min': 0, 'max': 1 }
        ]
    }

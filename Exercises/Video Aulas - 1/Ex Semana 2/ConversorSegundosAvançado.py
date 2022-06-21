seg_inicial = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dia = seg_inicial // 86400
seg_sec = seg_inicial % 86400
hora = seg_sec // 3600
seg_ter = seg_sec % 3600
minuto = seg_ter // 60
seg_final = seg_ter % 60

print(dia,"dias,",hora,"horas,",minuto,"minutos e",seg_final,"segundos.")

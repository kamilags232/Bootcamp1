print("\nFahrenheit | Celsius")
v_inicial = int(input("Valor inicial:"))
v_final = int(input("Valor final:"))

if v_inicial <= v_final:
 for f in range(v_inicial, v_final+1,1):
      c = 5 * (f - 32) / 9
      print(f"{f:7.1f} F | {c:7.3f} C")
else:
 for f in range(v_inicial, v_final - 1,-1):
      c = 5 * (f - 32) / 9
      print(f"{f:7.1f} F | {c:7.3f} C")


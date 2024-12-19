# Jums duotas sąrašas su skaičiais: [-9, 25, 34, 2, 0]
# Neigiamus skaičius apgliaubkite laužtiniais skliaustais []
# 0 - ()


# Jums duotas sąrašas su skaičiais: [-9, 25, 34, 2, 0]
# Neigiamus skaičius apgliaubkite laužtiniais skliaustais []
# 0 - ()
# Teigiamus - {}

listas = [-9, 25, 34, 2, 0]

for skaicius in listas:
  if skaicius < 0:
    print(f"[{skaicius}]")
  elif skaicius == 0:
    print(f"({skaicius})")
  else:
    print(f"{{ {skaicius} }}")



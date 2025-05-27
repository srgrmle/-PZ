#Составить генератор (yield), который переведет символы строки из нижнего
#регистра в верхний.

try:

  a = input("введите строку: ")

  if a.isdigit():
      raise ValueError("Ошибка! Введите строку из букв")

  def up(a):
   yield from [i.upper() for i in a]

  upp = "".join(up(a))
  print(upp)

except ValueError as e:
    print(f"Ошибка: {e}")

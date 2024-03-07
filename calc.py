import tkinter as tk
import ctypes # для messagebox
import math

# ф-я для отримання результата на основі отриманих аргументів
def getVal(num1: float, num2: float, op : str):
  result: float
  match op:
    case "+":
     result= num1 + num2
    case "-":
      result= num1 - num2
    case "*":
      result= num1 * num2
    case "/":
      if(num1 == 0 or num2 == 0):
        ctypes.windll.user32.MessageBoxW(0,"Операція не вдалася", "", 0x10)
        result = 0
      else: result= num1 / num2
    case "sqrt":
      result= math.sqrt(num1)
    case "pow":
      result= math.pow(num1, num2)
    case "sin":
      result= math.sin(num1)
    case "cos":
      result= math.cos(num1)
    case "tan":
      result= math.tan(num1)
  return result

#------

#------

def calculate():
  try:
    val1 = float(entry_num1.get())
    if(operation_var.get() == "sqrt" or operation_var.get() == "sin" or operation_var.get() == "cos" or operation_var.get() == "tan"):
      val2 = 0
    else:
      val2 = float(entry_num2.get())
  except ValueError:
    ctypes.windll.user32.MessageBoxW(0,"Неправильний формат вхідних чисел", "", 0x10)
    return

  result = getVal(val1, val2, operation_var.get())
  entry_result.delete(0, tk.END)
  entry_result.insert(0, result)

# створення вікна
wnd = tk.Tk()

# надпис на вікні
wnd.title("Калькулятор")

# Створення кадра
main_frame = tk.Frame(wnd)
main_frame.pack()

# Створення об'єктів для калькулятора
label_num1 = tk.Label(main_frame, text="Перше число:")
label_num2 = tk.Label(main_frame, text="Друге число:")
label_operation = tk.Label(main_frame, text="Операція:")
# ?
entry_num1 =tk.Entry(main_frame)
entry_num2 = tk.Entry(main_frame)
operation_var = tk.StringVar(wnd)
operation_var.set("+")
operation_menu = tk.OptionMenu(main_frame, operation_var, "+", "-", "*", "/", "sqrt", "pow", "sin","cos", "tan")
entry_result = tk.Entry(main_frame)

# кнопки
calculate_button = tk.Button(main_frame, text="Вирахувати", command=calculate)
#usedegrees_buttom = tk.Checkbutton(main_frame, text="use degrees")

# розмір і позиція
wnd.resizable(width=1, height=0) 
wnd.geometry("500x250+500+300")

label_operation.grid(row=2, column=0)
operation_menu.grid(row=2, column=1)
calculate_button.grid(row=3, column=0)
label_num1.grid(row=0, column=0)
label_num2.grid(row=0, column=1)
entry_num1.grid(row=1, column=0)
entry_num2.grid(row=1, column=1)
entry_result.grid(row=3, column=1)

#usedegrees_buttom.grid(row=4, column=0)

# Запуск
wnd.mainloop()

#------------------------#




# showWindow()

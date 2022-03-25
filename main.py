import torch
import numpy as np

def pp(exp):
   global answer

   nums = [0]
   operator = ""

   loaded_add_model = torch.load('torch_adding_model')
   loaded_sub_model = torch.load('torch_substraction_model')
   loaded_mul_model = torch.load('torch_multiplying_model')
   loaded_div_model = torch.load('torch_dividing_model')

   elems = exp.split()
   if len(elems) == 3:
      try:
         nums = [float(elems[0]), float(elems[2])]
         operator = elems[1]
      except Exception:
         answer = "Ошибка"
         return answer
   elif len(elems) == 4:
      try:
         nums = [float(elems[0]), float(elems[3])*(-1)]
         operator = elems[1]
      except Exception:
         try:
            nums = [float(elems[1])*(-1), float(elems[3])]
            operator = elems[2]
         except Exception:
            answer = "Ошибка"
            return answer
   elif len(elems) == 5:
      try:
         nums = [float(elems[1])*(-1), float(elems[4])*(-1)]
         operator = elems[2]
      except Exception:
         answer = "Ошибка"
         return answer
   else:
      answer = "Ошибка"
      return answer

   x = np.array(nums)
   x = torch.from_numpy(x).float()

   if operator == "+":
      exp = float(loaded_add_model(x))
   elif operator == "–":
      exp = float(loaded_sub_model(x))
   elif operator == "×":
      exp = float(loaded_mul_model(x))
   elif operator == "÷":
      if nums[1] == 0:
         answer = "Ошибка"
         return answer
      else:
         exp = float(loaded_div_model(x))

   answer = round(exp, 4)
   return exp
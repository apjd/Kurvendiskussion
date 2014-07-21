from sympy import Symbol, sympify
from sympy import diff
from sympy.integrals import integrate
from sympy.solvers import solve

class Func:
    def __init__(self, f):
        self.x = Symbol('x')
        self.f = sympify(f)
        self.derivate()
    
    class Cleanizer:
        def __init__(self, ls, decimal_places=2):
            self.ls = ls
            self.ls = self.del_complex(self.ls)
            self.cleaned_ls = self.round_list(ls, decimal_places)
   
        #remove complex numbers from ls
        def del_complex(self, ls):
            for each_item in ls:
                if (each_item != each_item.as_real_imag()[0]):
                    del ls[ls.index(each_item)]
                    self.del_complex(ls)
    
        #return list with rounded items
        def round_list(self, ls, decimal_places=2):
            rounded_list = []
            for each_item in ls:
                rounded_item = round(each_item, decimal_places)
                rounded_list.append(rounded_item)      
            return rounded_list
            
        
    def derivate(self):
        try:
            self.d1 = diff(self.f)
        except ValueError:
            self.d1 = False
            return 0
            
        try:
            self.d2 = diff(self.d1)
        except ValueError:
            self.d2 = False
            return 0
        
        try:
            self.d3 = diff(self.d2)
        except ValueError:
            self.d3 = False
            return 0


    #return x-intercept
    def y0(self):
        y0 = solve(self.f)
        y0 = self.Cleanizer(y0).cleaned_ls
             
        return y0
        
    #return y-intercept
    def x0(self):
        x0 = self.f.subs(self.x,0)
        return x0
       

     #return extrema. Possible values for wished = max or min
    def return_max_or_min(self, wished, both=False):
         
         extrema = solve(self.d1,self.x)
         extrema = self.Cleanizer(extrema).cleaned_ls
      
         for each_extrema in extrema:
             if  self.d2.subs(self.x,each_extrema)==0:
                 extrema.remove(each_extrema)
                 
         maxima = []
         minima = []
         
         for each_extrema in extrema:
             if self.d2.subs(self.x,each_extrema) < 0:
                 maxima.append(each_extrema)
             else:
                 minima.append(each_extrema)
         if both:
            return extrema
            
         elif wished == "max":
             return maxima
         else:
             return minima
      
    
       
       #return infelctions. Possible values for wished = rl or lr
    def d2_0(self,wished, both=False): 
      infelctions = solve(self.d2,self.x) 
      infelctions = self.Cleanizer(infelctions).cleaned_ls 
       
      rl_infelctions = []
      lr_infelctions = []
      
      for each_infelction in infelctions:
          if  self.d3.subs(self.x,each_infelction)==0:
              infelctions.remove(each_infelction)
          elif self.d3.subs(self.x,each_infelction)>0:
              rl_infelctions.append(each_infelction)
          else:
              lr_infelctions.append(each_infelction)
        
      if both:
          return infelctions      
      elif wished == 'rl':
          return rl_infelctions
      else:
          return lr_infelctions
        

    
        
        
    


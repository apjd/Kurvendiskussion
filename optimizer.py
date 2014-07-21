import re
from sympy import jscode, sympify

def optimize(f):
    """
    optimizes f for sympy operations. 
    """
    
    if ',' in f:
        f = f.replace(',', '.')
        
    if '^' in f:
        f = f.replace('^', '**')
        
    uncleans = re.findall(r'\d[xX]', f)
    for unclean in uncleans:
        f = re.sub(unclean, unclean[0] + '*x', f)
        
    uncleans = re.findall(r'[xX]\d', f)
    for unclean in uncleans:
        f = re.sub(unclean, unclean[0] + 'x*', f)
        
    
        
    return f
    
def return_js_code(f):
    """
    wrapper for sympy - jscode 
    """    
    f = sympify(f)
    return jscode(f)
    
    
def return_borders(points):
    
    borders = {}
    all_x = []
    all_y = []
    
    for p in points:
        all_x.append(p['x'])
        
    for p in points:
        all_y.append(p['y'])
        
    borders['x'] = max(all_x)
    borders['-x'] = min(all_x)
    borders['y'] = max(all_y)
    borders['-y'] = min(all_y)

    if borders['x'] < 4:
        borders['x'] = 4
    if borders['-x'] > -4:
        borders['-x'] = -4
    if borders['y'] < 4:
        borders['y'] = 4
    if borders['-y'] > -4:
        borders['-y'] = -4
        
    borders['x'] = borders['x']+1
    borders['-x'] = borders['-x']-1
    borders['y'] = borders['y']+1
    borders['-y'] = borders['-y']-1
    
    return borders
        
    
    
    
   
    
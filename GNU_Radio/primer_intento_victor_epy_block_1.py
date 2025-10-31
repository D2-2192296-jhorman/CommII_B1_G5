"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):    
    def __init__(self):  # solo argumentos por defecto
        gr.sync_block.__init__(
            self,
            name='e_Acum',  # aparecerá en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.total = 0.0  # acumulador para mantener el estado entre bloques

    def work(self, input_items, output_items):
        x = input_items[0]      # Señal de entrada
        y = output_items[0]     # Señal de salida acumulada

        # Acumulación continua con estado entre llamadas
        for i in range(len(x)):
            self.total += x[i]
            y[i] = self.total

        return len(y)

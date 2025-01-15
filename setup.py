from cx_Freeze import setup, Executable 
 
executables = [Executable("Expert_em_cifras.pyw", base='Win32GUI',targetName='Expert em Cifras', icon='ico.ico')] 
 
packages = ['enviar_file','ver_escalas', 'threading', 'idna', 'trans_A', 'trans_Am', 'trans_Ast', 'trans_Astm', 'trans_B', 'trans_C', 'trans_Cst', 'trans_D', 'trans_Dst', 'trans_E',
            'trans_F', 'trans_Fst', 'trans_G', 'trans_Gst', 'escala', 'enviar_email', 'pdf', 'time', 'os', 'clipboard', 'pyautogui', 'tkinter', 'reportlab',
            ] 
options = { 
    'build_exe': { 
 
        'packages':packages, 
    }, 
 
} 
 
setup( 
    name = "Expert em Cifras", 
    options = options, 
    version = "0.0.1", 
    description = 'Aplicativo para fazer a traca de tom de cifras', 
    executables = executables 
) 

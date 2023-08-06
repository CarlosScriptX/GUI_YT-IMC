from customtkinter import *

window = CTk("white")
window.title("IMC")
window.geometry("400x400")
window.resizable(False,False)

font = CTkFont(family="Arial",size=30)
font2 = CTkFont(family="Arial",size=20)
font3 = CTkFont(family="Arial",size=15)
font4 = CTkFont(family="Arial",size=50)
colorBlue = "#3123cc"
color = "#0a690e"
x = "#0a690e"
texto = ""

def config(idade, peso, imc):
    global x, color
    if hasattr(window, 'imccalculado'):
        window.imccalculado.destroy()
        
    if hasattr(window,'labelResult'):
        window.labelResult.destroy()

    if imc < 18.5:
        color = "#ff4040"
        texto = "Abaixo do peso"
    elif imc >= 18.5 and imc <= 24.9:
        color = "#00ff00"
        texto = "Peso normal"
    elif imc >= 25.0 and imc <= 29.9:
        color = "#330101"
        texto = "Sobrepeso"
    elif imc >= 30.0 and imc <= 34.9:
        color = "Obesidade 1"
    elif imc >= 35.0 and imc <= 39.9:
        color = "#960000"
        texto = "Obesidade 2"
    elif imc >= 40.0:
        color = "#ff0000"
        texto = "Obesidade 3"
    
    labelResult = CTkLabel(window,text=texto,font=font2,text_color=color)
    labelResult.place(x=120,y=300)
    window.labelResult = labelResult
    imccalculado = CTkLabel(window, text=round(imc, 1), text_color=color, font=font4, bg_color="#050a63")
    imccalculado.place(x=270, y=175)
    window.imccalculado = imccalculado

def calcular(event=config):
    global color,x
    labelResult.destroy()
    entryIdade, entryPeso, entryAltura = f"{idade.get()}", peso.get(), altura.get()
    try:
        calculo = float(entryPeso) / (float(entryAltura) ** 2)
        if hasattr(window, 'imccalculado'):
            window.imccalculado.destroy()
        buttonCalculate = CTkButton(window, text="Calcular", fg_color=x, corner_radius=5, width=380, height=40, font=font2, command=calcular, hover_color="#063b08")
        buttonCalculate.place(x=10, y=350)
        return event(entryIdade, entryPeso, calculo)
    except:
        buttonCalculate = CTkButton(window, text="Calcular", fg_color="red", corner_radius=5, width=380, height=40, font=font2, command=calcular, hover_color="#63040a")
        buttonCalculate.place(x=10, y=350)

imcTitle = CTkLabel(window,text="Calculadora de IMC",text_color="#3123cc",font=font,bg_color="white")
imcTitle.place(x=65,y=40)

frameLine = CTkFrame(window,width=500,height=20,fg_color=colorBlue,bg_color=colorBlue)
frameLine.place(x=0,y=80)

labelIdade = CTkLabel(window,text="Insira sua idade:",text_color="#0c055e",bg_color="white",font=font2)
labelIdade.place(x=10,y=130)
idade = CTkEntry(window,fg_color="white",width=40,height=20,text_color="black",font=font3,corner_radius=1,\
placeholder_text="00")
idade.place(x=170,y=132)

labelPeso = CTkLabel(window,text="Insira seu peso:",text_color="#0c055e",bg_color="white",font=font2)
labelPeso.place(x=10,y=200)
peso = CTkEntry(window,fg_color="white",width=40,height=20,text_color="black",font=font3,corner_radius=1,\
placeholder_text="00.00")
peso.place(x=170,y=202)

labelAltura = CTkLabel(window,text="Insira sua altura:",text_color="#0c055e",bg_color="white",font=font2)
labelAltura.place(x=10,y=260)
altura = CTkEntry(window,fg_color="white",width=40,height=20,text_color="black",font=font3,corner_radius=1,\
placeholder_text="0.00")
altura.place(x=170,y=262)

labelResult = CTkLabel(window,text="",font=font2,text_color="#0c055e")

frameimc = CTkFrame(window,width=150,height=150,fg_color="#050a63")
frameimc.place(x=230,y=130)

imccalculado = CTkLabel(window,text="0.0",text_color="#c3c2cf",font=font4,bg_color="#050a63")
imccalculado.place(x=270,y=175)

buttonCalculate = CTkButton(window,text="Calcular",fg_color=color,corner_radius=5,width=380,height=40,font=font2\
,command=calcular,hover_color="#063b08")
buttonCalculate.place(x=10,y=350)

window.mainloop()
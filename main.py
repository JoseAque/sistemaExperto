from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from pyswip import Prolog
import os
import shutil
import tkinter.font as tkFont


ARCHIVO_PROLOG = "base_de_hechos.pl"
CARPETA_IMAGENES = "./img"

if not os.path.exists(CARPETA_IMAGENES):
    os.makedirs(CARPETA_IMAGENES)

prolog = Prolog()
prolog.consult(ARCHIVO_PROLOG)

root = Tk()
root.title("Sistema Experto - Violencia y Discriminación")
root.resizable(False, False)
style = ttk.Style()
print(style.theme_names())
style.theme_use('winnative')
root.configure(bg="#F2F2F2")
ancho_ventana = 850
alto_ventana = 720

# Obtener ancho y alto de la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

# Calcular posición x, y
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

# Centrar la ventana
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
fuente = tkFont.Font(family="Segoe UI", size=11)
fuente_bold = tkFont.Font(family="Segoe UI", size=11, weight="bold")
root.option_add("*Font", fuente)

# Opciones
TIPOS = ["insultos_burlas", "exclusion_grupal", "agresion_fisica"]
LUGARES = ["escuela", "trabajo", "hogar", "calle_transporte"]
GRAVEDADES = ["me_molesta", "me_afecta", "me_pone_en_riesgo"]
CAUSAS = ["forma_de_ser", "origen", "economia"]

tipo_var = StringVar(value=TIPOS[0])
lugar_var = StringVar(value=LUGARES[0])
gravedad_var = StringVar(value=GRAVEDADES[0])
causa_var = StringVar(value=CAUSAS[0])

formulario_frame = Frame(root, bg="#F2F2F2")
formulario_frame.grid(row=0, column=0, rowspan=5, sticky="e", padx=(15, 30), pady=(20, 10))

ttk.Label(formulario_frame, text="Tipo de situación:", background="#F2F2F2").grid(row=0, column=0, sticky="e", padx=10, pady=10)
ttk.OptionMenu(formulario_frame, tipo_var, tipo_var.get(), *TIPOS).grid(row=0, column=1, sticky="w", padx=10, pady=10)

ttk.Label(formulario_frame, text="Lugar:", background="#F2F2F2").grid(row=1, column=0, sticky="e", padx=10, pady=10)
ttk.OptionMenu(formulario_frame, lugar_var, lugar_var.get(), *LUGARES).grid(row=1, column=1, sticky="w", padx=10, pady=10)

ttk.Label(formulario_frame, text="Gravedad:",  background="#F2F2F2").grid(row=2, column=0, sticky="e", padx=10, pady=10)
ttk.OptionMenu(formulario_frame, gravedad_var, gravedad_var.get(), *GRAVEDADES).grid(row=2, column=1, sticky="w", padx=10, pady=10)


ttk.Label(formulario_frame, text="Causa:", background="#F2F2F2").grid(row=3, column=0, sticky="e", padx=10, pady=10)
ttk.OptionMenu(formulario_frame, causa_var, causa_var.get(), *CAUSAS).grid(row=3, column=1, sticky="w", padx=10, pady=10)

# === Resultado lado derecho ===
ttk.Label(root, text="Recomendación:", font=fuente_bold, background="#F2F2F2").grid(row=0, column=1, sticky="w", padx=20, pady=10)
resultado_text = Text(root, height=8, width=57, wrap="word")
resultado_text.grid(row=1, column=1, padx=20, pady=5, sticky="w")

ttk.Label(root, text="Explicación:", font=fuente_bold, background="#F2F2F2").grid(row=2, column=1, sticky="w", padx=20, pady=10)
explicacion_text = Text(root, height=8, width=57,  wrap="word")
explicacion_text.grid(row=3, column=1, padx=20, pady=5, sticky="w")


image_label = ttk.Label(root)
image_label.grid(row=6, column=1, columnspan=2, sticky="nsew")
image_label.grid_propagate(False)

explicacion_actual = ""

def mostrar_imagen(nombre_archivo):
    ruta = os.path.join(CARPETA_IMAGENES, nombre_archivo)
    if os.path.exists(ruta):
        img = Image.open(ruta)
        img = img.resize((200, 200))
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
    else:
        image_label.config(image='', text="(Sin imagen)")

def guardar_en_archivo(accion_linea, imagen_linea, respuesta_linea):
    with open(ARCHIVO_PROLOG, "a", encoding="utf-8") as f:
        f.write("\n" + accion_linea + "\n")
        f.write(imagen_linea + "\n")
        f.write(respuesta_linea + "\n")

def agregar_nueva_info(tipo, lugar, gravedad, causa):
    nueva_ventana = Toplevel(root)
    nueva_ventana.title("Agregar nueva información")
    nueva_ventana.resizable(False, False)
    ancho_ventana = 430
    alto_ventana = 400
    # Obtener ancho y alto de la pantalla
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    # Calcular posición x, y
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)
    # Centrar la ventana
    nueva_ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    Label(nueva_ventana, text="Respuesta:", font=fuente_bold).pack()
    entrada_respuesta = Text(nueva_ventana, height=7, width=50)
    entrada_respuesta.pack()

    Label(nueva_ventana, text="Explicación:", font=fuente_bold).pack()
    entrada_explicacion = Text(nueva_ventana, height=7, width=50)
    entrada_explicacion.pack()

    def seleccionar_imagen():
        ruta = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Imágenes", "*.jpg *.png")])
        return ruta

    def guardar():
        nueva_respuesta = entrada_respuesta.get("1.0", END).strip()
        nueva_explicacion = entrada_explicacion.get("1.0", END).strip()
        ruta_img = seleccionar_imagen()

        if not nueva_respuesta or not nueva_explicacion or not ruta_img:
            messagebox.showwarning("Campos obligatorios", "Debes completar todos los campos y seleccionar una imagen.")
            return agregar_nueva_info(tipo, lugar, gravedad, causa)

        nombre_img = os.path.basename(ruta_img)
        nueva_ruta = os.path.join(CARPETA_IMAGENES, nombre_img)
        shutil.copy(ruta_img, nueva_ruta)

        prolog.assertz(f"accion({tipo}, {lugar}, {gravedad}, {causa}, \"{nueva_explicacion}\")")
        prolog.assertz(f"imagen_accion({tipo}, {lugar}, {gravedad}, {causa}, \"{nombre_img}\")")
        prolog.assertz(f"respuesta({tipo}, {lugar}, {gravedad}, {causa}, \"{nueva_respuesta}\")")

        guardar_en_archivo(
            f"accion({tipo}, {lugar}, {gravedad}, {causa}, \"{nueva_explicacion}\").",
            f"imagen_accion({tipo}, {lugar}, {gravedad}, {causa}, \"{nombre_img}\").",
            f"respuesta({tipo}, {lugar}, {gravedad}, {causa}, \"{nueva_respuesta}\")."
        )

        resultado_text.delete("1.0", END)
        explicacion_text.delete("1.0", END)
        resultado_text.tag_configure("justificado", justify="left")
        resultado_text.insert(END, nueva_respuesta)
        explicacion_text.tag_configure("justificado", justify="left")
        explicacion_text.insert(END, nueva_explicacion)
        mostrar_imagen(nombre_img)
        global explicacion_actual
        explicacion_actual = nueva_explicacion
        messagebox.showinfo("Guardado", "Nueva información guardada correctamente.")
        nueva_ventana.destroy()

    Button(nueva_ventana, text="Agregar imagen y guardar", command=guardar).pack(pady=10)

def consultar():
    global explicacion_actual
    resultado_text.delete("1.0", END)
    explicacion_text.delete("1.0", END)  # Se limpia, pero NO se muestra nueva explicación
    image_label.config(image='', text='')

    tipo = tipo_var.get()
    lugar = lugar_var.get()
    gravedad = gravedad_var.get()
    causa = causa_var.get()

    consulta = f"respuesta({tipo}, {lugar}, {gravedad}, {causa}, Texto)"
    respuestas = list(prolog.query(consulta))

    if respuestas:
        texto = respuestas[0]["Texto"]
        if isinstance(texto, bytes):
            texto = texto.decode("utf-8")
        resultado_text.tag_configure("justificado", justify="left")
        resultado_text.insert(END, texto, "justificado")

        consulta_img = f"imagen_accion({tipo}, {lugar}, {gravedad}, {causa}, Imagen)"
        imagenes = list(prolog.query(consulta_img))
        if imagenes:
            imagen_actual = imagenes[0]["Imagen"]
            if isinstance(imagen_actual, bytes):
                imagen_actual = imagen_actual.decode("utf-8")
            mostrar_imagen(imagen_actual)

        # Solo guarda la explicación, pero no la muestra aún
        consulta_exp = f"accion({tipo}, {lugar}, {gravedad}, {causa}, Exp)"
        explicaciones = list(prolog.query(consulta_exp))
        if explicaciones:
            explicacion_actual = explicaciones[0]["Exp"]
            if isinstance(explicacion_actual, bytes):
                explicacion_actual = explicacion_actual.decode("utf-8")
        else:
            explicacion_actual = ""
    else:
        if messagebox.askyesno("No encontrado", "No hay respuesta y explicación. ¿Deseas agregar nueva información?"):
            agregar_nueva_info(tipo, lugar, gravedad, causa)


def mostrar_explicacion():
    explicacion_text.delete("1.0", END)
    if explicacion_actual:
        explicacion_text.insert(END, explicacion_actual)
        
    else:
        explicacion_text.insert(END, "No hay explicación disponible.")

def limpiar():
    tipo_var.set(TIPOS[0])
    lugar_var.set(LUGARES[0])
    gravedad_var.set(GRAVEDADES[0])
    causa_var.set(CAUSAS[0])
    resultado_text.delete("1.0", END)
    explicacion_text.delete("1.0", END)
    image_label.config(image='', text='')

class RoundedButton(Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, text, command=None):
        Canvas.__init__(self, parent, borderwidth=0,
                        relief="flat", highlightthickness=0)
        self.command = command
        self.width = width
        self.height = height
        self.cornerradius = cornerradius
        self.padding = padding
        self.color = color
        self.original_color = color  # Guardamos color original para hover out
        self.text = text
        self.font = fuente_bold

        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

        # Bind para hover
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

        self.draw_rounded_rect()
        self.text_id = self.create_text(width//2, height//2, text=self.text, fill="white", font=self.font)

    def draw_rounded_rect(self):
        r = self.cornerradius
        w = self.width
        h = self.height
        self.delete("all")

        # Dibujar arcos y rectángulos para fondo redondeado
        self.create_arc((0, 0, r*2, r*2), start=90, extent=90, fill=self.color, outline=self.color)
        self.create_arc((w - r*2, 0, w, r*2), start=0, extent=90, fill=self.color, outline=self.color)
        self.create_arc((0, h - r*2, r*2, h), start=180, extent=90, fill=self.color, outline=self.color)
        self.create_arc((w - r*2, h - r*2, w, h), start=270, extent=90, fill=self.color, outline=self.color)

        self.create_rectangle((r, 0, w - r, h), fill=self.color, outline=self.color)
        self.create_rectangle((0, r, w, h - r), fill=self.color, outline=self.color)

        # Redibujar texto después del fondo
        self.text_id = self.create_text(self.width//2, self.height//2, text=self.text, fill="white", font=self.font)

    def config_color(self, new_color):
        self.color = new_color
        self.draw_rounded_rect()

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="flat")
        if self.command:
            self.command()

    def _on_enter(self, event):
        # Color más oscuro para hover (puedes ajustar)
        hover_color = self._darker_color(self.original_color, factor=0.8)
        self.config_color(hover_color)

    def _on_leave(self, event):
        # Regresar al color original
        self.config_color(self.original_color)

    def _darker_color(self, hex_color, factor=0.7):
        """Devuelve un color hex más oscuro multiplicando sus RGB por factor < 1."""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        rgb_oscuro = tuple(max(0, int(c * factor)) for c in rgb)
        return '#{:02x}{:02x}{:02x}'.format(*rgb_oscuro)


frame_botones = Frame(root, bg="#F2F2F2")
frame_botones.grid(row=5, column=0, columnspan=2, pady=15)

boton_consultar = RoundedButton(frame_botones, width=160, height=40, cornerradius=20, padding=5, color="#19D700", text="CONSULTA", command=consultar)
boton_consultar.grid(row=0, column=0, padx=15)
boton_explicar = RoundedButton(frame_botones, width=160, height=40, cornerradius=20, padding=5, color="#0078D7", text="EXPLICACIÓN", command=mostrar_explicacion)
boton_explicar.grid(row=0, column=1, padx=15)
boton_limpiar = RoundedButton(frame_botones, width=160, height=40, cornerradius=20, padding=5, color="#eea662", text="LIMPIAR", command=limpiar)
boton_limpiar.grid(row=0, column=3, padx=15)



root.mainloop()






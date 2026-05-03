# ==== Import ==== #
import customtkinter
 
# ==== Appearance and Color ==== #
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
 
# ==== Languages ==== #
LANGUAGES = {
    "PT": {
        "convert": "Converter",
        "invalid": "Valor Inválido!",
        "speed_placeholder": "Velocidade",
        "altitude_placeholder": "Altitude",
        "distance_placeholder": "Distância",
        "temperature_placeholder": "Temperatura",
        "speed_label": "Velocidade",
        "altitude_label": "Altitude",
        "distance_label": "Distância",
        "temperature_label": "Temperatura",
    },
    "EN": {
        "convert": "Convert",
        "invalid": "Invalid Value!",
        "speed_placeholder": "Speed",
        "altitude_placeholder": "Altitude",
        "distance_placeholder": "Distance",
        "temperature_placeholder": "Temperature",
        "speed_label": "Speed",
        "altitude_label": "Altitude",
        "distance_label": "Distance",
        "temperature_label": "Temperature",
    }
}
 
current_lang = "PT"
 
# ==== Configuration ==== #
app = customtkinter.CTk()
app.title("SimConvert")
app.geometry("1280x720")
 
# ==== Language Selector ==== #
lang_frame = customtkinter.CTkFrame(app)
lang_frame.grid(row=0, column=0, columnspan=4, padx=40, pady=(20, 0), sticky="e")
 
lang_menu = customtkinter.CTkOptionMenu(lang_frame, values=["PT", "EN"])
lang_menu.set("PT")
lang_menu.pack(side="right", padx=10, pady=5)
 
# ==== Speed Frame ==== #
speed_frame = customtkinter.CTkFrame(app)
speed_frame.grid(row=1, column=0, padx=40, pady=40)
 
# ==== Speed Label ==== #
speed_label = customtkinter.CTkLabel(speed_frame, text="Velocidade", font=("Arial", 14, "bold"))
speed_label.pack(pady=(10, 5))
 
# ==== Speed Options ==== #
speed_units = ["Km/h", "Mph", "Kt", "Mach", "M/s"]
 
speed_from = customtkinter.CTkOptionMenu(speed_frame, values=speed_units)
speed_from.set("Km/h")
speed_from.pack(pady=5)
 
speed_to = customtkinter.CTkOptionMenu(speed_frame, values=speed_units)
speed_to.set("Mph")
speed_to.pack(pady=5)
 
speed_entry = customtkinter.CTkEntry(speed_frame, placeholder_text="Velocidade")
speed_entry.pack(pady=10)
 
speed_result = customtkinter.CTkLabel(speed_frame, text="")
speed_result.pack(pady=10)
 
# ==== Speed Convertion ==== #
def speed_convert():
    try:
        value = float(speed_entry.get().replace(",", "."))
 
        from_unit = speed_from.get()
        to_unit = speed_to.get()
 
        # ==== Convert to M/s ==== #
        if from_unit == "Km/h":
            base = value / 3.6
        elif from_unit == "Mph":
            base = value * 0.44704
        elif from_unit == "Kt":
            base = value * 0.514444
        elif from_unit == "Mach":
            base = value * 340.3
        elif from_unit == "M/s":
            base = value
 
        # ==== Convert from M/s to chosen unit ==== #
        if to_unit == "Km/h":
            result_value = base * 3.6
        elif to_unit == "Mph":
            result_value = base / 0.44704
        elif to_unit == "Kt":
            result_value = base / 0.514444
        elif to_unit == "Mach":
            result_value = base / 340.3
        elif to_unit == "M/s":
            result_value = base
 
        speed_result.configure(text=f"{result_value:.2f} {to_unit}")
 
    except ValueError:
        speed_result.configure(text=LANGUAGES[current_lang]["invalid"])
 
button = customtkinter.CTkButton(speed_frame, text="Converter", command=speed_convert)
button.pack(pady=10)
 
# ==== Altitude Frame ==== #
altitude_frame = customtkinter.CTkFrame(app)
altitude_frame.grid(row=1, column=1, padx=40, pady=40)
 
# ==== Altitude Label ==== #
altitude_label = customtkinter.CTkLabel(altitude_frame, text="Altitude", font=("Arial", 14, "bold"))
altitude_label.pack(pady=(10, 5))
 
# ==== Altitude Options ==== #
altitude_units = ["M", "Ft"]
 
altitude_from = customtkinter.CTkOptionMenu(altitude_frame, values=altitude_units)
altitude_from.set("M")
altitude_from.pack(pady=5)
 
altitude_to = customtkinter.CTkOptionMenu(altitude_frame, values=altitude_units)
altitude_to.set("Ft")
altitude_to.pack(pady=5)
 
altitude_entry = customtkinter.CTkEntry(altitude_frame, placeholder_text="Altitude")
altitude_entry.pack(pady=10)
 
altitude_result = customtkinter.CTkLabel(altitude_frame, text="")
altitude_result.pack(pady=10)
 
# ==== Altitude Convertion ==== #
def convert_altitude():
    try:
        value = float(altitude_entry.get().replace(",", "."))
        from_unit = altitude_from.get()
        to_unit = altitude_to.get()
 
        if from_unit == "M" and to_unit == "Ft":
            base = value * 3.28084
        elif from_unit == "Ft" and to_unit == "M":
            base = value / 3.28084
        else:
            base = value
 
        altitude_result.configure(text=f"{base:.2f} {to_unit}")
 
    except ValueError:
        altitude_result.configure(text=LANGUAGES[current_lang]["invalid"])
 
alt_button = customtkinter.CTkButton(altitude_frame, text="Converter", command=convert_altitude)
alt_button.pack(pady=10)
 
# ==== Distance Frame ==== #
distance_frame = customtkinter.CTkFrame(app)
distance_frame.grid(row=1, column=2, padx=40, pady=40)
 
# ==== Distance Label ==== #
distance_label = customtkinter.CTkLabel(distance_frame, text="Distância", font=("Arial", 14, "bold"))
distance_label.pack(pady=(10, 5))
 
# ==== Distance Options ==== #
distance_units = ["Km", "NM"]
 
distance_from = customtkinter.CTkOptionMenu(distance_frame, values=distance_units)
distance_from.set("Km")
distance_from.pack(pady=5)
 
distance_to = customtkinter.CTkOptionMenu(distance_frame, values=distance_units)
distance_to.set("NM")
distance_to.pack(pady=5)
 
distance_entry = customtkinter.CTkEntry(distance_frame, placeholder_text="Distância")
distance_entry.pack(pady=10)
 
distance_result = customtkinter.CTkLabel(distance_frame, text="")
distance_result.pack(pady=10)
 
# ==== Distance Convertion ==== #
def convert_distance():
    try:
        value = float(distance_entry.get().replace(",", "."))
        from_unit = distance_from.get()
        to_unit = distance_to.get()
 
        if from_unit == "Km" and to_unit == "NM":
            result = value / 1.852
        elif from_unit == "NM" and to_unit == "Km":
            result = value * 1.852
        else:
            result = value
 
        distance_result.configure(text=f"{result:.2f} {to_unit}")
 
    except ValueError:
        distance_result.configure(text=LANGUAGES[current_lang]["invalid"])
 
distance_button = customtkinter.CTkButton(distance_frame, text="Converter", command=convert_distance)
distance_button.pack(pady=10)
 
# ==== Temperature Frame ==== #
temperature_frame = customtkinter.CTkFrame(app)
temperature_frame.grid(row=1, column=3, padx=40, pady=40)
 
# ==== Temperature Label ==== #
temperature_label = customtkinter.CTkLabel(temperature_frame, text="Temperatura", font=("Arial", 14, "bold"))
temperature_label.pack(pady=(10, 5))
 
# ==== Temperature Options ==== #
temperature_units = ["C", "F", "K"]
 
temperature_from = customtkinter.CTkOptionMenu(temperature_frame, values=temperature_units)
temperature_from.set("C")
temperature_from.pack(pady=5)
 
temperature_to = customtkinter.CTkOptionMenu(temperature_frame, values=temperature_units)
temperature_to.set("F")
temperature_to.pack(pady=5)
 
temperature_entry = customtkinter.CTkEntry(temperature_frame, placeholder_text="Temperatura")
temperature_entry.pack(pady=10)
 
temperature_result = customtkinter.CTkLabel(temperature_frame, text="")
temperature_result.pack(pady=10)
 
# ==== Temperature Convertion ==== #
def convert_temperature():
    try:
        value = float(temperature_entry.get().replace(",", "."))
 
        from_unit = temperature_from.get()
        to_unit = temperature_to.get()
 
        # ==== Convert to K ==== #
        if from_unit == "C":
            base = value + 273.15
        elif from_unit == "F":
            base = (value - 32) * (5 / 9) + 273.15
        elif from_unit == "K":
            base = value
 
        # ==== Convert from K to chosen unit ==== #
        if to_unit == "C":
            result = base - 273.15
        elif to_unit == "F":
            result = (base - 273.15) * (9 / 5) + 32
        elif to_unit == "K":
            result = base
 
        temperature_result.configure(text=f"{result:.2f} {to_unit}")
 
    except ValueError:
        temperature_result.configure(text=LANGUAGES[current_lang]["invalid"])
 
temperature_button = customtkinter.CTkButton(temperature_frame, text="Converter", command=convert_temperature)
temperature_button.pack(pady=10)
 
# ==== Update Language ==== #
def update_language(lang):
    global current_lang
    current_lang = lang
    t = LANGUAGES[lang]
 
    # ==== Labels ==== #
    speed_label.configure(text=t["speed_label"])
    altitude_label.configure(text=t["altitude_label"])
    distance_label.configure(text=t["distance_label"])
    temperature_label.configure(text=t["temperature_label"])
 
    # ==== Placeholders ==== #
    speed_entry.configure(placeholder_text=t["speed_placeholder"])
    altitude_entry.configure(placeholder_text=t["altitude_placeholder"])
    distance_entry.configure(placeholder_text=t["distance_placeholder"])
    temperature_entry.configure(placeholder_text=t["temperature_placeholder"])
 
    # ==== Buttons ==== #
    button.configure(text=t["convert"])
    alt_button.configure(text=t["convert"])
    distance_button.configure(text=t["convert"])
    temperature_button.configure(text=t["convert"])
 
lang_menu.configure(command=update_language)
 
# ==== End ==== #
app.mainloop()
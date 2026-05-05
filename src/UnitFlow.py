# ==== Imports ==== #
import os
import customtkinter
import sys
from PIL import Image 

# ==== Appearance and Color ==== #
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
 
# ==== Fonts per Language ==== #
# Arabic (AR) is included but RTL may not render correctly in CustomTkinter
FONTS = {
    "PT": "Arial", "EN": "Arial", "ES": "Arial",  "FR": "Arial",
    "DE": "Arial", "IT": "Arial", "NL": "Arial",  "RU": "Arial",
    "TR": "Arial",
    "ZH": "Microsoft YaHei",
    "JA": "Yu Gothic",
    "KO": "Malgun Gothic",
    "HI": "Mangal",
    "AR": "Arial",
}
 
# ==== Languages ==== #
LANGUAGES = {
    "PT": {
        "convert":                "Converter",
        "reset":                  "Reset",
        "invalid":                "Inválido!",
        "speed_placeholder":      "Velocidade",
        "altitude_placeholder":   "Altitude",
        "distance_placeholder":   "Distância",
        "temperature_placeholder":"Temperatura",
        "speed_tab":              "Velocidade",
        "altitude_tab":           "Altitude",
        "distance_tab":           "Distância",
        "temperature_tab":        "Temperatura",
        "history_tab":            "Histórico",
        "history_empty":          "Sem conversões ainda.",
        "clear_history":          "Limpar Histórico",
        "status_default":         "Pronto.",
    },
    "EN": {
        "convert":                "Convert",
        "reset":                  "Reset",
        "invalid":                "Invalid Value!",
        "speed_placeholder":      "Speed",
        "altitude_placeholder":   "Altitude",
        "distance_placeholder":   "Distance",
        "temperature_placeholder":"Temperature",
        "speed_tab":              "Speed",
        "altitude_tab":           "Altitude",
        "distance_tab":           "Distance",
        "temperature_tab":        "Temperature",
        "history_tab":            "History",
        "history_empty":          "No conversions yet.",
        "clear_history":          "Clear History",
        "status_default":         "Ready.",
    },
    "ES": {
        "convert":                "Convertir",
        "reset":                  "Reiniciar",
        "invalid":                "¡Valor inválido!",
        "speed_placeholder":      "Velocidad",
        "altitude_placeholder":   "Altitud",
        "distance_placeholder":   "Distancia",
        "temperature_placeholder":"Temperatura",
        "speed_tab":              "Velocidad",
        "altitude_tab":           "Altitud",
        "distance_tab":           "Distancia",
        "temperature_tab":        "Temperatura",
        "history_tab":            "Historial",
        "history_empty":          "Sin conversiones aún.",
        "clear_history":          "Borrar historial",
        "status_default":         "Listo.",
    },
    "FR": {
        "convert":                "Convertir",
        "reset":                  "Réinitialiser",
        "invalid":                "Valeur invalide!",
        "speed_placeholder":      "Vitesse",
        "altitude_placeholder":   "Altitude",
        "distance_placeholder":   "Distance",
        "temperature_placeholder":"Température",
        "speed_tab":              "Vitesse",
        "altitude_tab":           "Altitude",
        "distance_tab":           "Distance",
        "temperature_tab":        "Température",
        "history_tab":            "Historique",
        "history_empty":          "Aucune conversion encore.",
        "clear_history":          "Effacer l'historique",
        "status_default":         "Prêt.",
    },
    "DE": {
        "convert":                "Umrechnen",
        "reset":                  "Zurücksetzen",
        "invalid":                "Ungültiger Wert!",
        "speed_placeholder":      "Geschwindigkeit",
        "altitude_placeholder":   "Höhe",
        "distance_placeholder":   "Entfernung",
        "temperature_placeholder":"Temperatur",
        "speed_tab":              "Geschwindigkeit",
        "altitude_tab":           "Höhe",
        "distance_tab":           "Entfernung",
        "temperature_tab":        "Temperatur",
        "history_tab":            "Verlauf",
        "history_empty":          "Noch keine Umrechnungen.",
        "clear_history":          "Verlauf löschen",
        "status_default":         "Bereit.",
    },
    "IT": {
        "convert":                "Converti",
        "reset":                  "Reset",
        "invalid":                "Valore non valido!",
        "speed_placeholder":      "Velocità",
        "altitude_placeholder":   "Altitudine",
        "distance_placeholder":   "Distanza",
        "temperature_placeholder":"Temperatura",
        "speed_tab":              "Velocità",
        "altitude_tab":           "Altitudine",
        "distance_tab":           "Distanza",
        "temperature_tab":        "Temperatura",
        "history_tab":            "Cronologia",
        "history_empty":          "Nessuna conversione ancora.",
        "clear_history":          "Cancella cronologia",
        "status_default":         "Pronto.",
    },
    "NL": {
        "convert":                "Omrekenen",
        "reset":                  "Reset",
        "invalid":                "Ongeldige waarde!",
        "speed_placeholder":      "Snelheid",
        "altitude_placeholder":   "Hoogte",
        "distance_placeholder":   "Afstand",
        "temperature_placeholder":"Temperatuur",
        "speed_tab":              "Snelheid",
        "altitude_tab":           "Hoogte",
        "distance_tab":           "Afstand",
        "temperature_tab":        "Temperatuur",
        "history_tab":            "Geschiedenis",
        "history_empty":          "Nog geen conversies.",
        "clear_history":          "Geschiedenis wissen",
        "status_default":         "Klaar.",
    },
    "RU": {
        "convert":                "Конвертировать",
        "reset":                  "Сброс",
        "invalid":                "Неверное значение!",
        "speed_placeholder":      "Скорость",
        "altitude_placeholder":   "Высота",
        "distance_placeholder":   "Расстояние",
        "temperature_placeholder":"Температура",
        "speed_tab":              "Скорость",
        "altitude_tab":           "Высота",
        "distance_tab":           "Расстояние",
        "temperature_tab":        "Температура",
        "history_tab":            "История",
        "history_empty":          "Пока нет конверсий.",
        "clear_history":          "Очистить историю",
        "status_default":         "Готово.",
    },
    "TR": {
        "convert":                "Dönüştür",
        "reset":                  "Sıfırla",
        "invalid":                "Geçersiz değer!",
        "speed_placeholder":      "Hız",
        "altitude_placeholder":   "İrtifa",
        "distance_placeholder":   "Mesafe",
        "temperature_placeholder":"Sıcaklık",
        "speed_tab":              "Hız",
        "altitude_tab":           "İrtifa",
        "distance_tab":           "Mesafe",
        "temperature_tab":        "Sıcaklık",
        "history_tab":            "Geçmiş",
        "history_empty":          "Henüz dönüşüm yok.",
        "clear_history":          "Geçmişi Temizle",
        "status_default":         "Hazır.",
    },
    "ZH": {
        "convert":                "转换",
        "reset":                  "重置",
        "invalid":                "无效值!",
        "speed_placeholder":      "速度",
        "altitude_placeholder":   "高度",
        "distance_placeholder":   "距离",
        "temperature_placeholder":"温度",
        "speed_tab":              "速度",
        "altitude_tab":           "高度",
        "distance_tab":           "距离",
        "temperature_tab":        "温度",
        "history_tab":            "历史",
        "history_empty":          "暂无转换记录。",
        "clear_history":          "清除历史",
        "status_default":         "就绪。",
    },
    "JA": {
        "convert":                "変換",
        "reset":                  "リセット",
        "invalid":                "無効な値!",
        "speed_placeholder":      "速度",
        "altitude_placeholder":   "高度",
        "distance_placeholder":   "距離",
        "temperature_placeholder":"温度",
        "speed_tab":              "速度",
        "altitude_tab":           "高度",
        "distance_tab":           "距離",
        "temperature_tab":        "温度",
        "history_tab":            "履歴",
        "history_empty":          "まだ変換がありません。",
        "clear_history":          "履歴をクリア",
        "status_default":         "準備完了。",
    },
    "KO": {
        "convert":                "변환",
        "reset":                  "초기화",
        "invalid":                "잘못된 값!",
        "speed_placeholder":      "속도",
        "altitude_placeholder":   "고도",
        "distance_placeholder":   "거리",
        "temperature_placeholder":"온도",
        "speed_tab":              "속도",
        "altitude_tab":           "고도",
        "distance_tab":           "거리",
        "temperature_tab":        "온도",
        "history_tab":            "기록",
        "history_empty":          "아직 변환 기록이 없습니다.",
        "clear_history":          "기록 지우기",
        "status_default":         "준비됨.",
    },
    "HI": {
        "convert":                "परिवर्तित करें",
        "reset":                  "रीसेट",
        "invalid":                "अमान्य मान!",
        "speed_placeholder":      "गति",
        "altitude_placeholder":   "ऊंचाई",
        "distance_placeholder":   "दूरी",
        "temperature_placeholder":"तापमान",
        "speed_tab":              "गति",
        "altitude_tab":           "ऊंचाई",
        "distance_tab":           "दूरी",
        "temperature_tab":        "तापमान",
        "history_tab":            "इतिहास",
        "history_empty":          "अभी तक कोई रूपांतरण नहीं।",
        "clear_history":          "इतिहास साफ़ करें",
        "status_default":         "तैयार।",
    },
    "AR": {
        # Note: Arabic RTL may not render correctly in CustomTkinter
        "convert":                "تحويل",
        "reset":                  "إعادة تعيين",
        "invalid":                "قيمة غير صالحة!",
        "speed_placeholder":      "السرعة",
        "altitude_placeholder":   "الارتفاع",
        "distance_placeholder":   "المسافة",
        "temperature_placeholder":"درجة الحرارة",
        "speed_tab":              "السرعة",
        "altitude_tab":           "الارتفاع",
        "distance_tab":           "المسافة",
        "temperature_tab":        "درجة الحرارة",
        "history_tab":            "السجل",
        "history_empty":          "لا توجد تحويلات بعد.",
        "clear_history":          "مسح السجل",
        "status_default":         "جاهز.",
    },
}
 
# ==== Tab Keys ==== #
TAB_KEYS = ["speed_tab", "altitude_tab", "distance_tab", "temperature_tab", "history_tab"]
 
current_lang = "PT"
history_entries = []
 
# ==== Configuration ==== #
app = customtkinter.CTk()
app.title("UnitFlow")
app.geometry("600x600")
app.resizable(True, True)
 
# ==== Top Bar ==== #
top_bar = customtkinter.CTkFrame(app, corner_radius=0)
top_bar.pack(fill="x", padx=0, pady=0)
 
# ==== Logo ==== #
if getattr(sys, 'frozen', False):
    script_dir = sys._MEIPASS
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "assets", ".png", "UnitFlow_Logo_677x369.png")
 
try:
    logo_image = customtkinter.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(184, 100)
    )
    logo_label = customtkinter.CTkLabel(top_bar, image=logo_image, text="")
    logo_label.image = logo_image
except Exception as e:
    print(f"Erro no logo: {e}")
    logo_label = customtkinter.CTkLabel(top_bar, text="UnitFlow", font=("Arial", 20, "bold"))
 
logo_label.pack(side="left", padx=20, pady=10)
 
# ==== Theme Selector ==== #
theme_menu = customtkinter.CTkOptionMenu(top_bar, values=["Dark", "Light", "System"], width=100)
theme_menu.set("Dark")
theme_menu.pack(side="right", padx=10, pady=10)
 
# ==== Language Selector ==== #
lang_list = ["PT", "EN", "ES", "FR", "DE", "IT", "NL", "RU", "TR", "ZH", "JA", "KO", "HI", "AR"]
lang_menu = customtkinter.CTkOptionMenu(top_bar, values=lang_list, width=80)
lang_menu.set("PT")
lang_menu.pack(side="right", padx=5, pady=10)
 
# ==== Tab View ==== #
tabview = customtkinter.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=20, pady=(10, 0))
 
tabview.add("Velocidade")
tabview.add("Altitude")
tabview.add("Distância")
tabview.add("Temperatura")
tabview.add("Histórico")
 
# ==== Helper: add to history ==== #
def add_to_history(entry):
    history_entries.append(entry)
    history_box.configure(state="normal")
    history_box.delete("1.0", "end")
    for item in reversed(history_entries):
        history_box.insert("end", f"• {item}\n")
    history_box.configure(state="disabled")
 
# ==== Helper: update status ==== #
def set_status(text):
    status_label.configure(text=text)
 
# ==== Speed Tab ==== #
speed_tab = tabview.tab("Velocidade")
 
speed_units = ["Km/h", "Mph", "Kt", "Mach", "M/s"]
 
speed_from = customtkinter.CTkOptionMenu(speed_tab, values=speed_units)
speed_from.set("Km/h")
speed_from.pack(pady=10)
 
speed_to = customtkinter.CTkOptionMenu(speed_tab, values=speed_units)
speed_to.set("Mph")
speed_to.pack(pady=5)
 
speed_entry = customtkinter.CTkEntry(speed_tab, placeholder_text="Velocidade", width=200)
speed_entry.pack(pady=10)
 
speed_result = customtkinter.CTkLabel(speed_tab, text="", font=("Arial", 16, "bold"))
speed_result.pack(pady=5)
 
# ==== Speed Buttons ==== #
speed_btn_frame = customtkinter.CTkFrame(speed_tab, fg_color="transparent")
speed_btn_frame.pack(pady=5)
 
def speed_convert():
    try:
        value = float(speed_entry.get().replace(",", "."))
        from_unit = speed_from.get()
        to_unit = speed_to.get()
 
        if from_unit == "Km/h":   base = value / 3.6
        elif from_unit == "Mph":  base = value * 0.44704
        elif from_unit == "Kt":   base = value * 0.514444
        elif from_unit == "Mach": base = value * 340.3
        elif from_unit == "M/s":  base = value
 
        if to_unit == "Km/h":     result_value = base * 3.6
        elif to_unit == "Mph":    result_value = base / 0.44704
        elif to_unit == "Kt":     result_value = base / 0.514444
        elif to_unit == "Mach":   result_value = base / 340.3
        elif to_unit == "M/s":    result_value = base
 
        result_text = f"{value} {from_unit} → {result_value:.2f} {to_unit}"
        speed_result.configure(text=f"{result_value:.2f} {to_unit}")
        set_status(result_text)
        add_to_history(result_text)
 
    except ValueError:
        speed_result.configure(text=LANGUAGES[current_lang]["invalid"])
 
def speed_reset():
    speed_entry.delete(0, "end")
    speed_result.configure(text="")
    set_status(LANGUAGES[current_lang]["status_default"])
 
speed_button = customtkinter.CTkButton(speed_btn_frame, text="Converter", command=speed_convert, width=120)
speed_button.pack(side="left", padx=5)
 
speed_reset_btn = customtkinter.CTkButton(speed_btn_frame, text="Reset", command=speed_reset, width=80, fg_color="gray")
speed_reset_btn.pack(side="left", padx=5)
 
# ==== Altitude Tab ==== #
altitude_tab = tabview.tab("Altitude")
 
altitude_units = ["M", "Ft"]
 
altitude_from = customtkinter.CTkOptionMenu(altitude_tab, values=altitude_units)
altitude_from.set("M")
altitude_from.pack(pady=10)
 
altitude_to = customtkinter.CTkOptionMenu(altitude_tab, values=altitude_units)
altitude_to.set("Ft")
altitude_to.pack(pady=5)
 
altitude_entry = customtkinter.CTkEntry(altitude_tab, placeholder_text="Altitude", width=200)
altitude_entry.pack(pady=10)
 
altitude_result = customtkinter.CTkLabel(altitude_tab, text="", font=("Arial", 16, "bold"))
altitude_result.pack(pady=5)
 
altitude_btn_frame = customtkinter.CTkFrame(altitude_tab, fg_color="transparent")
altitude_btn_frame.pack(pady=5)
 
def convert_altitude():
    try:
        value = float(altitude_entry.get().replace(",", "."))
        from_unit = altitude_from.get()
        to_unit = altitude_to.get()
 
        if from_unit == "M" and to_unit == "Ft":   base = value * 3.28084
        elif from_unit == "Ft" and to_unit == "M": base = value / 3.28084
        else:                                       base = value
 
        result_text = f"{value} {from_unit} → {base:.2f} {to_unit}"
        altitude_result.configure(text=f"{base:.2f} {to_unit}")
        set_status(result_text)
        add_to_history(result_text)
 
    except ValueError:
        altitude_result.configure(text=LANGUAGES[current_lang]["invalid"])
 
def altitude_reset():
    altitude_entry.delete(0, "end")
    altitude_result.configure(text="")
    set_status(LANGUAGES[current_lang]["status_default"])
 
alt_button = customtkinter.CTkButton(altitude_btn_frame, text="Converter", command=convert_altitude, width=120)
alt_button.pack(side="left", padx=5)
 
alt_reset_btn = customtkinter.CTkButton(altitude_btn_frame, text="Reset", command=altitude_reset, width=80, fg_color="gray")
alt_reset_btn.pack(side="left", padx=5)
 
# ==== Distance Tab ==== #
distance_tab = tabview.tab("Distância")
 
distance_units = ["Km", "NM"]
 
distance_from = customtkinter.CTkOptionMenu(distance_tab, values=distance_units)
distance_from.set("Km")
distance_from.pack(pady=10)
 
distance_to = customtkinter.CTkOptionMenu(distance_tab, values=distance_units)
distance_to.set("NM")
distance_to.pack(pady=5)
 
distance_entry = customtkinter.CTkEntry(distance_tab, placeholder_text="Distância", width=200)
distance_entry.pack(pady=10)
 
distance_result = customtkinter.CTkLabel(distance_tab, text="", font=("Arial", 16, "bold"))
distance_result.pack(pady=5)
 
distance_btn_frame = customtkinter.CTkFrame(distance_tab, fg_color="transparent")
distance_btn_frame.pack(pady=5)
 
def convert_distance():
    try:
        value = float(distance_entry.get().replace(",", "."))
        from_unit = distance_from.get()
        to_unit = distance_to.get()
 
        if from_unit == "Km" and to_unit == "NM":   result = value / 1.852
        elif from_unit == "NM" and to_unit == "Km": result = value * 1.852
        else:                                        result = value
 
        result_text = f"{value} {from_unit} → {result:.2f} {to_unit}"
        distance_result.configure(text=f"{result:.2f} {to_unit}")
        set_status(result_text)
        add_to_history(result_text)
 
    except ValueError:
        distance_result.configure(text=LANGUAGES[current_lang]["invalid"])
 
def distance_reset():
    distance_entry.delete(0, "end")
    distance_result.configure(text="")
    set_status(LANGUAGES[current_lang]["status_default"])
 
distance_button = customtkinter.CTkButton(distance_btn_frame, text="Converter", command=convert_distance, width=120)
distance_button.pack(side="left", padx=5)
 
distance_reset_btn = customtkinter.CTkButton(distance_btn_frame, text="Reset", command=distance_reset, width=80, fg_color="gray")
distance_reset_btn.pack(side="left", padx=5)
 
# ==== Temperature Tab ==== #
temperature_tab = tabview.tab("Temperatura")
 
temperature_units = ["C", "F", "K"]
 
temperature_from = customtkinter.CTkOptionMenu(temperature_tab, values=temperature_units)
temperature_from.set("C")
temperature_from.pack(pady=10)
 
temperature_to = customtkinter.CTkOptionMenu(temperature_tab, values=temperature_units)
temperature_to.set("F")
temperature_to.pack(pady=5)
 
temperature_entry = customtkinter.CTkEntry(temperature_tab, placeholder_text="Temperatura", width=200)
temperature_entry.pack(pady=10)
 
temperature_result = customtkinter.CTkLabel(temperature_tab, text="", font=("Arial", 16, "bold"))
temperature_result.pack(pady=5)
 
temperature_btn_frame = customtkinter.CTkFrame(temperature_tab, fg_color="transparent")
temperature_btn_frame.pack(pady=5)
 
def convert_temperature():
    try:
        value = float(temperature_entry.get().replace(",", "."))
        from_unit = temperature_from.get()
        to_unit = temperature_to.get()
 
        if from_unit == "C":   base = value + 273.15
        elif from_unit == "F": base = (value - 32) * (5 / 9) + 273.15
        elif from_unit == "K": base = value
 
        if to_unit == "C":     result = base - 273.15
        elif to_unit == "F":   result = (base - 273.15) * (9 / 5) + 32
        elif to_unit == "K":   result = base
 
        result_text = f"{value} {from_unit} → {result:.2f} {to_unit}"
        temperature_result.configure(text=f"{result:.2f} {to_unit}")
        set_status(result_text)
        add_to_history(result_text)
 
    except ValueError:
        temperature_result.configure(text=LANGUAGES[current_lang]["invalid"])
 
def temperature_reset():
    temperature_entry.delete(0, "end")
    temperature_result.configure(text="")
    set_status(LANGUAGES[current_lang]["status_default"])
 
temperature_button = customtkinter.CTkButton(temperature_btn_frame, text="Converter", command=convert_temperature, width=120)
temperature_button.pack(side="left", padx=5)
 
temperature_reset_btn = customtkinter.CTkButton(temperature_btn_frame, text="Reset", command=temperature_reset, width=80, fg_color="gray")
temperature_reset_btn.pack(side="left", padx=5)
 
# ==== History Tab ==== #
history_tab = tabview.tab("Histórico")
 
history_box = customtkinter.CTkTextbox(history_tab, state="disabled", width=500, height=300)
history_box.pack(pady=10, padx=10, fill="both", expand=True)
 
def clear_history():
    global history_entries
    history_entries = []
    history_box.configure(state="normal")
    history_box.delete("1.0", "end")
    history_box.insert("end", LANGUAGES[current_lang]["history_empty"])
    history_box.configure(state="disabled")
    set_status(LANGUAGES[current_lang]["status_default"])
 
clear_history_btn = customtkinter.CTkButton(history_tab, text="Limpar Histórico", command=clear_history, fg_color="gray")
clear_history_btn.pack(pady=5)
 
# ==== Status Bar ==== #
status_bar = customtkinter.CTkFrame(app, corner_radius=0, height=30)
status_bar.pack(fill="x", side="bottom", padx=0, pady=0)
 
status_label = customtkinter.CTkLabel(status_bar, text="Pronto.", anchor="w", font=("Arial", 12))
status_label.pack(side="left", padx=15, pady=4)
 
# ==== Update Language ==== #
def update_language(lang):
    global current_lang
    old_t = LANGUAGES[current_lang]
    current_lang = lang
    t = LANGUAGES[lang]
    font = FONTS[lang]
 
    # ==== Tab Names ==== #
    for key in TAB_KEYS:
        old_name = old_t[key]
        new_name = t[key]
        if old_name != new_name:
            tabview.rename(old_name, new_name)
 
    tabview.set(t["speed_tab"])
 
    # ==== Placeholders ==== #
    speed_entry.configure(placeholder_text=t["speed_placeholder"])
    altitude_entry.configure(placeholder_text=t["altitude_placeholder"])
    distance_entry.configure(placeholder_text=t["distance_placeholder"])
    temperature_entry.configure(placeholder_text=t["temperature_placeholder"])
 
    # ==== Convert Buttons ==== #
    speed_button.configure(text=t["convert"],       font=(font, 13))
    alt_button.configure(text=t["convert"],         font=(font, 13))
    distance_button.configure(text=t["convert"],    font=(font, 13))
    temperature_button.configure(text=t["convert"], font=(font, 13))
 
    # ==== Reset Buttons ==== #
    speed_reset_btn.configure(text=t["reset"],       font=(font, 13))
    alt_reset_btn.configure(text=t["reset"],         font=(font, 13))
    distance_reset_btn.configure(text=t["reset"],    font=(font, 13))
    temperature_reset_btn.configure(text=t["reset"], font=(font, 13))
 
    # ==== Result Labels ==== #
    speed_result.configure(font=(font, 16, "bold"))
    altitude_result.configure(font=(font, 16, "bold"))
    distance_result.configure(font=(font, 16, "bold"))
    temperature_result.configure(font=(font, 16, "bold"))
 
    # ==== History ==== #
    clear_history_btn.configure(text=t["clear_history"], font=(font, 13))
    if not history_entries:
        history_box.configure(state="normal")
        history_box.delete("1.0", "end")
        history_box.insert("end", t["history_empty"])
        history_box.configure(state="disabled")
 
    # ==== Status ==== #
    status_label.configure(font=(font, 12))
    set_status(t["status_default"])
 
# ==== Update Theme ==== #
def update_theme(theme):
    customtkinter.set_appearance_mode(theme)
 
# ==== Bind Selectors ==== #
lang_menu.configure(command=update_language)
theme_menu.configure(command=update_theme)
 
# ==== End ==== #
app.mainloop()
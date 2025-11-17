import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import time
import threading
import math
from datetime import datetime
import webbrowser

class NurPikClientFree:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NurPik Client FREE Edition ULTRA")
        self.root.geometry("1000x800")
        self.root.configure(bg='#0a0a0a')
        
        # НОВЫЕ ПРИКОЛЫ
        self.rage_mode = False
        self.dorito_mode = False
        self.uwu_translator = False
        self.zelenskiy_mode = False
        self.amogus_count = 0
        self.rickroll_immunity = False
        self.fake_fps = 0
        self.matrix_rain = False
        self.discord_mod = False
        self.achievements = set()
        self.meme_level = 0
        self.blyat_counter = 0
        self.cyka_blyat = False
        
        self.setup_ui()
        self.start_madness()
        
    def setup_ui(self):
        # Создаем вкладки для еще большего хаоса
        self.tab_control = ttk.Notebook(self.root)
        
        # Вкладка 1: Основные приколы
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='🎮 ГЛАВНЫЕ ПРИКОЛЫ')
        
        # Вкладка 2: Секретные фичи
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text='🔮 СЕКРЕТНЫЕ ФИЧИ')
        
        # Вкладка 3: Статистика и достижения
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab3, text='🏆 ДОСТИЖЕНИЯ')
        
        self.tab_control.pack(expand=1, fill='both')
        
        self.setup_tab1()
        self.setup_tab2()
        self.setup_tab3()
        
    def setup_tab1(self):
        # Хедер с анимацией
        header = tk.Frame(self.tab1, bg='#1a1a1a', height=60)
        header.pack(fill='x', padx=10, pady=5)
        
        self.title_label = tk.Label(header, text="🔥 NURPIK CLIENT FREE ULTRA 🔥", 
                                   font=("Impact", 20, "bold"), 
                                   bg='#1a1a1a', fg='#ff4444')
        self.title_label.pack(side='left', padx=10)
        
        # Кнопки безумия
        madness_btns = [
            ("💢 RAGE MODE", self.toggle_rage_mode, '#ff0000'),
            ("🥤 DORITO MODE", self.toggle_dorito_mode, '#ff8800'),
            ("🇺🇦 ZELENSKIY MODE", self.toggle_zelenskiy, '#0057b7'),
            ("😠 CYKA BLYAT", self.toggle_cyka_blyat, '#ff0000')
        ]
        
        for text, cmd, color in madness_btns:
            btn = tk.Button(header, text=text, command=cmd,
                          font=("Arial", 8, "bold"), bg=color, fg='white')
            btn.pack(side='right', padx=2)
        
        # НОВЫЕ КАТЕГОРИИ МОДУЛЕЙ
        main_frame = tk.Frame(self.tab1, bg='#0a0a0a')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Левая колонка - Геймерские фичи
        left_frame = tk.Frame(main_frame, bg='#0a0a0a')
        left_frame.pack(side='left', fill='both', expand=True)
        
        categories = [
            ("🎯 ЭПИЧЕСКИЕ ЧИТЫ", [
                "🚀 Полет в 4K 240FPS",
                "👁️ Рентген с ИИ",
                "⚡ Скорость света", 
                "💀 Режим бога PRO",
                "🎯 Аимбот с машинным обучением",
                "📦 Авто-лутер 9000"
            ]),
            ("🤡 МЕМНЫЕ ФИЧИ", [
                "🎵 Рикролл на весь сервер",
                "👊 Ugandan Knuckles Army",
                "🌀 AMOGUS везде",
                "💥 Фейк-баны для друзей",
                "🎮 Фейк FPS 9999",
                "💬 UwU переводчик чата"
            ])
        ]
        
        self.module_vars = {}
        for category_name, modules in categories:
            cat_frame = tk.LabelFrame(left_frame, text=category_name, 
                                     bg='#1a1a1a', fg='#00ff00', font=("Arial", 10, "bold"))
            cat_frame.pack(fill='x', pady=5)
            
            for module in modules:
                var = tk.BooleanVar()
                self.module_vars[module] = var
                cb = tk.Checkbutton(cat_frame, text=module, variable=var,
                                  command=lambda m=module: self.epic_module_toggle(m),
                                  font=("Arial", 8), bg='#1a1a1a', fg='white',
                                  selectcolor='#ff00ff', anchor='w')
                cb.pack(fill='x', pady=1, padx=5)
        
        # Правая колонка - Крутые кнопки
        right_frame = tk.Frame(main_frame, bg='#0a0a0a', width=300)
        right_frame.pack(side='right', fill='y')
        
        epic_buttons = [
            ("🎪 АКТИВИРОВАТЬ ВСЁ", self.activate_everything, '#ff00ff'),
            ("🚨 ФЕЙК АНТИЧИТ", self.fake_anticheat, '#ffff00'),
            ("💾 СКАЧАТЬ ДОП RAM", self.download_more_ram, '#00ff00'),
            ("🎮 БУСТ FPS", self.boost_fps, '#ff8800'),
            ("🔮 СЛУЧАЙНЫЙ ПРИКОЛ", self.random_madness, '#00ffff'),
            ("💥 КРИТИЧЕСКИЙ УРОН", self.critical_damage, '#ff0000'),
            ("🌌 МАТРИЧНЫЙ ДОЖДЬ", self.matrix_rain_mode, '#00ff00'),
            ("📱 ДИСКОРД МОД", self.discord_mode, '#5865f2')
        ]
        
        for text, cmd, color in epic_buttons:
            btn = tk.Button(right_frame, text=text, command=cmd,
                          font=("Arial", 9, "bold"), bg=color, fg='black',
                          width=20, height=2)
            btn.pack(fill='x', pady=3)
        
        # Консоль с прокруткой
        console_frame = tk.LabelFrame(self.tab1, text="📟 ЭПИЧЕСКАЯ КОНСОЛЬ", 
                                     bg='#1a1a1a', fg='#ff00ff')
        console_frame.pack(fill='x', padx=10, pady=5)
        
        self.console = scrolledtext.ScrolledText(console_frame, height=8, 
                                                bg='#000000', fg='#00ff00',
                                                font=("Consolas", 8))
        self.console.pack(fill='both', padx=5, pady=5)
        
        self.log("🚀 NURPIK CLIENT FREE ULTRA ЗАПУЩЕН!")
        self.log("💥 Готов к эпичным приколам!")
    
    def setup_tab2(self):
        # Секретные экспериментальные фичи
        tk.Label(self.tab2, text="🔮 СЕКРЕТНЫЕ ЭКСПЕРИМЕНТАЛЬНЫЕ ФИЧИ", 
                font=("Arial", 16, "bold"), bg='#0a0a0a', fg='#ff00ff').pack(pady=10)
        
        secret_features = [
            ("🧠 ИИ для читов", "ai_cheats"),
            ("🌐 Взлом матрицы", "matrix_hack"),
            ("⚡ Квантовые вычисления", "quantum_calc"),
            ("🔮 Предсказание будущего", "future_predict"),
            ("👽 Инопланетные технологии", "alien_tech"),
            ("🌀 Телепортация", "teleport"),
            ("💫 Манипуляция временем", "time_manipulation"),
            ("🎭 Клонирование игроков", "player_clone")
        ]
        
        for text, feature in secret_features:
            btn = tk.Button(self.tab2, text=text, 
                          command=lambda f=feature: self.secret_feature(f),
                          font=("Arial", 12, "bold"), bg='#330033', fg='#ff00ff',
                          width=25, height=2)
            btn.pack(pady=3)
    
    def setup_tab3(self):
        # Система достижений
        tk.Label(self.tab3, text="🏆 СИСТЕМА ДОСТИЖЕНИЙ", 
                font=("Arial", 16, "bold"), bg='#0a0a0a', fg='#ffff00').pack(pady=10)
        
        self.achievements_text = scrolledtext.ScrolledText(self.tab3, height=15,
                                                          bg='#000000', fg='#ffff00',
                                                          font=("Arial", 10))
        self.achievements_text.pack(fill='both', padx=10, pady=5)
        
        self.update_achievements()
    
    # НОВЫЕ ФУНКЦИИ ПРИКОЛОВ
    
    def toggle_rage_mode(self):
        self.rage_mode = not self.rage_mode
        if self.rage_mode:
            self.log("💢 RAGE MODE АКТИВИРОВАН! AAAAAA!!!")
            self.title_label.config(fg='#ff0000')
            self.unlock_achievement("Rage Gamer")
        else:
            self.log("😐 Rage mode выключен...")
            self.title_label.config(fg='#ff4444')
    
    def toggle_dorito_mode(self):
        self.dorito_mode = not self.dorito_mode
        if self.dorito_mode:
            self.log("🥤 DORITO MODE! Mountain Dew активирован!")
            self.unlock_achievement("True Gamer")
        else:
            self.log("💧 Режим Dorito выключен")
    
    def toggle_zelenskiy(self):
        self.zelenskiy_mode = not self.zelenskiy_mode
        if self.zelenskiy_mode:
            self.log("🇺🇦 СЛАВА УКРАЇНІ! Zelenskiy mode активирован!")
            messagebox.showinfo("Zelenskiy Mode", "Героям слава! 🇺🇦")
        else:
            self.log("🇺🇦 Режим Zelenskiy выключен")
    
    def toggle_cyka_blyat(self):
        self.cyka_blyat = not self.cyka_blyat
        if self.cyka_blyat:
            self.log("😠 CYKA BLYAT! RUSH B!!!")
            self.blyat_counter += 1
            if self.blyat_counter >= 3:
                self.unlock_achievement("Russian Player")
        else:
            self.log("😊 Cyka blyat mode выключен")
    
    def epic_module_toggle(self, module):
        if self.module_vars[module].get():
            self.log(f"✅ АКТИВИРОВАН: {module}")
            
            if "AMOGUS" in module:
                self.amogus_count += 1
                self.log(f"🔴 SUS! AMOGUS count: {self.amogus_count}")
                if self.amogus_count >= 5:
                    self.unlock_achievement("SUS Detective")
            
            elif "UwU" in module:
                self.uwu_translator = True
                self.log("😊 UwU что это? Переводчик активирован!")
        else:
            self.log(f"❌ ВЫКЛЮЧЕН: {module}")
    
    def activate_everything(self):
        for var in self.module_vars.values():
            var.set(True)
        self.log("🎉 ВСЁ АКТИВИРОВАНО! Maximum power overload!")
        self.unlock_achievement("Power Overwhelming")
        
        # Случайные эффекты
        effects = ["🌈", "⚡", "🔥", "💥", "🎆"]
        for effect in random.sample(effects, 3):
            self.log(f"{effect} СЛУЧАЙНЫЙ ЭФФЕКТ АКТИВИРОВАН!")
    
    def fake_anticheat(self):
        anticheats = ["BattleEye", "EasyAntiCheat", "VAC", "FairFight"]
        anticheat = random.choice(anticheats)
        self.log(f"🚨 ФЕЙК {anticheat}: Обнаружены подозрительные действия!")
        
        if random.random() > 0.8:
            self.log("💀 ФЕЙК БАН! Вы 'забанены' на 9999 лет!")
            self.unlock_achievement("Banned Pro")
        else:
            self.log("✅ Фейк античит проигнорирован!")
    
    def download_more_ram(self):
        ram_amount = random.randint(8, 64)
        self.log(f"💾 СКАЧАНО {ram_amount}GB RAM! Ваш ПК теперь суперкомпьютер!")
        
        if ram_amount > 32:
            self.unlock_achievement("RAM King")
    
    def boost_fps(self):
        boost = random.randint(100, 999)
        self.fake_fps = boost
        self.log(f"🎮 FPS БУСТ! Теперь {boost} FPS! Монитор плавится!")
        
        if boost > 500:
            self.unlock_achievement("FPS God")
    
    def random_madness(self):
        madness_options = [
            "🌀 Случайная телепортация!",
            "🎭 Клон создан!",
            "⚡ Молния ударила!",
            "🌌 Портал открыт!",
            "💫 Время замедлилось!"
        ]
        madness = random.choice(madness_options)
        self.log(f"🔮 {madness}")
        self.meme_level += 1
        
        if self.meme_level >= 10:
            self.unlock_achievement("Meme Lord")
    
    def critical_damage(self):
        damage = random.randint(1000, 9999)
        self.log(f"💥 КРИТИЧЕСКИЙ УРОН {damage}! Враги уничтожены!")
        
        if damage > 5000:
            self.unlock_achievement("One Punch Man")
    
    def matrix_rain_mode(self):
        self.matrix_rain = not self.matrix_rain
        if self.matrix_rain:
            self.log("🌌 МАТРИЧНЫЙ ДОЖДЬ! Выбрана красная таблетка!")
            self.unlock_achievement("The One")
        else:
            self.log("💊 Синяя таблетка... Возврат в реальность")
    
    def discord_mode(self):
        self.discord_mod = not self.discord_mod
        if self.discord_mod:
            self.log("📱 ДИСКОРД МОД! Nitro активирован! (нет)")
            self.unlock_achievement("Discord Mod")
        else:
            self.log("📱 Режим Discord выключен")
    
    def secret_feature(self, feature):
        secret_messages = {
            "ai_cheats": "🧠 ИИ ДЛЯ ЧИТОВ: Нейросеть теперь помогает читать мысли противников!",
            "matrix_hack": "🌐 ВЗЛОМ МАТРИЦЫ: Вы видите код... 01001000 01000001 01000011 01001011",
            "quantum_calc": "⚡ КВАНТОВЫЕ ВЫЧИСЛЕНИЯ: Теперь вы в 1000 параллельных вселенных!",
            "future_predict": "🔮 ПРЕДСКАЗАНИЕ: Вы выиграете следующую игру! (или нет)",
            "alien_tech": "👽 ИНОПЛАНЕТНЫЕ ТЕХНОЛОГИИ: UFO подключен к вашему ПК!",
            "teleport": "🌀 ТЕЛЕПОРТАЦИЯ: Вы в другой комнате! (психически)",
            "time_manipulation": "💫 МАНИПУЛЯЦИЯ ВРЕМЕНЕМ: Прошлая минута повторяется!",
            "player_clone": "🎭 КЛОНИРОВАНИЕ: Теперь вас 10! (в воображении)"
        }
        
        message = secret_messages.get(feature, "Секретная фича активирована!")
        self.log(f"🔮 {message}")
        self.unlock_achievement("Secret Finder")
    
    def unlock_achievement(self, achievement):
        if achievement not in self.achievements:
            self.achievements.add(achievement)
            self.log(f"🏆 ДОСТИЖЕНИЕ РАЗБЛОКИРОВАНО: {achievement}!")
            
            # Показать уведомление
            messagebox.showinfo("🏆 ДОСТИЖЕНИЕ!", f"Разблокировано: {achievement}")
    
    def update_achievements(self):
        achievements_list = """
🏆 СИСТЕМА ДОСТИЖЕНИЙ:

✅ Разблокировано: {}/20

СПИСОК ДОСТИЖЕНИЙ:
────────────────────
{}

🎯 Прогресс: {}%
        """.format(
            len(self.achievements),
            "\n".join([f"🏅 {ach}" for ach in sorted(self.achievements)]),
            (len(self.achievements) * 5)
        )
        
        self.achievements_text.delete(1.0, 'end')
        self.achievements_text.insert(1.0, achievements_list)
        
        # Обновляем каждые 2 секунды
        self.root.after(2000, self.update_achievements)
    
    def start_madness(self):
        # Случайные события каждые 10-30 секунд
        def random_events():
            while True:
                time.sleep(random.randint(10, 30))
                if random.random() > 0.7:  # 30% шанс события
                    events = [
                        "🌠 Метеоритный дождь читов!",
                        "🎪 Цирк приколов в городе!",
                        "⚡ Внезапный буст морали!",
                        "🔮 Магическая сила активирована!",
                        "🎰 ДЖЕКПОТ! Вы выиграли ничего!"
                    ]
                    self.log(random.choice(events))
        
        thread = threading.Thread(target=random_events, daemon=True)
        thread.start()
    
    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.console.insert('end', f"[{timestamp}] {message}\n")
        self.console.see('end')
        self.root.update()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    client = NurPikClientFree()
    client.run()
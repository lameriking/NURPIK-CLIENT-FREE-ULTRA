import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import time
import threading
import webbrowser
from datetime import datetime

class NurPikClientFree:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NurPik Client FREE • ULTRA EDITION")
        self.root.geometry("1100x750")
        self.root.configure(bg='#0a0a0a')
        self.root.resizable(True, True)
        
        # НОВЫЕ СУПЕР ФИЧИ 2024
        self.quantum_tunnel = False
        self.neural_network = False
        self.time_travel = False
        self.reality_warp = False
        self.parallel_worlds = False
        self.telepathy_mode = False
        self.invisibility = False
        self.teleportation = False
        self.mind_control = False
        self.gravity_control = False
        self.weather_control = False
        self.luck_boost = False
        
        # Система прокачки
        self.player_level = 1
        self.xp = 0
        self.skills = {
            "speed": 0,
            "aim": 0, 
            "defense": 0,
            "luck": 0,
            "stealth": 0
        }
        
        # Крипто-майнинг (фейковый)
        self.bitcoin_mined = 0
        self.ethereum_mined = 0
        self.dogecoin_mined = 0
        
        self.setup_ultra_ui()
        self.start_crazy_animations()
        
    def setup_ultra_ui(self):
        # Создаем современный хедер с вкладками
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Вкладка 1: Гейминг
        self.gaming_tab = tk.Frame(self.notebook, bg='#0a0a0a')
        self.notebook.add(self.gaming_tab, text='🎮 ГЕЙМИНГ')
        
        # Вкладка 2: Крипто
        self.crypto_tab = tk.Frame(self.notebook, bg='#0a0a0a')
        self.notebook.add(self.crypto_tab, text='💰 КРИПТО')
        
        # Вкладка 3: Прокачка
        self.skills_tab = tk.Frame(self.notebook, bg='#0a0a0a')
        self.notebook.add(self.skills_tab, text='⚡ ПРОКАЧКА')
        
        # Вкладка 4: Эксперименты
        self.experiments_tab = tk.Frame(self.notebook, bg='#0a0a0a')
        self.notebook.add(self.experiments_tab, text='🔮 ЭКСПЕРИМЕНТЫ')
        
        self.setup_gaming_tab()
        self.setup_crypto_tab()
        self.setup_skills_tab()
        self.setup_experiments_tab()
        
    def setup_gaming_tab(self):
        # Хедер гейминг вкладки
        header = tk.Frame(self.gaming_tab, bg='#1a1a1a', height=80)
        header.pack(fill='x', padx=10, pady=5)
        
        tk.Label(header, text="🎮 ULTRA GAMING MODE", font=("Arial", 18, "bold"), 
                bg='#1a1a1a', fg='#ff00ff').pack(side='left', padx=10)
        
        # Основной контент
        main_frame = tk.Frame(self.gaming_tab, bg='#0a0a0a')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Левая колонка - Классические чита
        left_frame = tk.Frame(main_frame, bg='#0a0a0a')
        left_frame.pack(side='left', fill='both', expand=True)
        
        tk.Label(left_frame, text="🛠️ КЛАССИЧЕСКИЕ ЧИТЫ", font=("Arial", 14, "bold"),
                bg='#0a0a0a', fg='#00ff88').pack(anchor='w', pady=(0, 10))
        
        classic_cheats = [
            "🚀 Ультра-полет PRO",
            "⚡ Гипер-скорость V2",
            "👁️ Рентген 4K", 
            "💀 Бессмертие GOD",
            "🎯 Аимбот AI",
            "📦 Магнит для лута",
            "🛡️ Абсолютная защита",
            "🔮 Видение сквозь стены"
        ]
        
        self.classic_vars = {}
        for cheat in classic_cheats:
            var = tk.BooleanVar()
            self.classic_vars[cheat] = var
            cb = tk.Checkbutton(left_frame, text=cheat, variable=var,
                              font=("Arial", 10), bg='#0a0a0a', fg='white',
                              selectcolor='#ff00ff', anchor='w')
            cb.pack(fill='x', pady=2)
        
        # Правая колонка - Крутые кнопки
        right_frame = tk.Frame(main_frame, bg='#0a0a0a', width=300)
        right_frame.pack(side='right', fill='y')
        
        gaming_buttons = [
            ("🎯 АКТИВИРОВАТЬ ВСЁ", self.activate_all_cheats, '#ff00ff'),
            ("🚀 ЗАПУСК РАКЕТЫ", self.launch_rocket, '#ff4444'),
            ("⚡ БУСТ FPS", self.boost_fps, '#00ff88'),
            ("🎮 СИМУЛЯТОР БАНА", self.simulate_ban, '#ffff00'),
            ("🔮 СЛУЧАЙНЫЙ ЧИТ", self.random_cheat, '#00ffff'),
            ("💥 КРИТИЧЕСКИЙ УРОН", self.critical_damage, '#ff8800')
        ]
        
        for text, cmd, color in gaming_buttons:
            btn = tk.Button(right_frame, text=text, command=cmd,
                          font=("Arial", 10, "bold"), bg=color, fg='black',
                          width=20, height=2)
            btn.pack(fill='x', pady=5)
        
        # Консоль гейминга
        console_frame = tk.LabelFrame(self.gaming_tab, text="🎯 ГЕЙМИНГ КОНСОЛЬ", 
                                     bg='#1a1a1a', fg='#ff00ff')
        console_frame.pack(fill='x', padx=10, pady=5)
        
        self.gaming_console = scrolledtext.ScrolledText(console_frame, height=8,
                                                       bg='#000000', fg='#00ff00',
                                                       font=("Consolas", 8))
        self.gaming_console.pack(fill='both', padx=5, pady=5)
        
        self.gaming_log("🎮 Гейминг система активирована!")
        self.gaming_log("💡 Готов к эпичным победам!")
    
    def setup_crypto_tab(self):
        # Крипто майнинг интерфейс
        header = tk.Frame(self.crypto_tab, bg='#1a1a1a', height=60)
        header.pack(fill='x', padx=10, pady=5)
        
        tk.Label(header, text="💰 КРИПТО МАЙНИНГ 9000", font=("Arial", 16, "bold"), 
                bg='#1a1a1a', fg='#ffaa00').pack(side='left', padx=10)
        
        # Основной контент крипто
        main_frame = tk.Frame(self.crypto_tab, bg='#0a0a0a')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Левая колонка - Майнинг пулы
        left_frame = tk.Frame(main_frame, bg='#0a0a0a')
        left_frame.pack(side='left', fill='both', expand=True)
        
        mining_pools = [
            ("₿ Bitcoin Pool", "bitcoin", "#ff9900"),
            ("Ξ Ethereum Pool", "ethereum", "#8c8c8c"), 
            ("Ð Dogecoin Pool", "dogecoin", "#bb9c33"),
            ("₿ Bitcoin Cash", "bitcoincash", "#00cc66"),
            ("Ł Litecoin", "litecoin", "#bebebe"),
            ("X Monero", "monero", "#ff6600")
        ]
        
        for name, coin, color in mining_pools:
            pool_frame = tk.Frame(left_frame, bg='#1a1a1a', relief='ridge', bd=1)
            pool_frame.pack(fill='x', pady=3)
            
            tk.Label(pool_frame, text=name, font=("Arial", 10, "bold"),
                    bg='#1a1a1a', fg=color).pack(side='left', padx=10, pady=5)
            
            btn = tk.Button(pool_frame, text="⛏️ Майнить", 
                          command=lambda c=coin: self.start_mining(c),
                          font=("Arial", 8), bg=color, fg='black')
            btn.pack(side='right', padx=10, pady=5)
        
        # Правая колонка - Статистика майнинга
        right_frame = tk.Frame(main_frame, bg='#0a0a0a', width=300)
        right_frame.pack(side='right', fill='y')
        
        stats_frame = tk.LabelFrame(right_frame, text="📊 СТАТИСТИКА МАЙНИНГА", 
                                   bg='#1a1a1a', fg='#00ff88')
        stats_frame.pack(fill='x', pady=(0, 10))
        
        self.mining_stats = tk.Text(stats_frame, height=10, bg='#000000', fg='#ffaa00',
                                   font=("Consolas", 8), wrap=tk.WORD)
        self.mining_stats.pack(fill='both', padx=5, pady=5)
        
        # Кнопки крипто
        crypto_buttons = [
            ("💰 БЫСТРЫЙ МАЙНИНГ", self.quick_mining, '#ffaa00'),
            ("🎰 КРИПТО-ЛОТЕРЕЯ", self.crypto_lottery, '#ff00ff'),
            ("📈 ПРОГНОЗ КУРСА", self.predict_price, '#00ff88'),
            ("💸 ВЫВОД СРЕДСТВ", self.withdraw_funds, '#ff4444')
        ]
        
        for text, cmd, color in crypto_buttons:
            btn = tk.Button(right_frame, text=text, command=cmd,
                          font=("Arial", 9, "bold"), bg=color, fg='black',
                          width=20)
            btn.pack(fill='x', pady=3)
        
        self.update_mining_stats()
    
    def setup_skills_tab(self):
        # Система прокачки
        header = tk.Frame(self.skills_tab, bg='#1a1a1a', height=60)
        header.pack(fill='x', padx=10, pady=5)
        
        tk.Label(header, text="⚡ СИСТЕМА ПРОКАЧКИ", font=("Arial", 16, "bold"), 
                bg='#1a1a1a', fg='#00ffff').pack(side='left', padx=10)
        
        # Основной контент прокачки
        main_frame = tk.Frame(self.skills_tab, bg='#0a0a0a')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Левая колонка - Навыки
        left_frame = tk.Frame(main_frame, bg='#0a0a0a')
        left_frame.pack(side='left', fill='both', expand=True)
        
        skills = [
            ("⚡ Скорость", "speed", "Увеличивает скорость передвижения"),
            ("🎯 Точность", "aim", "Улучшает меткость стрельбы"),
            ("🛡️ Защита", "defense", "Повышает сопротивление урону"),
            ("🍀 Удача", "luck", "Увеличивает шанс критического урона"),
            ("👻 Стелс", "stealth", "Уменьшает заметность для врагов")
        ]
        
        for name, skill, desc in skills:
            skill_frame = tk.Frame(left_frame, bg='#1a1a1a', relief='ridge', bd=1)
            skill_frame.pack(fill='x', pady=3)
            
            tk.Label(skill_frame, text=name, font=("Arial", 10, "bold"),
                    bg='#1a1a1a', fg='#00ff88').pack(side='left', padx=10, pady=5)
            
            tk.Label(skill_frame, text=f"Ур. {self.skills[skill]}", font=("Arial", 9),
                    bg='#1a1a1a', fg='#ffaa00').pack(side='left', padx=10)
            
            btn = tk.Button(skill_frame, text="⬆️ Прокачать", 
                          command=lambda s=skill: self.upgrade_skill(s),
                          font=("Arial", 8), bg='#00ff88', fg='black')
            btn.pack(side='right', padx=10, pady=5)
            
            tk.Label(skill_frame, text=desc, font=("Arial", 8),
                    bg='#1a1a1a', fg='#888888').pack(side='top', anchor='w', padx=10, pady=(0, 5))
        
        # Правая колонка - Статистика игрока
        right_frame = tk.Frame(main_frame, bg='#0a0a0a', width=300)
        right_frame.pack(side='right', fill='y')
        
        player_frame = tk.LabelFrame(right_frame, text="👤 СТАТИСТИКА ИГРОКА", 
                                    bg='#1a1a1a', fg='#ff00ff')
        player_frame.pack(fill='x', pady=(0, 10))
        
        self.player_stats = tk.Text(player_frame, height=12, bg='#000000', fg='#00ffff',
                                   font=("Consolas", 9), wrap=tk.WORD)
        self.player_stats.pack(fill='both', padx=5, pady=5)
        
        # Кнопки прокачки
        skill_buttons = [
            ("🎯 БЫСТРАЯ ПРОКАЧКА", self.quick_level_up, '#ff00ff'),
            ("🔄 СБРОС НАВЫКОВ", self.reset_skills, '#ff4444'),
            ("💫 СЛУЧАЙНЫЙ БУСТ", self.random_boost, '#00ff88')
        ]
        
        for text, cmd, color in skill_buttons:
            btn = tk.Button(right_frame, text=text, command=cmd,
                          font=("Arial", 9, "bold"), bg=color, fg='black',
                          width=20)
            btn.pack(fill='x', pady=3)
        
        self.update_player_stats()
    
    def setup_experiments_tab(self):
        # Экспериментальные фичи
        header = tk.Frame(self.experiments_tab, bg='#1a1a1a', height=60)
        header.pack(fill='x', padx=10, pady=5)
        
        tk.Label(header, text="🔮 ЭКСПЕРИМЕНТАЛЬНЫЕ ТЕХНОЛОГИИ", font=("Arial", 16, "bold"), 
                bg='#1a1a1a', fg='#ff00ff').pack(side='left', padx=10)
        
        # Сетка экспериментальных фич
        main_frame = tk.Frame(self.experiments_tab, bg='#0a0a0a')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        experiments = [
            ("🌀", "Квантовый туннель", "Прохождение сквозь стены", self.toggle_quantum),
            ("🧠", "Нейросеть", "ИИ для предсказания врагов", self.toggle_neural),
            ("⏰", "Путешествие во времени", "Возврат на 5 секунд назад", self.toggle_time_travel),
            ("🌌", "Искажение реальности", "Изменение законов физики", self.toggle_reality_warp),
            ("🌐", "Параллельные миры", "Доступ к другим вселенным", self.toggle_parallel),
            ("💭", "Телепатия", "Чтение мыслей противников", self.toggle_telepathy),
            ("👻", "Невидимость", "Полная невидимость для врагов", self.toggle_invisibility),
            ("⚡", "Телепортация", "Мгновенное перемещение", self.toggle_teleportation),
            ("🎮", "Контроль разума", "Управление действиями врагов", self.toggle_mind_control),
            ("🌍", "Контроль гравитации", "Изменение силы тяжести", self.toggle_gravity),
            ("🌦️", "Контроль погоды", "Создание тумана и шторма", self.toggle_weather),
            ("🍀", "Увеличение удачи", "Критические удары x10", self.toggle_luck)
        ]
        
        for i, (emoji, name, desc, cmd) in enumerate(experiments):
            row, col = i // 3, i % 3
            exp_frame = tk.Frame(main_frame, bg='#1a1a1a', relief='ridge', bd=1)
            exp_frame.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            main_frame.columnconfigure(col, weight=1)
            main_frame.rowconfigure(row, weight=1)
            
            tk.Label(exp_frame, text=emoji, font=("Arial", 14),
                    bg='#1a1a1a', fg='#ff00ff').pack(pady=(10, 0))
            
            tk.Label(exp_frame, text=name, font=("Arial", 9, "bold"),
                    bg='#1a1a1a', fg='white').pack()
            
            tk.Label(exp_frame, text=desc, font=("Arial", 7),
                    bg='#1a1a1a', fg='#888888', wraplength=150).pack(padx=5, pady=5)
            
            btn = tk.Button(exp_frame, text="АКТИВИРОВАТЬ", command=cmd,
                          font=("Arial", 8, "bold"), bg='#ff00ff', fg='black')
            btn.pack(pady=(0, 10))
    
    # НОВЫЕ ФУНКЦИИ
    
    def activate_all_cheats(self):
        for var in self.classic_vars.values():
            var.set(True)
        self.gaming_log("🎉 ВСЕ ЧИТЫ АКТИВИРОВАНЫ! Maximum power!")
        self.add_xp(50)
    
    def launch_rocket(self):
        self.gaming_log("🚀 ЗАПУСК РАКЕТЫ! Поехали!")
        for i in range(3, 0, -1):
            self.root.after(1000 * (3-i), lambda x=i: self.gaming_log(f"🚀 Обратный отсчет: {x}..."))
        self.root.after(3000, lambda: self.gaming_log("🎇 РАКЕТА УСПЕШНО ЗАПУЩЕНА!"))
    
    def boost_fps(self):
        boost = random.randint(100, 500)
        self.gaming_log(f"⚡ FPS БУСТ! Теперь {boost} FPS!")
        self.add_xp(10)
    
    def simulate_ban(self):
        if random.random() > 0.3:
            self.gaming_log("💀 СИМУЛЯЦИЯ БАНА! Вы 'забанены' на 30 дней!")
        else:
            self.gaming_log("🍀 Бан прошел мимо! Вам повезло!")
        self.add_xp(5)
    
    def random_cheat(self):
        cheats = ["🌀 Невидимость", "⚡ Телепортация", "🎯 Авто-прицел", "💥 Мега-урон"]
        cheat = random.choice(cheats)
        self.gaming_log(f"🎰 СЛУЧАЙНЫЙ ЧИТ: {cheat}!")
        self.add_xp(15)
    
    def critical_damage(self):
        damage = random.randint(1000, 9999)
        self.gaming_log(f"💥 КРИТИЧЕСКИЙ УРОН {damage}! Враги уничтожены!")
        self.add_xp(20)
    
    def start_mining(self, coin):
        mined = random.uniform(0.001, 0.1)
        if coin == "bitcoin":
            self.bitcoin_mined += mined
            self.mining_log(f"⛏️ Добыто: {mined:.6f} BTC")
        elif coin == "ethereum":
            self.ethereum_mined += mined
            self.mining_log(f"⛏️ Добыто: {mined:.6f} ETH")
        elif coin == "dogecoin":
            self.dogecoin_mined += mined * 1000
            self.mining_log(f"⛏️ Добыто: {mined*1000:.2f} DOGE")
        
        self.add_xp(5)
    
    def quick_mining(self):
        coins = ["bitcoin", "ethereum", "dogecoin"]
        for coin in coins:
            self.start_mining(coin)
        self.mining_log("💰 БЫСТРЫЙ МАЙНИНГ завершен!")
    
    def crypto_lottery(self):
        prizes = ["0.5 BTC", "10 ETH", "50000 DOGE", "НИЧЕГО", "1 BTC"]
        prize = random.choice(prizes)
        self.mining_log(f"🎰 КРИПТО-ЛОТЕРЕЯ: Вы выиграли {prize}!")
        self.add_xp(10)
    
    def predict_price(self):
        changes = ["+15%", "-8%", "+23%", "+5%", "-12%", "+30%"]
        change = random.choice(changes)
        self.mining_log(f"📈 ПРОГНОЗ: Bitcoin вырастет на {change} завтра!")
    
    def withdraw_funds(self):
        total = self.bitcoin_mined * 50000 + self.ethereum_mined * 3000 + self.dogecoin_mined * 0.1
        self.mining_log(f"💸 ВЫВОД СРЕДСТВ: ${total:.2f} отправлены на ваш кошелек!")
    
    def upgrade_skill(self, skill):
        if self.xp >= 10:
            self.skills[skill] += 1
            self.xp -= 10
            self.skills_log(f"⬆️ Прокачан навык {skill} до уровня {self.skills[skill]}!")
            self.add_xp(0)  # Обновляем статистику
        else:
            self.skills_log("❌ Недостаточно опыта для прокачки!")
    
    def quick_level_up(self):
        if self.xp >= 30:
            self.player_level += 1
            self.xp -= 30
            self.skills_log(f"🎯 БЫСТРАЯ ПРОКАЧКА! Новый уровень: {self.player_level}!")
            self.add_xp(0)
        else:
            self.skills_log("❌ Недостаточно опыта для быстрой прокачки!")
    
    def reset_skills(self):
        for skill in self.skills:
            self.skills[skill] = 0
        self.skills_log("🔄 Все навыки сброшены!")
        self.add_xp(0)
    
    def random_boost(self):
        skill = random.choice(list(self.skills.keys()))
        self.skills[skill] += random.randint(1, 3)
        self.skills_log(f"💫 СЛУЧАЙНЫЙ БУСТ! Навык {skill} увеличен!")
        self.add_xp(0)
    
    def add_xp(self, amount):
        self.xp += amount
        while self.xp >= 100:
            self.player_level += 1
            self.xp -= 100
            self.gaming_log(f"🎉 НОВЫЙ УРОВЕНЬ! Теперь уровень {self.player_level}!")
        self.update_player_stats()
    
    # Тогглы экспериментальных фич
    def toggle_quantum(self): self.quantum_tunnel = not self.quantum_tunnel; self.experiment_log("🌀 Квантовый туннель")
    def toggle_neural(self): self.neural_network = not self.neural_network; self.experiment_log("🧠 Нейросеть")
    def toggle_time_travel(self): self.time_travel = not self.time_travel; self.experiment_log("⏰ Путешествие во времени")
    def toggle_reality_warp(self): self.reality_warp = not self.reality_warp; self.experiment_log("🌌 Искажение реальности")
    def toggle_parallel(self): self.parallel_worlds = not self.parallel_worlds; self.experiment_log("🌐 Параллельные миры")
    def toggle_telepathy(self): self.telepathy_mode = not self.telepathy_mode; self.experiment_log("💭 Телепатия")
    def toggle_invisibility(self): self.invisibility = not self.invisibility; self.experiment_log("👻 Невидимость")
    def toggle_teleportation(self): self.teleportation = not self.teleportation; self.experiment_log("⚡ Телепортация")
    def toggle_mind_control(self): self.mind_control = not self.mind_control; self.experiment_log("🎮 Контроль разума")
    def toggle_gravity(self): self.gravity_control = not self.gravity_control; self.experiment_log("🌍 Контроль гравитации")
    def toggle_weather(self): self.weather_control = not self.weather_control; self.experiment_log("🌦️ Контроль погоды")
    def toggle_luck(self): self.luck_boost = not self.luck_boost; self.experiment_log("🍀 Увеличение удачи")
    
    def experiment_log(self, feature):
        status = "активирована" if getattr(self, feature.split()[1].lower() + "_mode", 
                                         getattr(self, feature.split()[1].lower(), False)) else "выключена"
        messagebox.showinfo("Эксперимент", f"{feature} {status}!")
    
    # Система логирования
    def gaming_log(self, message): self._log_to_console(self.gaming_console, message)
    def mining_log(self, message): self._log_to_console(self.mining_stats, message)
    def skills_log(self, message): self._log_to_console(self.player_stats, message)
    
    def _log_to_console(self, console, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        console.insert('end', f"[{timestamp}] {message}\n")
        console.see('end')
    
    # Обновление статистики
    def update_mining_stats(self):
        stats = f"""
╔══════════════════════════════════╗
║         СТАТИСТИКА МАЙНИНГА      ║
╠══════════════════════════════════╣
║ ₿ Bitcoin:    {self.bitcoin_mined:.6f} BTC   ║
║ Ξ Ethereum:   {self.ethereum_mined:.6f} ETH  ║
║ Ð Dogecoin:   {self.dogecoin_mined:.2f} DOGE ║
║                                ║
║ 💰 Общая стоимость:            ║
║ ${self.bitcoin_mined*50000 + self.ethereum_mined*3000 + self.dogecoin_mined*0.1:.2f} ║
╚══════════════════════════════════╝
        """
        if hasattr(self, 'mining_stats'):
            self.mining_stats.delete(1.0, 'end')
            self.mining_stats.insert(1.0, stats)
        self.root.after(3000, self.update_mining_stats)
    
    def update_player_stats(self):
        stats = f"""
╔══════════════════════════════════╗
║         СТАТИСТИКА ИГРОКА        ║
╠══════════════════════════════════╣
║ 🎮 Уровень:      {self.player_level}          ║
║ ⭐ Опыт:         {self.xp}/100       ║
║                                ║
║ ⚡ НАВЫКИ:                      ║
║ • Скорость:     {self.skills['speed']}        ║
║ • Точность:     {self.skills['aim']}        ║
║ • Защита:       {self.skills['defense']}        ║
║ • Удача:        {self.skills['luck']}        ║
║ • Стелс:        {self.skills['stealth']}        ║
╚══════════════════════════════════╝
        """
        if hasattr(self, 'player_stats'):
            self.player_stats.delete(1.0, 'end')
            self.player_stats.insert(1.0, stats)
    
    def start_crazy_animations(self):
        def animate():
            while True:
                # Случайные события в консоли
                if random.random() > 0.95:
                    events = [
                        "🌟 В ближайшем матче вас ждет победа!",
                        "⚡ Обнаружена новая версия чита!",
                        "🎁 Секретная награда разблокирована!",
                        "🔮 Магическая сила активирована!",
                        "💫 Космический буст применен!"
                    ]
                    self.gaming_log(random.choice(events))
                time.sleep(10)
        
        thread = threading.Thread(target=animate, daemon=True)
        thread.start()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    client = NurPikClientFree()
    client.run()
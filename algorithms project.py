"""
كيفية تشغيل البرنامج:
1. تأكد من تثبيت Python 3.8 أو أحدث.
2. احفظ هذا الكود في ملف باسم app.py.
3. افتح الطرفية (Terminal) أو موجه الأوامر (Command Prompt) وانتقل إلى المجلد الذي يحتوي على الملف.
4. قم بتشغيل الأمر: python app.py

أمثلة إدخال للمصفوفات:
- 3,1,4,1,5
- 10,4,8,1,7,2,9,5,3,6

قيود معروفة:
- لا يوجد دعم لتلوين بناء الجملة لكود الخوارزميات المعروضة داخل التطبيق بدون مكتبات خارجية.
- قد تختلف سرعة المحاكاة بناءً على أداء الجهاز.
"""

import tkinter as tk
from tkinter import messagebox, ttk
import time
import threading
import math
import random

# بيانات الفريق
TEAM_INFO = {
    "students": [
        "محمد سيف عبده مسعد قايد",
        "محمد حمود محمد الحاج الحرق",
        "مهند عبدالقوي عبدالله غلاب",
        "معتز بشير محمد مصلح الرحبي"
    ],
    "supervisor": "أ.المهندس: عبد الرحمن غازي"
}

class ResponsiveApp(tk.Tk):
    """
    التطبيق الرئيسي مع واجهة متجاوبة
    """
    def __init__(self):
        super().__init__()
        self.title("مشروع خوارزميات عملي - واجهة متجاوبة")
        self.geometry("1400x900")
        self.minsize(1000, 700)
        
        # تهيئة النمط
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Tahoma", 10))
        self.style.configure("TLabel", font=("Tahoma", 10))
        
        self.current_frame = None
        self._setup_main_container()
        self.show_login_screen()

    def _setup_main_container(self):
        """إعداد الحاوية الرئيسية"""
        self.main_container = tk.Frame(self, bg="#f0f8ff")
        self.main_container.pack(fill=tk.BOTH, expand=True)
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

    def show_frame(self, frame_class, *args, **kwargs):
        """عرض إطار جديد"""
        new_frame = frame_class(self.main_container, self, *args, **kwargs)
        
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = new_frame
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

    def show_login_screen(self):
        self.show_frame(EnhancedLoginScreen)

    def show_menu_screen(self):
        self.show_frame(MenuScreen)

    def show_algorithm_screen(self, algorithm_class, algorithm_name):
        self.show_frame(algorithm_class, algorithm_name=algorithm_name)


class EnhancedLoginScreen(tk.Frame):
    """شاشة تسجيل الدخول محسنة مع معلومات الفريق"""
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f0f0")
        self.controller = controller
        self._create_enhanced_layout()

    def _create_enhanced_layout(self):
        """إنشاء واجهة تسجيل دخول متكاملة"""
        # إعداد grid متجاوب
        self.grid_rowconfigure(0, weight=0)  # header
        self.grid_rowconfigure(1, weight=1)  # content
        self.grid_rowconfigure(2, weight=0)  # footer
        self.grid_columnconfigure(0, weight=1)

        # الرأس مع معلومات الفريق
        self._create_header()

        # المحتوى الرئيسي
        content_frame = tk.Frame(self, bg="#f0f0f0")
        content_frame.grid(row=1, column=0, sticky="nsew")
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)

        # لوحة معلومات الفريق (اليسار)
        self._create_team_info_panel(content_frame)

        # لوحة تسجيل الدخول (اليمين)
        self._create_login_panel(content_frame)

        # التذييل
        self._create_footer()

    def _create_header(self):
        """إنشاء رأس الصفحة"""
        header_frame = tk.Frame(self, bg="#2c3e50", height=100)
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.grid_propagate(False)
        header_frame.grid_columnconfigure(0, weight=1)
        
        tk.Label(header_frame, text="مشروع خوارزميات عملي", 
                font=("Tahoma", 24, "bold"), bg="#2c3e50", fg="white"
        ).grid(row=0, column=0, pady=20)

    def _create_team_info_panel(self, parent):
        """إنشاء لوحة معلومات الفريق"""
        team_frame = tk.Frame(parent, bg="#ecf0f1", relief=tk.RAISED, bd=2)
        team_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=20)
        team_frame.grid_rowconfigure(1, weight=1)
        team_frame.grid_columnconfigure(0, weight=1)

        # عنوان اللوحة
        tk.Label(team_frame, text="معلومات الفريق", 
                font=("Tahoma", 16, "bold"), bg="#ecf0f1"
        ).grid(row=0, column=0, pady=10)

        # محتوى معلومات الفريق
        info_content = tk.Frame(team_frame, bg="#ecf0f1")
        info_content.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        # معلومات الطلاب
        tk.Label(info_content, text="أعضاء الفريق:", 
                font=("Tahoma", 14, "bold"), bg="#ecf0f1", anchor="w"
        ).pack(fill=tk.X, pady=(0, 10))

        for student in TEAM_INFO["students"]:
            student_frame = tk.Frame(info_content, bg="#ecf0f1")
            student_frame.pack(fill=tk.X, pady=2)
            tk.Label(student_frame, text="•", font=("Tahoma", 12), bg="#ecf0f1").pack(side=tk.LEFT)
            tk.Label(student_frame, text=student, font=("Tahoma", 12), 
                   bg="#ecf0f1", anchor="w").pack(side=tk.LEFT, padx=(5, 0))

        # معلومات المشرف
        tk.Label(info_content, text="المشرف:", 
                font=("Tahoma", 14, "bold"), bg="#ecf0f1", anchor="w"
        ).pack(fill=tk.X, pady=(20, 5))

        supervisor_frame = tk.Frame(info_content, bg="#ecf0f1")
        supervisor_frame.pack(fill=tk.X, pady=2)
        tk.Label(supervisor_frame, text=TEAM_INFO["supervisor"], 
                font=("Tahoma", 12, "italic"), bg="#ecf0f1", anchor="w"
        ).pack(side=tk.LEFT)

    def _create_login_panel(self, parent):
        """إنشاء لوحة تسجيل الدخول"""
        login_frame = tk.Frame(parent, bg="white", relief=tk.RAISED, bd=2)
        login_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 20), pady=20)
        login_frame.grid_rowconfigure(0, weight=1)
        login_frame.grid_columnconfigure(0, weight=1)

        # نموذج تسجيل الدخول
        form_frame = tk.Frame(login_frame, bg="white")
        form_frame.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)

        # عنوان النموذج
        tk.Label(form_frame, text="تسجيل الدخول", 
                font=("Tahoma", 20, "bold"), bg="white", fg="#2c3e50"
        ).pack(pady=(0, 30))

        # حقول الإدخال
        self._create_login_fields(form_frame)

        # أزرار التحكم
        self._create_login_buttons(form_frame)

    def _create_login_fields(self, parent):
        """إنشاء حقول تسجيل الدخول"""
        # اسم المستخدم
        user_frame = tk.Frame(parent, bg="white")
        user_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(user_frame, text="اسم المستخدم:", 
                font=("Tahoma", 12), bg="white"
        ).pack(anchor="w")
        
        self.username_entry = tk.Entry(user_frame, font=("Tahoma", 12), width=30)
        self.username_entry.pack(fill=tk.X, pady=5)

        # كلمة المرور
        pass_frame = tk.Frame(parent, bg="white")
        pass_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(pass_frame, text="كلمة المرور:", 
                font=("Tahoma", 12), bg="white"
        ).pack(anchor="w")
        
        self.password_entry = tk.Entry(pass_frame, font=("Tahoma", 12), 
                                     show="•", width=30)
        self.password_entry.pack(fill=tk.X, pady=5)

        # تأكيد كلمة المرور
        confirm_frame = tk.Frame(parent, bg="white")
        confirm_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(confirm_frame, text="تأكيد كلمة المرور:", 
                font=("Tahoma", 12), bg="white"
        ).pack(anchor="w")
        
        self.confirm_password_entry = tk.Entry(confirm_frame, font=("Tahoma", 12), 
                                             show="•", width=30)
        self.confirm_password_entry.pack(fill=tk.X, pady=5)

        # التحقق من الروبوت
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.correct_answer = self.num1 + self.num2
        
        robot_frame = tk.Frame(parent, bg="white")
        robot_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(robot_frame, text=f"ما هو ناتج {self.num1} + {self.num2}؟", 
                font=("Tahoma", 12), bg="white"
        ).pack(anchor="w")
        
        self.robot_check_entry = tk.Entry(robot_frame, font=("Tahoma", 12), width=30)
        self.robot_check_entry.pack(fill=tk.X, pady=5)

    def _create_login_buttons(self, parent):
        """إنشاء أزرار تسجيل الدخول"""
        button_frame = tk.Frame(parent, bg="white")
        button_frame.pack(fill=tk.X, pady=(30, 0))

        # زر الدخول (أزرق غامق)
        login_btn = tk.Button(button_frame, text="دخول (Login)", 
                            font=("Tahoma", 14, "bold"), 
                            bg="#2980b9", fg="white",
                            command=self.login, width=15, height=1)
        login_btn.pack(side=tk.RIGHT, padx=(10, 0))

        # زر الخروج (أحمر داكن)
        exit_btn = tk.Button(button_frame, text="خروج (Exit)", 
                           font=("Tahoma", 14, "bold"), 
                           bg="#c0392b", fg="white",
                           command=self.confirm_exit, width=15, height=1)
        exit_btn.pack(side=tk.LEFT, padx=(0, 10))

    def _create_footer(self):
        """إنشاء تذييل الصفحة"""
        footer_frame = tk.Frame(self, bg="#34495e", height=60)
        footer_frame.grid(row=2, column=0, sticky="ew")
        footer_frame.grid_propagate(False)
        
        tk.Label(footer_frame, text="جامعة حضرموت - كلية الهندسة", 
                font=("Tahoma", 10), bg="#34495e", fg="white"
        ).pack(side=tk.RIGHT, padx=20, pady=10)

    def login(self):
        """التحقق من بيانات التسجيل"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        robot_answer = self.robot_check_entry.get()

        if not username or not password:
            messagebox.showerror("خطأ", "يرجى إدخال اسم المستخدم وكلمة المرور")
            return

        if password != confirm_password:
            messagebox.showerror("خطأ", "كلمة المرور وتأكيدها غير متطابقين")
            return

        try:
            if int(robot_answer) != self.correct_answer:
                messagebox.showerror("خطأ", "الإجابة على سؤال التحقق غير صحيحة")
                return
        except ValueError:
            messagebox.showerror("خطأ", "يرجى إدخال رقم صحيح للإجابة على سؤال التحقق")
            return

        messagebox.showinfo("نجاح", f"مرحباً {username}! تم تسجيل الدخول بنجاح")
        self.controller.show_menu_screen()

    def confirm_exit(self):
        """تأكيد الخروج من التطبيق"""
        if messagebox.askyesno("تأكيد الخروج", "هل أنت متأكد من رغبتك في الخروج؟"):
            self.controller.quit()

class MenuScreen(tk.Frame):
    """
    شاشة قائمة الخوارزميات التي تعرض الخوارزميات المتاحة.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#e0f7fa")
        self.create_widgets()

    def create_widgets(self):
        """
        ينشئ عناصر واجهة المستخدم لشاشة القائمة.
        """
        tk.Label(self, text="اختر خوارزمية للبدء", font=("Arial", 20, "bold"), bg="#e0f7fa").pack(pady=20)

        algorithms_frame = tk.Frame(self, bg="#e0f7fa")
        algorithms_frame.pack(pady=10)

        # تعريف الخوارزميات
        algorithms = [
            ("خوارزمية الدمج (Merge Sort)", MergeSortScreen, "Merge Sort"),
            ("خوارزمية الفقاعية (Bubble Sort)", BubbleSortScreen, "Bubble Sort"),
            ("خوارزمية فيبوناتشي (Fibonacci)", FibonacciScreen, "Fibonacci"),
            ("خوارزمية فرز الكومة (Heap Sort)", HeapSortScreen, "Heap Sort"),
            ("خوارزمية الحشر (Insertion Sort)", InsertionSortScreen, "Insertion Sort"),
            ("خوارزمية الفرز السريع (Quick Sort)", QuickSortScreen, "Quick Sort"),  # إضافة الفرز السريع
        ]

        for i, (arabic_name, algo_class, english_name) in enumerate(algorithms):
            btn = tk.Button(algorithms_frame, text=arabic_name, font=("Arial", 14), width=30, height=2,
                            command=lambda ac=algo_class, an=english_name: self.controller.show_algorithm_screen(ac, an),
                            bg="#00796b", fg="white", relief=tk.RAISED, bd=3)
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)

        tk.Button(self, text="رجوع للواجهة الرئيسية", font=("Arial", 12), command=self.controller.show_login_screen, bg="#607d8b", fg="white", padx=15, pady=8).pack(pady=20)


class BaseAlgorithmScreen(tk.Frame):
    """
    الفئة الأساسية لشاشات الخوارزميات، توفر الهيكل المشترك والأزرار والوظائف الأساسية.
    """
    def __init__(self, parent, controller, algorithm_name):
        super().__init__(parent)
        self.controller = controller
        self.algorithm_name = algorithm_name
        self.original_array = []
        self.current_array = []
        self.simulation_thread = None
        self.is_running = False
        self.pause_event = threading.Event()
        self.pause_event.set() # Set to allow running initially
        self.stop_event = threading.Event()
        self.delay = 0.1 # Default animation delay

        self.configure(bg="#f0f8ff")
        self.grid_rowconfigure(1, weight=1) # Canvas row
        self.grid_columnconfigure(0, weight=1) # Left panel
        self.grid_columnconfigure(1, weight=3) # Canvas
        self.grid_columnconfigure(2, weight=1) # Right panel

        self.create_widgets()

    def create_widgets(self):
        """
        ينشئ عناصر واجهة المستخدم المشتركة لجميع شاشات الخوارزميات.
        """
        # Top Bar
        top_frame = tk.Frame(self, bg="#add8e6")
        top_frame.grid(row=0, column=0, columnspan=3, sticky="ew", pady=5)
        tk.Label(top_frame, text=f"خوارزمية: {self.algorithm_name}", font=("Arial", 18, "bold"), bg="#add8e6").pack(side=tk.LEFT, padx=10)
        tk.Button(top_frame, text="رجوع للقائمة", command=self.back_to_menu, bg="#607d8b", fg="white").pack(side=tk.RIGHT, padx=10)

        # Left Control Panel
        control_panel = tk.Frame(self, bg="#e6f7ff", bd=2, relief=tk.GROOVE)
        control_panel.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        control_panel.grid_rowconfigure(0, weight=1) # Make content fill
        control_panel.grid_columnconfigure(0, weight=1)

        tk.Label(control_panel, text="إدخال المصفوفة (أرقام مفصولة بفاصلة):", font=("Arial", 10), bg="#e6f7ff").pack(pady=5)
        self.array_input = tk.Entry(control_panel, width=30, font=("Arial", 10))
        self.array_input.pack(pady=5)
        
        # إضافة زر توليد أرقام عشوائية
        tk.Button(control_panel, text="توليد أرقام عشوائية", command=self.generate_random_numbers, bg="#9C27B0", fg="white").pack(pady=5)
        
        tk.Button(control_panel, text="تحويل وتأكيد", command=self.load_array, bg="#4CAF50", fg="white").pack(pady=5)

        tk.Button(control_panel, text="ترتيب (Start)", command=self.start_simulation, bg="#2196F3", fg="white").pack(pady=10)
        tk.Button(control_panel, text="إيقاف مؤقت / استئناف", command=self.pause_resume_simulation, bg="#FFC107", fg="black").pack(pady=5)
        tk.Button(control_panel, text="إعادة (Reset)", command=self.reset_simulation, bg="#FF5722", fg="white").pack(pady=5)
        tk.Button(control_panel, text="مسح العناصر", command=self.clear_elements, bg="#9E9E9E", fg="white").pack(pady=5)
        tk.Button(control_panel, text="عرض التقرير النهائي", command=self.show_report, bg="#00BCD4", fg="white").pack(pady=10)

        # Speed control
        tk.Label(control_panel, text="سرعة المحاكاة:", font=("Arial", 10), bg="#e6f7ff").pack(pady=(10,0))
        self.speed_slider = ttk.Scale(control_panel, from_=0.01, to=1.0, orient="horizontal", command=self.update_delay)
        self.speed_slider.set(self.delay) # Set initial value
        self.speed_slider.pack(pady=5)

        # Canvas for visualization
        self.canvas = tk.Canvas(self, bg="white", bd=2, relief=tk.SUNKEN)
        self.canvas.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.canvas.bind("<Configure>", self.draw_array)

        # Right Panel for Code and Complexity
        info_panel = tk.Frame(self, bg="#e6f7ff", bd=2, relief=tk.GROOVE)
        info_panel.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
        info_panel.grid_rowconfigure(1, weight=1) # Make text widget fill
        info_panel.grid_columnconfigure(0, weight=1)

        tk.Label(info_panel, text="كود الخوارزمية والتحليل:", font=("Arial", 12, "bold"), bg="#e6f7ff").pack(pady=5)
        self.code_text = tk.Text(info_panel, wrap=tk.WORD, font=("Courier New", 10), bg="#fdfdfd", bd=0, relief=tk.FLAT)
        self.code_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.code_text.insert(tk.END, self.get_algorithm_code_and_complexity())
        self.code_text.config(state=tk.DISABLED) # Make it read-only

    def generate_random_numbers(self):
        """
        يولد أرقام عشوائية ويدخلها في حقل الإدخال.
        """
        # توليد بين 5 و 15 رقم عشوائي بين 1 و 100
        n = random.randint(5, 15)
        random_numbers = [random.randint(1, 100) for _ in range(n)]
        random_string = ",".join(map(str, random_numbers))
        self.array_input.delete(0, tk.END)
        self.array_input.insert(0, random_string)
        messagebox.showinfo("تم التوليد", f"تم توليد {n} رقم عشوائي.")

    def load_array(self):
        """
        يقرأ المدخلات من حقل النص ويحولها إلى قائمة أعداد صحيحة.
        """
        input_str = self.array_input.get()
        try:
            self.original_array = [int(x.strip()) for x in input_str.split(',') if x.strip()]
            self.current_array = list(self.original_array)
            self.draw_array()
            messagebox.showinfo("نجاح", "تم تحميل المصفوفة بنجاح.")
        except ValueError:
            messagebox.showerror("خطأ في الإدخال", "الرجاء إدخال أرقام صحيحة مفصولة بفاصلة.")

    def draw_array(self, event=None):
        """
        يرسم المصفوفة الحالية على Canvas.
        يجب أن يتم تجاوز هذه الدالة في الفئات الفرعية لتوفير محاكاة مرئية خاصة بالخوارزمية.
        """
        self.canvas.delete("all")
        if not self.current_array:
            return

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        bar_width = canvas_width / len(self.current_array)
        max_val = max(self.current_array) if self.current_array else 1

        for i, val in enumerate(self.current_array):
            x1 = i * bar_width
            y1 = canvas_height - (val / max_val) * canvas_height * 0.9 # Scale to 90% of canvas height
            x2 = (i + 1) * bar_width
            y2 = canvas_height
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white", tags=f"bar_{i}")
            self.canvas.create_text(x1 + bar_width / 2, y1 - 10, text=str(val), fill="black", tags=f"text_{i}")

    def update_delay(self, value):
        """
        يحدث تأخير المحاكاة بناءً على قيمة شريط التمرير.
        """
        self.delay = float(value)

    def start_simulation(self):
        """
        يبدأ محاكاة الخوارزمية في خيط منفصل.
        """
        # للتعامل مع حالة فيبوناتشي بشكل خاص
        if isinstance(self, FibonacciScreen):
            if not hasattr(self, 'fib_n'):
                messagebox.showwarning("تحذير", "الرجاء إدخال وتأكيد قيمة N أولاً.")
                return
        else:
            if not self.current_array:
                messagebox.showwarning("تحذير", "الرجاء تحميل مصفوفة أولاً.")
                return

        if self.is_running:
            messagebox.showinfo("معلومات", "المحاكاة قيد التشغيل بالفعل.")
            return

        self.is_running = True
        self.stop_event.clear() # تأكد من أن حدث الإيقاف غير مفعل
        self.pause_event.clear() # تأكد من أن حدث الإيقاف المؤقت غير مفعل
        
        # تحديث حالة الأزرار
        if hasattr(self, 'start_button'):
            self.start_button.config(state=tk.DISABLED)
        if hasattr(self, 'pause_button'):
            self.pause_button.config(state=tk.NORMAL)
        if hasattr(self, 'resume_button'):
            self.resume_button.config(state=tk.DISABLED)
        
        # تحديث حالة الأزرار إذا كانت موجودة
        if hasattr(self, 'start_button'):
            self.start_button.config(state=tk.DISABLED)
        if hasattr(self, 'pause_button'):
            self.pause_button.config(state=tk.NORMAL)
        if hasattr(self, 'resume_button'):
            self.resume_button.config(state=tk.DISABLED)
            
        self.simulation_thread = threading.Thread(target=self._run_algorithm_simulation)
        self.simulation_thread.daemon = True
        self.simulation_thread.start()

    def _run_algorithm_simulation(self):
        """
        الدالة التي تحتوي على منطق تشغيل الخوارزمية والمحاكاة.
        يجب أن يتم تجاوز هذه الدالة في الفئات الفرعية.
        """
        messagebox.showinfo("Simulation", f"بدء محاكاة {self.algorithm_name}")
        # Placeholder for actual algorithm logic
        self.is_running = False

    def pause_resume_simulation(self):
        """
        يوقف مؤقتًا أو يستأنف المحاكاة.
        """
        if not self.is_running:
            messagebox.showwarning("تحذير", "لا توجد محاكاة قيد التشغيل.")
            return

        if self.pause_event.is_set():
            self.pause_event.clear() # Pause
            messagebox.showinfo("إيقاف مؤقت", "تم إيقاف المحاكاة مؤقتًا.")
        else:
            self.pause_event.set() # Resume
            messagebox.showinfo("استئناف", "تم استئناف المحاكاة.")

    def reset_simulation(self):
        """
        يعيد المصفوفة إلى حالتها الأصلية ويوقف أي محاكاة جارية.
        """
        if self.simulation_thread and self.simulation_thread.is_alive():
            self.stop_event.set() # Signal to stop the thread
            self.simulation_thread.join(timeout=1) # Wait for thread to finish
        self.is_running = False
        self.pause_event.set() # Reset pause state
        self.stop_event.clear() # Clear stop event for next run

        self.current_array = list(self.original_array)
        self.draw_array()
        messagebox.showinfo("إعادة تعيين", "تمت إعادة تعيين المحاكاة.")

    def clear_elements(self):
        """
        يمسح حقل الإدخال والمصفوفة المعروضة.
        """
        if self.simulation_thread and self.simulation_thread.is_alive():
            self.stop_event.set()
            self.simulation_thread.join(timeout=1)
        self.is_running = False
        self.pause_event.set()
        self.stop_event.clear()

        self.array_input.delete(0, tk.END)
        self.original_array = []
        self.current_array = []
        self.canvas.delete("all")
        messagebox.showinfo("مسح", "تم مسح العناصر.")

    def show_report(self):
        """
        يعرض تقريرًا نهائيًا عن الخوارزمية.
        يجب أن يتم تجاوز هذه الدالة في الفئات الفرعية لتضمين تفاصيل خاصة بالخوارزمية.
        """
        report_content = f"""
        تقرير خوارزمية: {self.algorithm_name}
        -----------------------------------
        المدخل: {self.original_array}
        النتيجة: {self.current_array}
        الزمن المستغرق: N/A (لم يتم القياس بعد)
        عدد المقارنات/التبديلات: N/A (لم يتم القياس بعد)
        التعقيد الزمني: N/A
        التعقيد المكاني: N/A
        """
        messagebox.showinfo("التقرير النهائي", report_content)

    def get_algorithm_code_and_complexity(self):
        """
        يعيد كود بايثون للخوارزمية وتحليل التعقيد.
        يجب أن يتم تجاوز هذه الدالة في الفئات الفرعية.
        """
        return f"""
        # كود خوارزمية {self.algorithm_name}
        # (سيتم توفيره لاحقًا)

        # تحليل التعقيد
        # الزمني: N/A
        # المكاني: N/A
        """

    def back_to_menu(self):
        """
        يعود إلى شاشة قائمة الخوارزميات.
        """
        if self.simulation_thread and self.simulation_thread.is_alive():
            self.stop_event.set()
            self.simulation_thread.join(timeout=1)
        self.controller.show_menu_screen()

    def animate_step(self, array, indices_to_highlight=None, color="red"):
        """
        يقوم بتحديث الرسم على Canvas ويضيف تأخيرًا للمحاكاة.
        Args:
            array (list): المصفوفة في حالتها الحالية.
            indices_to_highlight (list): قائمة بالفهارس التي يجب تمييزها.
            color (str): اللون المستخدم للتمييز.
        """
        # التحقق من طلب الإيقاف المؤقت
        while self.pause_event.is_set() and not self.stop_event.is_set():
            time.sleep(0.1)
            
        # التحقق من طلب الإيقاف
        if self.stop_event.is_set():
            raise StopIteration # إشارة لإيقاف سلسلة المحاكاة

        self.current_array = list(array)
        self.draw_array_with_highlight(indices_to_highlight, color)
        self.update_idletasks()
        
        # استخدام سرعة المحاكاة من شريط التمرير إذا كان متاحًا
        if hasattr(self, 'speed_slider'):
            simulation_speed = self.speed_slider.get()
            time.sleep(self.delay / simulation_speed)
        else:
            time.sleep(self.delay)

    def draw_array_with_highlight(self, indices_to_highlight=None, color="red"):
        """
        يرسم المصفوفة مع تمييز عناصر محددة.
        """
        self.canvas.delete("all")
        if not self.current_array:
            return

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        bar_width = canvas_width / len(self.current_array)
        max_val = max(self.current_array) if self.current_array else 1

        for i, val in enumerate(self.current_array):
            x1 = i * bar_width
            y1 = canvas_height - (val / max_val) * canvas_height * 0.9
            x2 = (i + 1) * bar_width
            y2 = canvas_height

            fill_color = "blue"
            if indices_to_highlight and i in indices_to_highlight:
                fill_color = color

            self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="white", tags=f"bar_{i}")
            self.canvas.create_text(x1 + bar_width / 2, y1 - 10, text=str(val), fill="black", tags=f"text_{i}")


# --- Specific Algorithm Screens (Inherit from BaseAlgorithmScreen) ---

class BubbleSortScreen(BaseAlgorithmScreen):
    """
    شاشة خوارزمية الفقاعية مع محاكاة مرئية.
    """
    def __init__(self, parent, controller, algorithm_name):
        super().__init__(parent, controller, algorithm_name)

    def get_algorithm_code_and_complexity(self):
        """
        يعيد كود بايثون لخوارزمية الفقاعية وتحليل التعقيد.
        """
        return """
# خوارزمية الفقاعية (Bubble Sort)
# الفكرة: تقوم بمقارنة كل عنصر مع العنصر المجاور له وتبديلهما إذا كانا في الترتيب الخاطئ.
# الخطوات: تمر على القائمة عدة مرات، وفي كل مرة 'تطفو' أكبر قيمة غير مرتبة إلى مكانها الصحيح في النهاية.
# التعقيد الزمني: O(n^2) في أسوأ وأغلب الحالات، O(n) في أفضل حالة (إذا كانت مرتبة بالفعل).
# التعقيد المكاني: O(1) لأنها لا تحتاج إلى مساحة تخزين إضافية كبيرة.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # في كل تمريرة، يتم وضع أكبر عنصر في مكانه الصحيح
        for j in range(n - 1 - i):
            # قارن العناصر المتجاورة
            if arr[j] > arr[j + 1]:
                # إذا كانا في الترتيب الخاطئ، قم بتبديلهما
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
"""

    def _run_algorithm_simulation(self):
        """
        منطق محاكاة خوارزمية الفقاعية.
        """
        arr = list(self.original_array)
        n = len(arr)
        self.comparisons = 0
        self.swaps = 0
        start_time = time.time()

        try:
            for i in range(n - 1):
                for j in range(n - 1 - i):
                    self.comparisons += 1
                    # Highlight elements being compared
                    self.animate_step(arr, indices_to_highlight=[j, j + 1], color="orange")

                    if arr[j] > arr[j + 1]:
                        self.swaps += 1
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        # Highlight elements being swapped
                        self.animate_step(arr, indices_to_highlight=[j, j + 1], color="red")
                # Highlight the element that is now in its final sorted position
                self.animate_step(arr, indices_to_highlight=[n - 1 - i], color="green")

            # Final state, all elements green
            self.animate_step(arr, indices_to_highlight=list(range(n)), color="green")

        except StopIteration:
            messagebox.showinfo("إيقاف", "تم إيقاف المحاكاة.")
        finally:
            end_time = time.time()
            self.elapsed_time = end_time - start_time
            self.current_array = arr
            self.is_running = False
            messagebox.showinfo("اكتملت المحاكاة", f"تم الانتهاء من فرز الفقاعية في {self.elapsed_time:.4f} ثانية.")
            self.draw_array()

    def show_report(self):
        """
        يعرض تقريرًا نهائيًا عن خوارزمية الفقاعية.
        """
        report_content = f"""
        تقرير خوارزمية: {self.algorithm_name}
        -----------------------------------
        المدخل: {self.original_array}
        النتيجة: {self.current_array}
        الزمن المستغرق: {getattr(self, 'elapsed_time', 'N/A'):.4f} ثانية
        عدد المقارنات: {getattr(self, 'comparisons', 'N/A')}
        عدد التبديلات: {getattr(self, 'swaps', 'N/A')}
        التعقيد الزمني: O(n^2)
        التعقيد المكاني: O(1)
        """
        messagebox.showinfo("التقرير النهائي", report_content)


class MergeSortScreen(BaseAlgorithmScreen):
    """
    شاشة خوارزمية الدمج مع محاكاة مرئية.
    """
    def __init__(self, parent, controller, algorithm_name):
        super().__init__(parent, controller, algorithm_name)

    def get_algorithm_code_and_complexity(self):
        """
        يعيد كود بايثون لخوارزمية الدمج وتحليل التعقيد.
        """
        return """
# خوارزمية الدمج (Merge Sort)
# الفكرة: تعتمد على مبدأ 'فرق تسد' (Divide and Conquer). تقسم المصفوفة إلى نصفين بشكل متكرر حتى يصبح كل نصف يحتوي على عنصر واحد، ثم تدمج هذه الأجزاء المرتبة.
# الخطوات:
# 1. تقسيم: قسّم المصفوفة إلى نصفين متساويين بشكل متكرر حتى يصبح حجم كل مصفوفة فرعية 1.
# 2. دمج: ادمج المصفوفات الفرعية المرتبة لإنشاء مصفوفات فرعية مرتبة جديدة حتى يتم دمج المصفوفة الأصلية بالكامل.
# التعقيد الزمني: O(n log n) في جميع الحالات (أسوأ، متوسط، أفضل).
# التعقيد المكاني: O(n) بسبب الحاجة إلى مصفوفات مساعدة أثناء عملية الدمج.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
"""

    def _run_algorithm_simulation(self):
        """
        منطق محاكاة خوارزمية الدمج.
        """
        arr = list(self.original_array)
        self.comparisons = 0
        self.swaps = 0 # Merge sort doesn't have direct swaps like in-place sorts
        start_time = time.time()

        try:
            self._merge_sort_recursive(arr, 0, len(arr) - 1)
            # Final state, all elements green
            self.animate_step(arr, indices_to_highlight=list(range(len(arr))), color="green")

        except StopIteration:
            messagebox.showinfo("إيقاف", "تم إيقاف المحاكاة.")
        finally:
            end_time = time.time()
            self.elapsed_time = end_time - start_time
            self.current_array = arr
            self.is_running = False
            messagebox.showinfo("اكتملت المحاكاة", f"تم الانتهاء من فرز الدمج في {self.elapsed_time:.4f} ثانية.")
            self.draw_array()

    def _merge_sort_recursive(self, arr, l, r):
        """
        دالة مساعدة لتنفيذ الدمج بشكل متكرر مع المحاكاة.
        """
        if self.stop_event.is_set():
            raise StopIteration

        if l < r:
            m = (l + r) // 2

            # Visualize splitting
            self.animate_step(self.current_array, indices_to_highlight=list(range(l, m + 1)), color="yellow")
            self.animate_step(self.current_array, indices_to_highlight=list(range(m + 1, r + 1)), color="cyan")

            self._merge_sort_recursive(arr, l, m)
            self._merge_sort_recursive(arr, m + 1, r)
            self._merge(arr, l, m, r)

    def _merge(self, arr, l, m, r):
        """
        دالة مساعدة لدمج مصفوفتين فرعيتين مع المحاكاة.
        """
        if self.stop_event.is_set():
            raise StopIteration

        n1 = m - l + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            self.comparisons += 1
            # Visualize elements being compared during merge
            self.animate_step(self.current_array, indices_to_highlight=[l + i, m + 1 + j], color="purple")
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            # Visualize the merged part
            self.animate_step(arr, indices_to_highlight=list(range(l, k)), color="blue")

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            self.animate_step(arr, indices_to_highlight=list(range(l, k)), color="blue")

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            self.animate_step(arr, indices_to_highlight=list(range(l, k)), color="blue")

    def show_report(self):
        """
        يعرض تقريرًا نهائيًا عن خوارزمية الدمج.
        """
        report_content = f"""
        تقرير خوارزمية: {self.algorithm_name}
        -----------------------------------
        المدخل: {self.original_array}
        النتيجة: {self.current_array}
        الزمن المستغرق: {getattr(self, 'elapsed_time', 'N/A'):.4f} ثانية
        عدد المقارنات: {getattr(self, 'comparisons', 'N/A')}
        عدد التبديلات: {getattr(self, 'swaps', 'N/A')} (لا ينطبق بشكل مباشر على الدمج)
        التعقيد الزمني: O(n log n)
        التعقيد المكاني: O(n)
        """
        messagebox.showinfo("التقرير النهائي", report_content)


class InsertionSortScreen(BaseAlgorithmScreen):
    """
    شاشة خوارزمية الحشر مع محاكاة مرئية.
    """
    def __init__(self, parent, controller, algorithm_name):
        super().__init__(parent, controller, algorithm_name)

    def get_algorithm_code_and_complexity(self):
        """
        يعيد كود بايثون لخوارزمية الحشر وتحليل التعقيد.
        """
        return """
# خوارزمية الحشر (Insertion Sort)
# الفكرة: تبني المصفوفة النهائية المرتبة عنصرًا تلو الآخر. تأخذ كل عنصر من الجزء غير المرتب وتضعه في مكانه الصحيح في الجزء المرتب.
# الخطوات:
# 1. ابدأ من العنصر الثاني (اعتبر العنصر الأول مرتبًا).
# 2. قارن العنصر الحالي بالعناصر في الجزء المرتب (على يساره).
# 3. حرّك العناصر الأكبر من العنصر الحالي خطوة واحدة إلى اليمين لإنشاء مساحة.
# 4. أدخل العنصر الحالي في المكان الصحيح.
# 5. كرر حتى يتم حشر جميع العناصر.
# التعقيد الزمني: O(n^2) في أسوأ ومتوسط الحالات، O(n) في أفضل حالة (إذا كانت مرتبة بالفعل).
# التعقيد المكاني: O(1) لأنها لا تحتاج إلى مساحة تخزين إضافية كبيرة.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # حرك العناصر الأكبر من key إلى اليمين
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
"""

    def _run_algorithm_simulation(self):
        """
        منطق محاكاة خوارزمية الحشر.
        """
        arr = list(self.original_array)
        n = len(arr)
        self.comparisons = 0
        self.swaps = 0 # For shifts, not direct swaps
        start_time = time.time()

        try:
            for i in range(1, n):
                key = arr[i]
                j = i - 1

                # Highlight the element to be inserted
                self.animate_step(arr, indices_to_highlight=[i], color="purple")

                while j >= 0 and key < arr[j]:
                    self.comparisons += 1
                    arr[j + 1] = arr[j]
                    self.swaps += 1
                    # Highlight elements being shifted
                    self.animate_step(arr, indices_to_highlight=[j, j + 1], color="orange")
                    j -= 1

                arr[j + 1] = key
                # Highlight the inserted element
                self.animate_step(arr, indices_to_highlight=[j + 1], color="red")
                # Highlight the sorted part
                self.animate_step(arr, indices_to_highlight=list(range(i + 1)), color="blue")

            # Final state, all elements green
            self.animate_step(arr, indices_to_highlight=list(range(n)), color="green")

        except StopIteration:
            messagebox.showinfo("إيقاف", "تم إيقاف المحاكاة.")
        finally:
            end_time = time.time()
            self.elapsed_time = end_time - start_time
            self.current_array = arr
            self.is_running = False
            messagebox.showinfo("اكتملت المحاكاة", f"تم الانتهاء من فرز الحشر في {self.elapsed_time:.4f} ثانية.")
            self.draw_array()

    def show_report(self):
        """
        يعرض تقريرًا نهائيًا عن خوارزمية الحشر.
        """
        report_content = f"""
        تقرير خوارزمية: {self.algorithm_name}
        -----------------------------------
        المدخل: {self.original_array}
        النتيجة: {self.current_array}
        الزمن المستغرق: {getattr(self, 'elapsed_time', 'N/A'):.4f} ثانية
        عدد المقارنات: {getattr(self, 'comparisons', 'N/A')}
        عدد التحويلات (Shifts): {getattr(self, 'swaps', 'N/A')}
        التعقيد الزمني: O(n^2)
        التعقيد المكاني: O(1)
        """
        messagebox.showinfo("التقرير النهائي", report_content)


class HeapSortScreen(BaseAlgorithmScreen):
    """
    شاشة خوارزمية فرز الكومة مع محاكاة مرئية.
    """
    def __init__(self, parent, controller, algorithm_name):
        super().__init__(parent, controller, algorithm_name)

    def get_algorithm_code_and_complexity(self):
        """
        يعيد كود بايثون لخوارزمية فرز الكومة وتحليل التعقيد.
        """
        return """
# خوارزمية فرز الكومة (Heap Sort)
# الفكرة: تستخدم بنية بيانات الكومة الثنائية (Binary Heap) لفرز العناصر. تقوم أولاً ببناء كومة قصوى (Max Heap) من المصفوفة، ثم تستخرج العنصر الأكبر (الجذر) وتضعه في نهاية المصفوفة، وتعيد بناء الكومة.
# الخطوات:
# 1. بناء كومة قصوى: تحويل المصفوفة إلى كومة قصوى (Max Heap).
# 2. استخراج وفرز: استخرج العنصر الأكبر من الكومة (الجذر) وضعه في نهاية المصفوفة. قلل حجم الكومة وأعد بناء الكومة القصوى للعناصر المتبقية.
# 3. كرر: كرر الخطوة 2 حتى تصبح الكومة فارغة.
# التعقيد الزمني: O(n log n) في جميع الحالات (أسوأ، متوسط، أفضل).
# التعقيد المكاني: O(1) إذا تم التنفيذ في المكان (in-place).

def heapify(arr, n, i):
    largest = i  # تهيئة الأكبر كجذر
    l = 2 * i + 1  # الابن الأيسر
    r = 2 * i + 2  # الابن الأيمن

    # إذا كان الابن الأيسر أكبر من الجذر
    if l < n and arr[largest] < arr[l]:
        largest = l

    # إذا كان الابن الأيمن أكبر من الأكبر حتى الآن
    if r < n and arr[largest] < arr[r]:
        largest = r

    # إذا لم يكن الأكبر هو الجذر
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # تبديل
        heapify(arr, n, largest)  # heapify الجذر المتأثر

def heap_sort(arr):
    n = len(arr)

    # بناء كومة قصوى (Max Heap)
    # نبدأ من آخر عقدة داخلية ونعمل heapify تنازليًا
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # استخراج العناصر واحدًا تلو الآخر
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # تبديل الجذر الحالي مع العنصر الأخير
        heapify(arr, i, 0)  # استدعاء heapify على الكومة المخفضة
    return arr
"""

    def _run_algorithm_simulation(self):
        """
        منطق محاكاة خوارزمية فرز الكومة.
        """
        arr = list(self.original_array)
        n = len(arr)
        self.comparisons = 0
        self.swaps = 0
        start_time = time.time()

        try:
            # Build max heap
            for i in range(n // 2 - 1, -1, -1):
                self._heapify_animate(arr, n, i)

            # Extract elements one by one
            for i in range(n - 1, 0, -1):
                # Highlight root and last element before swap
                self.animate_step(arr, indices_to_highlight=[0, i], color="red")
                arr[i], arr[0] = arr[0], arr[i]  # Swap
                self.swaps += 1
                # Highlight swapped elements and sorted part
                self.animate_step(arr, indices_to_highlight=[0, i], color="purple")
                self.animate_step(arr, indices_to_highlight=[i], color="green")
                self._heapify_animate(arr, i, 0)

            # Final element is also sorted
            self.animate_step(arr, indices_to_highlight=[0], color="green")
            # All elements green
            self.animate_step(arr, indices_to_highlight=list(range(n)), color="green")

        except StopIteration:
            messagebox.showinfo("إيقاف", "تم إيقاف المحاكاة.")
        finally:
            end_time = time.time()
            self.elapsed_time = end_time - start_time
            self.current_array = arr
            self.is_running = False
            messagebox.showinfo("اكتملت المحاكاة", f"تم الانتهاء من فرز الكومة في {self.elapsed_time:.4f} ثانية.")
            self.draw_array()

    def _heapify_animate(self, arr, n, i):
        """
        دالة مساعدة لـ heapify مع المحاكاة.
        """
        if self.stop_event.is_set():
            raise StopIteration

        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        # Highlight current node and its children
        highlight_indices = [i]
        if l < n: highlight_indices.append(l)
        if r < n: highlight_indices.append(r)
        self.animate_step(arr, indices_to_highlight=highlight_indices, color="orange")

        if l < n and arr[largest] < arr[l]:
            largest = l
            self.comparisons += 1

        if r < n and arr[largest] < arr[r]:
            largest = r
            self.comparisons += 1

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.swaps += 1
            # Highlight swap
            self.animate_step(arr, indices_to_highlight=[i, largest], color="red")
            self._heapify_animate(arr, n, largest)

    def show_report(self):
        """
        يعرض تقريرًا نهائيًا عن خوارزمية فرز الكومة.
        """
        report_content = f"""
        تقرير خوارزمية: {self.algorithm_name}
        -----------------------------------
        المدخل: {self.original_array}
        النتيجة: {self.current_array}
        الزمن المستغرق: {getattr(self, 'elapsed_time', 'N/A'):.4f} ثانية
        عدد المقارنات: {getattr(self, 'comparisons', 'N/A')}
        عدد التبديلات: {getattr(self, 'swaps', 'N/A')}
        التعقيد الزمني: O(n log n)
        التعقيد المكاني: O(1)
        """
        messagebox.showinfo("التقرير النهائي", report_content)


class QuickSortScreen(BaseAlgorithmScreen):
    """
    شاشة خوارزمية الفرز السريع مع محاكاة مرئية.
    """
    def __init__(self, parent, controller, algorithm_name):
        super().__init__(parent, controller, algorithm_name)

    def get_algorithm_code_and_complexity(self):
        """
        يعيد كود بايثون لخوارزمية الفرز السريع وتحليل التعقيد.
        """
        return """
# خوارزمية الفرز السريع (Quick Sort)
# الفكرة: تعتمد على مبدأ 'فرق تسد' (Divide and Conquer). تختار عنصرًا محوريًا (pivot) وتقسم المصفوفة إلى قسمين: عناصر أصغر من المحور وعناصر أكبر من المحور، ثم تعيد تطبيق الخوارزمية على القسمين.
# الخطوات:
# 1. اختيار المحور: اختيار عنصر محوري من المصفوفة (عادةً العنصر الأول، الأخير، أو الوسط).
# 2. التقسيم: إعادة ترتيب المصفوفة بحيث تكون جميع العناصر الأصغر من المحور على يساره، والعناصر الأكبر على يمينه.
# 3. التكرار: تطبيق الخوارزمية بشكل متكرر على القسمين الأيسر والأيمن.
# التعقيد الزمني: O(n log n) في المتوسط وأفضل الحالات، O(n^2) في أسوأ الحالة (عند اختيار محور سيء).
# التعقيد المكاني: O(log n) بسبب المكدس المستخدم في الاستدعاءات المتكررة.

def quick_sort(arr, low, high):
    if low < high:
        # pi هو index التقسيم، arr[pi] هو في مكانه الصحيح
        pi = partition(arr, low, high)
        
        # فرز العناصر قبل وبعد التقسيم
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # اختيار المحور (هنا نستخدم العنصر الأخير)
    pivot = arr[high]
    
    # index للعنصر الأصغر
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
"""

    def _run_algorithm_simulation(self):
        """
        منطق محاكاة خوارزمية الفرز السريع.
        """
        arr = list(self.original_array)
        self.comparisons = 0
        self.swaps = 0
        start_time = time.time()

        try:
            self._quick_sort_recursive(arr, 0, len(arr) - 1)
            # Final state, all elements green
            self.animate_step(arr, indices_to_highlight=list(range(len(arr))), color="green")

        except StopIteration:
            messagebox.showinfo("إيقاف", "تم إيقاف المحاكاة.")
        finally:
            end_time = time.time()
            self.elapsed_time = end_time - start_time
            self.current_array = arr
            self.is_running = False
            messagebox.showinfo("اكتملت المحاكاة", f"تم الانتهاء من الفرز السريع في {self.elapsed_time:.4f} ثانية.")
            self.draw_array()

    def _quick_sort_recursive(self, arr, low, high):
        """
        دالة مساعدة لتنفيذ الفرز السريع بشكل متكرر مع المحاكاة.
        """
        if self.stop_event.is_set():
            raise StopIteration

        if low < high:
            # Highlight the current partition
            self.animate_step(arr, indices_to_highlight=list(range(low, high + 1)), color="yellow")
            
            pi = self._partition_animate(arr, low, high)
            
            # Highlight the pivot in its final position
            self.animate_step(arr, indices_to_highlight=[pi], color="green")
            
            # Recursively sort elements before and after partition
            self._quick_sort_recursive(arr, low, pi - 1)
            self._quick_sort_recursive(arr, pi + 1, high)

    def _partition_animate(self, arr, low, high):
        """
        دالة مساعدة للتقسيم مع المحاكاة.
        """
        if self.stop_event.is_set():
            raise StopIteration

        # Choose the last element as pivot
        pivot = arr[high]
        
        # Highlight the pivot
        self.animate_step(arr, indices_to_highlight=[high], color="purple")
        
        i = low - 1  # Index of smaller element
        
        for j in range(low, high):
            self.comparisons += 1
            
            # Highlight elements being compared
            self.animate_step(arr, indices_to_highlight=[j, high], color="orange")
            
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    self.swaps += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    # Highlight elements being swapped
                    self.animate_step(arr, indices_to_highlight=[i, j], color="red")
        
        if i + 1 != high:
            self.swaps += 1
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            # Highlight final pivot placement
            self.animate_step(arr, indices_to_highlight=[i + 1, high], color="red")
        
        return i + 1

    def show_report(self):
        """
        يعرض تقريرًا نهائيًا عن خوارزمية الفرز السريع.
        """
        report_content = f"""
        تقرير خوارزمية: {self.algorithm_name}
        -----------------------------------
        المدخل: {self.original_array}
        النتيجة: {self.current_array}
        الزمن المستغرق: {getattr(self, 'elapsed_time', 'N/A'):.4f} ثانية
        عدد المقارنات: {getattr(self, 'comparisons', 'N/A')}
        عدد التبديلات: {getattr(self, 'swaps', 'N/A')}
        التعقيد الزمني: O(n log n) في المتوسط، O(n^2) في أسوأ الحالة
        التعقيد المكاني: O(log n)
        """
        messagebox.showinfo("التقرير النهائي", report_content)


class FibonacciScreen(BaseAlgorithmScreen):
    """
    شاشة خوارزمية فيبوناتشي (برمجة ديناميكية) مع عرض خطوات البناء.
    """
    def __init__(self, parent, controller, algorithm_name):
        super().__init__(parent, controller, algorithm_name)
        # Fibonacci doesn't sort an array, so adjust UI elements
        self.array_input.config(state=tk.DISABLED) # Disable array input
        
        # إضافة عناصر خاصة بـ Fibonacci
        self.create_fibonacci_widgets()

    def create_fibonacci_widgets(self):
        """
        ينشئ عناصر واجهة المستخدم الخاصة بخوارزمية فيبوناتشي.
        """
        # الحصول على لوحة التحكم
        control_panel = self.winfo_children()[2]
        
        # إزالة جميع العناصر الموجودة في لوحة التحكم
        for widget in control_panel.winfo_children():
            widget.destroy()
        
        # إضافة عنوان
        tk.Label(control_panel, text="أدخل عدد الحدود (N) لسلسلة فيبوناتشي:", 
                font=("Arial", 12), bg=control_panel.cget("bg")).pack(pady=(10, 5))
        
        # إضافة حقل إدخال لـ N
        self.fib_n_input = tk.Entry(control_panel, width=30, font=("Arial", 10))
        self.fib_n_input.pack(pady=5)
        
        # إضافة زر توليد N عشوائي وزر تأكيد
        buttons_input_frame = tk.Frame(control_panel, bg=control_panel.cget("bg"))
        buttons_input_frame.pack(pady=5, fill=tk.X)
        
        tk.Button(buttons_input_frame, text="توليد N عشوائي", 
                 command=self.generate_random_n, bg="#9C27B0", fg="white").pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        tk.Button(buttons_input_frame, text="تأكيد N", 
                 command=self.load_fib_n, bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # إضافة فاصل
        ttk.Separator(control_panel, orient='horizontal').pack(fill='x', pady=10)
        
        # إنشاء إطار للأزرار
        buttons_frame = tk.Frame(control_panel, bg=control_panel.cget("bg"))
        buttons_frame.pack(pady=10, fill=tk.X)
        
        # إضافة أزرار التحكم الجديدة
        self.start_button = tk.Button(buttons_frame, text="تشغيل المحاكاة", 
                                     command=self.start_simulation, bg="#4CAF50", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        self.pause_button = tk.Button(buttons_frame, text="إيقاف مؤقت", 
                                     command=self.pause_simulation, bg="#FF9800", fg="white", state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        self.resume_button = tk.Button(buttons_frame, text="متابعة", 
                                      command=self.resume_simulation, bg="#2196F3", fg="white", state=tk.DISABLED)
        self.resume_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        self.reset_button = tk.Button(buttons_frame, text="إعادة", 
                                     command=self.reset_fibonacci, bg="#F44336", fg="white")
        self.reset_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # إضافة زر مسح
        tk.Button(control_panel, text="مسح البيانات", 
                 command=self.clear_fibonacci, bg="#607D8B", fg="white").pack(pady=5, fill=tk.X, padx=20)
        
        # إضافة فاصل
        ttk.Separator(control_panel, orient='horizontal').pack(fill='x', pady=10)
        
        # إضافة شريط تمرير للتحكم في سرعة المحاكاة
        speed_frame = tk.Frame(control_panel, bg=control_panel.cget("bg"))
        speed_frame.pack(pady=10, fill=tk.X, padx=20)
        
        tk.Label(speed_frame, text="سرعة المحاكاة:", 
                font=("Arial", 10), bg=control_panel.cget("bg")).pack(side=tk.TOP, anchor="w")
        
        self.speed_slider = ttk.Scale(speed_frame, from_=0.1, to=2.0, orient=tk.HORIZONTAL, value=1.0, length=200)
        self.speed_slider.pack(side=tk.TOP, fill=tk.X, pady=5)
        
        # إضافة تسميات للسرعة
        speed_labels_frame = tk.Frame(speed_frame, bg=control_panel.cget("bg"))
        speed_labels_frame.pack(fill=tk.X)
        
        tk.Label(speed_labels_frame, text="بطيء", 
                font=("Arial", 8), bg=control_panel.cget("bg")).pack(side=tk.LEFT)
        
        tk.Label(speed_labels_frame, text="سريع", 
                font=("Arial", 8), bg=control_panel.cget("bg")).pack(side=tk.RIGHT)

    def generate_random_n(self):
        """
        يولد قيمة N عشوائية لسلسلة فيبوناتشي.
        """
        n = random.randint(5, 20)
        self.fib_n_input.delete(0, tk.END)
        self.fib_n_input.insert(0, str(n))
        messagebox.showinfo("تم التوليد", f"تم توليد N = {n}")

    def load_fib_n(self):
        """
        يقرأ المدخل N لسلسلة فيبوناتشي.
        """
        n_str = self.fib_n_input.get()
        try:
            n = int(n_str)
            if n < 0:
                messagebox.showerror("خطأ في الإدخال", "الرجاء إدخال عدد صحيح موجب.")
                return
            self.fib_n = n
            self.original_array = list(range(n+1)) # تهيئة المصفوفة للأرقام من 0 إلى n
            self.current_array = list(self.original_array)
            messagebox.showinfo("نجاح", f"تم تحديد N = {n}.")
            self.draw_array()
        except ValueError:
            messagebox.showerror("خطأ في الإدخال", "الرجاء إدخال عدد صحيح لـ N.")

    def reset_fibonacci(self):
        """
        يعيد تعيين خوارزمية فيبوناتشي.
        """
        if hasattr(self, 'simulation_thread') and self.simulation_thread and self.simulation_thread.is_alive():
            self.stop_event.set()
            self.simulation_thread.join(timeout=1)
        self.is_running = False
        self.pause_event.set()
        self.stop_event.clear()

        if hasattr(self, 'fib_n'):
            self.current_array = list(range(self.fib_n+1))
            self.draw_array()
        messagebox.showinfo("إعادة تعيين", "تمت إعادة تعيين فيبوناتشي.")

    def clear_fibonacci(self):
        """
        يمسح بيانات فيبوناتشي.
        """
        if hasattr(self, 'simulation_thread') and self.simulation_thread and self.simulation_thread.is_alive():
            self.stop_event.set()
            self.simulation_thread.join(timeout=1)
        self.is_running = False
        self.pause_event.set()
        self.stop_event.clear()

        self.fib_n_input.delete(0, tk.END)
        if hasattr(self, 'fib_n'):
            del self.fib_n
        self.original_array = []
        self.current_array = []
        self.canvas.delete("all")
        messagebox.showinfo("مسح", "تم مسح بيانات فيبوناتشي.")
        
    def pause_simulation(self):
        """
        إيقاف المحاكاة مؤقتًا.
        """
        if self.is_running:
            self.pause_event.clear()  # إيقاف المحاكاة
            self.pause_button.config(state=tk.DISABLED)
            self.resume_button.config(state=tk.NORMAL)
            self.start_button.config(state=tk.DISABLED)
            messagebox.showinfo("إيقاف مؤقت", "تم إيقاف المحاكاة مؤقتًا.")
            
    def resume_simulation(self):
        """
        متابعة المحاكاة بعد الإيقاف المؤقت.
        """
        if hasattr(self, 'simulation_thread') and self.simulation_thread and self.simulation_thread.is_alive():
            self.pause_event.set()  # متابعة المحاكاة
            self.pause_button.config(state=tk.NORMAL)
            self.resume_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.DISABLED)
            messagebox.showinfo("متابعة", "تمت متابعة المحاكاة.")

    def get_algorithm_code_and_complexity(self):
        """
        يعيد كود بايثون لخوارزمية فيبوناتشي (برمجة ديناميكية) وتحليل التعقيد.
        """
        return """
# خوارزمية فيبوناتشي (Fibonacci) باستخدام البرمجة الديناميكية (Dynamic Programming)
# الفكرة: حساب أرقام فيبوناتشي عن طريق تخزين النتائج الفرعية لتجنب الحسابات المتكررة.
# الخطوات:
# 1. تهيئة مصفوفة (أو قاموس) لتخزين النتائج.
# 2. تعيين القيم الأساسية: F(0) = 0, F(1) = 1.
# 3. حساب F(i) = F(i-1) + F(i-2) لكل i من 2 حتى N، وتخزين النتائج.
# التعقيد الزمني: O(N) لأن كل رقم يتم حسابه مرة واحدة فقط.
# التعقيد المكاني: O(N) لتخزين النتائج الفرعية.

def fibonacci_dp(n):
    if n <= 0: return []
    if n == 1: return [0]

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[:n+1]
"""

    def _run_algorithm_simulation(self):
        """
        منطق محاكاة خوارزمية فيبوناتشي (برمجة ديناميكية).
        """
        if not hasattr(self, 'fib_n'):
            messagebox.showwarning("تحذير", "الرجاء تشغيل محاكاة فيبوناتشي أولاً.")
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.resume_button.config(state=tk.DISABLED)
            return

        n = self.fib_n
        if n <= 0:
            self.current_array = []
            self.draw_array()
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.resume_button.config(state=tk.DISABLED)
            messagebox.showinfo("اكتملت المحاكاة", "سلسلة فيبوناتشي فارغة لـ N <= 0.")
            return

        # إعادة تعيين الإيقاف والتوقف المؤقت
        self.stop_event.clear()
        self.pause_event.clear()
        self.is_running = True

        # تحديث حالة الأزرار عند بدء المحاكاة
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.resume_button.config(state=tk.DISABLED)

        dp = [0] * (n + 1)
        self.comparisons = 0 # Not directly applicable, but for consistency
        self.swaps = 0 # Not applicable
        start_time = time.time()

        try:
            if n >= 0:
                dp[0] = 0
                self.current_array = dp[:1]
                self.animate_step(self.current_array, indices_to_highlight=[0], color="green")
            if n >= 1:
                dp[1] = 1
                self.current_array = dp[:2]
                self.animate_step(self.current_array, indices_to_highlight=[1], color="green")

            for i in range(2, n + 1):
                # التحقق من طلب الإيقاف المؤقت
                while self.pause_event.is_set() and not self.stop_event.is_set():
                    time.sleep(0.1)
                
                # التحقق من طلب الإيقاف
                if self.stop_event.is_set():
                    raise StopIteration

                # الحصول على سرعة المحاكاة من شريط التمرير
                simulation_speed = self.speed_slider.get()
                # حساب وقت الانتظار (أبطأ عندما تكون القيمة أقل)
                delay_time = 1.0 / simulation_speed
                
                dp[i] = dp[i-1] + dp[i-2]
                self.current_array = dp[:i+1]
                # Visualize calculation: highlight previous two, then current
                self.animate_step(self.current_array, indices_to_highlight=[i-1, i-2], color="orange")
                time.sleep(delay_time * 0.5)  # انتظار نصف الوقت قبل الخطوة التالية
                self.animate_step(self.current_array, indices_to_highlight=[i], color="green")
                time.sleep(delay_time * 0.5)  # انتظار نصف الوقت بعد الخطوة

            self.current_array = dp[:n+1]

        except StopIteration:
            messagebox.showinfo("إيقاف", "تم إيقاف المحاكاة.")
        finally:
            end_time = time.time()
            self.elapsed_time = end_time - start_time
            self.is_running = False
            
            # إعادة تعيين حالة الأزرار
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.resume_button.config(state=tk.DISABLED)
            
            messagebox.showinfo("اكتملت المحاكاة", f"تم الانتهاء من حساب فيبوناتشي في {self.elapsed_time:.4f} ثانية.")
            self.draw_array()

    def draw_array(self, event=None):
        """
        يرسم سلسلة فيبوناتشي على Canvas.
        """
        self.canvas.delete("all")
        if not self.current_array:
            return

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        num_elements = len(self.current_array)
        if num_elements == 0: return

        bar_width = canvas_width / num_elements
        max_val = max(self.current_array) if self.current_array else 1
        if max_val == 0: max_val = 1 # Avoid division by zero if all are zero

        for i, val in enumerate(self.current_array):
            x1 = i * bar_width
            y1 = canvas_height - (val / max_val) * canvas_height * 0.9
            x2 = (i + 1) * bar_width
            y2 = canvas_height
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white", tags=f"bar_{i}")
            self.canvas.create_text(x1 + bar_width / 2, y1 - 10, text=str(val), fill="black", tags=f"text_{i}")

    def draw_array_with_highlight(self, indices_to_highlight=None, color="red"):
        """
        يرسم سلسلة فيبوناتشي مع تمييز عناصر محددة.
        """
        self.canvas.delete("all")
        if not self.current_array:
            return

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        num_elements = len(self.current_array)
        if num_elements == 0: return

        bar_width = canvas_width / num_elements
        max_val = max(self.current_array) if self.current_array else 1
        if max_val == 0: max_val = 1

        for i, val in enumerate(self.current_array):
            x1 = i * bar_width
            y1 = canvas_height - (val / max_val) * canvas_height * 0.9
            x2 = (i + 1) * bar_width
            y2 = canvas_height

            fill_color = "blue"
            if indices_to_highlight and i in indices_to_highlight:
                fill_color = color

            self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="white", tags=f"bar_{i}")
            self.canvas.create_text(x1 + bar_width / 2, y1 - 10, text=str(val), fill="black", tags=f"text_{i}")

    def show_report(self):
        """
        يعرض تقريرًا نهائيًا عن خوارزمية فيبوناتشي.
        """
        if not hasattr(self, 'fib_n'):
            messagebox.showwarning("تحذير", "الرجاء تشغيل محاكاة فيبوناتشي أولاً.")
            return
            
        report_content = f"""
        تقرير خوارزمية: {self.algorithm_name}
        -----------------------------------
        المدخل (N): {getattr(self, 'fib_n', 'N/A')}
        النتيجة (السلسلة): {self.current_array}
        الزمن المستغرق: {getattr(self, 'elapsed_time', 'N/A'):.4f} ثانية
        التعقيد الزمني: O(N)
        التعقيد المكاني: O(N)
        """
        messagebox.showinfo("التقرير النهائي", report_content)


# Main execution
if __name__ == "__main__":
    app = ResponsiveApp()
    app.mainloop()
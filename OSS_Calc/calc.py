import tkinter as tk
from tkinter import simpledialog, messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")  # 높이를 조금 더 늘림

        self.expression = ""
        self.current_mode = "calc"  # 현재 모드 (calc: 계산기, cipher: 암호)

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 모드 선택 버튼
        mode_frame = tk.Frame(root)
        mode_frame.pack(fill="both", padx=10, pady=5)
        
        self.calc_btn = tk.Button(
            mode_frame,
            text="계산기",
            font=("Arial", 12),
            bg="#ddd",
            command=self.set_calc_mode
        )
        self.calc_btn.pack(side="left", expand=True, fill="both")
        
        self.cipher_btn = tk.Button(
            mode_frame,
            text="시프트 암호",
            font=("Arial", 12),
            command=self.set_cipher_mode
        )
        self.cipher_btn.pack(side="left", expand=True, fill="both")

        # 버튼 프레임
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(expand=True, fill="both")
        
        # 초기 모드는 계산기
        self.create_calc_buttons()
    
    def set_calc_mode(self):
        """계산기 모드로 변경"""
        if self.current_mode != "calc":
            self.current_mode = "calc"
            self.calc_btn.config(bg="#ddd")
            self.cipher_btn.config(bg="SystemButtonFace")
            self.clear_buttons()
            self.create_calc_buttons()
            self.expression = ""
            self.entry.delete(0, tk.END)
    
    def set_cipher_mode(self):
        """시프트 암호 모드로 변경"""
        if self.current_mode != "cipher":
            self.current_mode = "cipher"
            self.cipher_btn.config(bg="#ddd")
            self.calc_btn.config(bg="SystemButtonFace")
            self.clear_buttons()
            self.create_cipher_buttons()
            self.expression = ""
            self.entry.delete(0, tk.END)
    
    def clear_buttons(self):
        """버튼 프레임의 모든 위젯 제거"""
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
    
    def create_calc_buttons(self):
        """계산기 버튼 생성"""
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(self.buttons_frame)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_calc_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")
    
    def create_cipher_buttons(self):
        """시프트 암호 버튼 생성"""
        # 암호화 버튼
        encrypt_frame = tk.Frame(self.buttons_frame)
        encrypt_frame.pack(expand=True, fill="both", pady=5)
        
        encrypt_btn = tk.Button(
            encrypt_frame,
            text="암호화",
            font=("Arial", 16),
            bg="#8cf",
            command=self.encrypt
        )
        encrypt_btn.pack(expand=True, fill="both", padx=10)
        
        # 복호화 버튼
        decrypt_frame = tk.Frame(self.buttons_frame)
        decrypt_frame.pack(expand=True, fill="both", pady=5)
        
        decrypt_btn = tk.Button(
            decrypt_frame,
            text="복호화",
            font=("Arial", 16),
            bg="#fc8",
            command=self.decrypt
        )
        decrypt_btn.pack(expand=True, fill="both", padx=10)
        
        # 지우기 버튼
        clear_frame = tk.Frame(self.buttons_frame)
        clear_frame.pack(expand=True, fill="both", pady=5)
        
        clear_btn = tk.Button(
            clear_frame,
            text="지우기",
            font=("Arial", 16),
            bg="#f88",
            command=lambda: self.entry.delete(0, tk.END)
        )
        clear_btn.pack(expand=True, fill="both", padx=10)
        
        # 설명 레이블
        info_frame = tk.Frame(self.buttons_frame)
        info_frame.pack(expand=True, fill="both", pady=5)
        
        info_label = tk.Label(
            info_frame,
            text="텍스트를 입력한 후 암호화/복호화 버튼을 누르세요.\n시프트 값을 입력하라는 창이 나타납니다.",
            font=("Arial", 10),
            justify="center",
            wraplength=280
        )
        info_label.pack(expand=True, fill="both", padx=10)
    
    def on_calc_click(self, char):
        """계산기 버튼 클릭 처리"""
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
    
    def encrypt(self):
        """텍스트 암호화"""
        plaintext = self.entry.get()
        if not plaintext:
            messagebox.showinfo("알림", "암호화할 텍스트를 입력하세요.")
            return
        
        # 시프트 값 입력 받기
        shift = simpledialog.askinteger("시프트 값", "시프트 값을 입력하세요 (1-25):", 
                                       minvalue=1, maxvalue=25)
        if shift is None:  # 취소 버튼 누른 경우
            return
        
        ciphertext = self.caesar_cipher(plaintext, shift)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, ciphertext)
    
    def decrypt(self):
        """텍스트 복호화"""
        ciphertext = self.entry.get()
        if not ciphertext:
            messagebox.showinfo("알림", "복호화할 텍스트를 입력하세요.")
            return
          # 시프트 값 입력 받기
        shift = simpledialog.askinteger("시프트 값", "시프트 값을 입력하세요 (1-25):", 
                                       minvalue=1, maxvalue=25)
        if shift is None:  # 취소 버튼 누른 경우
            return
        
        plaintext = self.caesar_cipher(ciphertext, -shift)  # 복호화는 음수 시프트
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, plaintext)
    
    def caesar_cipher(self, text, shift):
        """시저 암호 알고리즘 구현"""
        result = ""
        for char in text:
            if char.isalpha():  # 알파벳인 경우
                ascii_offset = ord('A') if char.isupper() else ord('a')
                # 알파벳 위치 계산 (0-25)
                idx = (ord(char) - ascii_offset + shift) % 26
                # 새 문자 생성
                result += chr(idx + ascii_offset)
            elif char.isdigit():  # 숫자인 경우
                # 숫자 (0-9)를 시프트
                digit = (int(char) + shift) % 10
                result += str(digit)
            else:
                result += char  # 알파벳이나 숫자가 아닌 경우 그대로 유지
        return result




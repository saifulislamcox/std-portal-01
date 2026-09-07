import tkinter as tk
from tkinter import messagebox

# ডেমো মেমোরি ডেটাবেস
active_user = {
    "id": "student123",
    "name": "John Doe",
    "dept": "CSE",
    "pass": "123456"
}

# ডিপার্টমেন্ট অনুযায়ী রুটিন
routines = {
    "CSE": "Sun: Programming (9 AM)\nMon: Discrete Math (11 AM)",
    "EEE": "Sun: Circuit (10 AM)\nTue: EEE Lab (9 AM)",
    "BBA": "Mon: Management (9 AM)\nWed: Accounting (1 PM)"
}

# লগইন চেক করার ফাংশন
def check_login():
    input_id = entry_login_id.get().strip()
    input_pass = entry_login_pass.get().strip()
    
    if input_id == active_user["id"] and input_pass == active_user["pass"]:
        # ড্যাশবোর্ড আপডেট করা
        lbl_dash_name.config(text=f"Name: {active_user['name']}")
        lbl_dash_dept.config(text=f"Dept: {active_user['dept']}")
        lbl_routine.config(text=routines.get(active_user['dept'], "No Routine"))
        messagebox.showinfo("Success", "Login Successful! Dashboard Updated Below.")
    else:
        messagebox.showerror("Error", f"Wrong ID or Password!\nUse ID: {active_user['id']}\nPass: {active_user['pass']}")

# অ্যাকাউন্ট রেজিস্ট্রেশন করার ফাংশন
def register_account():
    name = entry_reg_name.get().strip()
    dept = combo_dept.get()
    password = entry_reg_pass.get().strip()
    
    if name == "" or password == "":
        messagebox.showwarning("Warning", "Please write your Name and Password!")
        return
        
    # মেমোরিতে নতুন ডেটা সেভ
    active_user["id"] = "newuser"
    active_user["name"] = name
    active_user["dept"] = dept
    active_user["pass"] = password
    
    # ড্যাশবোর্ড লাইভ আপডেট করা
    lbl_dash_name.config(text=f"Name: {name}")
    lbl_dash_dept.config(text=f"Dept: {dept}")
    lbl_routine.config(text=routines.get(dept, "No Routine"))
    
    messagebox.showinfo("Success", "Registration Done! Dashboard Updated Below.")
    
    # ইনপুট বক্স ক্লিয়ার করা
    entry_reg_name.delete(0, tk.END)
    entry_reg_pass.delete(0, tk.END)

# ---- মূল উইন্ডো তৈরি ----
root = tk.Tk()
root.title("Student Portal Box")
root.geometry("400x650")
root.configure(bg="#1e3c72")

# স্ক্রল করার জন্য একটি মেইন ফ্রেম
main_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=610)

# ---- ১. লগইন সেকশন ----
lbl_login_title = tk.Label(main_frame, text="1. Student Login", font=("Arial", 14, "bold"), fg="#1e3c72", bg="white")
lbl_login_title.pack(pady=(10, 5))

tk.Label(main_frame, text="Student ID:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", px=20)
entry_login_id = tk.Entry(main_frame, font=("Arial", 11), bd=1, relief="solid")
entry_login_id.insert(0, "student123")
entry_login_id.pack(fill="x", px=20, pady=2)

tk.Label(main_frame, text="Password:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", px=20)
entry_login_pass = tk.Entry(main_frame, font=("Arial", 11), bd=1, relief="solid")
entry_login_pass.insert(0, "123456")
entry_login_pass.pack(fill="x", px=20, pady=2)

btn_login = tk.Button(main_frame, text="Sign In", font=("Arial", 11, "bold"), fg="white", bg="#1e3c72", command=check_login, cursor="hand2")
btn_login.pack(fill="x", px=20, pady=8)

# ডিভাইডার লাইন
tk.Label(main_frame, text="--------------------------------------------------", fg="#ccc", bg="white").pack()

# ---- ২. রেজিস্ট্রেশন সেকশন ----
lbl_reg_title = tk.Label(main_frame, text="2. Student Registration", font=("Arial", 14, "bold"), fg="#1e3c72", bg="white")
lbl_reg_title.pack(pady=5)

tk.Label(main_frame, text="Full Name:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", px=20)
entry_reg_name = tk.Entry(main_frame, font=("Arial", 11), bd=1, relief="solid")
entry_reg_name.pack(fill="x", px=20, pady=2)

tk.Label(main_frame, text="Department:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", px=20)
combo_dept = tk.StringVar(root)
combo_dept.set("CSE") # ডিফল্ট ভ্যালু
dept_menu = tk.OptionMenu(main_frame, combo_dept, "CSE", "EEE", "BBA")
dept_menu.config(font=("Arial", 10), bg="white")
dept_menu.pack(fill="x", px=20, pady=2)

tk.Label(main_frame, text="Choose Password:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w", px=20)
entry_reg_pass = tk.Entry(main_frame, font=("Arial", 11), bd=1, relief="solid")
entry_reg_pass.pack(fill="x", px=20, pady=2)

btn_reg = tk.Button(main_frame, text="Create Account", font=("Arial", 11, "bold"), fg="white", bg="#2a5298", command=register_account, cursor="hand2")
btn_reg.pack(fill="x", px=20, pady=8)

# ডিভাইডার লাইন
tk.Label(main_frame, text="--------------------------------------------------", fg="#ccc", bg="white").pack()

# ---- ৩. লাইভ ড্যাশবোর্ড সেকশন ----
lbl_dash_title = tk.Label(main_frame, text="3. Live Dashboard", font=("Arial", 14, "bold"), fg="#1e3c72", bg="white")
lbl_dash_title.pack(pady=5)

# স্টুডেন্ট ইনফো প্যানেল
info_frame = tk.Frame(main_frame, bg="#f1f5f9", bd=1, relief="solid")
info_frame.pack(fill="x", px=20, pady=5)

lbl_dash_name = tk.Label(info_frame, text="Name: Demo Student", bg="#f1f5f9", font=("Arial", 10, "bold"), fg="#1e3c72")
lbl_dash_name.pack(anchor="w", px=5, py=2)

lbl_dash_dept = tk.Label(info_frame, text="Dept: CSE", bg="#f1f5f9", font=("Arial", 10, "bold"), fg="#1e3c72")
lbl_dash_dept.pack(anchor="w", px=5, py=2)

lbl_dash_cgpa = tk.Label(info_frame, text="CGPA: 3.85 (Active)", bg="#f1f5f9", font=("Arial", 10))
lbl_dash_cgpa.pack(anchor="w", px=5, py=2)

# রুটিন এরিয়া
tk.Label(main_frame, text="📅 Class Routine:", bg="white", font=("Arial", 10, "bold"), fg="#2a5298").pack(anchor="w", px=20)
lbl_routine = tk.Label(main_frame, text="Sun: Programming (9 AM)\nMon: Discrete Math (11 AM)", bg="#f0fdf4", font=("Arial", 9), bd=1, relief="solid", justify="left")
lbl_routine.pack(fill="x", px=20, pady=2)

root.mainloop()

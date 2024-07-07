import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

def draw_gradient(canvas, color1, color2):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    limit = height

    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))

        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color)

def generate_workout():
    upper_body_exercises = [
        "Push-ups", "Pull-ups", "Bench Press", "Shoulder Press", "Bicep Curls", "Tricep Dips"
    ]
    lower_body_exercises = [
        "Squats", "Lunges", "Deadlifts", "Leg Press", "Calf Raises"
    ]

    upper_body = random.choice(upper_body_exercises)
    lower_body = random.choice(lower_body_exercises)

    workout_text.set(f"Upper Body: {upper_body}\nLower Body: {lower_body}")

root = tk.Tk()
root.title("Personal Workout Generator")
root.geometry("600x400")

gradient_image = Image.open("gradient.png")
gradient_image = gradient_image.resize((600, 400), Image.LANCZOS)  
gradient_photo = ImageTk.PhotoImage(gradient_image)

gradient_canvas = tk.Canvas(root, width=600, height=400)
gradient_canvas.create_image(0, 0, anchor="nw", image=gradient_photo)
gradient_canvas.pack(fill="both", expand=True)

frame = ttk.Frame(gradient_canvas)
frame.place(relx=0.5, rely=0.5, anchor="center")

workout_text = tk.StringVar()
workout_label = ttk.Label(frame, textvariable=workout_text, font=("Helvetica", 18), background="#ffffff", width=30)
workout_label.pack(pady=20)

generate_button = ttk.Button(frame, text="Generate Workout", command=generate_workout)
generate_button.pack()

generate_workout()

root.mainloop()

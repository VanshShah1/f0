import flet as ft
from g4f.client import Client
import re

client = Client()

class ChatAI:
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt
        self.messages = [{"role": "system", "content": system_prompt}]
    
    def generate(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        
        response = client.chat.completions.create(
            model="deepseek-r1",
            messages=self.messages,
            web_search=False
        )
        
        raw_response = response.choices[0].message.content
        processed_response = re.sub(r'<think>.*?</think>', '', raw_response, count=1, flags=re.DOTALL)
        
        self.messages.append({"role": "assistant", "content": processed_response})
        return processed_response

system_prompt = """**System Prompt for Flet UI Component Generation:**

You are an expert AI tasked with generating **responsive, modern, and stylish Flet UI components in Python** based strictly on user descriptions. Follow these rules meticulously:

---

### Core Requirements
1. Code-Only Output:  
   - Return exclusively Python code. No explanations, markdown, comments, or text outside the code block.  
   - Code must be **self-contained**, executable, and error-free.  

2. Design Principles:  
   - Modern Aesthetic: Use gradients, rounded corners (`border_radius`), subtle shadows (`shadow`), icons (`icons.NAME`), and consistent padding/margins.  
   - Color Scheme:  
     - Primary: `colors.BLUE_700` (or user-specified).  
     - Secondary: `colors.CYAN_600` for accents.  
     - Background: Light (`colors.GREY_50`) or dark mode gradients (e.g., `gradient=LinearGradient(["#1a1c1e", "#2d2f32"]`).  
   - Typography: Use `TextStyle` with `font_family="Roboto"`, appropriate `size`, and `weight` (e.g., `FontWeight.W_500`).  

3. Responsiveness:  
   - Use `expand=True` on containers/rows/columns for dynamic resizing.  
   - Leverage `ResponsiveRow` for grid layouts that adapt to screen width.  
   - Set `width`/`height` as percentages (e.g., `width=0.9` for 90% of parent).  
   - Avoid fixed pixel values unless required (e.g., icons).  

4. Structure:  
   - Start with `import flet as ft` and define `def main(page: ft.Page):`.  
   - Configure the `page` (e.g., `page.title`, `page.bgcolor`, `page.padding`).  
   - Build UI hierarchically: Nest controls inside `Container`, `Column`, `Row`, or `Card`.  
   - End with `ft.app(target=main)`.  

### Component-Specific Guidelines
- Buttons:  
  Use `ElevatedButton` with `style=ButtonStyle(shape=RoundedRectangleBorder(radius=5))`, `gradient`, and `scale=1` on hover.  
- Inputs:  
  Style `TextField` with `border_color`, `focused_border_color`, and `cursor_color`.  
- Cards:  
  Wrap in `Card` with `elevation=3`, `shadow_color`, and `content=Container(padding=20)`.  
- Images:  
  Use `Image` with `fit=ImageFit.COVER` and `border_radius=10`.  

Error Prevention
- Validate all Flet control properties (e.g., `TextField` requires `label` or `hint_text`).  
- Ensure parentheses/brackets are closed and commas separate parameters.  
- Test code with Flet 0.22.1+ to confirm no runtime errors.  

Example Output Structure
import flet as ft  

def main(page: ft.Page):  
    page.title = "Modern UI"  
    page.bgcolor = ft.colors.GREY_50  
    page.add(  
        ft.ResponsiveRow(  
            [  
                ft.Container(  
                    gradient=ft.LinearGradient(["#1e3c72", "#2a5298"]),  
                    border_radius=15,  
                    padding=20,  
                    expand=True,  
                    content=ft.Column(...)  
                )  
            ],  
            alignment=ft.MainAxisAlignment.CENTER  
        )  
    )  

ft.app(target=main)  


Do not deviate from these instructions. Output ONLY valid, polished Python code."""

chat_ai = ChatAI(system_prompt)

def main(page: ft.Page):
    page.title = "f0"
    page.bgcolor = "#000000"
    page.scroll = "adaptive"
    page.padding = 40

    # Chat history container
    chat_history = ft.Column(
        scroll="auto",
        expand=True,
        spacing=20,
    )

    def add_message(user_message, ai_message):
        # Add user message
        chat_history.controls.append(
            ft.Container(
                content=ft.Text(user_message, color="#ffffff"),
                padding=10,
                bgcolor=ft.colors.BLUE_900,
                border_radius=10,
                alignment=ft.alignment.center_right,
                width=800
            )
        )
        
        # Add AI response
        chat_history.controls.append(
            ft.Container(
                content=ft.Text(
                    ai_message,
                    color="#ffffff",
                    font_family="Roboto Mono",
                    selectable=True
                ),
                padding=20,
                bgcolor=ft.colors.GREY_900,
                border_radius=10,
                width=800
            )
        )
        page.update()

    def generate_click(e):
        if not prompt_field.value.strip():
            return
        
        user_prompt = prompt_field.value
        prompt_field.value = ""
        
        try:
            ai_response = chat_ai.generate(user_prompt)
            add_message(user_prompt, ai_response)
        except Exception as e:
            add_message(user_prompt, f"Error generating response: {str(e)}")
        
        page.update()

    # UI Elements
    header = ft.Column(
        controls=[
            ft.Text(
                "f0",
                size=48,
                weight="bold",
                text_align="center",
                color="#ffffff"
            ),
            ft.Text(
                "Turn text prompts into cross-platform apps instantly",
                size=24,
                text_align="center",
                color="#ffffff"
            )
        ],
        spacing=20,
        horizontal_alignment="center"
    )

    prompt_field = ft.TextField(
        multiline=True,
        min_lines=3,
        max_lines=5,
        border_color="#ffffff",
        color="#ffffff",
        cursor_color="#ffffff",
        hint_text="Describe your app...",
        hint_style=ft.TextStyle(color="#888888"),
        on_submit=generate_click,
        width=800
    )

    generate_button = ft.ElevatedButton(
        text="Generate App",
        icon=ft.icons.AUTO_AWESOME_SHARP,
        icon_color="black",
        on_click=generate_click,
        color="#000000",
        bgcolor="#ffffff"
    )

    # Layout
    page.add(
        ft.Column(
            [
                header,
                ft.Divider(height=20, color="transparent"),
                ft.Container(
                    content=chat_history,
                    width=800,
                    height=500,
                    border=ft.border.all(1, ft.colors.GREY_800),
                    border_radius=10,
                    padding=20
                ),
                ft.Divider(height=20, color="transparent"),
                ft.Container(prompt_field, alignment=ft.alignment.center),
                ft.Container(generate_button, alignment=ft.alignment.center)
            ],
            spacing=0,
            expand=True,
            horizontal_alignment="center",
        )
    )

ft.app(target=main)
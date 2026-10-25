import os
import shutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class FileOrganizerApp(App):
    def build(self):
        # التصميم العام للشاشة
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # عنوان التطبيق في الواجهة
        self.label = Label(
            text='أهلاً بك في أداة GASSAR\nلنظيم وترتيب الملفات!',
            font_size=20,
            halign='center'
        )
        layout.add_widget(self.label)
        
        # زر التشغيل الكبير
        btn = Button(
            text='ابدأ ترتيب الملفات الآن',
            font_size=18,
            size_hint=(1, 0.3),
            background_color=(0.1, 0.6, 0.3, 1)
        )
        btn.bind(on_press=self.organize_files)
        layout.add_widget(btn)
        
        return layout

    def organize_files(self):
        target_dir = r"/storage/emulated/0/Download"
        
        if not os.path.exists(target_dir):
            self.label.text = "❌ عذراً، مسار التنزيلات غير موجود!"
            return

        extensions_map = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'],
            'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
            'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
            'Programs': ['.exe', '.msi', '.apk']
        }
        
        files_count = 0
        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            if os.path.isdir(file_path):
                continue

            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for folder_name, extensions in extensions_map.items():
                if file_ext in extensions:
                    folder_path = os.path.join(target_dir, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    moved = True
                    files_count += 1
                    break
            
            if not moved:
                other_folder = os.path.join(target_dir, 'Others')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))
                files_count += 1

        self.label.text = f"✨ تمت العملية بنجاح!\nتم تنظيم {files_count} ملفاً."

if __name__ == '__main__':
    FileOrganizerApp().run()
    

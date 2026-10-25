import os
import shutil

# حدد المسار الذي تريد ترتيبه (يمكنك تغيير المسار أدناه إلى مجلد التجربة أو مجلد التحميلات)
# ملاحظة: ضع حرف r قبل المسار لتجنب مشاكل الرموز الخاصة في ويندوز
target_dir = r"C:\path\to\your\folder" 

# قاموس تصنيف الامتدادات والمجلدات الخاصة بها
extensions_map = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
    'Programs': ['.exe', '.msi', '.apk']
}

def organize_files():
    # التحقق من وجود المجلد
    if not os.path.exists(target_dir):
        print(f"❌ عذراً، المسار غير موجود: {target_dir}")
        print("الرجاء تعديل متغير target_dir في الكود ليطابق مساراً حقيقياً على جهازك.")
        return

    print(f"جاري فحص وترتيب الملفات في: {target_dir}...")
    
    files_count = 0
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        # تخطي المجلدات والتركيز على الملفات فقط
        if os.path.isdir(file_path):
            continue

        # استخراج امتداد الملف بصيغة صغيرة (Lowercase)
        file_ext = os.path.splitext(filename)[1].lower()

        moved = False
        # البحث عن المجلد المناسب حسب الامتداد
        for folder_name, extensions in extensions_map.items():
            if file_ext in extensions:
                folder_path = os.path.join(target_dir, folder_name)
                
                # إنشاء المجلد إذا لم يكن موجوداً مسبقاً
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                # نقل الملف إلى مكانه الجديد
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"✅ نقل الملف: {filename} ➔ إلى مجلد [{folder_name}]")
                moved = True
                files_count += 1
                break
        
        # إذا كان الامتداد غير موجود في القاموس، يتم نقله لمجلد Others
        if not moved:
            other_folder = os.path.join(target_dir, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"📁 نقل إلى Others: {filename}")
            files_count += 1

    print(f"\n✨ تمت العملية بنجاح! تم تنظيم {files_count} ملفاً.")

if __name__ == "__main__":
    organize_files()
  

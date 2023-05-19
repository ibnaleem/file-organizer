import os
from shutil import move

def is_image_file(filename):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.psd', '.ai', '.indd']
    file_extension = os.path.splitext(filename)[1].lower()
    return file_extension in image_extensions

def is_video_file(filename):
    video_extensions = ['.mp4', '.mov', '.wmv', '.avchd', '.flv', '.f4v', '.swf', '.wkv', '.mpv', '.mpeg', '.mp2', '.mpg']
    file_extension = os.path.splitext(filename)[1].lower()
    return file_extension in video_extensions

def is_audio_file(filename):
    audio_extensions = ['.mp3', '.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', '.awb',
                        '.dss', '.dvf', '.flac', '.gsm', 'iklax', '.ivs', '.m4a', '.m4b', '.m4p', '.mmf', '.mpc', '.msv', '.nmf', '.ogg', '.oga', '.mogg', '.opus', '.ra', '.rm', '.rf64', '.sln', '.tta', '.voc', '.vox', '.wav', '.wma', '.wv', '.webm', '.8svx', '.cda']
    file_extension = os.path.splitext(filename)[1].lower()
    return file_extension in audio_extensions

def is_doc_file(filename):
    image_extensions = ['.pdf', '.txt', '.word', '.doc', '.docx', '.xls', '.xlsx', '.csv', '.ppt', '.pptx']
    file_extension = os.path.splitext(filename)[1].lower()
    return file_extension in image_extensions

current_dir = os.path.abspath(os.curdir)

if not os.path.exists("Images"):
    os.makedirs("Images/JPGs")
    os.makedirs("Images/PNGs")
    os.makedirs("Images/GIFs")
    os.makedirs("Images/BMPs")
    os.makedirs("Images/PSDs")
    os.makedirs("Images/TIFFs")
    os.makedirs("Images/Illustrator Documents")

if not os.path.exists("Videos"):
    os.mkdir("Videos")

if not os.path.exists("Audios"):
    os.mkdir("Audios")

if not os.path.exists("Documents"):
    os.makedirs("Documents/PDFs")
    os.makedirs("Documents/CSVs")
    os.makedirs("Documents/Word Documents")
    os.makedirs("Documents/Excel Sheets")
    os.makedirs("Documents/Powerpoints")
    os.makedirs("Documents/Text Files")

for file in os.listdir(current_dir):
    if os.path.isfile(file):
        source_path = os.path.join(current_dir, file)
        if is_image_file(file):
            if file.endswith('.jpg') or file.endswith('.jpeg'):
                destination_path = os.path.join("Images", "JPGs", file)
                move(source_path, destination_path)
            elif file.endswith('.png'):
                destination_path = os.path.join("Images", "PNGs", file)
                move(source_path, destination_path)
            elif file.endswith('.gif'):
                destination_path = os.path.join("Images", "GIFs", file)
                move(source_path, destination_path)
            elif file.endswith('.bmp'):
                destination_path = os.path.join("Images", "BMPs", file)
                move(source_path, destination_path)
            elif file.endswith('.psd'):
                destination_path = os.path.join("Images", "PSDs", file)
                move(source_path, destination_path)
            elif file.endswith('.ai'):
                destination_path = os.path.join("Images", "Illustrator Documents", file)
                move(source_path, destination_path)
            elif file.endswith('.tiff'):
                destination_path = os.path.join("Images", "TIFFs", file)
                move(source_path, destination_path)
        elif is_video_file(file):
            destination_path = os.path.join("Videos", file)
            move(source_path, destination_path)
        elif is_audio_file(file):
            destination_path = os.path.join("Audios", file)
            move(source_path, destination_path)
        elif is_doc_file(file):
            if file.endswith(".pdf"):
                destination_path = os.path.join("Documents", "PDFs", file)
                move(source_path, destination_path)
            elif file.endswith(".txt"):
                destination_path = os.path.join("Documents", "Text Files", file)
                move(source_path, destination_path)
            elif file.endswith(".csv"):
                destination_path = os.path.join("Documents", "CSVs", file)
                move(source_path, destination_path)
            elif file.endswith(".ppt") or file.endswith("pptx"):
                destination_path = os.path.join("Documents", "Powerpoints", file)
                move(source_path, destination_path)
            elif file.endswith(".doc") or file.endswith("docx"):
                destination_path = os.path.join("Documents", "Word Documents", file)
                move(source_path, destination_path)
            elif file.endswith(".xls") or file.endswith("xlsx"):
                destination_path = os.path.join("Documents", "Excel Sheets", file)
                move(source_path, destination_path)

# 🗂️ Smart File Organizer

A Python automation tool that scans a folder and automatically sorts your files into organized subfolders — because nobody has time for a cluttered Downloads folder.

Built as part of my Python Programming internship track at **Learn Depth**.

---

## What it does

You point it at a folder, it does the rest. Every file gets detected by its extension and moved into the right place:

| File Type | Extensions | Destination |
|-----------|-----------|-------------|
| Images | .jpg, .jpeg, .png, .gif, .bmp, .svg | `Images/` |
| Documents | .pdf, .docx, .doc, .txt, .xlsx, .pptx | `Documents/` |
| Videos | .mp4, .mov, .avi, .mkv | `Videos/` |
| Music | .mp3, .wav, .aac, .flac | `Music/` |
| Everything else | anything unrecognized | `Others/` |

---

## How to run it

**Requirements:** Python 3 (no external libraries needed)

1. Clone the repo
   ```bash
   git clone https://github.com/jesse-aj/smart-file-organizer.git
   cd smart-file-organizer
   ```

2. Run the script
   ```bash
   python file_organizer.py
   ```

3. Enter the full path to the folder you want to organize when prompted
   ```
   Enter the folder path to organize: C:\Users\Jesse\Downloads
   ```

4. Watch it work 👀
   ```
   Moved: photo.jpg → Images
   Moved: resume.pdf → Documents
   Moved: song.mp3 → Music
   Moved: movie.mp4 → Videos
   ```

---

## Before & After

**Before:**
```
Downloads/
  photo.jpg
  resume.pdf
  song.mp3
  movie.mp4
```

**After:**
```
Downloads/
  Images/photo.jpg
  Documents/resume.pdf
  Music/song.mp3
  Videos/movie.mp4
```

---

## Built with

- Python 3
- `os` — filesystem navigation
- `shutil` — file moving

---

*Internship project — Learn Depth | 2026*
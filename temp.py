import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        self.playlist = []

        self.initialize_player()

    def initialize_player(self):
        self.current_index = 0
        self.paused = False

        self.play_btn = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_btn.pack()

        self.pause_btn = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_btn.pack()

        self.stop_btn = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_btn.pack()

        self.next_btn = tk.Button(self.root, text="Next", command=self.next_music)
        self.next_btn.pack()

        self.prev_btn = tk.Button(self.root, text="Previous", command=self.prev_music)
        self.prev_btn.pack()

        self.add_btn = tk.Button(self.root, text="Add Music", command=self.add_music)
        self.add_btn.pack()

    def play_music(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            if not self.paused:
                pygame.mixer.music.pause()
                self.paused = True
            else:
                pygame.mixer.music.unpause()
                self.paused = False

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_music(self):
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.play_music()

    def prev_music(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.play_music()

    def add_music(self):
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Music",
                                               filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
        if file_path:
            self.playlist.append(file_path)


if __name__ == "__main__":
    pygame.init()
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()

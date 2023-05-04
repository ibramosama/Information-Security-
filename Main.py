
import PlayFair
import DES
import saes
import vigener
import RailFence
import ceaser
import Autokey

import tkinter as tk
from tkinter import ttk

def pad(msg):
  if(len(msg)%16!=0):
    print("Padding required")
    for i in range(abs(16-(len(msg)%16))):
      msg=msg+'0'
  else:
    print("No padding required")
  return(msg)

def bin_to_hexa(msg):
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex = ""
    for i in range(0, len(msg), 4):
        ch = ""
        ch = ch + msg[i]
        ch = ch + msg[i + 1]
        ch = ch + msg[i + 2]
        ch = ch + msg[i + 3]
        hex = hex + mp[ch]
    return hex
class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        self.title('Information Security')

        # initialize data
        self.languages = ('PlayFair', 'Autokey', 'DES',
                        'S-AES', 'Vigener', 'Rail Fence', 'Caeser')

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self,  text='Select your most favorite Algorithm:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.languages[0],
            *self.languages,
            command=self.option_changed)

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)
        self.output_label1=ttk.Label(self, foreground='black')
        self.output_label1.grid(column=0, row=2, sticky=tk.W, **paddings)
        self.output_label2 = ttk.Label(self, foreground='black')
        self.output_label2.grid(column=0, row=3, sticky=tk.W, **paddings)
        self.output_label5 = ttk.Label(self, foreground='red')
        self.output_label5.grid(column=0, row=5, sticky=tk.W, **paddings)



    def encrypt(self):
        algorithm=self.option_var.get()
        if(algorithm=="PlayFair"):
            self.output_label5['text'] = f'The ciphertext is: {PlayFair.encode(self.inputtxt1.get().upper(),self.inputtxt2.get().upper())}'
        elif(algorithm=="Autokey"):
            self.output_label5['text'] = f'The ciphertext is: {Autokey.encryptMessage(self.inputtxt1.get().upper(), self.inputtxt2.get().upper())}'
        elif (algorithm == "S-AES"):
            plaintext = int(self.inputtxt1.get(), 2)
            key = int(self.inputtxt2.get(), 2)
            ciphertext = hex(saes.SimplifiedAES(key).encrypt(plaintext))
            self.output_label5['text'] = f'The ciphertext is: {ciphertext}'
        elif (algorithm == "Vigener"):
            string = self.inputtxt1.get()
            string = string.replace(" ", "")
            key =  self.inputtxt2.get()
            key= key.strip()
            cipher_text = vigener.encrypt(string, key)
            self.output_label5['text'] = f'The ciphertext is: {cipher_text}'
        elif (algorithm == "Rail Fence"):
            self.output_label5['text'] = f'The ciphertext is: {RailFence.encryptRailFence(self.inputtxt1.get().upper(), int(self.inputtxt2.get()))}'
        elif (algorithm == "Caeser"):
            self.output_label5['text'] = f'The ciphertext is: {ceaser.encrypt( int(self.inputtxt2.get()),self.inputtxt1.get().upper())}'
        elif (algorithm=="DES"):
            plain_text = pad(self.inputtxt1.get())
            key = pad((self.inputtxt2.get()))
            cipherText=bin_to_hexa(DES.encrypt(plain_text,key ))
            self.output_label5['text'] = f'The ciphertext is: {cipherText}'
    def decrypt(self):
        algorithm=self.option_var.get()
        if(algorithm=="PlayFair"):
            self.output_label5['text'] = f'The plaintext is: {PlayFair.decode(self.inputtxt1.get().upper(),self.inputtxt2.get().upper())}'
        elif(algorithm=="Autokey"):
            self.output_label5['text'] = f'The plaintext is: {Autokey.decryptMessage(self.inputtxt1.get().upper(), self.inputtxt2.get().upper())}'
        elif (algorithm == "S-AES"):
            plaintext = int(self.inputtxt1.get(), 2)
            key = int(self.inputtxt2.get(), 2)
            ciphertext = hex(saes.SimplifiedAES(key).decrypt(plaintext))
            self.output_label5['text'] = f'The plaintext is: {ciphertext}'
        elif (algorithm == "Vigener"):
            string=self.inputtxt1.get()
            string = string.replace(" ", "")
            key =  self.inputtxt2.get()
            key= key.strip()
            cipher_text = vigener.decrypt(string, key)
            self.output_label5['text'] = f'The plaintext is: {cipher_text}'
        elif (algorithm == "Rail Fence"):
            self.output_label5['text'] = f'The plaintext is: {RailFence.decryptRailFence(self.inputtxt1.get().upper(), int(self.inputtxt2.get()))}'
        elif (algorithm == "Caeser"):
            self.output_label5['text'] = f'The plaintext is: {ceaser.decrypt( int(self.inputtxt2.get()),self.inputtxt1.get().upper())}'
        elif (algorithm=="DES"):
            plain_text = pad(self.inputtxt1.get())
            key = pad((self.inputtxt2.get()))
            plaintext=bin_to_hexa(DES.decrypt(plain_text,key ))
            self.output_label5['text'] = f'The plaintext is: {plaintext}'
    def option_changed(self, *args):
        self.output_label['text'] = f'You selected: {self.option_var.get()}'
        self.output_label1['text'] = f'Enter the Text: '
        self.output_label2['text'] = f'Enter the key: '
        self.inputtxt1=ttk.Entry(self, foreground='black')
        self.inputtxt1.grid(column=1, row=2, sticky=tk.W)

        self.inputtxt2 = ttk.Entry(self, foreground='black')
        self.inputtxt2.grid(column=1, row=3, sticky=tk.W)

        self.options1= ttk.Button(self, text="Encrypt",command=lambda :self.encrypt())
        self.options1.grid(row = 4, column = 0, sticky = tk.W)
        self.options2 = ttk.Button(self, text="Decrypt",command=lambda :self.decrypt())
        self.options2.grid(row=4, column=1, sticky=tk.W)


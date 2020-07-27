# Changing the default textures of a PSP game with custom ones using the PPSSPP emulator

1. Open the emulator and load a game you wish to replace its textures.
2. Press the "**Escape**" key, enter the "**Settings**" menu, then go to "**Tools**" on the left panel.
3. On the right panel, click on "**Developer tools**", and under the "**Texture replacement**" section click on "**Create/Open textures.ini file...**".

## Using the _textures.ini_ file

This is what you'll see when you open the file for the first time:

---

```ini
# This file is optional
# for syntax explanation check:
# - https://github.com/hrydgard/ppsspp/pull/8715
# - https://github.com/hrydgard/ppsspp/pull/8792

[options]
version = 1
hash = quick

[hashes]

[hashranges]
```

---

- Every line that starts with "**#**" is just descriptive, you can use that to add comments/notes to certain parts of the document.

- Under the **[options]** section you can see:

  1. "version = 1" - Keep this the way it is.

  2. "hash = quick" - There are different hashing methods, the default is "**quick**" but I heavily recommend using "**xxh64**", since it's faster and allows you to use more options.

  - If you use "**xxh64**" you can use 2 more options:

    1. "ignoreAddress = true" - This one is recommended in most cases since it replaces the first 8 digits of the hashes with 0, which prevents (mostly) the creation of repeated textures when extracting them using PPSSPP.

    2. "reduceHash = true" - Used as a last resort on some games where textures come out "wrong". **DO NOT** use it unless there's no other option.

For more info, read this: [GitHub Pull Request](https://github.com/hrydgard/ppsspp/pull/9668)

Now, let's see how the textures.ini file would look with the aforementioned changes:

---

```ini
# This file is optional
# for syntax explanation check:
# - https://github.com/hrydgard/ppsspp/pull/8715
# - https://github.com/hrydgard/ppsspp/pull/8792

[options]
version = 1
hash = xxh64
ignoreAddress = true

[hashes]

[hashranges]
```

---

- Make the same changes to your textures.ini file and save the document.
- It's important that you do this before starting to extract textures since the hashes will be different depending on the hashing method you choose here.

## Extracting textures from PSP games using the PPSSPP emulator

Now that we configured the textures.ini file, let's start extracting textures from a game to see how the hashes are created.

- Remember the settings menu on the emulator? Go to the "**Texture replacement**" section and activate the "**Save new textures**" option.

- Start playing the game and every texture that appears on screen will be saved on a folder called "**new**" placed on "<_ppsspp_path_>/PSP/TEXTURES/<_game_code_>" in PNG format.

  - _ppsspp_path_
    - Windows: User/documents/PPSSPP
    - Mac/Linux: \$HOME/.config/ppsspp
  - _game_code_
    - Monster Hunter Portable 3rd: **NPJB40001**

- The name of each texture will be its hash, that you will then use on the _textures.ini_ file (which is also located inside the NPJB40001 folder).
- As long as the "**Save new textures**" option is active, the emulator will continue extracting every texture that appears on screen.

## Replacing the original textures

Now that we've configured the _textures.ini_ file and extracted some textures, let's write down the hashes.

This is what the _textures.ini_ file would look with a couple of hashes writen down:

---

```ini
# This file is optional
# for syntax explanation check:
# - https://github.com/hrydgard/ppsspp/pull/8715
# - https://github.com/hrydgard/ppsspp/pull/8792

[options]
version = 1
hash = xxh64
ignoreAddress = true

[hashes]

#Monsters#
000000004e5c64ac47e2288d = Monsters/Arzuros.png

#Weapons#
00000000953ede2765bdd21a = Weapons/HM/01.png

[hashranges]
```

---

- Under the "**[hashes]**" section is where you will write down the hashes of the textures you extracted using the emulator and wish to change, alongside the route where the texture replacement is and its name.

- For example: 000000004e5c64ac47e2288d = Monsters/Arzuros.png

- The 24-digit code is the hash of a texture from MHP3rd, after that there's an "**=**" sign and the route of the texture replacement.

- Replacement textures are placed inside the folder NPJB40001 (in the case of P3rd).

- As you can see, you can create more folders and subfolders to organise your textures; so for example, under the NPJB40001 folder you can create a "Monsters" folder where you will place your custom textures that are gonna replace the original textures of the monsters from P3rd.

- Let's say you created a custom texture for the monster "Arzuros". You can place it there and name it as you wish. I recommend using the PNG format for replacement textures.

- If you already extracted the textures you wanted from the game, you can turn off the "**Save new textures**" option.

- For the emulator to load your custom textures you have to activate the "**Replace textures**" option placed right below the "**Save new textures**" option.

- Exit the game and enter again. Your custom textures should replace the orginal ones in-game.

---

Original tutorial by [Ice-w1nd](https://github.com/Ice-w1nd) can be found [here](https://github.com/David-vz/MonsterHunterPortable3rdHDRemake/files/2137700/TextureReplacementTutorial.txt).

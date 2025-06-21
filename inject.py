import os
import sys

MOD_CODE = open("assets/modhook.rpy", "r").read()
SCRIPTRPY_PAYLOAD = """jump mmpp1

label thesrar:"""

def inject_payload(file, scriptrpy_path):
    code = file.read()
    splitcode = code.split("# Play the main menu music")
    try:
        splitcode[1] = SCRIPTRPY_PAYLOAD + splitcode[1]
        code = splitcode[0] + splitcode[1]
        file.close()
        open(scriptrpy_path, "w", encoding="utf-8").write(code)
        print(f"Injected scriptrpy payload into {scriptrpy_path}")
    except IndexError:
        print("Payload injection failed. Skipping, expecting MMPM's payload to be already injected.")

def inject_assets(game_dir):
    audio_path = os.path.join(game_dir, "audio")
    images_path = os.path.join(game_dir, "images")
    os.system("cp -r assets/mmpmaudio/ " + audio_path)
    os.system("cp -r assets/mmpmimages/ " + images_path)

def inject_mod(game_dir, filename="modhook.rpy"):
    if not os.path.isdir(game_dir):
        print("Error: Not a valid Ren'Py game directory.")
        return

    game_folder = os.path.join(game_dir, "game")
    if not os.path.isdir(game_folder):
        print("Error: No 'game/' folder found.")
        return

    mod_path = os.path.join(game_folder, filename)
    with open(mod_path, "w", encoding="utf-8") as f:
        f.write(MOD_CODE)

    scriptrpy_path = os.path.join(game_folder, "script.rpy")
    with open(scriptrpy_path, "r", encoding="utf-8") as f:
        inject_payload(f, scriptrpy_path)

    inject_assets(game_folder)

    print(f"Injected assets")
    print(f"Injected mod script into {mod_path}")
    print("MMPM Injection done. Thank you.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inject_mod.py <path_to_renpy_game>")
    else:
        inject_mod(sys.argv[1])
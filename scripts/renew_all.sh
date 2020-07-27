#!/bin/bash
echo "Renewing custom textures..."
echo "Removing game TEXTURES/ directory..."
rm -rf $HOME/.config/ppsspp/PSP/TEXTURES/NPJB40001
echo "Finished removing."
echo "Copying new textures..."
cp -r $HOME/dev/rivenirvana/MonsterHunterPortable3rdHDRemake/TEXTURES/NPJB40001 $HOME/.config/ppsspp/PSP/TEXTURES/
echo "Finished copying."
echo "Finished renewing."
exit 0

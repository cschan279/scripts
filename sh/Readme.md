Isolated Workplace
```
gsettings set org.gnome.shell.app-switcher current-workspace-only true
gsettings set org.gnome.shell.extensions.dash-to-dock isolate-workspaces true
```
Disable encryption for VNC
```
gsettings set org.gnome.Vino require-encryption false
```

Others Settings
```
gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'
gsettings set org.gnome.shell.extensions.dash-to-dock show-mounts false
```
Enable Network Manager
```
sudo touch /etc/NetworkManager/conf.d/10-globally-managed-devices.conf
sudo systemctl restart NetworkManager
```

For long directory on terminal, 
search ```"$color_prompt" = yes``` in ```.bashrc```, 
add ```\n``` or anything simular, such as ```***\n$```

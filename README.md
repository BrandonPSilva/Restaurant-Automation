Move `/external/flask_automation.service` to `/etc/systemd/system/flask_automation.service`
    `sudo cp external/flask_automation.service /etc/systemd/system/flask_automation.service`
    
    `sudo systemctl start flask_automation.service`
    `sudo systemctl enable flask_automation.service`
    `sudo systemctl status flask_automation.service`
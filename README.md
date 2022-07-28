# Instagram DM Cleaner

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License

Thanks to: [0fve](https://twitter.com/0fve2) & [max.heiderscheidt](https://instagram.com/max.heiderscheidt)

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages for this tool.

```bash
pip install -r requirements.txt
```

## Usage

After successfully providing your Instagram account credentials you should be able to delete direct messages like the picture below.

![image](https://user-images.githubusercontent.com/54437675/181437533-bfd6d9d8-eba2-4d5f-a049-40b59fb3c921.png)

## Configuration
Use the `config.json` file to configure the tool.
```json
{
    "whitelist": [],
    "sleep_time": 1.2,
    "filter_whitelist":false,
    "delete_groups": false
}
```

`whitelist` is a list of users you want to keep (use thread_v2_id).

`sleep_time` is the time in seconds you want to wait before deleting the next DM.

`filter_whitelist` is a boolean value that determines if you want to delete the whitelisted users only (blacklist).

`delete_groups` is a boolean value that determines if you want to delete the groups.



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Download
**Tool binaries does not support 32 bit**.

* [Windows 64-bit](https://github.com/Ashilles/Instagram-DM-Cleaner/raw/main/bin/x86_64/Windows/Instagram%20DM%20Cleaner.exe)
* [Linux x86_64](https://github.com/Ashilles/Instagram-DM-Cleaner/raw/main/bin/x86_64/Linux/Instagram%20DM%20Cleaner.sh)

**Notice:** Windows may detect it as a malicious file.
You have to [disable real time protection](https://support.microsoft.com/en-us/windows/turn-off-defender-antivirus-protection-in-windows-security-99e6004f-c54c-8509-773c-a4d776b77960) from Windows Defender.

## License
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

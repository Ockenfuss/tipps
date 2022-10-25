# Tipps for Thunderbird
Some options and tricks, as well as my personal workflow


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Tipps for Thunderbird](#tipps-for-thunderbird)
  - [Shared Windows-Ubuntu usage](#shared-windows-ubuntu-usage)
  - [Thunderbird Folder structure](#thunderbird-folder-structure)
  - [Workflow](#workflow)
  - [Passwords](#passwords)

<!-- /code_chunk_output -->


## Shared Windows-Ubuntu usage
Ideally, you want to share the settings and Email folder to allow parallel usage in both OS. The problem arises, that the version of Ubuntu is sometimes behind (?) the Windows version. My solution so far is to start thunderbird in Ubuntu with `thunderbird --allow-downgrade`.

## Thunderbird Folder structure
Thunderbird stores profiles in folders with seemingly random, alphanumeric names like `alfdsj8k.default`. These contain settings, as well as a mirrored image of the filestructure of the IMAP server. Usually, the are located in `~/.thunderbird/`. You can also store them somewhere else, but then you need to tell it by modifying `profile.ini` in `.thunderbird`. Advise: Using relative paths makes migration easier.
```text
[Profile0]
Name=LinuxProfile
IsRelative=0
Path=absolute/path/alfdsj8k.default
Default=1

[General]
StartWithLastProfile=1
Version=2

[Install]
Default=alfdsj8k.default
Locked=1
```
Additionally, you have your local folder, which is independent from the IMAP server, e.g. to archive older mails. Set its path via the Thunderbird settings.

## Workflow
So far, I do not use folders for topics or personnes. This would lead to the questions of defining criteria which email belongs to which folder. If the main criterium is the sender, we do not gain any value as we can already search for specific senders.

If possible, I leave all recent (last two years) emails on the IMAP server in order to have them available anytime and anywhere. Emails which require an answer are left in the inbox, everything handled is put in an IMAP folder "Handled".
Emails older than two years  can be archived in thunderbird to a local folder (Local/Empfangen/EmailAddress), which deletes them on the IMAP server. 
This folder has to be listed in Settings->Kopien und Ordner->Nachrichtenarchiv for every Email account. Afterwards, just select all the emails to archive and click the archive button in thunderbird. Depending on the mail service, deleted messages are still in a trash folder on the server and count on the disk quota.

## Passwords
Thunderbird allows to store passwords using an integrated password manager.
You can view these under Options->Privacy and Security->Passwords.
To add a password, click the checkbox "remember password" when asked for it.
If there is no checkbox, you might need to add/edit the option `user_pref("signon.rememberSignons", true);` in the file `prefs.js` (located in your profile folder, see above)

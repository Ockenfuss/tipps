# Tipps for Thunderbird
Some options and tricks, as well as my personal workflow

## Shared Windows-Ubuntu usage
Ideally, you want to share the settings and Email folder to allow parallel usage in both OS. The problem arises, that the version of Ubuntu is sometimes behind (?) the Windows version. My solution so far is to start thunderbird in Ubuntu with `thunderbird --allow-downgrade`.

## Workflow
So far, I do not use folders for topics or personnes. This would lead to the questions of defining criteria which email belongs to which folder. If the main criterium is the sender, we do not gain any value as we can already search for specific senders.

If possible, I leave all recent (last two years) emails on the IMAP server in order to have them available anytime and anywhere. Older emails can be archived in thunderbird to a local folder (Local/Empfangen/EmailAddress), which deletes them on the IMAP server. 
This folder has to be listed in Settings->Kopien und Ordner->Nachrichtenarchiv for every Email account. Afterwards, just select all the emails to archive and click the archive button in thunderbird. Depending on the mail service, deleted messages are still in a trash folder on the server and count on the disk quota.

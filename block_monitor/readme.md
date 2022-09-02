# memo-monitor
A purposely sub-optimal memo field monitor for Cosmos SDK projects to demonstrate how seed phrases can be scraped. 

Download both files to the home directory. Use cron to run the scrape.py file every minute and output to a text file. Manually build the search.py
(cmd + B for mac on Sublime) to locate any seeds from the text file. autorun.py is an example of how these can be automated. Key details are removed from
each file for security.

Why Post This?
1) This is obviously not the best way to do this and these aren't operational as is.
2) Validators and good guys' scripts often fail when fighting for unbonds. Sometimes validators aren't the good guys.
3) FE/wallets could prohibit 12/24 character entries and solve 99.9% of this while maintaining full functionality at a protocol level.
